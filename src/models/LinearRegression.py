import pandas as pd

from common.training import train_model
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# Definir la configuración para el entrenamiento del modelo.
data_file = '../../data/processed/EXA_2022_1_Todos_Limp.csv'
model = LinearRegression()
name = "Regresión lineal 6"
params = {'data_file': data_file, 'test_size': 0.33, 'random_state': 42}
metrics = ["neg_mean_squared_error", "neg_mean_absolute_error"]

# Cargar los datos
diabetes = load_diabetes()
data = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
data['target'] = diabetes.target

train_model(model, name, data, 'target', params, metrics)