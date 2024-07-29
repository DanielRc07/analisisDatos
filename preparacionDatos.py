import pandas as pd

def cargar_y_preparar_datos(ruta_archivo):
    # Cargar datos especificando la codificación
    df = pd.read_csv(ruta_archivo, encoding='ISO-8859-1')
    
    # Limpieza de datos
    df['ingresos'].fillna(df['ingresos'].median(), inplace=True)
    df['historial_crediticio'].fillna(df['historial_crediticio'].mode()[0], inplace=True)
    df['numero_transacciones'].fillna(df['numero_transacciones'].median(), inplace=True)
    
    # Codificación de historial crediticio
    df['historial_crediticio_bueno'] = (df['historial_crediticio'] == 'bueno').astype(int)
    df['historial_crediticio_malo'] = (df['historial_crediticio'] == 'malo').astype(int)
    df['historial_crediticio_regular'] = (df['historial_crediticio'] == 'regular').astype(int)
    
    return df
