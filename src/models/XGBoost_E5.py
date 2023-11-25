import pandas as pd

from tqdm import tqdm
from common.training import train_model

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier

# Definir la configuración para el entrenamiento del modelo.
data_file = '../../data/processed/EXA_2022_1_Todos_Limp.csv'
target = 'EXA_C_RTAS_CORR_LC'

default_params = {
    "data_file": data_file,
    "scaling": False,
    "test_size": 0.2,
    "random_state": 42,
}

metrics = ["neg_mean_squared_error", "neg_mean_absolute_error"]

base_mod = pd.read_csv(data_file, sep=',')

# En el escenario 5 consideramos todas las variables categóricas y numéricas
# Además, consideramos la categorización de los resultados: 0 (o-4 respuestas correctas), 1 (5-9 respuestas correctas),
# 2 (10-14 respuestas correctas) y 3 (15-20 respuestas correctas)

base_mod_cat = base_mod.assign(EXA_C_RTAS_CORR_CN = lambda x: ((base_mod['EXA_N_RTAS_CORR_CN'] // 5)))
base_mod_cat = base_mod_cat.assign(EXA_C_RTAS_CORR_CC = lambda x: ((base_mod['EXA_N_RTAS_CORR_CC'] // 5)))
base_mod_cat = base_mod_cat.assign(EXA_C_RTAS_CORR_LC = lambda x: ((base_mod['EXA_N_RTAS_CORR_LC'] // 5)))
base_mod_cat = base_mod_cat.assign(EXA_C_RTAS_CORR_MT = lambda x: ((base_mod['EXA_N_RTAS_CORR_MT'] // 5)))

# Crea una lista de las variables categóricas
categoricas_var = ["ESTU_GENERO", "COLE_NATURALEZA", "COLE_JORNADA", "EXA_MODALIDAD"]

# Realiza la codificación one hot
for var in categoricas_var:
    base_mod_cat = pd.get_dummies(base_mod_cat, columns=[var])

base_mod_cat['EXA_C_RTAS_CORR_CN'] = base_mod_cat['EXA_C_RTAS_CORR_CN'].replace([4], 3)
base_mod_cat['EXA_C_RTAS_CORR_CC'] = base_mod_cat['EXA_C_RTAS_CORR_CC'].replace([4], 3)
base_mod_cat['EXA_C_RTAS_CORR_LC'] = base_mod_cat['EXA_C_RTAS_CORR_LC'].replace([4], 3)
base_mod_cat['EXA_C_RTAS_CORR_MT'] = base_mod_cat['EXA_C_RTAS_CORR_MT'].replace([4], 3)

predictors = ['ESTU_GRADO', 'COLE_COD_ICFES', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_C_RTAS_CORR_CN', 'EXA_C_RTAS_CORR_CC', 'EXA_C_RTAS_CORR_MT',
              'ESTU_GENERO_F', 'COLE_NATURALEZA_O', 'COLE_JORNADA_COMPLETA', 'COLE_JORNADA_MAÑANA', 'COLE_JORNADA_TARDE',
              'EXA_MODALIDAD_OFF', 'EXA_MODALIDAD_ON', 'EXA_MODALIDAD_PA']

X = base_mod_cat[predictors]

# Selecciona la variable dependiente
y = base_mod_cat[target]

# Definición de los experimentos -------------------------------------------------------------------------
experiments = [
    {
        "model": RandomForestClassifier(n_estimators=200, max_depth=80),
        "params": {
            "description": "Escenario 5.1",
            "predictors": predictors,
            "model params": "n_estimators=200, max_depth=80"
        } 
    },
    {
        "model": GradientBoostingClassifier(n_estimators=100, learning_rate=0.3),
        "params": {
            "description": "Escenario 5.2",
            "predictors": predictors,
            "n_estimators": 100,
            "model params": "n_estimators=100, learning_rate=0.3"
        } 
    },
    {
        "model": XGBClassifier(n_estimators=100, learning_rate=0.2),
        "params": {
            "description": "Escenario 5.3",
            "predictors": predictors,
            "model params": "n_estimators=100, learning_rate=0.2"
        } 
    },
    {
        "model": XGBClassifier(n_estimators=200, learning_rate=0.2, max_depth=5),
        "params": {
            "description": "Escenario 5.4 - Todas las variables categóricas y numéricas. Además, consideramos la categorización de los resultados: 0 (0-4 respuestas correctas), 1 (5-9 respuestas correctas), 2 (10-14 respuestas correctas) y 3 (15-20 respuestas correctas)",
            "predictors": predictors,
            "model params": "n_estimators=200, learning_rate=0.2, max_depth=5"
        } 
    }
]

for exp in tqdm(experiments):
    model = exp["model"]

    # Tomar la data base a menos que para el experimento se haya definido un conjunto distinto
    data = exp.get("data", base_mod_cat)

    # Crear una copia de los parámetros para evitar modificaciones directas
    params = exp["params"].copy()
    
    params["target"] = target
    params.setdefault("data_file", default_params["data_file"])
    params.setdefault("scaling", default_params["scaling"])
    params.setdefault("test_size", default_params["test_size"])
    params.setdefault("random_state", default_params["random_state"])

    train_model(model, data, params, metrics)
