import time
from flask import Flask
app = Flask(__name__)

sleep_time = 0

def change(amount):
    global sleep_time
    sleep_time = amount
    return sleep_time


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    time.sleep(sleep_time)
    return 'Hello World! I can make change at route: /change/sleepAmount'

@app.route('/change/<amount>')
def changeroute(amount):
    result = change(int(amount))
    return 'Timeout updated to {0}'.format(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
