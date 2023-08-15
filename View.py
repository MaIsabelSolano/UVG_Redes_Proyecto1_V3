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

