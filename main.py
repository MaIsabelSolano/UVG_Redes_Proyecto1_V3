"""

Universidad del Valle de Guatemala
Facultad de Ingeniería
Departamento de Ciencias de la computación
Redes
Proyecto # 1
Maria Isabel Solano - 20504

"""

import sys, asyncio
import pyfiglet
from Client import *
from View import *

def main():
    titulo = pyfiglet.figlet_format("Chat XMPP")
    print("\n"+titulo)  

    programRunning = True
    while(programRunning):

        option = main_menu()

        if (option == '1'):
            # log in
            host, jid, passw = login_v()

            # connection

            # user menu
            in_usage = True
            while(in_usage):
                option_2 = functions()

                if (option_2 == 1): 
                    # Mostrar todos los contactos y su estado
                    0

                elif (option_2 == 2): 
                    # Agregar un usuario a los contactos
                    0

                elif (option_2 == 3): 
                    # Chatear con un usuario/contacto
                    0

                elif (option_2 == 4):
                    # Participar en conversaciones gurpales
                    0

                elif (option_2 == 5): 
                    # Definir mensaje de presencia
                    0

                elif (option_2 == 6): 
                    # Enviar/recibir notificaciones
                    0

                elif (option_2 == 7): 
                    # Enviar/Recibir archivos
                    0

                elif (option_2 == 8): 
                    # Eliminar cuenta del servidor
                    res = deleteAccout(jid)
                    if res == True:
                        # Eliminar cuenta
                        0

                elif (option_2 == 9): 
                    # Cerrar sesión
                    print("Cerrando sesión")
                    in_usage = False


        elif (option == '2'):
            # sign in
            host, jid, passw = login_v()
            print("Ahora ingrese con sus nuevos datos")

        elif (option == '3'):
            # quit
            programRunning = False


    # if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # user = "solano20504-V2"
    # password = "rede2023"
    # host = "alumchat.xyz"

    # client = Client(host, user, password)
    # client.register_plugin('xep_0030') # Service Discovery
    # client.register_plugin('xep_0199') # XMPP Ping
    # client.connect(disable_starttls=True, use_ssl=False)
    # client.process(forever=False)

    # client.send_message_("chat")

    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    


if __name__ == '__main__':
    main()

