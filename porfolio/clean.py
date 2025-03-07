import pandas as pd
import numpy as np

def limpiar_datos(file_path):
    # Cargar el dataset
    df = pd.read_csv(file_path)
    
    # Eliminar filas duplicadas
    df = df.drop_duplicates()
    
    # Corregir tipos de datos
    df["Edad"] = pd.to_numeric(df["Edad"], errors='coerce')
    
    # Normalizar texto en respuestas de Sí/No
    df.replace({"si": "Sí", "Si": "Sí", "NO": "No", "no": "No"}, inplace=True)
    
    # Llenar valores nulos en columnas clave con "Desconocido"
    columnas_relleno = ["Género", "Residencia", "Ocupación", "Situación Habitacional"]
    df[columnas_relleno] = df[columnas_relleno].fillna("Desconocido")
    
    # Convertir Frecuencia de Asistencia a formato estándar
    df["Frecuencia de Asistencia"].replace({"Esporádica (3)": "Esporádica"}, inplace=True)
    
    # Convertir valores categóricos en números si aplica
    df["Suficiencia de Alimentos (1-5)"] = pd.to_numeric(df["Suficiencia de Alimentos (1-5)"], errors='coerce')
    df["Calidad de Alimentos (1-5)"] = pd.to_numeric(df["Calidad de Alimentos (1-5)"], errors='coerce')
    
    # Guardar dataset limpio
    clean_file_path = "./encuesta_limpia.csv"
    df.to_csv(clean_file_path, index=False)
    
    return clean_file_path

# Ruta del dataset sucio
dirty_file = "./encuesta_sucia.csv"
clean_file = limpiar_datos(dirty_file)
print(f"Archivo limpio guardado en: {clean_file}")
