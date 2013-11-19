The team server has all of the Python dependencies setup for development using Flask Sockets. 



**Documentation**
* Python - http://www.python.org/
* Flask - http://flask.pocoo.org/
* Flask Sockets - http://kennethreitz.org/introducing-flask-sockets/

**Local Setup**

Installing Dependencies on Local Laptop:
   - brew install libevent 
   - pip install gevent  
   - brew install python 
   - hash -r
   - pip install gevent-socketio
   - pip install flask
   - pip install flask-sockets

**Remote Setup:**

1. Login to the team server
```
ssh user@162.243.141.18
```
2. Setup git (this only needs to be done once)
```
git config --global user.name "Your Name"
git config --global user.email youremail@foo.com
```
3. Clone the repository (this only needs to be done once)
```
git clone https://github.com/MissionBit/chat-client.git
```

**Development Process**

1. Get the latest version of the code
```
cd chat-client
git pull origin
```
2. Work on the server code
```
cd server
nano server.py
```
3. Run the server (not on port 8080)
```
python server.py 8000

OR

./run.sh 8000
```
4. Test your changes
```
In a browser go to: http://162.243.141.18:8000
```

5. When you are happy, commit and push your code
```
git status
git add server.py
git commit -m "PUT SOME COMMIT MESSAGE HERE"
git push origin master