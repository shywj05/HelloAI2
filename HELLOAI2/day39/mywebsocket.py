from flask import Flask, render_template, request
import cx_Oracle
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('tetris_network_ai.html')

@app.route('/saveai', methods=['POST'])
def saveai():
    txt = request.form["datasets"]
    arr = txt.split(",")
    
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    sql = "insert into tetris (learn400, action) values (:1,:2)"
    
    for i in arr:   
        learn400 = i[0:400]
        action = i[400:]
        cs.execute(sql,(learn400,action)) 
    
    cs.close()
    conn.commit()
    conn.close()
    
    return "saveai"



@app.route('/suser_ins.ajax', methods=['POST'])
def suser_ins_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    birth = request.form["birth"]

def myreceive(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('to_server')
def to_server(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('to_client', json, callback=myreceive)

if __name__ == '__main__':
    socketio.run(app, host = "0.0.0.0",port=9999)