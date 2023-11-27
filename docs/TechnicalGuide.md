### Operaciones básicas con GIT
#### Guardar cambios actuales
git add .
git commit -m "Mensaje del commit"

#### Cambiar a la rama main
git checkout main

#### Actualizar la rama main
git pull origin main

#### cambiar de nuevo a la rama local
git checkout dc-models

#### Rebase de la rama local con main
git rebase main


### Operaciones básicas con DVC
Cheat sheet: https://derekchia.com/dvc/

### Cómo ejecutar el API
cd src\api\epa_modelolectura_api
uvicorn app.main:app --reload
ir en el navegador a http://127.0.0.1:8000

### Cómo contenerizar MLFlow
Usar la imagen https://hub.docker.com/r/burakince/mlflow
En una instancia EC2 ejecutar los pasos descritos en https://docs.docker.com/engine/install/ubuntu/ (Los comandos docker pull y docker run deben ejecutarse con sudo)
sudo docker pull burakince/mlflow
sudo docker run -p 5000:5000 -d burakince/mlflow

### Cómo ejecutar experimentos MLFlow
cd src\models
python NombreDelModelo.py

### Cómo ejecutar UI MLFlow
mlflow server -h 127.0.0.1 -p 8050

### Cómo contenerizar API
cd src\api
docker build -t epa_modelolectura_api .
docker run -p 8000:8000 -it -e PORT=8000 epa_modelolectura_api

### Cómo ejecutar la aplicación Angular

----
cp -r DataIcfesAnalysisDSA/src/api /home/Grupo11/api
sudo rm -r DataIcfesAnalysisDSA/
