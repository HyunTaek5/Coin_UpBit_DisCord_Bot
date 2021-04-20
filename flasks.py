from flask import Flask

app = Flask(__name__)


@app.route('/')
def coin_get():
    return


if __name__ == '__main__':
    app.run(debug=True)