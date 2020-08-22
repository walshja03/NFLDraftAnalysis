from flask import Flask, render_template, redirect, request
from runmodel import run_model



app = Flask(__name__)



@app.route("/")
def index():
    # Return template and data
    return render_template("index.html")

@app.route("/modelcreate")
def modelcreate():

    return render_template("modeldisplay.html")

@app.route("/model", methods = ['POST'])
def model():
    
    chosen = request.get_json()
    print(chosen)
    data = run_model(chosen)
    print(data)
    return data

@app.route("/Visual1")
def visual1():
    return render_template("Visualization1.html")

@app.route("/Visual2")
def Visual2():
    return render_template("Visualization2.html")
 
@app.route("/Visual3")
def Visual3():
    return render_template("Visualization3.html")
 
@app.route("/Visual4")
def Visual4():
    return render_template("Visualization4.html")


if __name__ == "__main__":
    app.run(debug=True)