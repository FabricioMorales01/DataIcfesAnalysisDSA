from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

from model.config.core import config
from model.processing import features as pp

epa_modelo_lectura_pipe = Pipeline(
    [
        # Scaler
        ("scaler", MinMaxScaler()
         ),
        # Random forest 
        ("Random Forest",
            RandomForestClassifier(
                n_estimators = config.model_config.n_estimators, 
                max_depth = config.model_config.max_depth,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
