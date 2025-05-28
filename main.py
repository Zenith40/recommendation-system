import numpy as np
import pandas as pd

from recommendationSystem.logging import logger
from recommendationSystem.components.data_ingestion import DataIngestion
from recommendationSystem.components.data_transformation import DataTransformation


logger.info("Starting the Custom logger")
logger.info("---------------x DIRECTORY CHANGE x------------------")

obj = DataIngestion()
data  = obj.initiate_data_ingestion()
DataTransformation().initiate_data_transformation_obj(data)

logger.info('------------------ | Execution Completed |---------------------')