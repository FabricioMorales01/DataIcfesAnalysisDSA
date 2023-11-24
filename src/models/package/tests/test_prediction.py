import math

import numpy 

from model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_first_prediction_value = 0  # TODO: Revisar
    expected_no_predictions = 5261 # TODO: Revisar

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    print(predictions[0])
    
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    # assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=0.001) # TODO: Revisar
