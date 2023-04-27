import random

num = 0 
# these are all the colors in the 25-pair twisted pair color code
colors = ["blue", "green", "orange", "brown", "slate", "white", "red", "black", "yellow", "violet"]
# the user can pick a game mode to play with
mode = ""
# in elimination mode, the game only provides each number (1-600) once; the game ends once all 600 have been answered
numlist = list(range(1, 601))

# these variables are all for keeping various scores
keepingscore = False
pairscore = 0
bindscore = 0
bothcorrect = 0
totalscore = 0

# this "array" lays out the color code for binders and pairs
color_chart = [["white", "blue"], ["white", "orange"], ["white", "green"], ["white", "brown"], ["white", "slate"], 
               ["red", "blue"], ["red", "orange"], ["red", "green"], ["red", "brown"], ["red", "slate"],
               ["black", "blue"], ["black", "orange"], ["black", "green"], ["black", "brown"], ["black", "slate"],
               ["yellow", "blue"], ["yellow", "orange"], ["yellow", "green"], ["yellow", "brown"], ["yellow", "slate"],
               ["violet", "blue"], ["violet", "orange"], ["violet", "green"], ["violet", "brown"], ["violet", "slate"]] 

# this section runs when the program starts
def initial():
    print("\nWelcome to the 25-pair color quiz! I'll give you the number of a 25-pair copper twisted pair, and you give me the color of the pair and binder!\nPlease give answers in lowercase format.")
    print("\nYour color options are: blue, orange, green, brown, slate, white, red, black, yellow, violet\nTo give your answer, separate the colors with a slash (/), like this: blue/white")
    print('\nWould you like to play in Elimination mode or Infinite mode?')
    mode = (input("Mode: _"))
    mode.lower    
    # boolean for whether or not the mode has been checked
    modecheck = False 
    # this checks to make sure that the mode is valid  
    while modecheck == False: 
        if mode in ["elimination", "infinite"]:
            modecheck = True 
        else:
            print("I don't recognize that mode. Please pick between elimination or infinite.")
            mode = input("Mode: _")
            mode.lower

initial()
temp3 = input("Do you want to keep score while you play? y/n _")
temp3.lower
temp1 = True
while temp1 == True:
    if temp3 == "y": 
        keepingscore = True
        temp1 = False
    elif temp3 == "n":
        keepingscore = False
        temp1 = False
    else:
        print("I'm not sure what you meant. Please type y or n.")
        temp3 = input("Do you want to keep score while you play? y/n _")

# this variable controls whether the game loop is running
running = True 

# this runs based on the mode that the user picked
while running == True: 
    if mode == "elimination":
        num = random.choice(numlist)
        numlist.remove(num)
        if len(numlist) == 0:
                if keepingscore == True:
                    print ("You got " + str(totalscore) + " guesses correct.")
                print("Thanks for playing!")
                running == False
    else:
        num = random.randint(1,600)
    print("\nWhat binder and pair colors map to pair # " + str(num) + "?\n") 
    
    # the user specifies the binder color(s)
    binder = input("Binder: _") 
    bincol = (color_chart[(int(num/25-1))][0] + "/" + color_chart[(int(num/25-1))][1]) 
    if bincol == binder:
        print("Correct!")
        if keepingscore == True:
            bindscore += 1
            totalscore += 1
    else: 
        print("Incorrect.")
        # parses the user's answer to get the individual colors
        colist = binder.split(sep="/")
        temp5 = False
        while temp5 == False:
            for col in colist:
                if col not in colors:
                    print("Sorry, you misspelled something there.")
                    temp5 = True
            temp5 = True
        print("The correct answer was: " + bincol)

    # the user specifies the pair color(s)
    pair = input("Pair: _")
    paicol = (color_chart[(num%25)-1][0] + "/" + color_chart[(num%25)-1][1])
    if paicol == pair:
        print("Correct!")
        if keepingscore == True:
            pairscore += 1
            totalscore += 1
            if paicol == pair and bincol == binder:
                bothcorrect += 1
    else:
        print("Incorrect.")
        colist = pair.split(sep="/")
        temp5 = False
        while temp5 == False:
            for col in colist:
                # checks to make sure the user didn't misspell any of the colors or use an invalid color
                if col not in colors:
                    print("Sorry, you misspelled something there.")
                    temp5 = True
            temp5 = True
        print("The correct answer was " + paicol)

    if keepingscore == True:
        print("\nYou have gotten " + str(bindscore) + " binders correct and " + str(pairscore) + " pairs correct.\nYou have guessed both answers correctly " + str(bothcorrect) + " times." + "\nYour total score is " + str(totalscore) + "!")
    if mode == "elimination":
        print("You have " + str(len(numlist)) + " pairs left until you've guessed them all.")
    
    # check if user wants to keep looping
    temp2 = input("Would you like to keep going? y/n _")
    temp2.lower
    temp4 = False
    while temp4 == False:
        if temp2 == "n":
            if keepingscore == True:
                print ("You got " + str(totalscore) + " total guesses correct.")
            print("Thanks for playing!")
            running = False
        elif temp2 == "y":
            temp4 = True
        else:
            print("Please type y or n.")
