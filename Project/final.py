from bottle import Bottle,route,run,template,response
import json 

a = open("/root/Desktop/Final/final.json","r")
b= a.read()
c=json.loads(b)
app = Bottle()

@route("/")
def index():
	return template("results",all_news=c)

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'




@app.route("/top")
def top():
	return(json.dumps(c['all_news'][:20]))


@app.route("/<num>")
def top_num(num):
	return(json.dumps(c['all_news'][:int(num)]))

run(host="localhost",port=9000)
