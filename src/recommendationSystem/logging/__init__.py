# Importing Libraries
import logging
import os
from datetime import datetime 
import sys

# Creating and saving log files 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs')
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# Defining Logs message structure
logging.basicConfig(
    #filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(levelno)s %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)",
    level = logging.INFO,

    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout),
    ]
)

# Testing the logger file
'''if __name__ == "__main__":
    logging.info("Logger has started")'''

logger = logging.getLogger('recommendation-system-logger')
logger.info("---------------x DIRECTORY CHANGE x------------------")