from flask import Flask, render_template, redirect, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "azerty"
bootstrap = Bootstrap(app)

class NameForm(Form):
	name = StringField("What is your name:", validators=[DataRequired()])
	submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
	form = NameForm()
	if form.validate_on_submit():
		session["name"] = form.name.data
		form.name.data = ""
		redirect(url_for("index"))
	return render_template("index.html", form=form, name=session.get("name"))

if __name__ == '__main__':
	app.run(debug=True)