import pandas as pd


def read_questions_and_responses_totals(questions_file_name, responses_file_name):
    questions = pd.read_csv(questions_file_name)
    responses = pd.read_csv(responses_file_name).dropna()
    survey_response_totals = dict.fromkeys(questions.columns)
    for question in questions.columns:
        survey_response_totals[question] = pd.DataFrame(data={}, index=[question], columns=questions[question].dropna().values)
        for value in questions[question].dropna().values:
            survey_response_totals[question].at[question, value] = len(responses[responses[question] == value])
    return survey_response_totals


def get_pivot_table(response_totals, questions_with_same_possible_answers):
    pivot_collector = []
    for totals in response_totals:
        if list(response_totals[totals].columns) == questions_with_same_possible_answers:
            pivot_collector.append(response_totals[totals])
    pivot_table = pd.concat(pivot_collector, axis=0)
    return pivot_table


def convert_words_to_numbers(responses_file_name, translations):
    converted_in_floats = pd.read_csv(responses_file_name).replace(to_replace=translations).dropna()
    for col in converted_in_floats.columns:
        if type(converted_in_floats[col]) == float:
            converted_in_floats[col] = int(converted_in_floats[col])
    return converted_in_floats

    
