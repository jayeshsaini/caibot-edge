import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)
port = '5000'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

@app.route("/startkit", methods = ['POST'])
def startkit():
    if request.method == 'POST':
        print(request.json)

    kit = request.json

    if kit == 'Smart Asset Monitoring':
        GPIO.output(11,1)
   
app.run(port=port)