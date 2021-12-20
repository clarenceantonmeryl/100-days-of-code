from day_17_data import question_data
from day_17_question import Question


class Quiz:

    def __init__(self):
        self.score = 0
        self.current_index = 0
        self.questions = []
        for item in question_data["results"]:
            self.questions.append(Question(item["question"], item["correct_answer"] == "True"))

    def display_current_question(self):
        print(self.questions[self.current_index].question)

    def display_score(self):
        print(f"{self.score} / {self.current_index + 1}")

    def check_answer(self):
        answer_input = input("Enter answer (t/f): ").lower()
        if answer_input == "t":
            answer_input = True
        elif answer_input == "f":
            answer_input = False
        else:
            print("Invalid answer")

        if answer_input == self.questions[self.current_index].answer:
            self.score += 1
            return True
        else:
            return False
