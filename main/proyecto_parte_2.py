import pandas as pd
import numpy as np

#Importamos nuestro archivo csv pero con formato string para no perder datos y elminamos el encabezado del archivo.
data = np.genfromtxt('C:\\Users\\rnma\\Documents\\GitHub\\retail-sales-analysis\\data\\retail_sales_dataset.csv', delimiter=',', dtype=str, skip_header=1) #en la importación se genera array de tipo string de todos los datos

# Carga de los datos
df = pd.read_csv('C:\\Users\\rnma\\Documents\\GitHub\\retail-sales-analysis\\data\\retail_sales_dataset.csv')
df.head(10)

# Exploración Inicial de los Datos
print(df.tail(5))
df.info()
df.describe()

# Inspección de los Datos
print(df.dtypes)
print(df['Gender'].value_counts())
print(df['Product Category'].unique())

# Filtrado de Datos
df_filtro_ventas = df[df['Total Amount'] > 50]
print(df_filtro_ventas)
df_filtro_precio = df[df['Price per Unit'] < 30]
print(df_filtro_precio)
df_query = df.query('`Total Amount` > 50 and `Product Category` == "Clothing"')
print(df_query)

# Slicing de Datos
df_filtro = df[['Product Category','Total Amount']]
print(df_filtro)
df_loc = df.loc[5:10, ['Gender', 'Age']]
print(df_loc)
df_iloc = df.iloc[:5, :3]
print(df_iloc)

# Parte 3 del proyecto

# Normalizamos la venta
df['Venta Normalizada'] = (df['Total Amount'] - df['Total Amount'].min()) / (df['Total Amount'].max() - df['Total Amount'].min())
print(df)

# Creamos una columna para identificar el rango etario y categorizamos la venta
# Definir los intervalos de edad
bins = [0, 20, 45, 65, np.inf]
labels = ['Jóvenes adultos', 'Adultos', 'Adultos mayores', 'Tercera edad']

# Crear la columna de rango etario
df['Rango Etario'] = pd.cut(df['Age'], bins=bins, labels=labels)

print(df)

# Definir los intervalos de ventas
bins = [0, 300, 1000, np.inf]
labels = ['Bajo', 'Medio', 'Alto']

# Crear la columna de rango etario
df['Categoria de Venta'] = pd.cut(df['Total Amount'], bins=bins, labels=labels)
print(df)

# Agrupacion por multiples columnas
df_agrupado = df.groupby(['Product Category', 'Categoria de Venta'])['Total Amount'].sum().reset_index()
print(df_agrupado)

# Agrupamos por 'Product Category' y calculamos valores estadisticos
agrupacion_estadistica = df.groupby('Product Category').agg({
    'Quantity': ['sum', 'mean', 'count', 'min', 'max', 'std', 'var'],
    'Price per Unit': ['sum', 'mean', 'count', 'min', 'max', 'std', 'var'],
    'Total Amount': ['sum', 'mean', 'count', 'min', 'max', 'std', 'var']
})

agrupacion_estadistica

# Calcular la media de cada grupo (Product Category) usando groupby y transform
media_por_categoria = df.groupby('Product Category')['Total Amount'].transform('mean')

# Calcular la desviación respecto a la media directamente
df['Desviación respecto a la media'] = df['Total Amount'] - media_por_categoria

# Mostrar los primeros resultados
df[['Product Category', 'Total Amount', 'Desviación respecto a la media']].head()

print(df)

# Parte 4 del proyecto

import matplotlib.pyplot as plt
import seaborn as sns

# Convertir la columna 'Date' a formato de fecha para el análisis temporal
df['Date'] = pd.to_datetime(df['Date'])

# 1. Estadísticas descriptivas
estadisticas_descriptivas = df.describe()

# 2. Histogramas y boxplots para variables numéricas clave
plt.figure(figsize=(16, 8))

# Histograma para Total Amount
plt.subplot(2, 2, 1)
sns.histplot(df['Total Amount'], bins=20, kde=True, color='skyblue')
plt.title('Distribución de Total Ganancias')

# Boxplot para Total Amount
plt.subplot(2, 2, 2)
sns.boxplot(x=df['Total Amount'], color='lightgreen')
plt.title('Boxplot de Total Ganancias')

# Histograma para Price per Unit
plt.subplot(2, 2, 3)
sns.histplot(df['Price per Unit'], bins=20, kde=True, color='orange')
plt.title('Distribución de Precio por Unida')

# Boxplot para Price per Unit
plt.subplot(2, 2, 4)
sns.boxplot(x=df['Price per Unit'], color='lightcoral')
plt.title('Boxplot de Precio por Unidad')

plt.tight_layout()
plt.show()

# 3. Gráfico de líneas para las tendencias de ventas a lo largo del tiempo
plt.figure(figsize=(15, 6))
df.groupby('Date')['Total Amount'].sum().plot(kind='line', marker='o', color='purple')
plt.title('Tendencia de ventas a lo largo del tiempo')
plt.ylabel('Total Ganancias')
plt.xlabel('Fechas')
plt.xticks(rotation=90)
plt.show()

# 4. Gráfico de dispersión para analizar la relación entre Total Amount y Quantity
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Quantity', y='Total Amount', data=df, color='blue')
plt.title('Relación entre Cantidad y Total Ganacias')
plt.xlabel('Cantidad')
plt.ylabel('Total Ganancias')
plt.show()

# 5. Combinación de histogramas y boxplots para visualizar la distribución de las ventas
plt.figure(figsize=(10, 6))

# Histograma y boxplot para Total Amount
sns.histplot(df['Total Amount'], kde=False, bins=20, color='lightblue', edgecolor='black')
sns.boxplot(x=df['Total Amount'], color='red', linewidth=2)
plt.title('Histograma y Boxplot combinados para Total Ganancias')
plt.show()

estadisticas_descriptivas