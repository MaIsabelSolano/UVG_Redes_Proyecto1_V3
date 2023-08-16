from getpass import getpass
from prettytable import PrettyTable

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
        print("\nIngrese los datos que se le solicitan a continuación:\n")
        user = input("Nombre de usuario: ")
        password = getpass("Contraseña: ")

        print("\nSon estos los datos con los que quiere iniciar sesión?")
        cont = input("(Y/n) ")

        if (cont == "Y" or cont == 'y'): return user, password


def functions():
    valid_options = range(1, 10) # [1, 9]

    stop = False
    while(not stop):
        print("\n__________________________")
        print("\nIngrese el número de la opción que desea realizar: ")
        print("\n1) Mostrar todos los contactos y su estado")
        print("\n2) Agregar un usuario a los contactos")
        print("\n3) Chatear con un usuario/contacto")
        print("\n4) Participar en conversaciones grupales")
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

def print_contacts(contacts):
    x = PrettyTable()
    x.field_names = ["Contacto", "Estado", "Mensaje de estado"]
    for c in contacts:
        x.add_row([c[0], c[1], c[2]])

    print(x)

def select_contact(contacts):
    # crear la tabla
    x = PrettyTable()
    x.field_names = ["#", "Contacto"]
    for i in range(len(contacts)):
        x.add_row([i + 1, contacts[i]])
    x.add_row([len(contacts) + 1, "Escribir usuario"])
    x.add_row([len(contacts) + 2, "CANCELAR"])

    choosing = True 
    while(choosing):
        print("\nElige el contacto al que le quieres enviar mensaje")
        print(x)

        try:
            op_ = int(input("No. del contacto/opción: "))

            if (op_ - 1 in range(len(contacts))):
                return contacts[op_ - 1]
            
            elif (op_ == len(contacts) + 1):
                cont = input("Ingrese el usuario: ")
                return cont 
            
            elif (op_ == len(contacts) + 2): 
                print("Cancelando enviar mensaje")
                return None
            
            else:
                print("\n[[Opción inválida, pruebe nuevamente]]")

        except:
            print("\n[[Opción inválida, pruebe nuevamente]]")

def print_messages(list_m):

    if len(list_m) == 0:
        # No hay mensajes que imprimir
        print("\nBuzón de mensajes vacío")
        return 

    for m in list_m:
        print(m)

def select_presence():

    choosing = True

    while(choosing):

        possibleStatus = ['chat', 'xa', 'away', 'dnd']

        print("\nPor favor elija el status que al cual desea cambiar")
        print("\n1) Disponible")
        print("\n2) Ocupado")
        print("\n3) Ausente")
        print("\n4) No molestar")

        try:

            opStat = int(input("\nNo. de la opción: "))
            if opStat in range(1, 5):
                # definir mensaje
                print("\nAhora escriba el mesaje que desea")
                status_m = input("\nNuevo estado:")

                return possibleStatus[opStat - 1], status_m

            else:
                print("\n[[Opción inválida, pruebe nuevamente]]")

        except:
            print("\n[[Opción inválida, pruebe nuevamente]]")


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

        

