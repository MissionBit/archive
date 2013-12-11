
var chatList= document.getElementById("chatList");


function send (){
	var inputTextArea= document.getElementById("input");
	var inputText= inputTextArea.value;
	var send={action: "send",data: inputText};
    var message= JSON.stringify(send);
    console.log(message);
    socket.send(message);

}
function appendOutput (text) {
	var outputTextArea= document.getElementById("output");
	var oldText= outputTextArea.value;
	var newText= oldText + "\n" + text;
	outputTextArea.value= newText;
}
function refreshText() { 
	var refreshText= document.getElementById("output");
		refreshText.value="" ;

}

var login= document.getElementById("login");
var button= document.getElementById("join");
var chat=document.getElementById("chat");
var button2=document.getElementById("logout");
var showchat= function() {
	login.style.display="none";
	chat.style.display="block";
	button2.style.display="block"
}

var showlogin= function() {
	chat.style.display="none";
	login.style.display="block";
	button2.style.display="none";
} 

button.addEventListener("click", function(e) {
	socket = new WebSocket('ws://162.243.141.18:8080/chat');



    socket.onopen = function() {
    	console.log("Connected to socket");
    	var loginPUT=document.getElementById('loginPUT');
    	var join={action: "join",data: loginPUT.value};
    	var message= JSON.stringify(join);
    	console.log(message);
    	socket.send(message);

    };

    socket.onmessage = function(msg) {
        console.log(msg.data);
        var message= JSON.parse(msg.data);
        var e= message.event;
        if (e=='message') {
        	   appendOutput(message.data);
        };

        if (e=='joined') { 
            refreshList (chatList,message.data);

        };
    };

	socket.onerror = function(error) {
        console.log(error);
    };

    socket.onclose = function(close) {
        console.log("Disconnected from socket") ;


    };
    showchat();
});

button2.addEventListener("click", function(e) {
		socket.close();
		showlogin()
});


showlogin();
