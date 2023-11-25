from typing import Any, List, Optional

from pydantic import BaseModel
from model.processing.validation import DataInputSchema

# Esquema de los resultados de predicción
class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]

# Esquema para inputs múltiples
class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "ESTU_GRADO": 3,
                        "COLE_COD_ICFES": 13110,
                        "COLE_COD_MCPIO": 91001,
                        "COLE_COD_DPTO": 91,
                        "EXA_C_RTAS_CORR_CN": 0,
                        "EXA_C_RTAS_CORR_CC": 0,
                        "EXA_C_RTAS_CORR_MT": 1,
                        "ESTU_GENERO_F": True,
                        "COLE_NATURALEZA_O": True,
                        "COLE_JORNADA_COMPLETA": False,
                        "COLE_JORNADA_MAÑANA": False,
                        "COLE_JORNADA_TARDE": True,
                        "EXA_MODALIDAD_OFF": False,
                        "EXA_MODALIDAD_ON": False,
                        "EXA_MODALIDAD_PA": True
                    }
                ]
            }
        }
