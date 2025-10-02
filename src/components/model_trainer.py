import os 
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor, 
    GradientBoostingRegressor,
    RandomForestRegressor)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import custom_exceptions
from src.logger import logging
from src.utils import evaluate_model
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        self.model = None
        
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            # params={
            #     "Decision Tree": {
            #         'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'], 
            #     },
            #     "Random Forest":{
            #         # Number of trees in random forest
            #         'n_estimators': [8,16,32,64,128,256]
            #     }
            #     }
            model_report:dict= evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models = models)
            
            
            # to get best model score from dictionary
            best_model_score = max(sorted(model_report.values())) 
            
            
            # to get best model name from dictionary  
             
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)   
            ]
            best_model = models[best_model_name]
            
            if best_model_score<0.6:
                raise Exception("No best model found")
            
            logging.info(f"Best found model on both training and testing dataset")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted=best_model.predict(X_test)
            
            r2_square = r2_score(y_test,predicted)
            return r2_square
        
        except Exception as e:
            raise custom_exceptions(e,sys)
            
                