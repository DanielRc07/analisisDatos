import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def calcular_scores(df):
    # Normalización de datos
    scaler = MinMaxScaler()
    df[['ingresos', 'numero_transacciones', 'tiempo_como_cliente']] = scaler.fit_transform(df[['ingresos', 'numero_transacciones', 'tiempo_como_cliente']])
    
    # Asignación de scores
    def score_ingresos(ingresos):
        if ingresos > 60000:
            return 0.4
        elif ingresos >= 50000:
            return 0.3
        elif ingresos >= 30000:
            return 0.2
        else:
            return 0.1

    def score_transacciones(transacciones):
        if 20 <= transacciones <= 30:
            return 0.3
        elif 10 <= transacciones < 20:
            return 0.2
        else:
            return 0.1

    def score_tiempo_cliente(tiempo):
        return 0.2 if tiempo > 2 else 0.1

    def score_historial_crediticio(historial):
        if historial == 'bueno':
            return 0.1
        elif historial == 'malo':
            return -0.1
        else:
            return 0.0

    # Aplicar las funciones de scoring
    df['score_ingresos'] = df['ingresos'].apply(score_ingresos)
    df['score_transacciones'] = df['numero_transacciones'].apply(score_transacciones)
    df['score_tiempo_cliente'] = df['tiempo_como_cliente'].apply(score_tiempo_cliente)
    df['score_historial_crediticio'] = df['historial_crediticio'].apply(score_historial_crediticio)

    # Cálculo del score final como una suma ponderada
    df['score'] = (
        df['score_ingresos'] * 0.4 +
        df['score_transacciones'] * 0.3 +
        df['score_tiempo_cliente'] * 0.2 +
        df['score_historial_crediticio'] * 0.1
    )

    # Eliminar columnas auxiliares
    df.drop(columns=['score_ingresos', 'score_transacciones', 'score_tiempo_cliente', 'score_historial_crediticio'], inplace=True)
    
    return df[['id_cliente', 'score']]
