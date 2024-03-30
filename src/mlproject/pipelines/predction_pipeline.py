import os
import sys
import pandas as pd
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.utils import load_object

class PredictPipeline:

    
    def __init__(self):
        print("init.. the object")

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")

            model=load_object(model_path)

            
            pred=model.predict(features)

            return pred

        except Exception as e:
            raise CustomException(e,sys)
        


class CustomData:
    def __init__(self,
                 Nitrogen:int,
                 Phosphorous:int,
                 Potassium:int,
                 temperature:float,
                 humidity:float,
                 ph:float,
                 rainfall:float,
                ):
        
        self.Nitrogen=Nitrogen
        self.Phosphorous=Phosphorous
        self.Potassium=Potassium
        self.temperature=temperature
        self.humidity=humidity
        self.ph=ph
        self.rainfall=rainfall
            
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Nitrogen':[self.Nitrogen],
                'Phosphorous':[self.Phosphorous],
                'Potassium':[self.Potassium],
                'temperature':[self.temperature],
                'humidity':[self.humidity],
                'ph':[self.ph],
                'rainfall':[self.rainfall]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
