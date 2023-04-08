import pandas as pd
import numpy as np

def read_questions_to_df():
    pass

def read_responses_to_df():
    pass

def read_questions_and_responses_to_df(file_name):
    survey_data = pd.read_excel(io=file_name, sheet_name=None)  # will have to see if the dictionary returned uses sheet names as keys.
    return survey_data
    

# will need something like an array to save responses