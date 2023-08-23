import slixmpp
import asyncio
from slixmpp.xmlstream.stanzabase import ET
from View import *

class Client(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)

        self.name = jid.split('@')[0]
        self.host = jid.split('@')[1]
        self.status = ""
        self.status_message = ""
        self.message_history = {}
        self.room = None
        

        # Obtenido de ejemplos de slixmpp
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0004') # Data Forms
        self.register_plugin('xep_0060') # PubSub
        self.register_plugin('xep_0199') # XMPP Ping
        self.register_plugin('xep_0045') # Group chat

        self.add_event_handler("session_start", self.start)
        self.add_event_handler('presence', self.presence_handler)
        self.add_event_handler("message", self.message_received)  # Join rooms upon login
        self.add_event_handler("subscribe", self.handle_subscription)
        self.add_event_handler("roster_subscription_request", self.handle_subscription_request)
        self.add_event_handler("roster_subscription_remove", self.handle_removed_sub)
        

    # Necesary functions for the program

    async def start(self, event):
        print("start")

        # presence
        self.send_presence()
        await self.get_roster()

        asyncio.create_task(self.user_menu())
        """Initializes de program by sending the presence, getting the roster and creating the user menu
        """

    
    async def presence_handler(self, presence):

        if presence['type'] == 'subscribe':
            try:
                self.send_presence_subscription(pto=presence['from'], ptype='subscribe')
                await self.get_roster()
            except:
                print("Hubo un error en el presence handler")

        if presence['type'] == 'available':
            print_pres(f"{presence['from']} se ha conectado")

        elif presence['type'] == "unavailable":
            print_pres(f"{presence['from']} se ha desconectado")

        elif presence['type'] == "away":
            print_pres(f"{presence['from']} se ga ido")

        elif presence['type'] == "dnd":
            print_pres(f"No molestar a {presence['from']}.")

        elif presence['type'] == "xa":
            print_pres(f"{presence['from']} no está disponible")

        """
        Handles how the presence is dealt with. It sends the currente presence to the accounts the user is subscribed to
        """

    async def handle_subscription_request(self, pres):
        await self.get_roster()
        pop_m = f"Nueva solicitud de subscripción de {pres['from']}"
        popUp("Notificación", pop_m)
        """
        Handles subscriptions requests
        """


    async def handle_subscription(self, presence):
        if presence["type"] == "subscribe":
            pop_m = f"Nueva solicitud de subscripción de {presence['from']}"
            res = popUp()

            if res:
                self.send_presence(pto=presence["from"], ptype=["subscribed"])
                print("Suscripción aceptada")
            else:
                print("Suscripción denegada")
        """
        Handles subscriptions requests
        """

    async def handle_removed_sub(self, pres):
        # notify user
        pop_m = f"{pres['from']} ha removido su suscripción"
        popUp("Removed Sub", pop_m)

        self._handle_removed_subscription(pres)
        """
        Handles when another account has canceled a subscription to the user's account
        """

    # Funciones para el usuario
    # menú
    async def user_menu(self):

        await self.get_roster()

        print("menu")
        # user menu
        while(self.is_connected):

            option_2 = functions()

            if (option_2 == 1): 
                # Mostrar todos los contactos y su estado
                await self.contacts_status()

            elif (option_2 == 2): 
                # Agregar un usuario a los contactos
                await self.add_new_contact()

            elif (option_2 == 3): 
                # Chatear con un usuario/contacto
                await self.send_message_()

            elif (option_2 == 4):
                # Conseguir info de un contacto
                await self.get_contact_info()

            elif (option_2 == 5):
                # Participar en conversaciones grupales
                print("\nn/i")

            elif (option_2 == 6): 
                # Definir mensaje de presencia
                await self.update_presence()

            elif (option_2 == 7): 
                # Enviar/recibir notificaciones
                await self.get_roster()

            elif (option_2 == 8): 
                # Enviar/Recibir archivos
                print("\nn/i")

            elif (option_2 == 9): 
                # Eliminar cuenta del servidor
                res = deleteAccout(self.jid)
                if res == True:
                    # Eliminar cuenta
                    await self.del_account()

            elif (option_2 == 10): 
                # Cerrar sesión
                print("Cerrando sesión")
                self.disconnect()
                self.is_connected = False

        """
        Main menu. Handles the users needs
        """

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

        """
        Gets all the user's contacts and stores their information to display it
        """

    # opción # 2
    async def add_new_contact(self):
        # conseguir el nombre del nuevo contacto 
        print("\nIngrese la direción del nuevo usuario a agregar:")
        newCont = input("Dirección: ")

        if (len(newCont) == 0): return # cancelar la acción

        try:
            # Hacer el request
            self.send_presence_subscription(pto=newCont)
            await self.get_roster()
            print("\nSe le ha enviado una solicitud de suscripción a ", newCont)

        except:
            print("\n[[No se pudo realizar la acción]]")

        """
        Givena new a directions, adds that direction to dhe contact lists even if it doesn't exist. 
        """
        

    # opción # 3
    async def send_message_(self):
        
        await self.get_roster()
        # elegir contacto 
        conts = self.client_roster
        contacts = [c for c in conts.keys()]

        if (len(contacts) > 0):

            cont = select_contact(contacts)

            if (cont is None or cont == ""): return

        else:
            print("No se han encontrado contactos")
            cont = input("Dirección del contacto") 
            if (cont == ""): return 

        # Impresión de mensajes previos
        if (cont in self.message_history):
            print_messages(self.message_history[cont])
        else: print("\nno hay mensajes previos")

        # definir el mensaje
        message = input("Mensaje a enviar: ")
        if (message == ""):
            print("\n[[El mensje no puede estar vacío]]")
            return

        # función de envío de mensajes de slixmpp
        self.send_message(mto=cont, 
                          mbody=message, 
                          mtype='chat')
        
        await self.get_roster()
        
        print(f"{self.name} le a enviado a {cont}: {message}")

        """
        Sends a messages. This can be done by either choosing an account from the user's contacts of 
        by writing it's direction. 
        """

    async def message_received(self, message): 

        await self.get_roster()

        # mensajes_from_contact = []
        
        if message['type'] == 'chat' or message['type'] == 'normal':
            fromusr = str(message['from']).split("@")[0] # nombre del usuario

            if message['body'].startswith("file://"):
                # Es un archivo el que se está recibiendo 
                0

            else:
                body = message['body']
                print("\n********* Mensaje entrante! *******")
                print(f"{fromusr}: {body}")
                print("\n***********************************\n")

                pop_m = f"Nuevo mensaje de {fromusr}"
                popUp("Mensaje entrante", pop_m)

                # Añadir al historial de mensajes
                if fromusr not in self.message_history:
                    # Se agrega el contacto al historial
                    self.message_history[fromusr] = []
                self.message_history[fromusr].append((fromusr, body))
                

        await self.get_roster()

        """
        Handles incoming new messegas and displays an alet for them 
        """

    # opción 4
    async def get_contact_info(self):
        # conseguir toda la info de contactos
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

        else:
            print("No se han encontrado contactos")
            return

        # elegir contacto (por id)
        cont_i = select_contact_id(contacts)

        if (cont_i == None): return

        print_contact_info(contactsFullInfo[cont_i])

        """
        Gets all the information of chosen user from the contact list
        """



    # opción 5
    async def update_presence(self):
        await self.get_roster() 
        self.status, self.status_message = select_presence()
        self.send_presence(pshow=self.status, pstatus=self.status_message)
        await self.get_roster() 

        """
        Updats presence by status and message
        """


    # opción # 8
    async def del_account(self):
        
        try:
            self.send_presence()
            self.disconnect()
            res = self.Iq()
            res['type'] = 'set'
            res['from'] = self.boundjid.user 
            print("\nEliminando...")
            # query obtenido pidiendo ayuda a compañeros
            frag = ET.fromstring("<query xmlns='jabber:iq:register'><remove/></query>")
            res.append(frag)

            await res.send()
            print("\nCuenta eliminada con éxito")
            self.is_connected = False

        except Exception as e:
            print(f"\nOcurrió un error {e} al momento de eliminar la cuenta")

        """
        Deletes the user's account. Asks for verification first. 
        """

        