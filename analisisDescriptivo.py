import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analisis_descriptivo(df):
    # Estadísticas descriptivas básicas
    print("Estadísticas Descriptivas:")
    print(df[['ingresos', 'numero_transacciones', 'tiempo_como_cliente']].describe())
    
    # Visualización de la distribución de ingresos
    plt.figure(figsize=(10, 6))
    sns.histplot(df['ingresos'], bins=20, kde=True)
    plt.title('Distribución de Ingresos')
    plt.xlabel('Ingresos')
    plt.ylabel('Score')
    plt.savefig('distribucion_ingresos.png')  # Guardar gráfico
    plt.close()

    # Visualización de la distribución del número de transacciones
    plt.figure(figsize=(10, 6))
    sns.histplot(df['numero_transacciones'], bins=20, kde=True)
    plt.title('Distribución del Número de Transacciones')
    plt.xlabel('Número de Transacciones')
    plt.ylabel('Score')
    plt.savefig('distribucion_transacciones.png')  # Guardar gráfico
    plt.close()

    # Visualización de la distribución del tiempo como cliente
    plt.figure(figsize=(10, 6))
    sns.histplot(df['tiempo_como_cliente'], bins=10, kde=True)
    plt.title('Distribución del Tiempo como Cliente')
    plt.xlabel('Tiempo como Cliente (años)')
    plt.ylabel('Score')
    plt.savefig('distribucion_tiempo_cliente.png')  # Guardar gráfico
    plt.close()
