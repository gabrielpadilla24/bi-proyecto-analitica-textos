# Etapa 1 - Proyecto Inteligencia de Negocios  
### Grupo 27  
**Autores:** Gabriel Padilla, Juan Pablo Rivera  

---

## Sección 1. (20%) Documentación del proceso de aprendizaje automático  

Para esta sección se completó el **Canvas de Aprendizaje Automático** siguiendo la adaptación de *OWNML MACHINE LEARNING CANVAS* (CRISP-ML(Q): The ML Lifecycle Process).  

📎 **Canvas del proyecto (PDF):**  
[Descargar Canvas de Aprendizaje Automático](./canvas_model.pdf)

---


## Sección 2. (20%) Entendimiento y preparación de los datos

En esta etapa se realizó un **perfilamiento de los datos** con el fin de analizar su calidad, consistencia y completitud. El proceso incluyó las siguientes tareas:

1. **Exploración inicial de los datos**  
   - Identificación de columnas relevantes para el problema de clasificación de texto.  
   - Revisión de valores nulos, duplicados y distribución de las variables.  
   - Análisis descriptivo para entender la representatividad de cada clase.

2. **Calidad de los datos**  
   - Se verificó la existencia de inconsistencias en los registros (ejemplo: textos vacíos o mal codificados).  
   - Se eliminaron valores duplicados y se estandarizaron entradas inconsistentes.  
   - Se revisó la distribución de las clases para evaluar si existía desbalance.

3. **Tratamiento de los datos**  
   - **Limpieza de texto:** conversión a minúsculas, eliminación de caracteres especiales y stopwords.  
   - **Tokenización:** segmentación del texto en palabras para facilitar el análisis.  
   - **Lematización/Stemming:** reducción de las palabras a su forma raíz para mejorar la representación.  
   - **Vectorización:** uso de representaciones como *TF-IDF* para transformar el texto en vectores numéricos.  

4. **Transformaciones aplicadas según los algoritmos seleccionados**  
   - Para **Naive Bayes Multinomial**, se empleó TF-IDF como representación de texto, dado que este modelo se beneficia de frecuencias normalizadas.  
   - Para **Regresión Logística** y **SVM**, también se utilizó TF-IDF, asegurando que las variables tuvieran la misma escala para optimizar la convergencia y precisión.  

5. **Preparación final de los datos**  
   - División del dataset en **conjunto de entrenamiento y prueba** con una proporción de 80/20.  
   - Validación cruzada en la etapa de modelado para asegurar generalización.  
   - Exportación de los datos procesados para su uso en los diferentes algoritmos.  

En conclusión, el proceso de **entendimiento y preparación de los datos** permitió garantizar que la información utilizada en el modelado fuera **limpia, balanceada y transformada** adecuadamente, alineada con las técnicas y algoritmos definidos para resolver el problema planteado.

---

## Sección 3. (20%) Modelado y selección del modelo final

En esta etapa se entrenaron y evaluaron tres algoritmos de clasificación de texto: **Naive Bayes Multinomial**, **Regresión Logística** y **SVM (Support Vector Machine)**. El proceso incluyó los siguientes pasos:

1. **Definición de los modelos a entrenar**
   - **Naive Bayes Multinomial (NB):** Modelo probabilístico simple basado en la independencia condicional de las palabras.  
   - **Regresión Logística (LR):** Modelo lineal discriminativo utilizado para clasificación binaria y multiclase, optimizado mediante gradiente descendente.  
   - **SVM (Support Vector Machine):** Modelo que busca un hiperplano óptimo para separar las clases maximizando el margen entre ellas.

2. **Pipeline de entrenamiento**
   - Transformación de texto mediante **TF-IDF** para todos los modelos.  
   - División del dataset en **conjunto de entrenamiento (80%) y prueba (20%)**.  
   - Validación cruzada para evaluar estabilidad del rendimiento.  
   - Optimización de hiperparámetros en Regresión Logística y SVM.  

3. **Resultados obtenidos (métrica F1-macro)**

| Modelo               | F1-macro |
|-----------------------|----------|
| Naive Bayes          | 0.9353   |
| Regresión Logística  | 0.9577   |
| SVM                  | 0.9631   |

4. **Interpretación de resultados**
   - **Naive Bayes:** Alcanzó un rendimiento aceptable (F1 ≈ 0.93), aunque con limitaciones en clases minoritarias.  
   - **Regresión Logística:** Mejoró notablemente el rendimiento (F1 ≈ 0.96), mostrando balance entre precisión y recall.  
   - **SVM:** Obtuvo el mejor desempeño (F1 ≈ 0.963), con mayor capacidad para distinguir entre clases y reduciendo errores en la matriz de confusión.

5. **Selección del modelo final**
   - Se seleccionó **SVM (Support Vector Machine)** como el modelo final debido a:
     - Su mayor **F1-macro**.  
     - Balance óptimo entre precisión y recall.  
     - Mejor generalización y robustez frente a casos ambiguos.  

Este modelo será utilizado en las siguientes etapas del proyecto para la implementación y validación final.

### Contribución de los integrantes
- **Naive Bayes Multinomial:** desarrollado por **Juan Pablo Rivera**.  
- **Regresión Logística:** desarrollada por **Gabriel Padilla**.  
- **SVM:** implementado y ajustado en conjunto por **Gabriel Padilla y Juan Pablo Rivera**.

---

---

## Sección 5. (8%) Trabajo en equipo

### Roles y responsabilidades
- **Gabriel Padilla**  
  - Rol: Líder de proyecto y Líder de negocio.  
  - Tareas realizadas: Implementación del modelo de **Regresión Logística**, participación conjunta en el modelo **SVM**, procesamiento de los datos, apoyo en la documentación y estructuración de la wiki.  
  - Tiempo dedicado: ~10 horas.  
  - Retos enfrentados: Coordinación general del proyecto, reinstalación del kernel de Jupyter y ajuste de dependencias.  
  - Uso de ChatGPT: Comprensión del problema, desglose de la metodología, apoyo en la escritura en formato Markdown y estructuración de la wiki. Uso de GitHub Copilot para apoyo en sintaxis de programación.

- **Juan Pablo Rivera**  
  - Rol: Líder de datos y Líder de analítica.  
  - Tareas realizadas: Implementación del modelo de **Naive Bayes**, participación conjunta en el modelo **SVM**, limpieza de datos, apoyo en la documentación y validación de resultados.  
  - Tiempo dedicado: ~10 horas.  
  - Retos enfrentados: Problemas con librerías en el entorno, reinstalación del kernel de Jupyter y resolución de inconsistencias de datos.  
  - Uso de ChatGPT: Consulta de algoritmos, guía del modelado, explicación de métricas y apoyo en la documentación en Markdown. Uso de GitHub Copilot para asistencia en programación.

### Distribución de puntos
La distribución de 100 puntos entre los integrantes se realizó de manera equitativa, dado que ambos contribuyeron en partes complementarias del proyecto:

- Gabriel Padilla: **50 puntos**  
- Juan Pablo Rivera: **50 puntos**

### Puntos a mejorar
- Optimizar el tiempo de reuniones y coordinación.  
- Mejorar la organización del repositorio para separar claramente código, datos y documentación.  
- Ampliar el uso de métricas adicionales para validar los modelos.  

