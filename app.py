from flask import Flask, render_template, request, redirect

app = Flask(__name__)
contacts = {}

@app.route('/')
def home():
    return render_template('index.html', contacts = contacts)

@app.route("/add", methods = ["POST"])
def add():
    contactName = request.form["contact_name"]
    contactPhone = request.form["contact_phone"]
    contactEmail = request.form["contact_email"]

    contacts[contactName] = {"phone": contactPhone, "email": contactEmail}

    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True, port = 5001)