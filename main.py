from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from time import sleep
import response as rp
import random

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, manage_session=False)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')
@app.route('/chat',methods=['GET', 'POST'])
def chat():
	try:
		username = request.form['username']
		room = request.form['room']
		session['username']=username
		return render_template('chat.html', session=session,username=session['username'],room=room)
	except:
		username = request.form['username']
		room = random.randint(1000,9999)
		rp.putroom(room)
		return render_template('chat.html', session=session,username=session['username'],room=room)
@socketio.on('join', namespace='/chat')
def join(message):
    join_room(message["rm"])
@socketio.on('text', namespace='/chat')
def text(message):
	room = message["rm"]
	emit('message', {'msg':message['msg'],'username':session['username']},room=room)
@socketio.on('filter',namespace='/chat')
def filter(message):
	room = message["rm"]
	sleep(0.2)
	response = rp.msgFilterHandle(message['msg'])
	if response:
		emit('message', {'msg':response,'username':'Bot'},room=room)
@socketio.on('promo',namespace='/chat')
def promos(message):
	room = message["rm"]
	sleep(0.2)
	response = rp.promo()
	emit('message', {'msg':response,'username':'Bot'},room=room)
@socketio.on("detils",namespace="/chat")
def detils(msg):
	room = msg["rm"]
	response =rp.detil(msg['msg'])
	emit('message', {'msg':response,'username':'Bot'},room=room)
@socketio.on('stocks',namespace='/chat')
def stocks(msg):
	room = msg["rm"]
	response = rp.stock(msg['msg'])
	emit('message', {'msg':response,'username':'Bot'},room=room)
@socketio.on('bot',namespace="/chat")
def bot (msg):
	room = msg["rm"]
	emit('message', {'msg':msg["msg"],'username':'Bot'},room=room)
if __name__ == '__main__':
    socketio.run(app)