import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.metrics import mean_squared_error

def evaluate_model(model_path, data_path):
    # Se carga el modelo especificado.
    model = mlflow.sklearn.load_model(model_path)

    # Se cargan datos sobre los cuales se quieren realizar predicciones
    data = pd.read_csv(data_path)

    X = data.drop('target_column', axis=1)
    y_true = data['target_column']
    y_pred = model.predict(X)

    # Evaluar el desempeño del modelo
    mse = mean_squared_error(y_true, y_pred)

    # Registrar las métricas de desempeño del modelo en MLFlow
    with mlflow.start_run():
        mlflow.log_metric("mse", mse)
