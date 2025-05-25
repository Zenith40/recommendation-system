# Importing Libraries
import sys

# Defining structure of exception message
def error_message_detail(error:Exception,error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno
    error_message = f"Error occured in python script name [{file_name}] " \
        f"line number [{line_number}] error message [{error}]"
    return error_message

# Getting the exception message from sys
class CustomException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

# Testing the exception file
'''if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e,sys)''' 