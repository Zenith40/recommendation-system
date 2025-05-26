import sys

from recommendationSystem.logging import logger
from recommendationSystem.utils.common import CustomException
from recommendationSystem.components.data_ingestion import DataIngestion
from recommendationSystem.components.data_transformation import DataTransformation

logger.info("Starting the Custom logger")

obj = DataIngestion()
data  = obj.initiate_data_ingestion()
DataTransformation().initiate_data_transformation_obj(data)