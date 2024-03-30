import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, LabelEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging




class FeatureEncoder(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        encoder=LabelEncoder()
        matrix=encoder.fit_transform(X[["label"]])
        X['label'] = matrix
        return X
    



class DataTransformation:

    def __init__(self):

        pass


    def initialize_data_transformation(self,raw_data):
        logging.info("data transformation started .......")
        try:
            data=pd.read_csv(raw_data)

            logging.info("Applying preprocessing object on training and testing datasets.")

            preprocessing_obj = FeatureEncoder()

            input_feature_data_arr=preprocessing_obj.fit_transform(data)
            logging.info(print(data['label'].value_counts()))

            train_data, test_data=train_test_split(data, test_size=0.25)

            logging.info("Applying preprocessing object on training and testing datasets.")

            train_arr=np.array(train_data)
            test_arr=np.array(test_data)



            return (
               train_arr,
               test_arr
            )

        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)