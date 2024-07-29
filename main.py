from preparacionDatos import cargar_y_preparar_datos
from analisisDescriptivo import analisis_descriptivo
from modeloScore import calcular_scores

def main():
    # Cargar y preparar los datos
    df = cargar_y_preparar_datos('dataCliente.csv')
    
    # Análisis descriptivo
    analisis_descriptivo(df)
    
    # Calcular scores
    df_scores = calcular_scores(df)
    
    # Mostrar resultados
    print(df_scores)

if __name__ == "__main__":
    main()
