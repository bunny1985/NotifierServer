#!/home/michal/Project/notifyTest/venv/bin/python

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from connectivity.server import DefaultListener
import json
from collections import namedtuple

class Notification:
  title = "Title"
  body = "content"
  type ="information" 
  def __init__(self, title, body , notificationType):
    self.title = title
    self.body = body
    self.type = notificationType
  def show(self):
    Notify.init(self.title)
    Hello=Notify.Notification.new(self.title, self.body , "dialog-"+ self.type)
    Hello.show()

class Message:
  title   = ""
  body = ""

print("starting")
def msg_recived(client, server, message):
    print(message)
    msg = json.loads(message , object_hook=lambda d: namedtuple('X', d.keys())(*d.values()) )
    print(msg.title)
    notification = Notification(msg.title , msg.body,  "information")
    notification.show()
    print("DUPA")


notification = Notification("Starting" , "Starting Server" , "warning" )
notification.show()
listener = DefaultListener()
listener.newMessage = msg_recived
listener.open()

