# Nombre: jocsan aribee camas muñoz
# Ejercicio 2: La pizzería pide el tamaño de la pizza y la cantidad que esea el cliente. los precios son 1 =personal:$99,2 = mediana:$149,3 = familiar:$199. si el tamaño no esta entre 1 y 3 muestra tamaño no valido y no calcules el total. si el cliente lleva tre pizzas o mas se le aplica un descuento del 10% al total. muestra el total a pagar con dos decimales.

tamaño = int(input("Ingresa el tamaño de la pizza (1, 2 o 3): "))
cantidad = int(input("¿Cuántas pizzas deseas?: "))

if tamaño == 1:
    precio = 99
elif tamaño == 2:
    precio = 149
elif tamaño == 3:
    precio = 199
else:
    precio = 0
    print("Tamaño no válido")

if tamaño >= 1 and tamaño <= 3:
    if cantidad > 0:
        total = precio * cantidad

        if cantidad >= 3:
            total = total * 0.90

        print("Total a pagar: $", format(total, ".2f"))
    else:
        print("Cantidad no válida")