import pandas as pd

from common.training import train_model
from sklearn.linear_model import LinearRegression
from tqdm import tqdm

# Definir la configuración para el entrenamiento del modelo.
data_file = '../../data/processed/EXA_2022_1_Todos_Limp.csv'
target = 'EXA_N_RTAS_CORR_LC'

default_params = {
    "data_file": data_file,
    "scaling": False,
    "test_size": 0.33,
    "random_state": 42,
}

metrics = ["neg_mean_squared_error", "neg_mean_absolute_error"]

# Datos
def get_hot_encoded_data():
    categoricas_var = ["ESTU_GENERO", "COLE_NATURALEZA", "COLE_CALENDARIO", "COLE_JORNADA", "EXA_MODALIDAD"]

    # Realiza la codificación one hot
    data_mod = pd.read_csv(data_file, sep=',')
    for var in categoricas_var:
        data_mod = pd.get_dummies(data_mod, columns=[var])

    return data_mod

base_data = pd.read_csv(data_file, sep=',')
encoded_data = get_hot_encoded_data()

# Definición de experimentos
experiments = [
    {
        "params": {
            "description": "Escenario 0",
            "predictors": ['ESTU_GRADO', 'COLE_COD_ICFES', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT'],
        } 
    },
    {
        "params": {
            "description": "Escenario 1. Sin COLE_COD_ICFES",
            "predictors": ['ESTU_GRADO', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT'],
         }
    },
    {
        "params": {
            "description": "Escenario 2. Considerando solamente el grado y los puntajes de los otros 3 instrumentos",
            "predictors": ['ESTU_GRADO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT'],
         }
    },
    {
        "params": {
            "description": "Escenario 3. Considerando todas las variables numéricas menos COLE_COD_ICFES para evaluar el impacto del colegio en los resultados",
            "predictors": ['ESTU_GRADO', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT'],
         }
    },
    {
        "data": encoded_data,
        "params": {
            "description": "Escenario 4. Considerando todas las variables numéricas y categóricas",
            "predictors": ['ESTU_GRADO',  'COLE_COD_ICFES', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_LC', 'EXA_N_RTAS_CORR_MT',
              'ESTU_GENERO_F', 'ESTU_GENERO_M', 'COLE_NATURALEZA_NO', 'COLE_NATURALEZA_O', 'COLE_CALENDARIO_A', 'COLE_JORNADA_COMPLETA', 'COLE_JORNADA_MAÑANA', 'COLE_JORNADA_TARDE', 'COLE_JORNADA_UNICA',
              'EXA_MODALIDAD_OFF', 'EXA_MODALIDAD_ON', 'EXA_MODALIDAD_PA', 'EXA_MODALIDAD_PAL'],
         }
    },
    {
        "data": encoded_data,
        "params": {
            "description": "Escenario 5. Escalando las variables numéricas",
            "predictors": ['ESTU_GRADO', 'COLE_COD_ICFES', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT'],
            "scaling": True,
         }
    }
]

for exp in tqdm(experiments):
    model = LinearRegression()
    # Tomar la data base a menos que para el experimento se haya definido un conjunto distinto
    data = exp.get("data", base_data)

    # Crear una copia de los parámetros para evitar modificaciones directas
    params = exp["params"].copy()

    params["target"] = target
    params.setdefault("data_file", default_params["data_file"])
    params.setdefault("scaling", default_params["scaling"])
    params.setdefault("test_size", default_params["test_size"])
    params.setdefault("random_state", default_params["random_state"])

    train_model(model, data, params, metrics)
