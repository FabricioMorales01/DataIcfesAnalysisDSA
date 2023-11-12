import pandas as pd

from common.training import train_model
from sklearn.neural_network import MLPClassifier

# Definir la configuración para el entrenamiento del modelo.
data_file = '../../data/processed/EXA_2022_1_Todos_Limp.csv'
predictors = ['ESTU_GRADO', 'COLE_COD_ICFES', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT']
target = 'EXA_N_RTAS_CORR_LC'
params = {
    'data_file': data_file, 
    'predictors': predictors, 
    'target': target, 
    'scaling': False, 
    'test_size': 0.33, 
    'random_state': 42,
    'hidden_layer_sizes':( 10, 10), 
    'activation': "relu", 
    'solver': "adam", 
    'max_iter': 1000
}
metrics = ["neg_mean_squared_error", "neg_mean_absolute_error"]

model = MLPClassifier(hidden_layer_sizes=params['hidden_layer_sizes'], activation=params['activation'], solver=params['solver'], max_iter=params['max_iter'])

# Cargar los datos
data = pd.read_csv(data_file, sep=',')

# Entrenar el modelo y registrar experimento en MLFlow
train_model(model, data, params, metrics)

# Escenario sin COLE_COD_ICFES
predictors.remove('COLE_COD_ICFES')
train_model(model, data, params, metrics)

# Escenario 2 considerando solamente el grado y los puntajes de los otros 3 instrumentos
predictors = ['ESTU_GRADO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT']
train_model(model, data, params, metrics)

# Escenario 3 considerando todas las variables numéricas menos COLE_COD_ICFES para evaluar el impacto del colegio en los resultados
predictors = ['ESTU_GRADO', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN',  'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT']
train_model(model, data, params, metrics)

# Escenario 4 considerando todas las variables numéricas y categóricas
categoricas_var = ["ESTU_GENERO", "COLE_NATURALEZA", "COLE_CALENDARIO", "COLE_JORNADA", "EXA_MODALIDAD"]

# Realiza la codificación one hot
data_mod = pd.read_csv(data_file, sep=',')
for var in categoricas_var:
    data_mod = pd.get_dummies(data_mod, columns=[var])

predictors = ['ESTU_GRADO',  'COLE_COD_ICFES', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_LC', 'EXA_N_RTAS_CORR_MT',
              'ESTU_GENERO_F', 'ESTU_GENERO_M', 'COLE_NATURALEZA_NO', 'COLE_NATURALEZA_O', 'COLE_CALENDARIO_A', 'COLE_JORNADA_COMPLETA', 'COLE_JORNADA_MAÑANA', 'COLE_JORNADA_TARDE', 'COLE_JORNADA_UNICA',
              'EXA_MODALIDAD_OFF', 'EXA_MODALIDAD_ON', 'EXA_MODALIDAD_PA', 'EXA_MODALIDAD_PAL']

train_model(model, data_mod, params, metrics)

# Escenario 5 escalando las variables numéricas
params['scaling'] = True
train_model(model, data_mod, params, metrics)