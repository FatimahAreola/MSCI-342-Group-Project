from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    print('Hello Request Received')
    return 'Hello This is the Flask App'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
