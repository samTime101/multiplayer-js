from flask import Flask, render_template, jsonify
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

@app.route('/guess/<guess>', methods=['GET'])
def guess(guess):
    if guess.isdigit():
        correct = int(guess) == usr_choice
        return render_template('guess.html', guess=guess, correct=correct, choose=usr_choice)
    return INTEGER_ERROR

@app.route('/choose/<choose>', methods=['GET'])
def choose(choose):
    global usr_choice
    if choose.isdigit():
        usr_choice = int(choose)
        socketio.emit('update_usr_choice', {'usr_choice': usr_choice})
        return render_template('choose.html', choose=choose)
    return INTEGER_ERROR

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
