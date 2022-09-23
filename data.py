import requests

NUMBER_OF_QUESTIONS = 10
TYPE_OF_QUESTIONS = "boolean"
question_data = []

parameters = {
    "amount": NUMBER_OF_QUESTIONS,
    "type": TYPE_OF_QUESTIONS
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

for questions in data["results"]:
    question_data.append(questions)
