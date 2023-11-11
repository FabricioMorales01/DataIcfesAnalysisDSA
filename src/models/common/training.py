import mlflow
import mlflow.sklearn

# from config.core import config
from sklearn.model_selection import train_test_split
from sklearn.metrics import get_scorer

def train_model(model, name, data, target_name, params, metrics):
    X = data.drop(target_name, axis=1)
    y = data[target_name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params['test_size'], random_state=params['random_state'])

    # Iniciar el registro de eventos del modelo en MLFlow.
    # TODO: mlflow.set_tracking_uri("http://127.0.0.1:8050")

    # Registrar el experimento
    experiment = mlflow.set_experiment(name)

    with mlflow.start_run(experiment_id=experiment.experiment_id):
        # Dejar registro del conjunto de datos usado en el experimento
        # TODO: mlflow.log_artifact(params['data_file'], "datasets")

        model.fit(X_train, y_train)

        # Se generan predicciones para el conjunto de prueba y se registran las métricas de desempeño del modelo.
        y_pred = model.predict(X_test)
        
        # Registrar los parámetros en MLFlow
        mlflow.log_params(params)

        # Registrar las métricas en MLFlow
        for metric_name in metrics:
            metric_scorer = get_scorer(metric_name)
            metric_value = metric_scorer(model, X_test, y_test)
            mlflow.log_metric(metric_name, metric_value)

        # Finalmente se guarda el modelo en MLFlow.
        mlflow.sklearn.log_model(model, name)