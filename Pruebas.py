import os 
import os.path
import getpass

while True:
    userp = input("Escriba el nombre del usuario personal:")
    while True:
        rootpass = getpass.getpass("Introduzca la contraseña del usuario "+userp+": ")
        rootpassver = getpass.getpass("Compruebe la contraseña del usuario "+userp+": ")
        if (rootpass == rootpassver):
            break
        else:
            print("Las contraseñas no coinciden, intentelo nuevamente.")
    print("¿Desea agregar otro usuario?")
    print("1.Si , 2. No")
    otrouser = input("Seleccione una opcion:")
    if otrouser != "1":
        break







