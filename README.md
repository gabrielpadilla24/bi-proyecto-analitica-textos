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
