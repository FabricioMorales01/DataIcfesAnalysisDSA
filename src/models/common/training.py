import mlflow
import mlflow.sklearn

# from config.core import config
from sklearn.model_selection import train_test_split
from sklearn.metrics import get_scorer
from sklearn.preprocessing import StandardScaler

def train_model(model, data, params, metrics):
    name = type(model).__name__

    X = data[params['predictors']]
    y = data[params['target']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params['test_size'], random_state=params['random_state'])

    if params['scaling'] == True:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # Iniciar el registro de eventos del modelo en MLFlow.
    mlflow.set_tracking_uri("http://127.0.0.1:8050")
    # mlflow.set_tracking_uri("http://54.225.16.223:5000/")

    # Registrar el experimento
    experiment = mlflow.set_experiment(name)

    # Identificar la cantidad de corridas actuales para el experimento
    runs_info = mlflow.search_runs(experiment_ids=mlflow.get_experiment_by_name(name).experiment_id)
    runs_count = len(runs_info)

    with mlflow.start_run(experiment_id=experiment.experiment_id, run_name=f'{name} {runs_count}'):
        # Dejar registro del conjunto de datos usado en el experimento
        # TODO: mlflow.log_artifact(params['data_file'], "datasets")
        
        # Establecer texto descriptivo del experimento si fue establecido en los parámetros
        if "description" in params:
            mlflow.log_param("description", params["description"])

        model.fit(X_train, y_train)

        # Se generan predicciones para el conjunto de prueba y se registran las métricas de desempeño del modelo.
        y_pred = model.predict(X_test)
        
        # Registrar los parámetros en MLFlow
        mlflow.log_params(params)

        # Registrar las métricas en MLFlow
        score = model.score(X_test, y_test)
        mlflow.log_metric('score', score)

        for metric_name in metrics:
            metric_scorer = get_scorer(metric_name)
            metric_value = metric_scorer(model, X_test, y_test)
            mlflow.log_metric(metric_name, metric_value)

        # Finalmente se guarda el modelo en MLFlow.
        mlflow.sklearn.log_model(model, name)