from flask import Flask, render_template, request, flash

app = Flask(__name__) # this step creates a Flask for our app
app.secret_key = "cayman_99_LAMO"

@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=['POST','GET'])
def greet():
    flash("Hi " + str(request.form['name_input']) + ', great to see you!')
    return render_template("index.html")