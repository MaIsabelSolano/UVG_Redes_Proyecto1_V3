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
import xmpp
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
            jid, passw = login_v()
            
            newUser = xmpp.JID(jid)

            newUser_ = xmpp.Client(newUser.getDomain(), debug=[])
            newUser_.connect()
            
            res = bool(
                xmpp.features.register(
                newUser_, 
                newUser.getDomain(), 
                {
                    'username': newUser.getNode(),
                    'password': passw
                })
            )

            if res:
                print("\nCuenta creada con éxito")
            else:
                print("\nOcurrió un error al momento de crear la cuenta")

            print("Por favor seleccione el la primera opción para ingresar con sus nuevos datos")

        elif (option == '3'):
            # salir
            programRunning = False



if __name__ == '__main__':
    main()

