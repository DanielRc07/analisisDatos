import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde un archivo Excel
data = pd.read_excel('data.xlsx')

# Limpiar los nombres de las columnas
data.columns = data.columns.str.strip()

# Convertir las columnas de fecha y hora en un solo datetime
data['datetime'] = pd.to_datetime(data[['AÑO', 'MES', 'DIA', 'HORA']].astype(str).agg('-'.join, axis=1), format='%Y-%m-%d-%H%M%S')

# Definir el intervalo de tiempo
hora_inicio = pd.to_datetime('09:48', format='%H:%M').time()
hora_fin = pd.to_datetime('09:56', format='%H:%M').time()

# Convertir columna HORA a formato de tiempo
data['HORA'] = pd.to_datetime(data['HORA'], format='%H%M%S').dt.time

# Filtrar datos por rango de tiempo
filtered_data = data[(data['HORA'] >= hora_inicio) & (data['HORA'] <= hora_fin)]

# Agrupar los datos filtrados
summary = filtered_data.groupby(['DEPOSITO_NUMERO_CUENTA']).agg(
    valor_total=('VALOR', 'sum'),
    numero_transacciones=('VALOR', 'count')
).reset_index()

# Preparar el gráfico
plt.figure(figsize=(12, 8))

# Crear un gráfico de barras donde el eje X sea el DEPOSITO_NUMERO_CUENTA y el eje Y sea el número de transacciones
bar_plot = sns.barplot(data=summary, x='DEPOSITO_NUMERO_CUENTA', y='numero_transacciones', palette='viridis')

# Etiquetas y título
plt.xlabel('Número de Cuenta')
plt.ylabel('Número de Transacciones')
plt.title(f'Fraccionamientos de Transacciones entre {hora_inicio} y {hora_fin}')

# Ajustar el eje Y para mostrar el número total de transacciones
max_transacciones = summary['numero_transacciones'].max()
plt.ylim(0, max_transacciones + 1)  # Ajuste del límite superior para el número de transacciones

# Mostrar el total de valores en cada barra
for p in bar_plot.patches:
    cuenta = summary['DEPOSITO_NUMERO_CUENTA'].iloc[int(p.get_x() // p.get_width())]
    valor_total = summary.loc[summary['DEPOSITO_NUMERO_CUENTA'] == cuenta, 'valor_total'].values[0]
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2., height, f'${valor_total:,.2f}', ha='center', va='bottom', color='black')

# Ajustar los ticks del eje Y para mostrar desde 0 hasta el número máximo de transacciones
plt.gca().set_yticks(range(0, max_transacciones + 1, max(1, max_transacciones // 10)))  # Ajuste dinámico de ticks

plt.tight_layout()
plt.show()

# Guardar los resultados a un archivo Excel
summary.to_excel('fraccionamientos.xlsx', index=False)
