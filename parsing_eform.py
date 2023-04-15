import pandas as pd


def read_questions_and_responses_totals(questions_file_name, responses_file_name):
    questions = pd.read_csv(questions_file_name).dropna()
    responses = pd.read_csv(responses_file_name).dropna()
    # TODO: check what questions looks like when dropna'd
    survey_data = dict.fromkeys(questions.columns)
    for col in questions.columns:
        survey_data[col] = pd.DataFrame(data={}, index=questions[col].values, columns=[col])
        for value in questions[col].values:
            survey_data[col].at[value, col] = len(responses[responses[col] == value])
    return survey_data


def read_questions_and_responses_related(questions_file_name, responses_file_name):
    questions = pd.read_excel(questions_file_name)
    responses = pd.read_excel(responses_file_name)

# TODO: Separate demographics from the actual data
# TODO: encode the length of the response sheet as the number of responses you get.
    
