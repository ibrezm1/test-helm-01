from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def display_secret():
    username = os.getenv('SECRET_USERNAME', 'default_user')
    password = os.getenv('SECRET_PASSWORD', 'default_password')
    return render_template('index.html', username=username, password=password)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
