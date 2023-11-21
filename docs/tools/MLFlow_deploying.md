## ¿Cómo desplegar el servidor MLFlow para registrar los experimentos de los modelos?

A continuación se describe el procedimiento para desplegar el servidor MLFlow que servirá al propósito del proyecto de registrar los experimentos realizados con diferentes modelos.  El servidor estára desplegado a través de un contenedor Docker sobre una máquina virtual EC2 de AWS.

1. **Configuración de la máquina virtual EC2**  
   Se lanza una nueva instancia de EC2 con las siguientes características:  
   - Ubuntu t2.micro
   - Seleccionar un grupo de seguridad que permita las conexiones TCP por el puerto 5000.
   - 20Gb almacenamiento cifrado.  Esto permitirá habilitar la opción de hibernación en la sección de opciones avanzadas.
   - Habilitar la opción de Hibernación en opciones avanzadas.  Esto hará que en l volumen por defecto de la máquina virtual se guarde el estado de la máquina, permitiendo que la proxima vez que se inicie la instancia estén disponibles los resultados de los experimentos ejecutados.  

2. **Instalación y configuración de Docker en la máquina virtual EC2**  
   Tras conectarse a la máquina virtual a través de SSH, se debe realizar el procedimiento de instalación y configuración descrito en la sección *Install using the apt repository* descrito en https://docs.docker.com/engine/install/ubuntu/.

3. **Descargar la imagen que contiene una versión reciente de MLFlow**  
   Ejecutar el siguiente comando en la consola con conexión SSH.  Esto descargará una imagen con todos los prerequisitos y configuraciones necesarias para ejecutar un servidor MLFlow:  
   `sudo docker pull burakince/mlflow`

4. **Ejecutar el contenedor**  
   En la misma consola con conexión SSH ejecutar el siguiente comando para ejecutar el contenedor  
   `sudo docker run -p 5000:5000 -d burakince/mlflow`

5. **Verificar**  
   Copiar la IP pública de la máquina virtual creada en el paso 1 y pegarla en un navegador agregando el puerto 5000 para confirmar que el servidor MLFlow es accesible.

6. **Ejecutar experimentos**  
   Ejecutar los scripts del folder src/models individualmente a medida que se hagan ajustes o todos a la vez usando el script AllModels.py.  Estos scripts usan internamente common/training.py el cual registra los experimentos de cualquier modelo en el servidor remoto de MLFlow del proyecto.
