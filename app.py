from src.Student_Performance_Indicator.logger import logging
from src.Student_Performance_Indicator.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("The execution has started")


    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
 