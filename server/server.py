from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.exceptions import WebSocketError
from flask import Flask
from flask_sockets import Sockets
import json

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

@sockets.route('/testing')
def echo_socket(ws):
    while True:
        message = ws.receive()
        print message
        dictionary = json.loads(message)
        print dictionary
        dictionary["name"] = "Jim Doe"
        message2 = json.dumps(dictionary)
        print message2
        ws.send(message2)

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
