import logging
from logger import setup_logger

def extract_data():
    logging.info("Starting data extraction")
    # Simulate extraction
    logging.info("Data extraction completed")

def transform_data():
    logging.info("Starting data transformation")
    # Simulate transformation
    logging.info("Data transformation completed")

def load_data():
    logging.info("Starting data loading")
    # Simulate load
    logging.info("Data loaded successfully")

def main():
    setup_logger()
    extract_data()
    transform_data()
    load_data()

if __name__ == "__main__":
    main()