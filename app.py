from src.Student_Performance_Indicator.logger import logging
from src.Student_Performance_Indicator.exception import CustomException
from src.Student_Performance_Indicator.components.data_ingestion import DataIngestion
from src.Student_Performance_Indicator.components.data_ingestion import DataIngestionConfig
from src.Student_Performance_Indicator.components.data_transformation import DataTransformation, DataTransformationConfig
# from src.Student_Performance_Indicator.components.data_transformation import DataTransformationConfig


import sys


if __name__=="__main__":
    logging.info("The execution has started")


    try:
        # data_ingestion.initiate_data_ingestion()
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

        # config = DataTransformationConfig()
        # data_transformation_config = DataTransformationConfig
        data_transformation=DataTransformation()
        # train_arr,test_arr = data_transformation.initiate_data_transormation(train_data_path, test_data_path)
        data_transformation.initiate_data_transormation(train_data_path, test_data_path)

        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
 