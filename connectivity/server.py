from websocket_server import WebsocketServer
import json

# Called for every client connecting (after handshake)
def new_client(client, server):
  print("New client connected and was given id %d" % client['id'])
  #server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
  print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
  
  print("Client(%d) said: %s" % (client['id'],  message))

class DefaultListener:
	newClientCallBack = new_client
  	clientLeftCallBack = client_left
  	newMessage = message_received
	def open(self):
		nw = self.newClientCallBack
		server = WebsocketServer(9001 , "192.168.8.106")
		#server.set_fn_new_client(new_client)
		#server.set_fn_client_left(self.clientLeftCallBack)
		server.set_fn_message_received(self.newMessage)
		server.run_forever()
