from flask import flask, render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
	msg="hello world"
	return render_template("index.html",msg=msg)

@app.route('/integer/<int:value>')
def int_type(value):
	print value
	return "correct"

@app.route('/float/<float:value>')
def float_type(value):
	print value + 1.1
	return "correct"

@app.route('/path/<path:value>')
def path_type(value):
	print value
	return "correct"

if __name__=='__main__':
	app.run()