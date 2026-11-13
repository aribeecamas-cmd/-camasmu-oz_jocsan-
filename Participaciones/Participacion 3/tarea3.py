# Nombre: jocsan aribee camas muñoz
# Ejercicio 3: El año bisiesPide un año y determina si es bisiesto. Un año es bisiesto si es divisible entre 4, excepto los que terminan en 00: esos solo son bisiestos si además son divisibles entre 400.Muestra el resultado con el año incluido, por ejemplo «El año 2024 es bisiesto» o «El año 1900 no es bisiesto». Comprueba tu programa con 2024, 1900 y 2000.

año = int(input("Ingresa un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año", año, "es bisiesto")
        else:
            print("El año", año, "no es bisiesto")
    else:
        print("El año", año, "es bisiesto")
else:
    print("El año", año, "no es bisiesto")