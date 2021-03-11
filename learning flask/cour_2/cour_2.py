from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<name>")
def user(name):
	return render_template("user.html", name=name)

@app.errorhandler(404)
def error_404(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def error_500(e):
	return render_template("500.html"), 500

if __name__ == "__main__":
	app.run(debug=True)