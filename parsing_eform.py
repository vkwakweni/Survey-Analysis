import pandas as pd
import numpy as np

def read_questions_to_df():
    pass

def read_responses_to_df():
    pass

def read_questions_and_responses_to_df(file_name):
    # this basically an alias so need this step would probably fit in with the step that builds the array for responses
    survey_data = pd.read_excel(io=file_name, sheet_name=None) 
    return survey_data
    

# will need something like an array to save responses