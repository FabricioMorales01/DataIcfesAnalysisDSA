import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(data_path, model_path):
    # TODO: Revisar qué otras cosas deberían recibirse como parámetro o estar en un archivo de configuración
    # TODO: Crear pruebas unitarias
    # TODO: Se pueden crear pruebas adicionales que revisen las métricas del modelo y alerten si se sale de cierto umbral
    # Cargar los datos y extraer conjuntos de entrenamiento y prueba
    data = pd.read_csv(data_path)

    X = data.drop('target_column', axis=1)
    y = data['target_column']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Configurar y entrenar el modelo
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Iniciar el registro de eventos del modelo en MLFlow.
    with mlflow.start_run():
        # Se registran los hiperparámetros para el modelo en MLFlow.
        mlflow.log_param("n_estimators", model.n_estimators)

        # Se generan predicciones para el conjunto de prueba y se registran las métricas de desempeño del modelo.
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        mlflow.log_metric("mse", mse)

        # Finalmente se guarda el modelo en MLFlow.
        mlflow.sklearn.log_model(model, model_path) # TODO: Asegurar que los modelos se guarden en la carpeta models