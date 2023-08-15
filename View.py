from getpass import getpass

def main_menu():

    "\nBienvenid@ al programa. A continuación ingrese el número de opción que desea realizar"

    while(True):
        print("\n1) Iniciar sesión")
        print("\n2) Crear una cuenta")
        print("\n3) Salir\n")

        op = input("No. de opción: ")

        if (op == '1'or op == '2' or op == '3'):
            return op 
        else:
            print("\n[[Opción inválida, pruebe nuevamente]]")


def login_v():
    while(True):
        print("\n__________________________")
        print("\nIngrese los datos que se le solicitan a continuación:")
        host = input("Servidor al que desea conectarse: ")
        user = input("Nombre de usuario: ")
        password = getpass("Contraseña: ")

        print("\nSon estos los datos con los que quiere iniciar sesión?")
        cont = input("(Y/n) ")

        if (cont == "Y" or cont == 'y'): return host, user, password


def functions():
    valid_options = range(1, 10) # [1, 9]

    stop = False
    while(not stop):
        print("\n__________________________")
        print("\nIngrese el número de la opción que desea realizar: ")
        print("\n1) Mostrar todos los contactos y su estado")
        print("\n2) Agregar un usuario a los contactos")
        print("\n3) Chatear con un usuario/contacto")
        print("\n4) Participar en conversaciones gurpales")
        print("\n5) Definir mensaje de presencia")
        print("\n6) Enviar/recibir notificaciones")
        print("\n7) Enviar/Recibir archivos")
        print("\n8) Eliminar cuenta del servidor")
        print("\n9) Cerrar sesión")

        try:
            op = int(input("\nNo.de opción: "))

            if (op in valid_options): 
                stop = True
                return op 
            else: print("\n[[Opción inválida, pruebe nuevamente]]")

        except:
            print("\n[[Opción inválida, pruebe nuevamente]]")


def addContact():
    0


def deleteAccout(jid):
    print("\nEstá segur@ de que desea eliminar la cuenta? ")
    ver_1 = input("(Y/n)")

    if (ver_1 == 'Y' or ver_1 == 'y'):
        # continue
        print("Como medida de seguridad, reescriba su usuario")
        ver_2 = input()

        if (ver_2 == jid):
            print("\nInicio de proceso de eliminación de cuenta")
            return False

        else:
            print("\nLa cuenta escrita no es igual a la cuenta actual. Pruebe más tarde")
            return False

    else: 
        return False

        

