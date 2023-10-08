from channels.generic.websocket import SyncConsumer
from channels.exceptions import StopConsumer


class MyConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('=========================================================================')
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print("------------- Websocket Received ---------------")
        print(f"Message Received From Client ==> {event['text']}")
        self.send({
            "type": "websocket.send",
            "text": "Server is responding",
        })

    def websocket_disconnect(self, event):
        print('=========================================================================')
        raise StopConsumer()
