from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class DataInputSchema(BaseModel):
    ESTU_GRADO: Optional[int]
    COLE_COD_ICFES: Optional[int]
    COLE_COD_MCPIO: Optional[int]
    COLE_COD_DPTO: Optional[int]
    EXA_C_RTAS_CORR_CN: Optional[int]
    EXA_C_RTAS_CORR_CC: Optional[int]
    EXA_C_RTAS_CORR_MT: Optional[int]
    ESTU_GENERO_F: Optional[int]
    COLE_NATURALEZA_O: Optional[int]
    COLE_JORNADA_COMPLETA: Optional[int]
    COLE_JORNADA_MAÑANA: Optional[int]
    COLE_JORNADA_TARDE: Optional[int]
    EXA_MODALIDAD_OFF: Optional[int]
    EXA_MODALIDAD_ON: Optional[int]
    EXA_MODALIDAD_PA: Optional[int]

class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]
