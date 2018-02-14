from flask import Flask, render_template
from led_controller import setupLed, ON, OFF 
from sys import argv

app = Flask(__name__)
led_gpio = int(argv[1])

def setup():
    setupLed(led_gpio)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ON')
def ledON():
    ON(led_gpio)
    return render_template('index.html')

@app.route('/OFF')
def ledOFF():
    OFF(led_gpio)
    return render_template('index.html')    

if __name__ == '__main__':
    setup()
    app.run(debug=True, host='0.0.0.0')

