#data_ingestion.py  →  data_transformation.py  →  model_trainer.py  →  predict_pipeline.py
#data_ingestion.py = Data ko laana + split/save karna
#data_transformation.py = Missing values, encoding, scaling
#model_trainer.py = ML/DL model train
#predict_pipeline.py = Model load + predictions

import os
import sys
from src.exception import custom_exceptions
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# Data fetching / loading
# Model training ke liye data ko train.csv aur test.csv me split karna.
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) 
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)  
            
            logging.info("Ingestion of the data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise custom_exceptions(e,sys)
    
if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data,_=obj.initiate_data_ingestion()
            
        
