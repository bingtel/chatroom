from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event', namespace='chatroom')
def handle_my_custom_event(json):
    return 'received json: ' + str(json)

if __name__ == '__main__':
    socketio.run(app)
