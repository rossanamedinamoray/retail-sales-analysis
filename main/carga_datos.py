# Carga de datos
import numpy as np
# Cargar los datos del archivo CSV
file_path = 'C:\\Users\\rnma\\Documents\\GitHub\\retail-sales-analysis\\data\\retail_sales_dataset.csv'
data = np.genfromtxt(file_path, delimiter=',', dtype=str) #en la importación se genera array de tipo string de todos los datos

# Preprocesamiento: eliminar el encabezado y convertir las columnas numéricas
header = data[0]  # Extraer el encabezado
data = data[1:]  # Eliminar el encabezado

# Convertir las columnas relevantes a tipos numéricos
data_numeric = data.copy()
data_numeric[:, 6] = data_numeric[:, 6].astype(float)  # Cantidad
data_numeric[:, 7] = data_numeric[:, 7].astype(float)  # Precio por Unidad
data_numeric[:, 8] = data_numeric[:, 8].astype(float)  # Monto Total

# 1. Agrupar ventas diarias por producto
# Obtener todas las categorías de productos únicas
product_categories = np.unique(data_numeric[:, 5])  # La columna 5 es la categoría del producto
# Obtener todas las fechas únicas en el dataset
unique_dates = np.unique(data_numeric[:, 1])  # La columna 1 es la fecha de venta

# Crear un diccionario para almacenar las ventas por producto y por día
sales_by_product_by_day = {category: {} for category in product_categories}

# Agrupar las ventas de cada producto por fecha
for category in product_categories:
    # Filtrar las ventas del producto actual
    product_sales = data_numeric[data_numeric[:, 5] == category]
    
    # Iterar sobre cada fecha única
    for date in unique_dates:
        # Filtrar las ventas de este producto en la fecha actual
        sales_on_date = product_sales[product_sales[:, 1] == date]
        
        # Sumar el total de ventas en esa fecha
        total_sales_on_date = sales_on_date[:, 8].astype(float).sum()  # No es necesario usar astype(float)
        
        # Guardar las ventas totales en esa fecha para el producto actual
        sales_by_product_by_day[category][date] = total_sales_on_date

# 2. Calcular el promedio de ventas diarias por producto
average_sales_by_product = {}

for category in product_categories:
    # Obtener las ventas por día para este producto
    sales_per_day = list(sales_by_product_by_day[category].values())
    
    # Calcular el promedio de ventas diarias
    average_sales_by_product[category] = np.mean(sales_per_day)

# 3. Identificar el producto con mayores y menores ventas totales
total_sales_by_product = {category: sum(sales_by_product_by_day[category].values()) for category in product_categories}
product_with_max_sales = max(total_sales_by_product, key=total_sales_by_product.get)
product_with_min_sales = min(total_sales_by_product, key=total_sales_by_product.get)

# 4. Filtrar las ventas de un producto específico (ejemplo: 'Electronics')
product_filter = 'Electronics'
filtered_by_product = data_numeric[data_numeric[:, 5] == product_filter]

# 5. Operaciones de suma, resta, multiplicación y división en los datos
# Sumar las ventas totales del producto 'Electronics'
sum_sales_electronics = filtered_by_product[:, 8].astype(float).sum()

# Restar un valor fijo (ejemplo: $1000) de cada venta de 'Electronics'
adjusted_sales_electronics = filtered_by_product[:, 8].astype(float) - 1000

# Multiplicar cada venta por un 10% adicional
increased_sales_electronics = filtered_by_product[:, 8].astype(float) * 1.1

# Calcular el precio por unidad (Monto Total / Cantidad)
price_per_unit_electronics = filtered_by_product[:, 8].astype(float) / filtered_by_product[:, 6].astype(float)

# Imprimir resultados
print("Promedio de ventas diarias por producto:", average_sales_by_product)
print("Producto con mayores ventas totales:", product_with_max_sales)
print("Producto con menores ventas totales:", product_with_min_sales)
print("Suma total de ventas de 'Electronics':", sum_sales_electronics)
print("Ventas ajustadas de 'Electronics' (primeras 5 transacciones):", adjusted_sales_electronics[:5])
print("Ventas con un incremento del 10% (primeras 5 transacciones):", increased_sales_electronics[:5])
print("Precio por unidad de 'Electronics' (primeras 5 transacciones):", price_per_unit_electronics[:5])