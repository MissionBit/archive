To deploy the client and server for the chat project, perform the following steps:

1. Login to the team server as the 'missonbit' user (password is missionbit).
```
ssh missionbit@162.243.141.18
```
2. Get the latest version of the code.
```
cd chat-client
git pull origin
```
3. Deploy the application
```
cd ~
./deploy.sh
```