import csv
import pandas as pd

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

dashboard_router = APIRouter()

@dashboard_router.get("/get_summarized_data")
def get_summarized_data():
    try:
        df = pd.read_csv("../../data/data.csv", delimiter='|')
        data_dict = df.to_dict(orient='records')
        return JSONResponse(content=data_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al tratar de leer el archivo. {str(e)}")