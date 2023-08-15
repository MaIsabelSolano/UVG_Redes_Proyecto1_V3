import slixmpp
import asyncio

class Client(slixmpp.ClientXMPP):
    def __init__(self, host, jid, password):
        super().__init__(jid, password)


    async def send_message_(self, cont, message):
        self.send_message(mto=cont, mbody=message, mtype='chat')
        