import logging
import os

# Ensure the logs folder exists
os.makedirs('../logs', exist_ok=True)

# Configure logging to a file
logging.basicConfig(
    filename='../logs/etl.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()

# Log messages
logger.info("Logging to a file now")
logger.warning("This is a warning logged into file")
logger.error("An error logged into file")
