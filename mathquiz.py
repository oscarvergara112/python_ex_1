import random
import time
import keyboard
import os

num1 = 0
num2 = 0
rightAnswer = 0
operandChar = ""
userExists = False
attempts = 0
correctAnswers = 0
name = ""
score = 0


def GenerateQuestion():
    global rightAnswer
    global num1
    global num2
    global operandChar
    randomOperand = random.randint(0, 2)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if randomOperand == 0:
        rightAnswer = num1 + num2
        operandChar = "+"
    elif randomOperand == 1:
        rightAnswer = num1 - num2
        operandChar = "-"
    elif randomOperand == 2:
        rightAnswer = num1 * num2
        operandChar = "x"


def LoadGame():
    global userExists
    global score
    global attempts
    global correctAnswers
    try:
        f = open(name + ".txt", "r")
        lines = f.readlines()
        userExists = True
        score = int(str.strip((lines[1])))
        attempts = int(str.strip((lines[2])))
        correctAnswers = int(str.strip((lines[3])))
        f.close()
    except FileNotFoundError:
        pass


def SaveGame():
    if not userExists:
        f = open(name + ".txt", "w")
        f.write(name + '\n')
        f.write(str(score) + '\n')
        f.write(str(attempts) + '\n')
        f.write(str(correctAnswers) + '\n')
        f.close()
    else:
        os.remove(name + ".txt")
        f = open(name + ".txt", "w")
        f.write(name + '\n')
        f.write(str(score) + '\n')
        f.write(str(attempts) + '\n')
        f.write(str(correctAnswers) + '\n')
        f.close()
        f.close()


def main():
    gameFinished = False
    global attempts
    global correctAnswers
    global userExists
    global name
    global score
    name = input("What is your name?")
    score = 0
    LoadGame()
    time.sleep(1)
    if userExists:
        print("Welcome back " + name + ", let's begin")
    else:
        print("Hi " + name + ", let's begin")
    while not gameFinished:
        GenerateQuestion()
        userAnswer = input("What is " + str(num1) + " " + operandChar + " " + str(num2) + "?")
        if str(userAnswer) == str(rightAnswer):
            score = score + 2
            attempts = attempts + 1
            correctAnswers = correctAnswers + 1
            print("Correct! +2 \nScore: " + str(score))
        else:
            score = score - 1
            attempts = attempts + 1
            print("Wrong! -1 \nScore: " + str(score))
            if score < 0:
                score = 0
        if keyboard.is_pressed('q'):
            print("Bye " + name + "!")
            SaveGame()
            time.sleep(2)
            gameFinished = True


main()
