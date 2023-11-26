import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger
from model import __version__ as model_version
from model.predict import make_prediction

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()

# Ruta para verificar que la API se esté ejecutando correctamente
@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Permite realizar un diagnóstico del API y conocer su estado actual.
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()

# Ruta para datos del dashboard
@api_router.get("/get_summarized_data", status_code=200)
def get_summarized_data():
    """
    Permite obtener los datos agrupados de la manera adecuada para las visualizaciones en el tablero.
    """
    file = 'EXA_2022_1_Todos_Limp.csv'

    try:
        df = pd.read_csv(f"app/data/processed/{file}", delimiter='|')
        data_dict = df.to_dict(orient='records')
        return JSONResponse(content=data_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al tratar de leer el archivo {file}. {str(e)}")

# Ruta para realizar las predicciones
@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleDataInputs) -> Any:
    """
    Permite realizar predicciones del nivel de lectura de 1 o varios estudiantes basado en sus características y desempeño en otros componentes de la prueba Evaluar para avanzar.
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")
    return results
