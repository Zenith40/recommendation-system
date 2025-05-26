import sys
import pandas as pd
import pickle

from recommendationSystem.utils.common import CustomException

class return_data:
    def __init__(self):
        pass

    def predict(self):
        try:
            matrix_path = 'artifact\\similarity.pkl'
            data_path = 'artifact\\transformed_data.csv'
            transformed_data = pd.read_csv(data_path)
            matrix = pickle.load(open(file=matrix_path,mode='rb'))
            return transformed_data, matrix

        except Exception as e:
            raise CustomException(e,sys)
        