import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)
port = '5000'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

@app.route('/')
def index():
    return "<h2>SAP Conversational AI Edge<h2>"

@app.route("/startkit", methods = ['POST'])
def startkit():
    if request.method == 'POST':
        print(request.json)

    kit = request.json

    if kit == 'Smart Asset Monitoring':
        GPIO.output(11,1)

     return jsonify(
        status = 200,
        replies = [
            {
                'type': 'text',
                'content': 'Starting Kit'
                }
            ]
        )
app.run(port=port)