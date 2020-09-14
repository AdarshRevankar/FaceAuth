import base64
import io
import os

from flask import Flask, request, jsonify
from flask import render_template
from PIL import Image

from login import input_verification, create_new_account, check_username_existence

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    uname = str(request.values['username'])
    password = str(request.values['password'])

    # Input validation
    if not input_verification(uname, password):
        return jsonify({'register': 'Credential Error Please follow guidelines for username & password'})

    # If already a user exists
    if check_username_existence(uname):
        return jsonify({'register': 'Account Already Exists'})
    else:
        # Create A new Account
        create_new_account(uname, password)
        return jsonify({'register': 'Registration Successful'})


@app.route('/capture', methods=['POST'])
def capture():
    name = request.values['user']
    picture_base64 = request.values['image']
    picture_bytes = base64.b64decode(picture_base64.split('base64,')[1])
    img = Image.open(io.BytesIO(picture_bytes))
    return jsonify({'status': 'done'})


@app.route('/')
def start():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
