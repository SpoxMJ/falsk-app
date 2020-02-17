import mysql.connector
from flask import Flask, render_template, request, jsonify, make_response
import random
from typing import List, Dict
import json
import names


app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return render_template("index.html")


@app.route('/echo', methods=['POST'])
def add():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'heroes'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    msg1 = request.json['msg']
    msg = json.dumps(msg1)
    name = names.get_first_name()
    cursor.execute('INSERT INTO favorite_colors (name, color) VALUES (%s, %s)', (name, msg))
    connection.commit()
    cursor.close()
    connection.close()
    echo = {
        'status': 'ok',
        'msg': request.json['msg']
    }
    return jsonify(echo), 201


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'status': 'error'})), 400


@app.route('/random', methods=['GET'])
def rran():
    x = random.randint(0, 100)
    return jsonify({'status': 'ok', 'number': x})


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'heroes'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/list', methods=['GET'])
def index():
    return json.dumps({'favorite_colors': favorite_colors()})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
