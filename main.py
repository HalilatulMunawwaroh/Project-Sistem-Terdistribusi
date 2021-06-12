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
	lroom = rp.getrm()
	return render_template('admin.html',room_json=lroom)
@app.route('/chat',methods=['GET', 'POST'])
def chat():
	if(request.method=='POST'):
		try:
			username = request.form['username']
			room = request.form['room']
			session['username'] = username
			session['room'] = room
			return render_template('chat.html',username=session['username'],room=room)
		except:
			username = request.form['username']
			session['username'] = username
			room = random.randint(1000,9999)
			session['room'] = room
			return render_template('chat.html',username=session['username'],room=room)
	else:
		if(session.get('username') is not None):
			return render_template('chat.html', session = session)
		else:
			return redirect(url_for('index'))
@socketio.on('join', namespace='/chat')
def join(message):
	join_room(message["rm"])
	emit('pop',{'msg':session['username']+' memasuki chat'},room=message["rm"])
	emit('pop',{'msg':'ketik menu untuk bantuan'},room=message["rm"] )
@socketio.on('text', namespace='/chat')
def text(message):
	room = message["rm"]
	if message['msg'] !="":	
		emit('message', {'msg':message['msg'],'username':session['username']},room=room)
	else:
		pass
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
	response = rp.promo()
	emit('message', {'msg':response,'username':'Bot'},room=room)
@socketio.on("infos",namespace="/chat")
def info(msg):
	room = msg["rm"]
	response =rp.menu1()
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
@socketio.on('admin',namespace='/chat')
def admin(msg):
	room = msg['rm']
	rp.putroom(room)
	emit('pop',{'msg':session['username']+' membuat ruang menjadi public'},room=room )
@socketio.on('saran',namespace='/chat')
def saran(msg):
	room = msg['rm']
	pesan =msg['msg']
	if pesan.lower()=="cancel":
		emit('message',{'msg':'saran di cancel','username':'Bot'},room=room )
	else:	
		rp.srn(pesan)
		emit('message',{'msg':'saran anda telah ditambahkan, terima kasih','username':'Bot'},room=room )
@socketio.on('left', namespace='/chat')
def left(message):
	room = session.get('room')
	username = session.get('username')
	leave_room(room)
	session.clear()
	emit('pop', {'msg': username + ' telah keluar.'}, room=room)
    
@socketio.on('disconnect')
def test_disconnect():
	try:
		room = session['room']
		rp.dcroom(room)
	except:
		room = session["room"]
		print('failure')
if __name__ == '__main__':
    socketio.run(app)