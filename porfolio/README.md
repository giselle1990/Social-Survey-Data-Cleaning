Limpieza y Transformación de Datos - Encuesta sobre Subsidios Habitacionales

Descripción del Proyecto

Este proyecto forma parte de un portafolio de Ciencia de Datos y tiene como objetivo la limpieza y transformación de un dataset con datos de una encuesta sobre subsidios habitacionales. Se trabajó con datos desordenados para aplicar técnicas de preprocesamiento y garantizar su calidad para futuros análisis.

Estructura del Dataset

El dataset original contiene información sobre personas encuestadas y sus condiciones habitacionales, incluyendo las siguientes columnas:

Persona: Identificador del encuestado.

Edad: Edad del encuestado.

Género: Identidad de género.

Residencia: Ubicación de residencia.

Ocupación: Tipo de empleo o situación laboral.

Situación Habitacional: Condición de vivienda (ej., "Calle", "Alquilada").

Conoce Subsidios: Indica si el encuestado conoce los subsidios disponibles.

Solicitó Subsidios: Indica si ha realizado solicitudes de subsidios.

Recibió Subsidios: Indica si recibió algún tipo de subsidio.

Suficiencia de Alimentos (1-5): Escala de suficiencia alimentaria.

Calidad de Alimentos (1-5): Escala de calidad de los alimentos consumidos.

Proceso de Limpieza

El dataset original contenía inconsistencias, valores nulos y problemas de formato que fueron corregidos con el siguiente proceso:

Eliminación de duplicados: Se eliminaron filas repetidas.

Corrección de tipos de datos: Se convirtieron edades y escalas numéricas al tipo de dato adecuado.

Normalización de respuestas: Se unificaron respuestas de "Sí"/"No" en un formato estándar.

Manejo de valores nulos: Se rellenaron valores vacíos en columnas clave con "Desconocido".

Estandarización de categorías: Se corrigieron errores en nombres de categorías.

Instrucciones para Ejecutar el Código

Para limpiar el dataset, sigue estos pasos:

Clonar este repositorio o descargar los archivos.

Asegurar que el dataset desordenado (encuesta_sucia.csv) esté en la misma carpeta que el script.

Instalar las dependencias necesarias con:

pip install pandas numpy

Ejecutar el script de limpieza:

python clean.py

El archivo limpio se generará como encuesta_limpia.csv.

Resultados Esperados

Tras la ejecución del script, se obtiene un dataset estructurado, con valores coherentes y listo para su análisis en estudios de impacto de subsidios habitacionales.