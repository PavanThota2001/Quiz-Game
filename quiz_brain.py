class QuizBrain:
    def __init__(self, Q_list):
        self.question_number = 0
        self.question_list = Q_list
        self.score = 0

    def has_any_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"your final score {self.score}/{self.question_number}")
            return False


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower()Q:
            print("correct")
            self.score += 1
        else:
            print("wrong")
        print(f"correct answer is {correct_answer}")
        print(f"your current score: {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)




