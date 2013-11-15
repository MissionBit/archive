function send (){
	var inputTextArea= document.getElementById("input");
	var inputText= inputTextArea.value;
	alert (inputText);
	appendOutput(inputText);
}
function appendOutput (text) {
	var outputTextArea= document.getElementById("output");
	var oldText= outputTextArea.value;
	var newText= oldText+text;
	outputTextArea.value= newText;
}
