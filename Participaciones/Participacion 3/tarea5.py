# Nombre: jocsan aribee camas muñoz
# Ejercicio 5: Acceso al sistema Un sistema escolar tiene registrado el usuario «alumno» con la contraseña «python2026». Pide ambos datos y muestra un mensaje según el caso.usuario y contraseña correctos: Bienvenido al sistema usuario correcto y contraseña distinta: Contraseña incorrectausuario distinto: Usuario no encontrado Resuélvelo con condicionales anidados: primero comprueba el usuario y, solo si existe, comprueba la contraseña.

usuario = input("Ingresa tu nombre de usuario: ")
contraseña = input("Ingresa tu contraseña: ")

if usuario == "alumno":
    if contraseña == "python2026":
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")
