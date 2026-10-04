from flask import Flask, render_template, request, redirect
import json

# To run the app, use the command: python3 app.py
# lower() turns the string into lowercase, strip() removes whitespace from the beginning and end of the string

app = Flask(__name__)

try: 
    with open ("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

@app.route('/')
def home():
    return render_template('index.html', contacts = contacts, resultMessage = "")

@app.route("/add", methods = ["POST"])
def add():
    contactName = request.form["contact_name"].strip()
    contactPhone = request.form["contact_phone"].strip()
    contactEmail = request.form["contact_email"].strip()

    contacts[contactName] = {"phone": contactPhone, "email": contactEmail}
    save_contacts()

    return redirect("/")

@app.route("/delete", methods = ["POST"])
def delete():
    contactName = request.form["contact_name"]
    
    if contactName in contacts:
        del contacts[contactName]
    
    save_contacts()
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

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
            




if __name__ == "__main__":
    app.run(debug = True, port = 5001)