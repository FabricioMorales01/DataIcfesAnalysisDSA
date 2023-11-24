## ¿Cómo validar el modelo con Tox antes de empaquetarlo?

A continuación se describe el procedimiento para ejecutar el pipeline de validación del modelo usando TOX para luego empaquetar el modelo en un whl o tar.gz de manera que pueda estar disponible en otros ambientes desde la consola de comandos o pueda ser consumido en un api.

1. Identificar el mejor modelo, hiperparámetros y configuraciones necesarias tras registrar y analizar los experimentos a través de MLFlow.
2. Ubicarse en la ruta *src\models\package*.
3. Aplicar la configuración en los archivos config.yml.
4. Ejecutar el comando `tox run -e train`, siendo *train* el nombre del entorno de tox definido en el archivo *tox.ini* para el entrenamiento del modelo.  
   Tener en cuenta que si el directorio de trabajo contiene espacios es mejor copiar la carpeta *package* a una ruta sin espacios, por ejemplo *c:\temp* y ejecutar desde allí los comandos de tox.
5. Ejecutar el comando `tox run -e test_package`, siendo *test_package* el nombre del entorno de tox definido en el archivo *tox.ini* para las pruebas del modelo.
6. Si las pruebas se ejecutaron de manera exitosa, ejecutar el comando `python3 -m build`, para construir el paquete (desde *src\models\package*).
7. Se creará la carpeta dist, que contendrá el archivo .whl para distribuir el modelo.