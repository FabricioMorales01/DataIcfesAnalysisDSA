from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier

from model.config.core import config
from model.processing import features as pp

epa_modelo_lectura_pipe = Pipeline(
    [
        # Scaler
        ("scaler", MinMaxScaler()
         ),
        # XGBoost classifier 
        ("XGBoost classifier",
            XGBClassifier(
                n_estimators=config.model_config.n_estimators, 
                learning_rate=config.model_config.learning_rate, 
                max_depth=config.model_config.max_depth,
                random_state=config.model_config.random_state
            )
        ),
    ]
)
