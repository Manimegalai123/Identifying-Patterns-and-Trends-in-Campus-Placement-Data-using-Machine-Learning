from flask import Flask, request, render_template
import pickle
import sklearn
import joblib

app = Flask(__name__)
model=pickle.load(open("placement.pkl", 'rb'))

@app.route('/')
def ind():
    return render_template("index.html")

@app.route("/predict")
def pred():
    return render_template("predict.html")

@app.route("/y_predict", methods=["POST"])
def y_predict():

    age = request.form["age"]
    sex = request.form["sex"]
    stream = request.form["stream"]
    interns = request.form["interns"]
    cgpa = request.form["cgpa"]
    backlog = request.form["backlog"]


    prediction = model.predict([[age, sex, stream, interns, cgpa, backlog]])


    if prediction == 0:
        output = "Not-Placed"
    else:
        output = "Placed"

    return render_template("output.html", y=output)

if __name__ == "__main__":
    app.run()
