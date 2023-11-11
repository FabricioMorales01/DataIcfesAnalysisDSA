![Alt text](docs/imgs/header.png)

# Caracterización de instituciones educativas de Colombia a partir de algunas variables educativas y los resultados de Evaluar para Avanzar

**Contenido**  
- [Contexto](#Contexto)
  - [Problema](#Problema)
- [Definición del proyecto de analítica](#Definicion)
  - [Pregunta de negocio y alcance del proyecto](#Pregunta)
  - [Objetivo del proyecto](#Objetivo)
  - [Alcance del proyecto](#Alcance)
  - [Resultados esperados](#Resultados)
  - [Seguimiento a las actividades del proyecto](#Seguimiento)
- [¿Cómo está estructurado este repositorio?](#Estructura)

## Contexto<a name="Contexto"></a>
En Colombia, el Instituto Colombiano para la Evaluación de la Educación ICFES, es la entidad encargada de evaluar a nivel nacional las habilidades y competencias de los estudiantes en los distintos niveles escolares, desde grado 3° hasta la formación profesional. Para cumplir con este propósito, el ICFES diseña y aplica un conjunto de exámenes estandarizados conocidos como Pruebas Saber (Saber 3°, 5°, 7° y 9°, Saber 11°, Saber TyT y Saber Pro).

Sin embargo, en los últimos años, el ICFES ha desarrollado una estrategia complementaria a las Pruebas Saber conocida como Evaluar para Avanzar. Este instrumento se diferencia de las anteriores por su intencionalidad diagnóstica-formativa, en la que los docentes de las instituciones educativas que apliquen de forma voluntaria esta estrategia son los principales beneficiados al obtener un diagnóstico del desarrollo de las habilidades y conocimientos de sus estudiantes, lo que le permite identificar las fortalezas y las dificultades de cada uno de ellos.

La implementación de Evaluar para Avanzar se realiza entre los grados 3° y 11°. En estos grados se aplican instrumentos de valoración asociados a las áreas básicas de conocimiento. La siguiente figura muestra la distribución de los instrumentos a lo largo de los grados.

![Alt text](docs/imgs/Fig1.png)


### Problema<a name="Problema"></a>
En este sentido, el problema considerado consiste en analizar el impacto de Evaluar para Avanzar en términos de aplicación en instituciones educativas en algunas regiones de Colombia, así como analizar los resultados de estas instituciones en los distintos instrumentos presentados.


## Definición del proyecto de analítica<a name="Definición"></a>
### Pregunta de negocio y alcance del proyecto<a name="Pregunta"></a>

La pregunta de negocio busca establecer una herramienta analítica que presente la información asociada con la aplicación de Evaluar para Avanzar en distintas regiones de Colombia, así como los resultados generales de las instituciones que aplicaron los instrumentos que componen esta estrategia. También se busca generar agrupaciones de estas instituciones en términos de su naturaleza y los resultados de la aplicación.

### Objetivo del proyecto<a name="Objetivo"></a>

El presente proyecto tiene como objetivo analizar los resultados de las instituciones educativas colombianas que participaron en la estrategia de Evaluar para Avanzar durante los semestres 2021-1, 2021-2 y 2022-1 y utilizarlos junto con otras variables educativas para caracterizar y encontrar clusters que agrupan estas instituciones educativas.

### Alcance del proyecto<a name="Alcance"></a>

El análisis descrito previamente busca:

- Identificar el impacto de Evaluar para Avanzar en términos de la aplicación en distintas regiones de Colombia por parte de las instituciones educativas.

- Encontrar agrupaciones de las instituciones educativas que aplicaron Evaluar para Avanzar a partir de variables relacionadas con su naturaleza y con los resultados de los instrumentos de valoración aplicados.

### Resultados esperados<a name="Resultados"></a>

Como resultado principal del proyecto, se busca obtener un tablero de control que permita conocer la cantidad de instituciones que aplicaron la estrategia de Evaluar para Avanzar en una región particular, así como una agrupación de estas instituciones según su naturaleza y los resultados obtenidos en los instrumentos. También se espera que el tablero permita visualizar los resultados de las instituciones en cada uno de los instrumentos de valoración que componen esta estrategia.

### Seguimiento a las actividades del proyecto<a name="Seguimiento"></a>
Accede a la programación de actividades por cada iteración semanal a través de: https://github.com/users/dayroncj/projects/4/views/4


## ¿Cómo está estructurado este repositorio?<a name="Estructura"></a>

Este repositorio nace de la necesidad de aplicar los conceptos y buenas prácticas aprendidas en el curso de Despliegue de soluciones analíticas de la Maestría de inteligencia analítica de datos de la Universidad de Los Andes basado en las etápas de la metodología CRISP-ML (Cross-Industry Standard Process for Machine Learning).

A continuación, se describe la estructura de directorios que reflejan las diferentes etapas en la metodología, esto con el objetivo de facilitar a los colaboradores el mantenimiento del repositorio y a usuarios e interesados navegar por el contenido:

- **docs/**  
  Directorio para la documentación del proyecto. 
   - CRISP-ML.md: Describe cómo se aplicará la metodología CRISP-ML en el proyecto.
   - Data_Dictionary.md: Describe las variables y características de los datos utilizados en el proyecto.

- **data/**  
  Directorio para almacenar los datos brutos y procesados.
   - raw/: Datos en bruto sin procesar.
   - processed/: Datos procesados y limpios, que pueden incluir subdirectorios para diferentes etapas de procesamiento.

- **src/**  
  Directorio para el código fuente del proyecto.
   - data_preparation/: Scripts y notebooks relacionados con la preparación de datos y análisis exploratorio de los mismos.
   - modeling/: Scripts y notebooks relacionados con la construcción de modelos.
   - evaluation/: Scripts y notebooks relacionados con la evaluación de modelos.
   - deployment/: Scripts y notebooks relacionados con la implementación de modelos.
   - utils/: Código de utilidades y funciones compartidas.
   - visualizations/: Componentes visuales de apoyo para análisis descriptivo.

- **results/**
  Directorio para almacenar los resultados intermedios y finales del proyecto.
   - models/: Modelos entrenados y sus artefactos relacionados.
   - reports/: Informes y visualizaciones generadas a lo largo del proyecto.

- **deliverables/**  
  Directorio para los entregables finales del proyecto.
   - presentations/: Presentaciones o informes finales.
   - final_model/: Archivos relacionados con el modelo final seleccionado.
