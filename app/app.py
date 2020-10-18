from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
