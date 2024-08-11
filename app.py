from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='Front-end/templates', static_folder='Front-end/static')

@app.route('/Front-end/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.static_folder, filename)

app.config['DEBUG'] = True

@app.route("/", endpoint='main')
def hello():
    return render_template("main.html")

@app.route("/month")
def month():
    return render_template("month.html")

@app.route("/medium")
def medium():
    return render_template("medium.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/detail")
def detail():
    return render_template('detail.html')

@app.route("/season")
def season():
    return render_template('season.html')

@app.route("/recommend")
def recommend():
    return render_template('recommend.html')

@app.route("/withchild")
def withchild():
    return render_template('withchild.html')

@app.route("/alone")
def alone():
    return render_template('alone.html')

@app.route("/date")
def date():
    return render_template('date.html')

@app.route("/animal")
def animal():
    return render_template('animal.html')

@app.route("/weather")
def weather():
    return render_template('weather.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
