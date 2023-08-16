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
                await self.contacts_status()

            elif (option_2 == 2): 
                # Agregar un usuario a los contactos
                0

            elif (option_2 == 3): 
                # Chatear con un usuario/contacto
                await self.send_message_()

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
                self.is_connected = False

    # option # 1
    async def contacts_status(self):
        # listado de contactos
        await self.get_roster()
        conts = self.client_roster
        contacts = [c for c in conts.keys()]
        contactsFullInfo = []

        if (len(contacts) > 0):
            for contact in contacts:

                sh = 'avaliable'
                st = ''

                # info del contacto
                info = conts.presence(contact)

                for answ, pres in info.items():
                    if pres['show']:
                        sh = pres['show']
                    if pres['status']:
                        st = pres['status']

                contactsFullInfo.append([contact, sh, st])

            print_contacts(contactsFullInfo)
                

        else:
            print("No se han encontrado contactos")
        

    # opción # 3
    async def send_message_(self):
        
        await self.get_roster()
        # elegir contacto 
        conts = self.roster
        contacts = [c for c in conts.keys()]

        if (len(contacts) > 0):

            cont = select_contact(contacts)

            if (cont is None or cont == ""): return

        else:
            print("No se han encontrado contactos")
            cont = input("Dirección del contacto") 
            if (cont == ""): return 

        # definir el mensaje
        message = input("Mensaje a enviar: ")
        if (message == ""):
            print("\n[[El mensje no puede estar vacío]]")
            return

        # función de envío de mensajes de slixmpp
        self.send_message(mto=cont, 
                          mbody=message, 
                          mtype='chat')
        
        print(f"{self.name} le a enviado a {cont}: {message}")
        