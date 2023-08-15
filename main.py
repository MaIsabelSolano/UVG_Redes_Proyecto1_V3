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
            host, jid, passw = login_v()

        elif (option == '2'):
            host, jid, passw = login_v()

        elif (option == '3'):
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

