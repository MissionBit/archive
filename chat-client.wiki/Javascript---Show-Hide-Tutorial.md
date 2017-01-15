This tutorial will demonstrate how to dynamically show and hide sections of html using Javascript.

1. Create a new directory called ```jstutorial```
2. Create a new html file called ```index.html``` with the following contents:
```
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Show/Hide Tutorial</title>
</head>

<body>

	<div id="section1">
		<h1>This is section 1!!!</h1>
		<p>To use javascript to hide me, click the button below</p>
		<button id="button1">Show Section 2</button>
	</div>

        <div id="section2">
		<h1>This is section 2!!!</h1>
		<p>Awesome, you used javascript to hide section1 and show section2</p>
		<button id="button2">Show Section 1</button>
	</div>

        <script src="main.js"></script>
</body>
</html>
```
3. Create a javascript file called ```main.js``` with the following content:
```
var section1 = document.getElementById("section1");
var button1= document.getElementById("button1");
		
var section2 = document.getElementById("section2");
var button2= document.getElementById("button2");
		
var showSection1 = function() {
	section1.style.display = "block";
	section2.style.display = "none";
};
		
var showSection2 = function() {
	section1.style.display = "none";
	section2.style.display = "block";
};
		
button1.addEventListener("click", function(e) {
	showSection2();
});
		
button2.addEventListener("click", function(e) {
	showSection1()
});
		
showSection1();
```

4. Open ```index.html``` in your browser to try it out.

**Review**

To select an element by id and store it to a variable use: 
```
var element = document.getElementById("someId");
```

To hide an element:
```
element.style.display = "none";
```

To show an element: 
```
element.style.display = "block";
```