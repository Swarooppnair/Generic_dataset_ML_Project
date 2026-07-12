import logging
import os
from datetime import datetime


# Create a unique log file name using current date and time
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Create path to the logs folder
logs_path = os.path.join(os.getcwd(), "logs")


# Create logs folder if it does not exist
os.makedirs(logs_path, exist_ok=True)


# Create complete path of log file
log_file_path = os.path.join(logs_path, log_file)


# Configure logging system
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)


