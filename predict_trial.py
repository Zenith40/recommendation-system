import sys
#import pandas as pd
#import pickle
import os

from recommendationSystem.components.data_ingestion import DataIngestion
from recommendationSystem.components.data_transformation import DataTransformation
from recommendationSystem.utils.common import CustomException

class return_data:
    def __init__(self):
        pass

    def predict(self):
        try:
            #matrix_path = os.path.join("artifact","similarity.pkl")
            #data_path = os.path.join("artifact","transformed_data.csv")
            obj = DataIngestion().initiate_data_ingestion()
            matrix_path, data_path = DataTransformation().initiate_data_transformation_obj(obj)
            #transformed_data = pd.read_csv(data_path)
            #matrix = pickle.load(open(file=matrix_path,mode='rb'))
            #return transformed_data, matrix
            return matrix_path,data_path

        except Exception as e:
            raise CustomException(e,sys)