import os 
import sys

import numpy as np
import pandas as pd

from src.exception import custom_exceptions

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            np.save(file_obj,obj)
    except Exception as e:
        raise custom_exceptions(e,sys)
