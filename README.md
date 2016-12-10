chatroom
=================
### About chatroom
A chatroom based on ``flask`` and ``flask-socketio`` supports following functions:

* peer to peer chatting
* chating in a room or group

### Usage
```
git clone https://github.com/bingtel/chatroom
cd chatroom
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
FLASK_APP=app flask run 
```
then, visit page A with url:

    http://localhost:5000
    
and open a new page B with url:

    http://localhost:5000
    
do operations on one page and you will notice the change in another page.