This tutorial will demonstrate how to connect to a WebSocket using Javascript.

1. Create a new directory called ```wstutorial```
2. Create a new html file called ```index.html``` with the following contents:
```
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>WebSocket Tutorial</title>
</head>

<body>

	<div>
		<button id="connectButton">Connect</button>
	</div>
	
	<div>
		<button id="chatButton">Send Message</button>
	</div>
	
	<div>
		<button id="disconnectButton">Disconnect</button>
	</div>
	
    <script src="main.js"></script>
</body>
</html>
```
3. Create a javascript file called ```main.js``` with the following content:
```
var connectButton = document.getElementById("connectButton");
var chatButton = document.getElementById("chatButton");
var disconnectButton = document.getElementById("disconnectButton");

var socket;
				
connectButton.addEventListener("click", function(e) {
    socket = new WebSocket('ws://162.243.141.18:8080/echo');
    socket.onopen = function() {
        console.log("Connected to socket");
    };

    socket.onmessage = function(msg) {
        console.log(msg.data);
    };
	
	socket.onerror = function(error) {
        console.log(error);
    };

    socket.onclose = function() {
        console.log("Disconnected from socket");
    };
});

chatButton.addEventListener("click", function(e) {
	socket.send("hello world");
});
		
disconnectButton.addEventListener("click", function(e) {
	socket.close();
});
```

4. Open ```index.html``` in your browser to try it out.