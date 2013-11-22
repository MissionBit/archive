function send (){
	var inputTextArea= document.getElementById("input");
	var inputText= inputTextArea.value;
	appendOutput(inputText);
}
function appendOutput (text) {
	var outputTextArea= document.getElementById("output");
	var oldText= outputTextArea.value;
	var newText= oldText+text;
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
	showchat();
});

button2.addEventListener("click", function(e) {
	showlogin()
});


showlogin();