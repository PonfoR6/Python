from question import question_data
import random


class QuestionBank:

    def __init__(self, list_of_questions):
        self.pts = 0
        self.list_of_questions = list_of_questions
        self.q_number = 0

    def other_questions(self):
        f_question = self.list_of_questions[self.q_number]
        self.q_number += 1
        user_answer = input(f"{self.q_number}, {f_question.text} T/F?")
        if user_answer == f_question.answer:
            self.pts += 1
            print(f"correct! your score is: {self.pts}")
        elif user_answer == "T" and f_question.answer == "True":
            self.pts += 1
            print(f"correct! your score is: {self.pts}")
        elif user_answer == "F" and f_question.answer == "False":
            self.pts += 1
            print(f"correct! your score is: {self.pts}")
        else:
            print("wrong.")

    def end_and_points(self):

        if self.q_number < len(self.list_of_questions):
            return True
        else:
            print(f"Total sum of all points {self.pts}")
            if self.pts > 7:
                print("wow you really know your computer history!")
            elif self.pts < 2:
                print("I see you haven't done your homework")
            return False
