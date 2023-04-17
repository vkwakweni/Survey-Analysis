import pandas as pd


def read_questions_and_responses_totals(questions_file_name, responses_file_name):
    questions = pd.read_csv(questions_file_name)
    responses = pd.read_csv(responses_file_name).dropna()  # drop the entire row (response)
    survey_response_totals = dict.fromkeys(questions.columns)  # having questions.columns lines 7&8 feels redundant
    for col in questions.columns:
        survey_response_totals[col] = pd.DataFrame(data={}, index=questions[col].values, columns=[col]).dropna()
        for value in questions[col].dropna().values:
            survey_response_totals[col].at[value, col] = len(responses[responses[col] == value])
    return survey_response_totals


def convert_words_to_numbers(responses_file_name, translations):
    return pd.read_csv(responses_file_name).dropna().replace(to_replace=translations)

# TODO: Separate demographics from the actual data
# TODO: encode the length of the response sheet as the number of responses you get.
    
