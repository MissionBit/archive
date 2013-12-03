from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.exceptions import WebSocketError
from flask import Flask
from flask_sockets import Sockets
import json

app = Flask(__name__)
sockets = Sockets(app)
names = []
usersockets = []
@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

@sockets.route('/testing')
def echo_socket(ws):

    #create a unique key that identifies this socket
    host, port = ws.socket.getpeername()
    socket_key = host + ":" + str(port)
    print "Connected: {0}".format(socket_key)

    while True:
        raw_message = ws.receive()
        if ws.socket is None:
            print "Disconnected: {0}".format(socket_key)
            break    

        message = json.loads(raw_message)
        action = message["action"]
        data = message["data"]
        if action == "join":
            response = { "event": "joined", "data": data }
        elif action == "send":
            response = { "event": "message", "data": data } 
        else:
            response = { "event": "bad_message", "data": "Bad message: {0}".format(message) }

        if ws.socket is not None:
            ws.send(json.dumps(response))


@sockets.route("/chat")
def chat(ws):
    while True:
        message = ws.receive()
        print message
        dictionary = json.loads(message)
        print dictionary
        action = dictionary["action"]
        print action 
        if action == "join": 
            print "join" ;
            name = dictionary["name"]
            names.append(name)
            usersockets.append(ws)
            print len(names)
        ws.send("action; " + action)
        if action == "send":  
            name = dictionary["name"]
            text = dictionary["text"]
            for usersocket in usersockets:
                usersocket.send(name + " said.." + text)





@app.route("/")			
def hello():
        return "chat server is running..."

if __name__ == "__main__":
    import sys

    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    server = pywsgi.WSGIServer(("", port), app, handler_class=WebSocketHandler)
    server.serve_forever() 
