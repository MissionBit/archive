**Client Messages (handled by the server)**

Client message should be JSON strings with the following form.

```
{ "action": "some action", "data": "some data" }
```

**Join**

When a user clicks the join button in the chat application, a "join" message needs to be sent to the server.
```
{ "action": "join", "data": "Kevin" }
```
The server should associate the user name with the client's web socket and broadcast a "joined" event.

**Send**

When a user clicks the send button in the chat application, a "send" message needs to be sent to the server.
```
{ "action": "send", "data": "Hello World!!!" }
```

The server should lookup the user name associated with the client's web socket and broadcast a "message" event.

**Server Messages (handled by the client)**

Server message should be JSON strings with the following form.

```
{ "event": "some event", "data": "some data" }
```

**Joined**

When the server receives a "join" message, a "joined" event needs to be sent to the clients.
```
{ "event": "joined", "data": "Kevin" }
```

When the client receives a "joined" event, it should append the user's name to the chat member list.

**Message**

When the server receives a "send" message, a "message" event needs to be sent to the clients.
```
{ "event": "message", "data": "Kevin: Hello World!!!" }
```

When the client receives a "message" event, it should append the message to the chat window.