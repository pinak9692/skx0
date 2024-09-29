from src.drei.logger import logging #A1
from src.drei.exception import CustomException
#from src.Ein0.components import data_ingestion
from src.drei.components.data_ingestion import DataIngestion
from src.drei.components.data_ingestion import DataIngestionConfig

import sys

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

        #data_ingestion=DataIngestion()
            
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)