from flask import Flask, render_template, request, redirect, url_for, jsonify
import json


app = Flask(__name__)
DATA_FILE = "data.json"


with open(DATA_FILE, "w") as file:
    json.dump([], file)

def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        new_entry = {"name": name, "email": email, "password": password}

        data = load_data()
        data.append(new_entry)
        save_data(data)

        return redirect(url_for("data_page"))

    return render_template("login.html")

@app.route("/data")
def data_page():
    data = load_data()
    return render_template("data.html", users=data)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=True)







# flask project which render a template create routes for adding data in json file updating data deleating and display data every json data should have format of name phone email skill and id
