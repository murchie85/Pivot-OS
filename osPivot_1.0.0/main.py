from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")

@app.route("/home")
def home():
	return render_template("base.html")

@app.route("/landing")
def about():
    return render_template("landing.html")




if __name__ == '__main__':
	print('main')
	app.run(host='localhost', port=5001)
	app.run(debug=True)