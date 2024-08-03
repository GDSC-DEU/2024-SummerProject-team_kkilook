from flask import Flask, render_template

app = Flask(__name__, template_folder='Front-end/templates', static_folder='Front-end/static')
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return render_template("main.html", title="Jinja test1")

@app.route("/test")
def home():
    return "Hello, Flask~~~"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
