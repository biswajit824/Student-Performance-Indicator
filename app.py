from src.Student_Performance_Indicator.logger import logging
from src.Student_Performance_Indicator.exception import CustomException
from src.Student_Performance_Indicator.components.data_ingestion import DataIngestion
from src.Student_Performance_Indicator.components.data_ingestion import DataIngestionConfig

import sys


if __name__=="__main__":
    logging.info("The execution has started")


    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
 