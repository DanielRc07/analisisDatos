import pandas as pd

def procesar_reportes(ruta_archivo):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_archivo)

    # Mostrar el DataFrame para verificar los datos
    print("Datos cargados:")
    print(df.head())
    
    # Verificar las columnas del DataFrame
    print("\nColumnas en el DataFrame:")
    print(df.columns)

    # Filtrar solo los reportes de fraccionamiento
    df_fraccionamiento = df[df['Subtipo mala práctica'] == 'Fraccionamiento']
    
    # Verificar el DataFrame filtrado
    print("\nDatos de fraccionamiento:")
    print(df_fraccionamiento.head())

    # Contar el número de reportes de fraccionamiento por CB
    conteo_fraccionamiento = df_fraccionamiento.groupby('Código Punto')['Mala práctica'].count()
    
    # Verificar el conteo de fraccionamiento
    print("\nConteo de reportes de fraccionamiento por CB:")
    print(conteo_fraccionamiento)

    # Identificar los CB que tienen 4 o más reportes de fraccionamiento
    alertas = conteo_fraccionamiento[conteo_fraccionamiento >= 4]
    
    # Verificar las alertas
    print("\nAlertas (CB con 4 o más reportes de fraccionamiento):")
    print(alertas)

    # Crear un DataFrame con el consolidado de reportes
    consolidado = pd.DataFrame({
        'Código Punto': conteo_fraccionamiento.index,
        'Número de Reportes de Fraccionamiento': conteo_fraccionamiento.values
    })
    
    # Verificar el DataFrame consolidado
    print("\nDataFrame consolidado:")
    print(consolidado)

    # Crear un DataFrame con las alertas
    consolidado_alertas = pd.DataFrame({
        'Código Punto': alertas.index,
        'Número de Reportes de Fraccionamiento': alertas.values,
        'Alerta': 'Sí'
    })
    
    # Verificar el DataFrame de alertas
    print("\nDataFrame de alertas:")
    print(consolidado_alertas)

    # Guardar el consolidado y las alertas en un archivo Excel
    with pd.ExcelWriter('consolidado_reportes.xlsx') as writer:
        consolidado.to_excel(writer, sheet_name='Consolidado', index=False)
        consolidado_alertas.to_excel(writer, sheet_name='Alertas', index=False)

if __name__ == "__main__":
    # Ruta del archivo Excel
    ruta_archivo = 'data.xlsx'
    
    # Procesar reportes y generar alertas
    procesar_reportes(ruta_archivo)
