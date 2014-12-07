from expression import Expression
from DBmanager import Player
from DBmanager import take_highscore, save_user


class TakeThatMath:

    def __init__(self, name):
        self.name = name
        self.correct_answers = 0

    def ask_question(self):
        expression = Expression()
        print("Question #%s" % (str(self.correct_answers + 1)))
        print("What is the answer to %s?" % (expression))
        answer = input("Answer: ")
        if int(answer) != expression.calculate():
            print("You stupid motherfucker!")
            return False
        else:
            self.correct_answers += 1
            return True


def menu():
    while True:
        print("Welcome to the Do you even math? game!\n \
                Here are your options:\n \
                [1] Start \n \
                [2] Highscores\n \
                [3] Exit")
        selection = input("Option: ")

        if selection == 1 or selection == "Start":
            start_game()
        elif selection == 2 or selection == "Highscores":
            print_scores()
        elif selection == 3 or selection == "Exit":
            return
        else:
            print("That was invalid selection")


def print_scores():
    print("This is our current Top 10:\n")
    take_highscore()


def start_game():
    name = input("Enter your name: ")
    Math = TakeThatMath(name)
    print("Welcome %s! Let the math games begin!" % (Math.name))

    while True:
        if not Math.ask_question():
            save_user(name, Math.correct_answers*2)
            return


def main():
    print("Start")
    menu()

if __name__ == '__main__':
    main()
