from fastapi import APIRouter

models_router = APIRouter()

@models_router.post("/predict")
def predict():
    return {"message": "Prediction made successfully"}

@models_router.get("/get_metrics")
def get_metrics():
    return {"message": "Metrics retrieved successfully"}
