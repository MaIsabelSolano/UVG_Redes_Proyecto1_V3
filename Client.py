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

    # Funciones necesarias para el funcionamiento correcto del cliente

    async def start(self, event):
        print("start")

        # presencia
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
    # menú
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
                0

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
            print("\n[No se pudo realizar la acción]")
        

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



    # opción 5
    async def update_presence(self):
        await self.get_roster() 
        self.status, self.status_message = select_presence()
        self.send_presence(pshow=self.status, pstatus=self.status_message)
        await self.get_roster() 


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

        