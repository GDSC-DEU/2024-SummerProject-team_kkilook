from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] ='True'


@app.route("/")
def hello():
    return render_templates("main.html", title="Jinja test")

if __name__ == '__main__':
    app.run(debug=True)