##madlibs
##
## sign up /
    ##ask user if he is new or existing user
    ##if new/existing user
    ##input username
    ##input password
    ##if correct, let him play
    ##if wrong, kick him out
##
##select game mode (topics) /
##load the game /
##play /
##number of lives /
##if run out, u die /
##can retry or exit game /
##
##can share on socials /
##unlock new modes



##username = input ('Enter a username...')
##password = input ('Enter a password...')

##if exist_username.lower() == 'a':
##    print('username check: yes')
##if exist_password.lower() == 'b':   
##    print('password check: yes')
##else:
##    print('password check: no. Quitting Progam')
##    quit()
##print('Rest of code')



##stored_credentials = {'user1':'a','user2':'a'}
##
### .lower() changes any input to lowercase - for checking
### if user is a new user
##if not (username.lower() in stored_credentials.keys()):
##    stored_credentials[username] = password
### if user is an existing user
##else:
##    if password == stored_credentials[username.lower()]:
##        pass
##        #rest of game
##        
##    else:
##        #reprompt
##        quit()




def login(user=None, tries=2):
    users = ['user1', 'user2']
    if user == None:
        user = input("username: ")
    if tries == 0:
        print("Maximum number of tries exceeded! Quitting Program...")
        quit()

    correct_password = ['a','b']
    password = input("password: ")

    # user exists
    if user in users:
        index = users.index(user)
        if password == correct_password[index]:
            print("login successful")
        else:
            print("wrong password")
            tries = tries - 1
            login(user=user, tries=tries)
        print()
    # new user
    else:
        users.append(user)
        correct_password.append(password)
        print(users)
        print(correct_password)

def lives_qn():
    lives = 3
    questions = ["How old am I? ",
                 "What is my gender? ",
                 "What is my favorite waifu? "]

    answers   = ["26",
                 "Male",
                 "Ram" ]

    score = 0
    guesses = []

    for index,question in enumerate(questions):
        while lives:
            guess = input(question)
            guesses.append(guess)
            
            if guess.lower() == answers[index].lower(): #slicing [index]
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
    matlib_save(guesses,save=True)
    retry=input("Do you want to retry? ")
    if retry.lower() == "yes":
        print()
        mode()
    else:
        quit()


def matlib_save(guesses, save = False): #change to without playing game
    if save == False:
        return
    
    import json
    filename = 'answers.json'

    with open(filename, 'r') as infile:
        data = json.load(infile)
        
##    data = {}
    username = input('enter your name: ')
    data[username] = guesses
    
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)

    with open(filename, 'r') as infile:
        data = json.load(infile)
        

#rest of game
def mode():
    topic=input("choose a topic: ")
    if topic=="biography":
        lives_qn()
    else:
        print("Topic doesn't exist. \n")
        mode()



mode()













    
