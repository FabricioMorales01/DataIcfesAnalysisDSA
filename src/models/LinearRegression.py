import pandas as pd

from common.training import train_model
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# Definir la configuración para el entrenamiento del modelo.
data_file = '../../data/processed/EXA_2022_1_Todos_Limp.csv'
model = LinearRegression()
name = "Regresión lineal 6"
predictors = ['ESTU_GRADO', 'COLE_COD_ICFES', 'COLE_COD_MCPIO', 'COLE_COD_DPTO', 'EXA_N_RTAS_CORR_CN', 'EXA_N_RTAS_CORR_CC', 'EXA_N_RTAS_CORR_MT']
target = 'EXA_N_RTAS_CORR_LC'
params = {'data_file': data_file, 'predictors': predictors, 'target': target, 'test_size': 0.33, 'random_state': 42}
metrics = ["neg_mean_squared_error", "neg_mean_absolute_error"]

# Cargar los datos
data = pd.read_csv(data_file, sep=',')

# Entrenar el modelo y registrar experimento en MLFlow
train_model(model, name, data, params, metrics)