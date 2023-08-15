import slixmpp
import asyncio

from View import *

class Client(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)

        self.name = jid.split('@')[0]
        self.host = jid.split('@')[1]
        

        # Obtenido de ejemplos de slixmpp
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0004') # Data Forms
        self.register_plugin('xep_0060') # PubSub
        self.register_plugin('xep_0199') # XMPP Ping

        self.add_event_handler("session_start", self.start)
        self.add_event_handler('presence', self.presence_handler)

    # Funciones necesarias para el funcionamiento correcto del cliente

    async def start(self, event):
        print("start")

        self.send_presence()
        await self.get_roster()

        asyncio.create_task(self.user_menu())

    
    async def presence_handler(self, presence):

        if presence['type'] == 'subscribe':
            try:
                self.send_presence_subscription(pto=presence['from'], ptype='subscribe')
                await self.get_roster()


            except:
                print("Hubo un error en el presence handler")



    # Funciones para el usuario

    async def user_menu(self):
        print("menu")
        # user menu
        while(self.is_connected):

            option_2 = functions()

            if (option_2 == 1): 
                # Mostrar todos los contactos y su estado
                0

            elif (option_2 == 2): 
                # Agregar un usuario a los contactos
                0

            elif (option_2 == 3): 
                # Chatear con un usuario/contacto
                await self.send_message_("echobot@alumchat.xyz", "clue")

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
                res = deleteAccout(self.jid)
                if res == True:
                    # Eliminar cuenta
                    0

            elif (option_2 == 9): 
                # Cerrar sesión
                print("Cerrando sesión")
                self.disconnect()


    async def send_message_(self, cont, message):
        print("se envió ", message)
        await self.get_roster()
        self.send_message(mto=cont, 
                          mbody=message, 
                          mtype='chat')
        