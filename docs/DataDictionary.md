### **Información del estudiante**
| Campo                              | Descripción                                                  | Opciones de respuesta            |
|-----------------------------------|--------------------------------------------------------------|----------------------------------|
| ESTU_CONSECUTIVO                   | ID público del estudiante                                    | Texto                            |
| ESTU_FECHAPRESENTACION             | Fecha de la primera aplicación de instrumentos de valoración presentada por el estudiante | [DD/MM/AAAA] |
| ESTU_GRADO                         | Grado del estudiante en el momento de presentar el instrumento de valoración | Enteros del 3 al 11 |
| ESTU_GENERO                        | Género reportado en Evaluar para Avanzar 3° a 11°          | [Masculino, Femenino]            |

### **Información del colegio**
| Campo                              | Descripción                                                  | Opciones de respuesta            |
|-----------------------------------|--------------------------------------------------------------|----------------------------------|
| COLE_COD_DANE_ESTABLECIMIENTO      | Código DANE del Establecimiento Educativo                   | Número                           |
| COLE_COD_DANE_SEDE                 | Código DANE de la sede educativa                             | Número                           |
| COLE_NOM_ESTABLECIMIENTO           | Nombre del establecimiento educativo                         | Texto                            |
| COLE_NOM_SEDE                      | Nombre de la sede educativa                                  | Texto                            |
| COLE_COD_ICFES                     | Código Icfes de la sede-jornada                              | Número                           |
| COLE_NATURALEZA                    | Indica la naturaleza del establecimiento educativo          | [No oficial, Oficial]           |
| COLE_CALENDARIO                   | Indica el calendario de la sede                              | [A, B]                           |
| COLE_JORNADA                      | Indica la jornada de la sede                                 | [Mañana, Noche, Sabatina, Tarde, Única] |
| COLE_COD_MCPIO                    | Código DANE del municipio donde está ubicada la sede        | Número                           |
| COLE_NOM_MCPIO                    | Nombre del municipio donde está ubicada la sede             | Texto                            |
| COLE_COD_DPTO                     | Código DANE del departamento donde está ubicada la sede      | Número                           |
| COLE_NOM_DPTO                     | Nombre del departamento donde está ubicada la sede           | Texto                            |

### **Resultados de las pruebas**
| Campo                              | Descripción                                                  | Opciones de respuesta            |
|-----------------------------------|--------------------------------------------------------------|----------------------------------|
| EXA_CUADERNILLO                   | Indica el cuadernillo al que pertenece el instrumento de valoración | [1, 2]                        |
| EXA_MODALIDAD                     | Indica la modalidad de presentación del instrumento de valoración | [Online, Offline, Cuadernillos PDF, Papel y lápiz] |
| EXA_INSTRUMENTO                   | Indica el área de conocimiento valorada por el instrumento de valoración | [A, B]                     |
| EXA_COMPONENTE                    | Indica el componente asociado a las respuestas del estudiante | Texto                         |
| EXA_COMPETENCIA                   | Indica la competencia asociada a las respuestas del estudiante | Texto                         |
| EXA_N_PREGUNTAS                   | Indica el número de preguntas en total por cada grupo de análisis | Número                    |
| EXA_N_PREGUNTAS_OM                | Indica el número de preguntas que el/la estudiante se abstuvo de responder | Número               |
| EXA_PRC_PREGUNTAS_OM              | Indica el porcentaje de preguntas que el/la estudiante se abstuvo de responder | Número           |
| EXA_N_RTAS_CORR                   | Número de respuestas correctas asociadas al grupo de análisis | Número                    |
| EXA_N_RTAS_NOCORR                | Número de respuestas incorrectas asociadas al grupo de análisis | Número                  |
| EXA_PRC_RTAS_CORR                 | Indica el porcentaje de respuestas correctas asociadas al grupo de análisis | Número              |
| EXA_PRC_RTAS_NOCORR              | Indica el porcentaje de respuestas no correctas asociadas al grupo de análisis | Número         |
