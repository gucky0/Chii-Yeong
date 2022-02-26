"""
Mad Libs
- a word game where one player prompts another for a list of words
to substitute for blanks in a story

Program Flow:
0) take/make a paragraph for your story
1) ask user for all the words needed -using input()
2) display story to user - using print and f-string
3) default story -using if statement

Noun: object, person, animal, place
Example words:
- man
- home
- table
- John

Adjective: descriptor
Example words:
- gentle
- sharp
- big
- charming

Verb: action
- run
- dance
- slide
- go

Example Sentences
this is a (adjective) (noun).
this is a    green      car.

Other Resources:
Creating a menu window /
https://data-flair.training/blogs/python-mad-libs-generator-game/#:~:text=Mad%20libs%20generator%20is%20a,stories%20after%20filling%20the%20blanks.
Replace method /
https://www.teachwithict.com/mad_libs.html
Look for indicators instead of multiple inputs /
http://anh.cs.luc.edu/handsonPythonTutorial/madlib2.html
Other ideas:
- different stories (random) /
- save answers into a profile (txt) / 
- grammer (if)
- random word inputs (random)
"""

def examples():
    noun = input("Noun: ")
    noun2 = input("Noun: ")
    adj = input("Adjective: ")

def madlib(default=True):
    if default == True:
        feeling1 =          "tired"
        action1 =           "showering"
        feeling2 =          "love"
        action2 =           "cuddle"
        action_or_feeling = "squeal"
        action3 =           "snuggle"
        outfit1 =           "apron"
        bodyPart1 =         "hands"
        outfit2 =           "pants"
        bodyPart2 =         "tongue"
        bodyPart3 =         "ear"
        action4 =           "moan"
        adjective1 =        "sloppy"
        food1 =             "banana"
        food2 =             "lollipop"
        action5 =           "swallow"
        adjective2 =        "darkest"
        action6 =           "let"
        explitive =         "Fxck"
        holiday =           "Valentine's"
    else:
        feeling1 =          input("Enter a bad feeling: ")
        action1 =           input("Enter an action (with -ing): ")
        feeling2 =          input("Enter a good feeling: ")
        action2 =           input("Enter an action: ")
        action_or_feeling = input("Enter an action or feeling: ")
        action3 =           input("Enter an action: ")
        outfit1 =           input("Enter a type of outfit: ")
        bodyPart1 =         input("Enter a body part: ")
        outfit2 =           input("Enter a part of outfit: ")
        bodyPart2 =         input("Enter a body part: ")
        bodyPart3 =         input("Enter a body part: ")
        action4 =           input("Enter an action: ")
        adjective1 =        input("Enter an adjective (w/o -ing): ")
        food1 =             input("Enter a type of food: ")
        food2 =             input("Enter a type of food: ")
        action5 =           input("Enter an action: ")
        adjective2 =        input("Enter an adjective (with -est): ")
        action6 =           input("Enter an action: ")
        explitive =         input("Enter an explitive: ")
        holiday =           input("Enter a holiday: ")
    print(f"I feel so {feeling1}. \
I was {action1} \
this morning and I was fantasizing about \
how I would {feeling2} \
it if you would {action2} \
me; that would realy make me {action_or_feeling} \
and I would want to {action3} \
all night long. \nWhat I would really want is to see you with a/an {outfit1}. \
What it would do to me when I put my {bodyPart1} \
on your {outfit2}, \
my {bodyPart2} \
in your {bodyPart3}, \
you {action4}, \
and lots of {adjective1} \
kissing. \nI was wondering about your {food1}. \
Do you want me to lick it like a/an {food2}? \
I would love to {action5} \
you. I want to explore your most {adjective2} \
fantasy. If you would {action6} \
me. \n{explitive}! \
I want you. I want you so bad. So anyway, give me a call back. I \
would love to have a {holiday} \
date very very soon. :)")
    
def madlib1():
    animals= input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')
def madlib2():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')  
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  
def madlib3():
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')

def madlib_tk():
    from tkinter import Tk, Label, Button
    WIDTH = HEIGHT = 300
    FONT = 'arial 15'
    COLOR = 'ghost white'

    # boilerplate / template
    screen = Tk()
    screen.geometry(str(WIDTH)+'x'+str(HEIGHT))
    screen.title('Mad Libs Game')
    Label(screen, text= 'Mad Libs\n Have Fun!' , font = 'arial 20 bold').pack()
    Label(screen, text = 'Click Any One :', font = f'{FONT} bold').place(x=40, y=80)
    Button(screen,
           text=    'The Photographer',
           font=    FONT,
           command= madlib1,
           bg =     COLOR)\
           .place(x=60, y=120)
    Button(screen,
           text=    'apple and apple',
           font=    FONT,
           command= madlib2 ,
           bg =     COLOR)\
           .place(x=70, y=180)
    Button(screen,
           text=    'The Butterfly',
           font=    FONT,
           command= madlib3,
           bg =     COLOR)\
           .place(x=80, y=240)
    screen.mainloop()

def madlib_replace(choice = 0):
    import random, re
    
    with open('story.txt','r') as f:
        texts = f.readlines()    
        #print(texts)

    if choice != None:
        text = texts[choice]
    else:
        text = random.choice(texts)
    new_text = text
    
    words = []
    start_index = new_text.find('<')+1
    while start_index != 0:
        end_index = new_text.find('>')
        
        word = new_text[start_index:end_index]
        new_word = input(f'enter a {word:<9} : ')
        words.append(new_word)
        new_text = new_text[:start_index - 1] + new_word + new_text[end_index + 1:]

        start_index = new_text.find('<')+1
    print(new_text)
    return words

def matlib_save():
    import json

    with open('words.json') as infile:
        data = json.load(infile)
        
    #data = {}
    username = input('enter your name: ')
    data[username] = madlib_replace(choice = 0)
    with open('words.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)

    with open('words.json') as infile:
        data = json.load(infile)
        print(data)
    

def matlib_load(username, choice=0):
    from itertools import cycle
    import json

    with open('story.txt','r') as f:
        texts = f.readlines()    
        #print(texts)

    if choice != None:
        text = texts[choice]
    else:
        text = random.choice(texts)
    new_text = text
    
    with open('words.json') as infile:
        data = json.load(infile)

    words = data[username]
    words_cycle = cycle(words)

    start_index = new_text.find('<')+1
    while start_index != 0:
        end_index = new_text.find('>')
        
        word = new_text[start_index:end_index]

        #changes made here
        new_word = next(words_cycle)

        new_text = new_text[:start_index - 1] + new_word + new_text[end_index + 1:]

        start_index = new_text.find('<')+1
    print(new_text)









    

'''
moody
running
happy
eat
cry
write
pajama
hair
pant
hand
shoulder
type
sharp
ramen
burger
drink
happiest
sleep
cibai
national day
'''






