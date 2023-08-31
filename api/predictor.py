from api import app
import json
from catboost import CatBoostRegressor
import pandas as pd
import os


def get_price_prediction(data):
    '''
    Get prediction for realty price
    :param data: A dict with realty features
    :return: integer or None
    '''
    model = CatBoostRegressor()      # parameters not required.
    model_id = 2
    path_to_model = os.path.abspath(os.path.join(
        'api', 'static', 'ml_models', f'model{model_id}.cbm'))
    model.load_model(path_to_model)
    try:
        df = pd.DataFrame(data, index=[0])
        result = round(model.predict(df)[0])
        
    except Exception as e:
        result = None
    return result
