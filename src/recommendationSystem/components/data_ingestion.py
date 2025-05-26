import os
import sys

from recommendationSystem.logging import logger
from recommendationSystem.utils.common import CustomException
from recommendationSystem.config.configuration import DataIngestionConfig

import pandas as pd

#from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logger.info("Entered  the  Data Ingestion method")

        try:
            df_info = pd.read_csv('data/anime_data_24.csv')
            df_links = pd.read_csv('data/anime_links.csv')
            logger.info("Read the dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.data_path),exist_ok=True)
            logger.info("created directory for datframe")

            anime = df_info.merge(df_links,on='name')   

            anime.to_csv(self.ingestion_config.data_path,index=False,header=True)
            logger.info("Ingestion is completed")


            return(
                self.ingestion_config.data_path
            )

        except Exception as e:
            raise CustomException(e,sys)