# Trivia
# Lets see how much you know Chii Yeong!

##1) questions -using input /
##2) check answer -using if statement /
##3) score -using increment /

def one_qn():
    question = 'How old am I? '
    answer = '26'
    guess = input(question) 

    score = 0

    if guess == answer:
        score += 1 # score = score + 1 aka increment
        print("correct")
    else:
        print("wrong")




# many questions
def many_qn():
    questions = ["How old am I? ",
                 "What is my gender? "]

    answers   = ["26",
                 "Male"]

    score = 0
    for index,question in enumerate(questions):
        guess = input(question)

        if guess == answers[index]: #slicing [index]
            score += 1 # score = score + 1 aka increment
            print("Correct!\n")
        else:
            print("Wrong!\n")

    print("You scored:", score)





# lives
def lives_qn():
    lives = 3
    questions = ["How old am I? ",
                 "What is my gender? "]

    answers   = ["26",
                 "Male"]

    score = 0

    for index,question in enumerate(questions):
        while lives:
            guess = input(question)

            if guess == answers[index]: #slicing [index]
                score += 1 # score = score + 1 aka increment
                print("Correct!\n")
                break # for while-loop
            else:
                lives -= 1 # lives = lives - 1
                print("Wrong!",lives,"lives left.\n")
                
        if lives == 0:
            print("You are not a true friend! :(")
            break # for the for-loop
            
    print("You scored:", score,"/",len(questions))
    quit()
