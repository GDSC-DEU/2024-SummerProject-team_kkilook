from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='Front-end/templates', static_folder='Front-end/static')
app.config['DEBUG'] = True

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/heart")
def heart():
    return render_template('heart.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
