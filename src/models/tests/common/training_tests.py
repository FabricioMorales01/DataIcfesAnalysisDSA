import mlflow
import unittest

from models.common.training import train_model
from sklearn.linear_model import LinearRegression

class TrainModelTests(unittest.TestCase):
    def train_model_WhenLinearRegressionIsPassed_ThenReturnsModelMetrics(self):
        # Arrange
        model = LinearRegression()
        metrics_to_log = ["neg_mean_squared_error", "neg_mean_absolute_error"]

        # Act
        train_model(model, "Regresión lineal inicial", metrics_to_log)

        # Assert
        metrics = mlflow.search_runs().iloc[0][['mse', 'mae']]
        self.assertTrue('mse' in metrics)
        self.assertTrue('mae' in metrics)

if __name__ == '__main__':
    unittest.main()