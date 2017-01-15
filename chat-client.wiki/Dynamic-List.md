This tutorial will show you how to create populate list using Javascript.

index.html
```
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Dynamic List Tutorial</title>
</head>

<body>

	<ul id="chatList"></ul>
	
    <script src="main.js"></script>
</body>
</html>
```

main.js
```
var chatMembers = ["Kevin", "Joe", "Hank"];

var chatList = document.getElementById("chatList");

var clearList = function(list) {
	for(i=0; i < list.childNodes.length; i++) {
		var item = chatList.childNodes[i];
		list.removeChild(item);
	}
};

var populateList = function(list, members) {
	
	for(i=0; i < members.length; i++) {
		var li = document.createElement("li");
		
		var img = document.createElement("img");
		img.setAttribute("src", "http://lorempixum.com/40/40/nature/1");
		
		var h3 = document.createElement("h3");
		h3.innerHTML = members[i];
		
		var p = document.createElement("p");
		p.innerHTML = "Hi";
		
		li.appendChild(img);
		li.appendChild(h3);
		li.appendChild(p);
		
		list.appendChild(li);
	}
};

var refreshList = function(list, members) {
	clearList(list);
	populateList(list, members);
};

refreshList(chatList, chatMembers);


```