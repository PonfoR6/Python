from question import question_data
from model import Questions
import random
from question_bank import QuestionBank


question_bank = []
for items in range(len(question_data)):
    quest = question_data[items]
    txt = quest["question"]
    ans = quest["correct_answer"]
    test_q = Questions(txt, ans)
    question_bank.append(test_q)


question_can = QuestionBank(question_bank)
question_can.kitas_klausimas()

while question_can.pabaiga_ir_taskai():
      question_can.kitas_klausimas()



