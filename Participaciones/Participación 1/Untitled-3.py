#* Pide al usuario la longitud de tres lados. Verifica si se pueden formar un triángulo válido evaluando con operadores lógicos, que la suma de cualquier par de lados sea mayor que el tercer lado.

lado1 = float(input("Ingresa el primer lado: "))
lado2 = float(input("Ingresa el segundo lado: "))
lado3 = float(input("Ingresa el tercer lado: "))

triangulo = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

print("¿Se puede formar un triángulo?:", triangulo)