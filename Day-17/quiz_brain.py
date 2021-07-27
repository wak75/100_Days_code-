class QuizBrain():
    def __init__(self, q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0;
        
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"{self.question_number}: {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer, answer):
        if user_answer.lower()==answer.lower():
            print("You are Correct")
            self.score+=1            
        else:
            print("Sorry, your answer is incorrect")
        print(f"The correct answer is {answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")

   

        