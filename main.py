import sys

from recommendationSystem.logging import logger
from recommendationSystem.utils.common import CustomException
from recommendationSystem.components.data_ingestion import DataIngestion

logger.info("Welcome to my custom logging")

obj = DataIngestion()
obj.initiate_data_ingestion()