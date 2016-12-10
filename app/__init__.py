from collections import defaultdict
from flask import Flask, redirect, url_for, render_template, request, session
from flask_socketio import SocketIO, send, emit
from flask.ext.bootstrap import Bootstrap
from app.util import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

# {'roo-name': user_cnt}
ROOMS = defaultdict(dict)
USERS = ['default']
ROOMS['default'] = {'default': None}


@app.route('/')
@auth
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.values.get('user_name')
        if not user_name:
            return redirect(url_for('login'))
        session['user_name'] = user_name
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/room/<room_name>')
@auth
def enter_room(room_name):
    return render_template('room.html', room_name=room_name)


@socketio.on('get_rooms', namespace='/')
@auth
def handle_get_rooms():
    return ROOMS


@socketio.on('get_users', namespace='/')
@auth
def handle_get_users():
    return USERS


@socketio.on('get_room_users', namespace='/')
@auth
def handle_get_room_users(room_name):
    return ROOMS[roo_name]

if __name__ == '__main__':
    socketio.run(app)
