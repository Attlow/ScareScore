from flask import  Flask, request, jsonify 
import pandas as pd
import json
from pandas.core.indexes.api import _new_Index

app = Flask(__name__)

tabela = pd.read_csv('ScareScore.csv')
tb_data = tabela.to_json(orient='records')
tb_json = json.loads(tb_data)


@app.route('/')
def home():
    return 'A API está no ar'


@app.route('/movies')
def movies():
    return tb_json


@app.route('/movies/<name>')
def movie_name(name):
    movie = tabela[tabela['name'].str.lower() == name.lower()]
    return movie.to_json(orient='records')

app.run(host='0.0.0.0')