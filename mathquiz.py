import random

num1 = 0
num2 = 0
rightAnswer = 0
operandChar = ""


def GenerateQuestion():
    randomOperand = random.randint(0, 3)
    global rightAnswer
    global num1
    global num2
    global operandChar
    num1 = random.randint(0, 11)
    num2 = random.randint(0, 11)
    if randomOperand == 0:
        rightAnswer = num1 + num2
        operandChar = "+"
    if randomOperand == 1:
        rightAnswer = num1 - num2
        operandChar = "-"
    if randomOperand == 2:
        rightAnswer = num1 * num2
        operandChar = "x"


def main():
    gameFinished = False
    score = 0
    name = input("What is your name?")
    print("Hi " + name + ", let's begin")
    while not gameFinished:
        GenerateQuestion()
        userAnswer = input("What is " + str(num1) + " " + operandChar + " " + str(num2) + "?")
        if userAnswer == str(rightAnswer):
            score = score + 1
            print("Correct! +1 \nScore: " + str(score))
        elif userAnswer == "bye":
            print("Bye " + name + "!")
            return
        else:
            print("Wrong!")
            score = score - 1
            if score < 0:
                score = 0


main()
