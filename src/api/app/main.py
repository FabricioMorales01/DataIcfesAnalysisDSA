from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import Contact
from fastapi.responses import RedirectResponse
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging

# setup logging as early as possible
setup_app_logging(config=settings)

app = FastAPI(
    title=settings.PROJECT_NAME, 
    description="API para el proyecto de análisis de los resultados del instrumento de Lectura de Evaluar para Avanzar 2022-1 para los estudiantes de instituciones educativas de los departamentos de la Amazonía colombiana.",
    version=settings.API_V1_STR,
    contact=Contact(name="Grupo 11 - Daniel Londoño, Fabricio Morales, David Ruíz, Dayron Cuadros"), 
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

app.include_router(api_router, prefix=settings.API_V1_STR)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    # Use this for debugging purposes only
    logger.warning("Running in development mode. Do not run like this in production.")
    import uvicorn

    # ejecución del servidor - host para ejecutar en servidor 
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
