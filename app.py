from flask import Flask
from model.mysql import DataBase

app = Flask(__name__)


@app.route('/coin', methods=['GET'])
def coin_get():
    pass


if __name__ == '__main__':
    app.run(debug=True)