from question import question_data
import random


class QuestionBank:

    def __init__(self, list_of_questions):
        self.taskai = 0
        self.list_of_questions = list_of_questions
        self.q_number = 0

    def kitas_klausimas(self):
        f_question = self.list_of_questions[self.q_number]
        self.q_number += 1
        user_answer = input(f"{self.q_number}, {f_question.text} T/F?")
        if user_answer == f_question.answer:
            self.taskai += 1
            print(f"geras atsakymas, your score is: {self.taskai}")
        else:
            print("netinkamas atsakymas")

    def pabaiga_ir_taskai(self):
        if self.q_number < len(self.list_of_questions):
            return True
        else:
            print(f"Visu tasku suma {self.taskai}")
            if self.taskai > 7:
                print("wow nusimanai kompiuteriu istorija!")
            elif self.taskai < 2:
                print("aiskiai vadovelio neskaitei")
            return False
