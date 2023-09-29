from flask import Flask
new = Flask(__name__)

@new.route('/')
def home():
    return '<h1>Hello</h1>'

@new.route('/name/<string>')
def name(string):
    return '<h1>Welcome %s </h1>' % string

@new.route('/age/<int:num>')
def age(num):
    return  '<h1> Your age %d </h1>' % num

new.run()
