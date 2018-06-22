from bottle import route,run,template
import json 

x = open("/root/Desktop/Final/home.json","r")
y = x.read()
z =json.loads(y)

@route("/")
def index():
	return template("result",top_news=z)

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

run(host="localhost",port=8000)
