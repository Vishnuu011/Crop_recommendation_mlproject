import os
import pickle
from dataclasses import dataclass
from sklearn.metrics import accuracy_score
import numpy as np

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging


import os
import sys
import pandas as pd
#from pathlib import Path
import numpy as np
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pickle
#from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score




def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    
def evaluate_models(X_train, y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get accuracy scores for train and test data
            
            test_model_score = accuracy_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report



    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
    

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)
