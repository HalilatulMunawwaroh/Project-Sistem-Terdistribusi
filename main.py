from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from time import sleep
from response import msgFilterHandle

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, manage_session=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/chat',methods=['GET', 'POST'])
def chat():
	username = request.form['username']
	session['username']=username
	return render_template('chat.html', session=session)
@socketio.on('text', namespace='/chat')
def text(message):
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']})
@socketio.on('filter',namespace='/chat')
def filter(message):
	sleep(0.2)
	response = msgFilterHandle(message['msg'])
	if response:
		emit('message', {'msg': "bot" + ' : ' + response})



if __name__ == '__main__':
    socketio.run(app)