#* Diseña un programa que reciba una cantidad total de dulces y un número de niños. Debe calcular cuántos dulces le tocan a cada uno de forma equitativa y cuántos dulces sobran en la caja.

dulces = int(input("Ingresa la cantidad total de dulces: "))
ninos = int(input("Ingresa el número de niños: "))

reparto = dulces // ninos
sobrantes = dulces % ninos

print("Dulces para cada niño:", reparto)
print("Dulces sobrantes:", sobrantes)