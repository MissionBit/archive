**Data Serialization**
> In computer science, in the context of data storage and transmission, serialization is the process of translating data structures or object state into a format that can be stored (for example, in a file or memory buffer, or transmitted across a network connection link) and resurrected later in the same or another computer environment. - [wikipedia](http://en.wikipedia.org/wiki/Serialization)

**JSON**
> JSON (JavaScript Object Notation) is a lightweight data-interchange format. - [JSON](http://www.json.org/)

**Serializing a Javascript Object**

1. Open the development console in your browser 
2. Create an object representing a person and save it to a variable
```
var kevin = { name: "Kevin", age: 30, email: "krchard@gmail.com" };
```
3. Log the object to the console
```
console.log(kevin);
```
4. Serialize the object and log it to the console
```
console.log(JSON.stringify(kevin));
```
5. Create a JSON string representing another person
```
var bob = '{ "name": "Bob", "age": 20, "email": "bob@email.com" }';
```
6. Log the JSON to the console
```
console.log(bob);
```
7. Parse the JSON to an object and log it to the console
```
console.log(JSON.parse(bob));
```

**Serializing a Python Dictionary**

1. Start the python interpreter
```
python
```
2. Import the json module
```
>>> import json
```
3. Create a dictionary representing a person and save it to a variable
```
>>> kevin = { "name": "Kevin", "age": 30, "email": "krchard@gmail.com" }
```
4. Print the dictionary and its type
```
>>> print kevin
>>> print type(kevin)
```
5. Serialize the dictionary to JSON and print it and its type
```
>>> print json.dumps(kevin)
>>> print type(json.dumps(kevin))
```
6. Create a JSON string representing another person
```
bob = '{ "name": "Bob", "age": 20, "email": "bob@email.com" }'
```
7. Print the string and its type
```
>>> print bob
>>> print type(bob)
```
8. Parse the JSON string to a Python dictionary and print it and its type
```
>>> print json.loads(bob)
>>> print type(json.loads(bob))
```