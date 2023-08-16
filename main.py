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

    # Evita el error Exception ignored from cffi callback <function _sock_state_cb at 0x000002C1CE3BF940>:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    titulo = pyfiglet.figlet_format("Chat XMPP")
    print("\n"+titulo)  

    programRunning = True
    while(programRunning):

        option = main_menu()

        if (option == '1'):
            # obtener usuario
            jid, passw = login_v()

            # conexión
            client = Client(jid, passw)
            client.connect(disable_starttls=True, use_ssl=False)
            client.process(forever=False)


        elif (option == '2'):
            # registrarse
            host, jid, passw = login_v()
            print("Ahora ingrese con sus nuevos datos")

        elif (option == '3'):
            # salir
            programRunning = False



if __name__ == '__main__':
    main()

