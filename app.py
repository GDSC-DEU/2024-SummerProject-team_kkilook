from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='Front-end/templates', static_folder='Front-end/static')

@app.route('/Front-end/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.static_folder, filename)
from flask import Flask, render_template

app.config['DEBUG'] = True

@app.route("/")
def hello():
    return render_template("main.html", title="Jinja test1")

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/month")
def month():
    return render_template("month.html")

@app.route("/medium")
def medium():
    return render_template("medium.html")



if __name__ == '__main__':
    app.run(debug=True, port=5001)
