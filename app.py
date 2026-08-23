from flask import Flask, render_template

app = Flask(__name__)
contacts = {}

@app.route('/')
def home():
    return render_template('index.html', contacts = contacts)

if __name__ == "__main__":
    app.run(debug = True, port = 5001)