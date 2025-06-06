#Igrese el precio de un producto y el porcentaje de descuento. Muestre el precio final con desc

precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
print(f"El precio final es: {precio - (precio * descuento/100)}")