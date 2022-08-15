from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
