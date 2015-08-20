from flask import flask, render_template

app=Flask(__name__)

@app.route('/')
	msg="hello world"
	return render_template("index.html",msg=msg)

if __name__=='__main__':
	app.run()