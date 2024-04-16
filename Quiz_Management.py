import time
import random

class Question:
    def __init__(self, prompt, options, correct_answer, points):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer
        self.points = points

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def display_question(self, question):
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        user_answer = int(input("Enter your choice (1, 2, 3, etc.): ")) - 1
        if question.options[user_answer] == question.correct_answer:
            print("Correct!")
            self.score += question.points
        else:
            print("Incorrect!")

    def play_quiz(self):
        print("Welcome to the Quiz Game!")
        for question in self.questions:
            self.display_question(question)
            print()
            time.sleep(1)
        print(f"Quiz completed! Total score: {self.score}")
    
    def get_score_breakdown(self):
        score_breakdown = {}
        for question in self.questions:
            if question.points in score_breakdown:
                score_breakdown[question.points] += 1
            else:
                score_breakdown[question.points] = 1
        return score_breakdown

if __name__ == "__main__":
    quiz = Quiz()

    question1 = Question("What is the capital of France?", ["A. London", "B. Paris", "C. Berlin"], "B. Paris", 10)
    question2 = Question("Who wrote 'Romeo and Juliet'?", ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen"], "A. William Shakespeare", 15)
    question3 = Question("What is the chemical symbol for water?", ["A. H2O", "B. CO2", "C. NaCl"], "A. H2O", 20)
    question4 = Question("Which planet is known as the Red Planet?", ["A. Mars", "B. Venus", "C. Jupiter"], "A. Mars", 25)
    question5 = Question("Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso"], "B. Leonardo da Vinci", 30)
 

    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)
    quiz.add_question(question4)
    quiz.add_question(question5)

    quiz.play_quiz()
    
    score_breakdown = quiz.get_score_breakdown()
    print("\nScore Breakdown:")
    for points, count in score_breakdown.items():
        print(f"Points: {points} - Questions: {count}")