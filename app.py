from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def home():
    os.system("echo MALICIOUS COMMAND EXECUTED")
    return "DevSecOps STRIDE Project Running"
if __name__ == '__main__':
    app.run(host='0.0.0', port=5000)
