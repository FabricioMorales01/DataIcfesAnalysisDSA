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
cd src\api
uvicorn main:app --reload
ir en el navegador a http://127.0.0.1:8000/docs

### Cómo ejecutar experimentos MLFlow
cd src\models
python NombreDelModelo.py

### Cómo ejecutar UI MLFlow
mlflow server -h 127.0.0.1 -p 8050

### Cómo ejecutar las pruebas unitarias

### Cómo ejecutar la aplicación Angular