FROM python:3.11.5

# Crear usuario que ejecuta la app
RUN adduser --disabled-password --gecos '' api-user

# Definir directorio de trabajo 
WORKDIR /opt/epa_modelolectura_api

# Instalar dependencias
ADD ./epa_modelolectura_api /opt/epa_modelolectura_api/
RUN pip install --upgrade pip
RUN pip install -r /opt/epa_modelolectura_api/requirements.txt

# Hacer el directorio de trabajo ejecutable 
RUN chmod +x /opt/epa_modelolectura_api/run.sh
# Cambiar propiedad de la carpeta a api-user 
RUN chown -R api-user:api-user ./

USER api-user
# Puerto a exponer para la api 
EXPOSE 8000

# Comandos a ejecutar al correr el contenedor 
CMD ["bash", "./run.sh"]