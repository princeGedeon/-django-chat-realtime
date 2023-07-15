import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """ Consumer pour chat room"""
    """Quand chaque utser se connecte il a sa propre couche"""

    # On travaille sur la connexion
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name'] # on recupere le slug
        self.room_group_name=f'chat_{self.room_name}' # id du groupe

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        #On accepte la connection
        await self.accept()

    # Se déconnecter fermer le groupe
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data=json.loads(text_data)
        print(text_data)
        message=data['message']
        username=data['username']
        room=data['room']

        #Sauvegarder
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                "message": message,
                "username":username,
                "room":room
            }
        )


