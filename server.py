import base64
import io

from flask import Flask, request, jsonify
from flask import render_template
from PIL import Image

from login import check_credintial, insert_new

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    uname = str(request.values['username'])
    password = str(request.values['password'])

    # Check credintial
    if check_credintial(uname, password):
        return jsonify({'register': 'exists'})
    else:

        return jsonify({'register': 'done'})


@app.route('/capture', methods=['POST'])
def capture():
    name = request.values['user']
    picture_base64 = request.values['image']
    picture_bytes = base64.b64decode(picture_base64.split('base64,')[1])
    img = Image.open(io.BytesIO(picture_bytes))
    return jsonify({'status': 'done'})


if __name__ == '__main__':
    app.run()
