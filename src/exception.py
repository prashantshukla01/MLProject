import sys
from .logger import logging


def error_message_details(error , error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script [{0}] at line [{1}] with message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message   # return alag line pe hona chahiye

class custom_exceptions(Exception):
    def __init__(self , error_message, error_detail:sys):
        super().__init__(error_message)  # fixed super()
        self.error_message = error_message_details(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
    
    
    
    