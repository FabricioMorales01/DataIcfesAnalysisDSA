from fastapi import FastAPI
from routers.dashboard_router import dashboard_router
from routers.models_router import models_router
from fastapi.openapi.models import Info, Contact

app = FastAPI(
    title="API Evaluar para avanzar",
    description="API para el proyecto de análisis de los resultados del instrumento de Lectura de Evaluar para Avanzar 2022-1 para los estudiantes de instituciones educativas de los departamentos de la Amazonía colombiana.",
    version="1.0.0",
    contact=Contact(name="Grupo 12", email="d.cuadros@uniandes.edu.co"))

# Include routers in the main app
app.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])
app.include_router(models_router, prefix="/models", tags=["models"])
