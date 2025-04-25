import sys
import os

# store error in  line no, filename, error
def error_message_detail():
    _,_,exc_tb = sys.exc_error_detail.exc_info()

# store error in  line no, filename, error

class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

    def __str__(self):
        return self.error_message
        
