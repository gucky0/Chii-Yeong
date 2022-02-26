"""
Mad Libs
- a word game where one player prompts another for a list of words
to substitute for blanks in a story

Noun: object, person, animeal, place
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
Creating a menu window
https://data-flair.training/blogs/python-mad-libs-generator-game/#:~:text=Mad%20libs%20generator%20is%20a,stories%20after%20filling%20the%20blanks.
Replace method
https://www.teachwithict.com/mad_libs.html
Look for indicators instead of multiple inputs
http://anh.cs.luc.edu/handsonPythonTutorial/madlib2.html
Other ideas:
- different stories (random)
- save answers into a profile (txt)
- grammer (if)
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
        noun =              "apron"
        bodyPart1 =         "hands"
        bodyPart2 =         "pants"
        bodyPart3 =         "tongue"
        bodyPart4 =         "ear"
        action4 =           "moan"
        adjective1 =        "sloppy"
        food1 =             "banana"
        food2 =             "lollipop"
        action5 =           "swallow"
        adjective2 =        "darkest"
        verb =              "let"
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
        adjective1 =        input("Enter an adjective (w/o -ing: ")
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
all night long. \nWhat I would really want is to see you with a/an {outfit}. \
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
fantasy. If you would {verb} \
me. \n{explitive}! \
I want you. I want you so bad. So anyway, give me a call back. I \
would love to have a {holiday} \
date very very soon. :)")








