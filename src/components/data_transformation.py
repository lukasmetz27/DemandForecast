import sys 
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transforamtion_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gen"
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps =[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )

            logging.info("Categorical columns encoding completed")

            preprocessor = ColumnTransformer(
                steps = [
                    ("num_pipeline", num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                 ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        

        