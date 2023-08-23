from getpass import getpass
from prettytable import PrettyTable
import tkinter as tk
from tkinter import messagebox


def main_menu():
    """
    Displays main meny for the user to either log in, sing up or quit

    Returns:
        str: User's option
    """

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
    """
    Obtains user input and verifys if the user think it's okayy

    Returns:
        str: user's user direction
        str: user's password
    """
    while(True):
        print("\n__________________________")
        print("\nIngrese los datos que se le solicitan a continuación:\n")
        user = input("Nombre de usuario: ")
        password = getpass("Contraseña: ")

        print("\nSon estos los datos con los que quiere iniciar sesión?")
        cont = input("(Y/n) ")

        if (cont == "Y" or cont == 'y'): return user, password


def functions():
    """
    Shows options to user and gets the input

    Returns:
        int: User's option between 1 and 10
    """
    valid_options = range(1, 11) # [1, 10]

    stop = False
    while(not stop):
        print("\n__________________________")
        print("\nIngrese el número de la opción que desea realizar: ")
        print("\n01) Mostrar todos los contactos y su estado")
        print("\n02) Agregar un usuario a los contactos")
        print("\n03) Chatear con un usuario/contacto")
        print("\n04) Ver información de un contacto")
        print("\n05) Participar en conversaciones grupales")
        print("\n06) Definir mensaje de presencia")
        print("\n07) Enviar/recibir notificaciones")
        print("\n08) Enviar/Recibir archivos")
        print("\n09) Eliminar cuenta del servidor")
        print("\n10) Cerrar sesión")

        try:
            op = int(input("\nNo.de opción: "))

            if (op in valid_options): 
                stop = True
                return op 
            else: print("\n[[Opción inválida, pruebe nuevamente]]")

        except:
            print("\n[[Opción inválida, pruebe nuevamente]]")

def print_pres(mess):
    print("\n=============================================")
    print(mess)
    print("=============================================\n")

def print_contacts(contacts):
    """
    Given a list of contacts, this function creates a table to display them

    Args:
        contacts (str): contact list
    """
    x = PrettyTable()
    x.field_names = ["Contacto", "Estado", "Mensaje de estado"]
    for c in contacts:
        x.add_row([c[0], c[1], c[2]])

    print(x)

def select_contact(contacts):
    """
    Given a list of contacts, this function creates a table to display them and give's the option
    to choose one of them

    Args:
        contacts (str): contact list

    Returns:
        str: chosen contact directon
    """
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

def select_contact_id(contacts):
    """
    Given a list of contacts, this function creates a table to display them and give's the option
    to choose one of them

    Args:
        contacts (str): contact list

    Returns:
        str: chosen contact number in the lsit
    """
    # crear la tabla
    x = PrettyTable()
    x.field_names = ["#", "Contacto"]
    for i in range(len(contacts)):
        x.add_row([i + 1, contacts[i]])
    x.add_row([len(contacts) + 1, "CANCELAR"])

    choosing = True 
    while(choosing):
        print("\nElige el contacto al que le quieres enviar mensaje")
        print(x)

        try:
            op_ = int(input("No. del contacto: "))

            if (op_ - 1 in range(len(contacts))):
                return op_ - 1
            
            elif (op_ == len(contacts) + 1): 
                print("Cancelando acción")
                return None
            
            else:
                print("\n[[Opción inválida, pruebe nuevamente]]")

        except:
            print("\n[[Opción inválida, pruebe nuevamente]]")

def print_contact_info(contact):
    """
    Given a list of contacts, and their information, it creates a table to display the information

    Args:
        contact (array): Contact and information
    """
    
    print("\n*****************************************************")
    print("Información del usuario:")
    print("Nombre: ", contact[0].split('@')[0])
    print("Host: ", contact[0].split('@')[1])
    print("Estado: ", contact[1])
    print("Mensaje de estado: ", contact[2])
    print("*****************************************************\n")

def print_messages(list_m):
    """
    Given a message, it prints all the messages
    """

    if len(list_m) == 0:
        # No hay mensajes que imprimir
        print("\nBuzón de mensajes vacío")
        return 

    for m in list_m:
        print(m)

def select_presence():
    """Gives the user the option to change presence message and presence status

    Returns:
        int: status id
        str: message status
    """

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
    """
    Delete Account verification. Assures that the user is deleted the current account and not
    mistaken it with another they might have 

    Args:
        jid (JID): User's JID

    Returns:
        bool: permition to delete account
    """
    print("\nEstá segur@ de que desea eliminar la cuenta? ")
    ver_1 = input("(Y/n) ")

    if (ver_1 == 'Y' or ver_1 == 'y'):
        # continue
        print(f"Como medida de seguridad, reescriba su usuario {jid}")
        ver_2 = input().lower()

        if (ver_2 == jid):
            print("\nInicio de proceso de eliminación de cuenta...")
            return True

        else:
            print("\nLa cuenta escrita no es igual a la cuenta actual. Pruebe más tarde")
            return False

    else: 
        return False
    
def popUp_ask(title, message):
    """
    Generates a pop um message user tkinter. Lets the user decline

    Args:
        title (str): Title of the action
        message (str): Actual message

    Returns:
        bool: Wheather or not accept incoming message
    """

    root = tk.Tk()

    res = messagebox.askokcancel(title, message)
    
    root.mainloop() 

    if res:
        return True
    else:
        return False
    

def popUp(title, message):
    """_summary_
    Generates a pop um message user tkinter

    Args:
        title (str): Title of the action
        message (str): Actual message
    """

    root = tk.Tk()

    messagebox.showinfo(title, message)

    # messagebox.showinfo(title, message)
    
    
    root.mainloop() 


        

