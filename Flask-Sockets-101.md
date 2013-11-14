Here are the basic steps to get started on developing the Chat Server using Flask Sockets.

1. Do the initial project setup: [instructions](https://github.com/MissionBit/chat-client/wiki/Developing-the-Chat-Server)

2. Create an 'Echo Server' using the chat-client/server/server.py template and the Flask Socket [documentation](http://kennethreitz.org/introducing-flask-sockets/)

3. Test the 'Echo Server' in the development console of your web browser

Create a connection:
```
var socket = new WebSocket("ws://162.243.141.18:8000/echo");
```

Setup a message handler:
```
socket.onmessage = function(msg) { console.log("The server said: " + msg.data); }
```

Send a message:
```
socket.send("Hello World!!!");
```

Close the socket:
```
socket.close();
```