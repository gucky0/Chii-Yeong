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
##select game mode (topics)
##load the game
##play
##number of lives
##if run out, u die
##can retry or exit game
##
##if u win, can share on socials
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

login()

#rest of game



















    
