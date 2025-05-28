import os
import sys

import numpy as np
import pandas as pd

from recommendationSystem.logging import logger
from recommendationSystem.config.configuration import DataTransformationConfig
from recommendationSystem.utils.common import (
    CustomException,
    save_object,
    removing_blank_lines,
    removing_pre_suff_ix,
    converting_into_vectors,
    finding_similarity
)

class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation_obj(self,data_path):

        logger.info("Entered the Data Transformation method")

        try:
            anime = pd.read_csv(data_path)
            logger.info("Read the dataset")

            # Making Directory to store the data
            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_data_path),exist_ok=True)
            logger.info("created directory for datframe")

            anime_1 = anime.copy()
            logger.info("Created a copy of the dataset")

            anime_1 = anime_1[['image','name','tags','links']]
            anime_1 = anime_1.reset_index(drop=True)
            anime_1 = anime_1.rename({'name':'title'},axis=1)
            logger.info("Formatted the copied dataset")

            anime_1.tags = anime_1.tags.apply(removing_blank_lines)
            anime_1.tags = anime_1.tags.apply(removing_pre_suff_ix)
            vectors = converting_into_vectors(anime_1.tags)
            similarity = finding_similarity(vectors)
            logger.info("Calculated the similarity score")

            anime_1.to_csv(self.data_transformation_config.transformed_data_path,index=False,header=True)
            
            save_object(

                file_path = self.data_transformation_config.similarity_obj_path,
                obj = similarity


            )

            logger.info("Saved the transformed dataframe & similarity matrix")
            logger.info("Transformation is completed")
            logger.info("---------------x DIRECTORY CHANGE x------------------")

            return (
                self.data_transformation_config.transformed_data_path,
                self.data_transformation_config.similarity_obj_path
            )

            
        except Exception as e:
            raise CustomException(e,sys)
