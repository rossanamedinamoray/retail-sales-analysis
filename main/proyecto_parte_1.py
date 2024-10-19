import numpy as np

#Importamos nuestro archivo csv pero con formato string para no perder datos y elminamos el encabezado del archivo.
data = np.genfromtxt('C:\\Users\\rnma\\Documents\\GitHub\\retail-sales-analysis\\data\\retail_sales_dataset.csv', delimiter=',', dtype=str, skip_header=1) #en la importación se genera array de tipo string de todos los datos

# Mostramos el tipo de dato de nuestro array
type (data)

# Mostramos la dimensión de nuestro array
data.shape

# Verificar las categorías de la columna 5
ventas_totales = []
categoria = np.unique(data[:, 5])

for categoria in categoria:
    ventas_por_categoria = data[data[:, 5] == categoria]
    total_ventas = np.sum(ventas_por_categoria[:, 8].astype(float))
    print(f"Total ventas para la categoría {categoria}: {total_ventas}")
    ventas_totales.append((categoria,total_ventas))


# Calculamos el promedio de ventas diaria por categoria de productos
# Agrupamos primeramente los datos por fecha y categoria
data_por_fecha_categoria = data[:, [1, 5, 8]]
categorias_unicas = np.unique(data_por_fecha_categoria[:, 1])
# Calculamos el promedio de ventas diaras por categoria
for categoria in categorias_unicas:
    ventas_por_categoria = data_por_fecha_categoria[data_por_fecha_categoria[:, 1] == categoria]
    promedio_ventas_diarias = np.mean(ventas_por_categoria[:, 2].astype(float))
    print(f"Promedio de ventas diarias para la categoría {categoria}: {promedio_ventas_diarias}")


# Identifica las categorías de productos con mayores y menores ventas.
print(ventas_totales)
# Comparamos el total de las ventas para obtener el mayor y menor
venta_mayor = max(ventas_totales, key=lambda x: x[1])
print('La categoría con mayor venta es:', venta_mayor[0])
venta_menor = min(ventas_totales, key=lambda x: x[1])
print('La categoría con menor venta es:', venta_menor[0])


# Filtra los datos para mostrar solo las ventas de una categoría de producto específica.
filtro_categoria = data[data[:, 5] == 'Beauty']
print(filtro_categoria)

# Suma de cantidad de productos vendidos por categoria
categoria = np.unique(data[:, 5])
for categoria in categoria:
    ventas_por_categoria = data[data[:, 5] == categoria]
    cantidad_ventas = np.sum(ventas_por_categoria[:, 6].astype(float))
    print(f"Total ventas para la categoría {categoria}: {cantidad_ventas}")


# Monto y cantidad de productos vendidos por genero
genero = np.unique(data[:, 3])
for genero in genero:
    ventas_por_genero = data[data[:, 3] == genero]
    cantidad_ventas = np.sum(ventas_por_genero[:, 6].astype(float))
    monto_ventas = np.sum(ventas_por_genero[:, 8].astype(float))
    print(f"Total ventas para el genero {genero}: {cantidad_ventas} por el monto de: {monto_ventas}")


# Hallamos el promedio de edad de los clientes por categoria
categoria = np.unique(data[:, 5])
for categoria in categoria:
    ventas_por_categoria = data[data[:, 5] == categoria]
    promedio_edad = np.mean(ventas_por_categoria[:, 4].astype(float))
    promedio_de_compra = np.mean(ventas_por_categoria[:, 8].astype(float))
    print(f"Promedio de edad para la categoría {categoria}: {promedio_edad} con un gasto promedio de: {promedio_de_compra}")


