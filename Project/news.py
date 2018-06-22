from bottle import route,run,get,template,static_file


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route("/")
def index():
	return template("index")

run(host="localhost",port=7000)
