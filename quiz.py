import random

class Question:
    def __init__(self, prompt, answer_choices, correct_answer):
        self.prompt = prompt
        self.answer_choices = answer_choices
        self.correct_answer = correct_answer

    def __str__(self):
        return f"{self.prompt}\n\n{self.answer_choices}\n"

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def ask_question(self):
        current_question = self.questions[self.current_question_index]
        print(current_question)

        user_answer = input("Your answer: ")

        if user_answer == current_question.correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", current_question.correct_answer)

        self.current_question_index += 1

    def is_finished(self):
        return self.current_question_index == len(self.questions)

    def get_score(self):
        return self.score

def main():
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Rome"], "Paris"), #Paros is the capital of France
        Question("What is the largest ocean in the world?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean"], "Pacific Ocean"), #Pacific Ocean is the largest ocean in the world
        Question("What is the square root of 16?", ["4", "8", "12"], "4"), #4 is the square root of 16
        Question("Which of these is not a Data Unit?", ["Bit", "Riple", "Perabyte"], "Riple"), #Riple"   is not a Data Unit
        Question("Which of these is not a programmnig language?", ["Ruby", "Python", "Rast"], "Rast"), # "Recult" is not a programming language
        Question("What is the root of 9?", ["769", "683", "729"], "729"), #729 is the cube of 9
        Question("What country is most populated in the world?", ["India", "Russia", "Korea"], "India"), #India is the most populated country in the world
        Question("Which of these is not a JavaScript Framework?", ["react", "kivy", "angular"], "kivy"), #Kivy is not a JavaScript framework, it is a rather Python's
    ]

    quiz = Quiz(questions)

    while not quiz.is_finished():
        quiz.ask_question()

    print("Your score is:", quiz.get_score())

if __name__ == "__main__":
    main()
