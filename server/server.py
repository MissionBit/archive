from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.exceptions import WebSocketError
from flask import Flask
from flask_sockets import Sockets
import json

app = Flask(__name__)
sockets = Sockets(app)
names = {}
usersockets = {} 
@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

@sockets.route('/chat')
def echo_socket(ws):

    #create a unique key that identifies this socket
    
    host, port = ws.socket.getpeername()
    socket_key = host + ":" + str(port)
    print "Connected: {0}".format(socket_key)
    usersockets[socket_key] = ws
    while True:
        raw_message = ws.receive()
        if ws.socket is None:
            print "Disconnected: {0}".format(socket_key)
            del usersockets[socket_key]
            del names[socket_key]
            break    
        message = json.loads(raw_message)
        action = message["action"]
        data = message["data"]
        if action == "join":
            names[socket_key] = data
            for key in usersockets.keys():
                connection = usersockets[key]
                name = names[socket_key]
                response = {"event": "joined", "data": names.values()}
                connection.send(json.dumps(response))
        elif action == "send":
             for key in usersockets.keys():
                connection = usersockets[key]
                name = names[socket_key]
                response = { "event": "message", "data": name + ": " + data}
                if ws.socket is not None:
                    connection.send(json.dumps(response))
        else:
            response = { "event": "bad_message", "data": "Bad message: {0}".format(message) }






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
