from flask import request, jsonify
from api import app
from .predictor import get_price_prediction

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Welcome to realty price calculator!</h1>"

@app.route('/api/price/', methods=['POST'])
def get_price():
    realty_features = request.get_json()
    price = get_price_prediction(data)
    response = { 'price' : price }
    return jsonify(response)
