# Nombre: jocsan aribee camas muñoz
# Ejercicio 4: Piedra, papel o tijera Dos jugadores escriben su jugada: piedra, papel o tijera. El programa indica quién gana el round.piedra vence a tijera vence a papel vence a piedra Si ambos escriben lo mismo, el resultado es «Empate». Si alguna de las dos jugadas no es piedra, papel o tijera, muestra «Jugada no válida» antes de comparar. Al final imprime uno de estos mensajes: «Gana el jugador 1», «Gana el jugador 2», «Empate» o «Jugada no válida». Puedes normalizar lo que escriben los jugadores con lower().

jugador1 = input("Jugador 1, escribe piedra, papel o tijera: ")
jugador2 = input("Jugador 2, escribe piedra, papel o tijera: ")

jugador1 = jugador1.lower()
jugador2 = jugador2.lower()

if (jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera") or (jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera"):
    resultado = "Jugada no válida"

elif jugador1 == jugador2:
    resultado = "Empate"

elif jugador1 == "piedra":
    if jugador2 == "tijera":
        resultado = "Gana el jugador 1"
    else:
        resultado = "Gana el jugador 2"

elif jugador1 == "papel":
    if jugador2 == "piedra":
        resultado = "Gana el jugador 1"
    else:
        resultado = "Gana el jugador 2"

else:
    if jugador2 == "papel":
        resultado = "Gana el jugador 1"
    else:
        resultado = "Gana el jugador 2"

print(resultado)