#import module  
from tkinter import *             # Importing everything from the tkinter module
                                                 
# initialize window
root = Tk()                                                                       # Creating the main window
root.geometry('300x300')                                                          # Setting the window size to 300x300 pixels
root.title('Fun with Mad Libs!')                                                  # Setting the window title
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()  # Adding a label to the window with the title
Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)       # Adding a label with instructions

# Predefined sets of nouns, verbs, and adjectives
valid_nouns = {"dog", "cat", "elephant", "pilot", "teacher", "doctor", "shirt", "car", "pizza", "ice cream", "banana", "monkey", "chocolate", "biryani", 
               "park", "apple", "house", "tree", "computer", "chair", "table", "book", "bottle", "phone", "shoe", "hat", "beach",
               "restaurant", "bicycle", "garden", "mountain", "river", "city", "village", "cheese", "skirt", "pant", "frock", "butterfly", "bee", "cockroach", "ant", 
               "grasshopper"} 

valid_verbs = {"running", "jumping", "eating", "flying", "swim", "reading", "writing",
               "singing", "dancing", "playing", "walking", "talking", "driving", "sleeping", "crying", "listening", "thinking",
               "laughing", "crying"} 
               
valid_adjectives = {"happy", "sad", "colorful", "bright", "dark", "big", "small", "fast", "slow",
                    "hot", "cold", "warm", "cool", "strong", "weak", "beautiful", "ugly", "new",
                    "old", "shiny", "dull", "one", "two", "three", "many", "this","these","that", 
                    "those", "my", "your", "his", "her", "better", "bigger","smaller", "delicious"}  

################   Stories  ##############

# Function to validate user input against a set of valid inputs
def validate_input(prompt, valid_set):
    user_input = input(prompt)                                                      # Prompting user for input
    while user_input not in valid_set:                                              # Checking if input is in the valid set
        print("Please enter a valid input from the predefined set.")                # Printing error message if input is invalid
        user_input = input(prompt)                                                  # Prompting user for input again
    return user_input                                                               # Returning valid input

# Function for the first Mad Libs story
def madlib1():
    animals = validate_input('enter an animal name: ', valid_nouns)                 # Validating animal name input
    profession = validate_input('enter a profession name: ', valid_nouns) 
    cloth = validate_input('enter a piece of clothing: ', valid_nouns)  
    things = validate_input('enter a thing name: ', valid_nouns)  
    name = input('enter a name: ')                                                  # Prompting user for name input without validation
    place = validate_input('enter a place name: ', valid_nouns)  
    verb = validate_input('enter a verb in -ing form: ', valid_verbs)  
    food = validate_input('enter a food name: ', valid_nouns) 

    # Printing the completed story with the user's inputs
    print(f'''
          Story : The Photographer''')
    print(f'''
          Say {food}, the photographer said as the camera flashed! {name} and I had gone to {place} to get our photos taken today. 
          The first photo we really wanted was a picture of us dressed as {animals} pretending to be {profession}. 
          When we saw the second photo, it was exactly what I wanted. 
          We both looked like {things} wearing {cloth} and {verb} exactly what I had in mind.''')

# Function for the second Mad Libs story
def madlib2():
    adjective = validate_input('enter an adjective: ', valid_adjectives)             # Validating adjective input
    color = input('enter a color name: ')  
    thing = validate_input('enter a thing name: ', valid_nouns)  
    place = validate_input('enter a place name: ', valid_nouns) 
    person = input('enter a person name: ')                                          # Prompting user for person name input without validation
    adjective1 = validate_input('enter another adjective: ', valid_adjectives)  
    insect = validate_input('enter an insect name: ', valid_nouns)                 
    food = validate_input('enter a food name: ', valid_nouns) 
    verb = validate_input('enter a verb: ', valid_verbs)  

    # Printing the completed story with the user's inputs
    print(f'''
          Story : The Butterfly''')
    print(f'''
          Last night I dreamed I was a {adjective} butterfly with {color} splotches that looked like {thing}.
          I flew to {place} with my best friend {person} who was a {adjective1} {insect}. 
          We ate some {food} when we got there and then decided to {verb}. 
          The dream ended when I said—let\'s {verb}.''')

# Function for the third Mad Libs story
def madlib3():
    person = input('enter a person name: ')                                          # Prompting user for person name input without validation
    color = input('enter a color: ')  
    foods = validate_input('enter a food name: ', valid_nouns)  
    adjective = validate_input('enter an adjective: ', valid_adjectives) 
    thing = validate_input('enter a thing name: ', valid_nouns)  
    place = validate_input('enter a place name: ', valid_nouns) 
    verb = validate_input('enter a verb: ', valid_verbs)  
    adverb = input('enter an adverb: ')                                              # Prompting user for adverb input
    food = validate_input('enter a food name: ', valid_nouns)  
    things = validate_input('enter a thing name: ', valid_nouns) 
    # Printing the completed story with the user's inputs
    print(f'''
          Story : Apple and Apple''')
    print(f'''
          Today we picked apples from {person}\'s orchard. 
          I had no idea there were so many different varieties of apples. 
          I ate {color} apples straight off the tree that tasted like {foods}. 
          Then there was a {adjective} apple that looked like {thing}. 
          When our bags were full, we went on a free hay ride to {place} and back. 
          It ended at a hay pile where we got to {verb} {adverb}. 
          I can hardly wait to get home and cook with the apples. 
          We are going to make apple {food} and {things} pies!''')
    
######  Buttons  ######
# Setting up buttons to launch the different Mad Libs stories
Button(root, text='The Photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)  #Button for the first story
Button(root, text='Apple and Apple', font='arial 15', command=madlib3, bg='ghost white').place(x=70, y=180) 
Button(root, text='The Butterfly', font='arial 15', command=madlib2, bg='ghost white').place(x=80, y=240)  
# Running the main loop of the tkinter window
root.mainloop() 
