from recommendationSystem.logging import logger
from recommendationSystem.utils.common import CustomException
import sys


logger.info("Welcome to my custom logging")

try:
    a = 1/0
except Exception as e:
    logger.info("Divide by Zero Error")
    raise CustomException(e,sys)