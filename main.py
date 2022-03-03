from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_route():
    return render_template("index.html")


@app.route("/blog")
def blog_route():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
