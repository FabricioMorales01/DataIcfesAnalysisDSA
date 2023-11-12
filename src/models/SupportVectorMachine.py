import pandas as pd

from common.training import train_model
from sklearn.svm import SVC

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
    'kernel':'linear', 
    'probability': True
}
metrics = ["neg_mean_squared_error", "neg_mean_absolute_error"]

model = SVC(kernel='linear', probability=True)

# Cargar los datos
data = pd.read_csv(data_file, sep=',')

# Entrenar el modelo y registrar experimento en MLFlow
train_model(model, data, params, metrics)