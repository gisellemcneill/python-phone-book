from flask import Flask, render_template, request, redirect

# To run the app, use the command: python3 app.py

app = Flask(__name__)
contacts = {}

@app.route('/')
def home():
    return render_template('index.html', contacts = contacts, resultMessage = "")

@app.route("/add", methods = ["POST"])
def add():
    contactName = request.form["contact_name"]
    contactPhone = request.form["contact_phone"]
    contactEmail = request.form["contact_email"]

    contacts[contactName] = {"phone": contactPhone, "email": contactEmail}

    return redirect("/")

@app.route("/delete", methods = ["POST"])
def delete():
    contactName = request.form["contact_name"]
    
    if contactName in contacts:
        del contacts[contactName]
    
    return redirect("/")

@app.route("/search", methods = ["POST"])
def search():

    searchName = request.form["search_name"].strip()
    matchedKey = None

    for contact in contacts:
        if contact.lower() == searchName.lower():
            matchedKey = contact
    
    if(matchedKey == None):
        resultMessage = ("Contact Not Found")
    else:
        resultMessage = (f"Contact Name: {matchedKey}, Phone: {contacts[matchedKey]['phone']}, Email: {contacts[matchedKey]['email']}")
    
    return render_template('index.html', contacts = contacts, resultMessage = resultMessage)
            




if __name__ == "__main__":
    app.run(debug = True, port = 5001)