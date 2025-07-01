🏡 Limpieza y Transformación de Datos - Encuesta sobre Subsidios Habitacionales
📌 Descripción del Proyecto
Este proyecto forma parte de un portafolio de Ciencia de Datos, y se centra en la limpieza y transformación de un conjunto de datos provenientes de una encuesta sobre subsidios habitacionales.
El objetivo es procesar datos desordenados utilizando técnicas de preprocesamiento, garantizando así la calidad de los datos para futuros análisis.

📊 Estructura del Dataset
El conjunto de datos original contiene información sobre personas encuestadas y sus condiciones habitacionales. Algunas columnas incluidas:

Persona: Identificador único del encuestado.
Edad: Edad del encuestado.
Género: Identidad de género.
Residencia: Lugar de residencia.
Ocupación: Situación laboral.
Situación Habitacional: Condición de vivienda (ej. "Calle", "Alquilada").
Conoce Subsidios: Indica si conoce los subsidios disponibles.
Solicitó Subsidios: Indica si solicitó algún subsidio.
Recibió Subsidios: Indica si recibió algún subsidio.
Suficiencia de Alimentos (1-5): Escala que mide cuán suficiente es su alimentación.
Calidad de Alimentos (1-5): Escala que mide la calidad de los alimentos disponibles.
🛠️ Proceso de Limpieza de Datos
El conjunto de datos original presentaba inconsistencias, valores faltantes y problemas de formato. Se aplicaron los siguientes pasos:

✅ Eliminación de Duplicados: Se eliminaron entradas repetidas.
✅ Corrección de Tipos de Datos: Conversión correcta de edades y escalas numéricas.
✅ Normalización de Respuestas: Unificación de respuestas como "Sí"/"No".
✅ Manejo de Valores Faltantes: Relleno con "Desconocido" en columnas clave.
✅ Estandarización de Categorías: Corrección ortográfica y coherencia en categorías.
🚀 Cómo Ejecutar el Código
Seguí estos pasos para limpiar el dataset:

1️⃣ Cloná este repositorio o descargá los archivos.
2️⃣ Asegurate de tener el archivo encuesta_sucia.csv en el mismo directorio que el script.
3️⃣ Instalá las dependencias necesarias:

pip install pandas numpy

Ejecuta: python clean.py
