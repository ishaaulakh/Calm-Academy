default quotes=["List three things you are grateful for today.", "Describe a moment when you took a deep breath and felt instant relief. What caused the stress to dissipate?","Write about your favorite self-care activities and how they make you feel more relaxed.","Share a positive affirmation or mantra that helps you stay calm in challenging moments.", "Reflect on how disconnecting from screens for a while can ease stress. What do you do during this time?"]
define p = Character("Prompt:")
define n = Character("Read Entry:")
define t = Character("Calm Academy")
image bg room = "bg.png"
image ellie:
    "ellie.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73

label start:
    scene bg room 
    with fade
    show ellie
default menuset = set() 

t "Welcome to Calm Academy!"
t "Our goal is to provide you with knowledge and resources to help you manage your school-related stress."
t "We offer many informative lessons along with time-management, journalling, and meditation tools."
t "It is recommended to complete the lessons first in order to gain a better understanding of your mental health."

menu lessson_and_tools: 
    set menuset
    t "Would you like to view lessons or tools first?"

    "Lessons":
        jump lessons 

    "Tools":
        jump tools

menu lessons:
    set menuset
    t "Which tool would you like to visit first?"

    "All about Burnout":
        jump tm 

    "Mapping Habit Loops":
        jump journal 
            
    "Time Management":
        jump meditation 
        
    "Meditation":
        jump meditation 

    
menu tools:

    set menuset
    t "Which tool would you like to visit first?"

    "Time Management":
        hide ellie
        jump tm 

    "Guided Journalling":
        hide ellie
        jump journal 
        
    "Meditation":
        hide ellie
        jump meditation 

label journal:
    hide ellie
    scene bg room 
    with fade
    image b:
        "beta.png"
        zoom 0.75
    show b
    python:
        import os
        filename = renpy.input("Name your entry. (Previous journal entries can be found in app files)", length=32)
        directory = os.path.abspath(os.path.join(config.basedir, "Game","Journal", filename))
        file = open(directory+".txt","w") 
        rd_quotes = renpy.random.choice(quotes) 
    
    p "[rd_quotes]"
   
    python:
        file.write(renpy.input(""))
        file.close()

    t "Entry saved. (Previous journal entries can be found in the 'Journal' folder in your app files)."

    jump next 

label next:
hide b 
scene bg room 
with fade
menu nxt:
    
    set menuset
    "Where to next?"

    "Guided Journalling.":
        jump journal 

    "Meditation.":
        jump meditation 

    "Time Management":
        jump tm 
   
label meditation: 
    scene bg room 
    with fade

menu meditation2:
    set menuset
    "How long would you like to meditate for?"

    "1 minute":
        jump one

    "2 minutes":
        jump two

    "5 minutes":
        jump five

label tm:
    call screen planner 
    with fade
    t "Today's date is [renpy.store.formatted_date]. Click a '+' to add a task."


