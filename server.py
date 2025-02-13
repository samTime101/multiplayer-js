from flask import Flask, render_template, jsonify , request
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

INTEGER_ERROR = """
<script>
alert("Don't put non-integer!") 
window.history.back()
</script>
"""

usr_choice = 0  

@app.route('/play/', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        return render_template('play.html', guess="")
    
    data = request.get_json()
    table_num = data.get("clicked", "").strip()
    socketio.emit('clicked', {'table_num': table_num})
    # return INTEGER_ERROR


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True )
