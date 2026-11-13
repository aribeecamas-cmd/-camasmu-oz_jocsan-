#nombre: jocsan aribee camas muñoz
#ejercicio: 1 el semaforo pide al usurio el color de un semaforo y muestra la accion que debe realizar el conductor. el programa debe aceptar el color en mayusculas o minusculas, es decir rojo, rojo y ROJO son el mismo caso

color = input("Ingresa el color del semáforo: ")
color = color.lower()

if color == "rojo":
    print("Alto total")
elif color == "amarillo":
    print("Precaución, disminuye la velocidad")
elif color == "verde":
    print("Puedes avanzar")
else:
    print("Color no válido")