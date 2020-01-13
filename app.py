import RPi.GPIO as GPIO
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
port = '5000'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

@app.route('/')
def index():
    return "<h2>SAP Conversational AI Edge<h2>"

@app.route("/fan-fail", methods = ['POST'])
def startkit():
    if request.method == 'POST':
        print(request.json)

    kit = request.json['text']

    if kit == 'fan':
        GPIO.output(11,0)
        print("Primary fan failed")

    return jsonify(
        status = 200,
        replies = [
            {
                'type': 'text',
                'content': 'Failing primary fan'
                }
            ]
        )
app.run(port=port)