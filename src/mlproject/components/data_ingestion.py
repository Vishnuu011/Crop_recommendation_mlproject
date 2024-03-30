import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "raw.csv")


class DataIngestion:

    def __init__(self):

        self.data_ingestion_config=DataIngestionConfig()


    def initiate_data_ingestion(self):

        logging.info("data ingestion started.......")

        try:
            data=pd.read_csv("https://raw.githubusercontent.com/Vishnuu011/datastore/main/Crop_recommendation.csv")


            os.makedirs(os.path.dirname(os.path.join(self.data_ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.data_ingestion_config.raw_data_path, index=False)
            logging.info("raw dataset saved in atifacts")



            logging.info("data ingestion completed..........")

            return(
               self.data_ingestion_config.raw_data_path

            )
        except Exception as e:
            raise CustomException(e, sys)  

                   

