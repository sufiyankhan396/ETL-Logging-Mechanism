import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure the logs folder exists
os.makedirs('../logs', exist_ok=True)

# Create a custom logger
logger = logging.getLogger('ETLLogger')
logger.setLevel(logging.DEBUG)

# Create a handler for rotating logs after file size reaches 1 KB (1000 bytes)
handler = RotatingFileHandler(
    '../logs/etl.log', maxBytes=1000, backupCount=3
)

# Create formatter and add it to the handler
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

# Log messages
logger.debug("Debug message - for troubleshooting")
logger.info("ETL job started")
logger.warning("This is a warning")
logger.error("ETL job failed")
logger.critical("Critical issue!")
