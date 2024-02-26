define y = Character("You", color="#813b68")
define e = Character('Ellie', color="#3f596c")
define t = Character("Calm Academy")

image bg room:
    "bg.png"
image messy:
    "messy.jpeg"
    zoom 0.68
image clean:
    "clean.jpeg"
    zoom 0.2
image SAB1:
    "SAB1.png"
    xpos 0.5
    ypos 0.55
image stress1:
    "stress1.png"
    xpos 0.45
    ypos 0.7
image stress2:
    "stress2.png"
    xpos 0.45
    ypos 0.7
image stress3:
    "stress3.png"
    xpos 0.5
    ypos 0.8
image stress31:
    "stress31.png"
    xpos 0.5
    ypos 0.8
image stress32:
    "stress32.png"
    xpos 0.5
    ypos 0.8
image stress4:
    "stress4.png"
    xpos 0.43
    ypos 0.7
image stress5:
    "stress5.png"
    xpos 0.43
    ypos 0.8
image anxiety1:
    "Anxiety1.png"
    xpos 0.5
    ypos 0.8
image anxiety2:
    "Anxiety2.png"
    xpos 0.45
    ypos 0.77
image anxiety3:
    "Anxiety3.png"
    xpos 0.45
    ypos 0.7
image anxiety31:
    "Anxiety31.png"
    xpos 0.45
    ypos 0.77
image anxiety32:
    "Anxiety32.png"
    xpos 0.45
    ypos 0.73
image anxiety33:
    "Anxiety33.png"
    xpos 0.4
    ypos 0.7
image anxiety4:
    "Anxiety4.png"
    xpos 0.43
    ypos 0.77
image burnout1:
    "burnout1.png"
    xpos 0.4
    ypos 0.7
image burnout2:
    "burnout2.png"
    xpos 0.5
    ypos 0.8
image burnout21:
    "burnout21.png"
    xpos 0.5
    ypos 0.8
image burnout22:
    "burnout22.png"
    xpos 0.5
    ypos 0.8
image burnout23:
    "burnout23.png"
    xpos 0.5
    ypos 0.8
image burnout24:
    "burnout24.png"
    xpos 0.5
    ypos 0.8
image 3P:
    "3P.png"
    xpos 0.45
    ypos 0.7
image P1:
    "P1.png"
    xpos 0.45
    ypos 0.7
image P2:
    "P2.png"
    xpos 0.45
    ypos 0.85
image P3:
    "P3.png"
    xpos 0.45
    ypos 0.85
image P4:
    "P4.png"
    xpos 0.45
    ypos 0.85
image 2P1:
    "2P1.png"
    xpos 0.45
    ypos 0.7
image 2P2:
    "2P2.png"
    zoom 0.8
    xpos 0.42
    ypos 0.62
image 2P3:
    "2P3.png"
    zoom 0.8
    xpos 0.42
    ypos 0.62
image 2P4:
    "2P4.png"
    zoom 0.8
    xpos 0.42
    ypos 0.62
image 2P5:
    "2P5.png"
    zoom 0.8
    xpos 0.42
    ypos 0.62
image 2P6:
    "2P6.png"
    xpos 0.45
    ypos 0.8
image S1:
    "S1.png"
    xpos 0.5
    ypos 0.75
image S2:
    "S2.png"
    xpos 0.5
    ypos 0.75
image S3:
    "S3.png"
    xpos 0.5
    ypos 0.75
image S4:
    "S4.png"
    xpos 0.5
    ypos 0.75
image S5:
    "S5.png"
    xpos 0.5
    ypos 0.75
image Matrix:
    "Matrix.png"
    zoom 0.85
    xpos 0.5
    ypos 0.63

python:
    rd_prompt = renpy.random.choice(prompt) 
    ellie_costume = ""
image ellie:
    "ellie.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image ellie1:
    zoom 0.6
    xpos 0.8
    ypos 0.73
image ellie2:
    zoom 0.6
    xpos 0.8
    ypos 0.73
image ellie3:
    zoom 0.6
    xpos 0.8
    ypos 0.73
image ellie4:
    zoom 0.6
    xpos 0.8
    ypos 0.73
image ellie5:
    zoom 0.6
    xpos 0.8
    ypos 0.73
image ellie6:
    zoom 0.6
    xpos 0.8
    ypos 0.73
image l_ellie:
    "ellie.png"
    zoom 0.3
    xpos 0.87
    ypos 0.68
image ellie4:
    "ellie4.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image artellie:
    "artellie.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image artellie1:
    "artellie1.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image artellie2:
    "artellie2.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image artellie3:
    "artellie3.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image artellie4:
    "artellie4.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image bakerellie:
    "bakerellie.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image bakerellie1:
    "bakerellie1.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image bakerellie2:
    "bakerellie2.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image bakerellie3:
    "bakerellie3.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image bakerellie4:
    "bakerellie4.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image bakerellie5:
    "bakerellie5.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
image bakerellie6:
    "bakerellie6.png"
    zoom 0.6
    xpos 0.8
    ypos 0.73
init python:
    config.keymap['screenshot'] = None 
    config.keymap['hide_windows'] = None
    config.keymap['accessibility'] = None
    
label start:
    play music "audio/Bossa.mp3"
    scene bg room 
    with fade
    show screen skip
    default menuset = set() 
    show ellie

    t "Welcome to Calm Academy!"
    hide ellie
    hide screen quick_menu
    show ellie4
    t "Our goal is to provide you with knowledge and resources to help you manage your school-related stress."
    t "This app offers a planner that organizes and colour codes your tasks by priority..."
    hide ellie4
    show ellie
    t "a guided journal where you can reflect on your experiences or read previous entries..."
    t "and three types of meditation where you can practice mindfulness."
    t "In addition to those three tools, this app offers informative activities where you can learn about mental health and burnout management strategies."
    hide ellie
    show l_ellie

label lesson_and_tools:
    hide ellie4
    hide artellie4
    hide bakerellie4
    hide ellie
    scene bg room
    hide screen skip
    show l_ellie
    show screen activities_or_tools
    t "Would you like to view activities or tools (planner, journal, meditation)?"

label activities:
    hide screen activities_or_tools
    show screen activity_menu
    t "Which activity would you like to start?"

label tools:
    hide screen activities_or_tools
    show screen tools_menu
    t "Which tool would you like to use?"

label Journal:
    hide l_ellie
    hide screen tools_menu
    call screen name_new_entry
    with fade
    jump tools

label Meditation: 
    hide screen tools_menu 
    show screen meditation_menu
    t "Select a meditation type."

    label boxBreathing:
        hide l_ellie
        hide screen meditation_menu
        show ellie4
        python:
            def is_positive_float(value):
                try:
                    temp = float(value)
                    is_positive = temp > 0
                    return is_positive
                except ValueError:
                    return False

            while True:
                meditation_length = renpy.input("Great choice! How many minutes would you like to meditate for?")

                if is_positive_float(meditation_length):
                    meditation_length = float(meditation_length)
                    break
                else:
                    renpy.say("Calm Academy", "Please enter a valid positive number.")
        hide ellie4
        show ellie
        t "Got it, [meditation_length] minutes. Grab some headphones and find a comfortable place to sit and click whenever you're ready to begin."
        t "You may click again while meditating to finish early."
        play music "audio/Meditation.mp3"
        $ renpy.movie_cutscene("boxBreathing.webm", delay=(meditation_length * 60.0), stop_music=False, loops=-1)
        stop movie
        play music "audio/Bossa.mp3"
        t "Meditation complete! Remember that you can return to this sense of calm whenever you need it. (Click to return to menu)"
        hide ellie
        show l_ellie
        jump lesson_and_tools

    label deepBreathing:
        show ellie4
        hide l_ellie
        hide screen meditation_menu
        python:
            def is_positive_float(value):
                try:
                    temp = float(value)
                    is_positive = temp > 0
                    return is_positive
                except ValueError:
                    return False

            while True:
                meditation_length = renpy.input("Nice pick! How many minutes would you like to meditate for?")

                if is_positive_float(meditation_length):
                    meditation_length = float(meditation_length)
                    break
                else:
                    renpy.say("Calm Academy", "Please enter a valid positive number.")
        hide ellie4
        show ellie
        t "Got it, [meditation_length] minutes. Grab some headphones and find a comfortable place to sit and click whenever you're ready to begin."
        t "You may click again while meditating to finish early."
        play music "audio/Meditation.mp3"
        $ renpy.movie_cutscene("deepBreathing.webm", delay=(meditation_length * 60.0), stop_music=False, loops=-1)
        stop movie
        play music "audio/Bossa.mp3"
        t "Meditation complete! Remember that you can return to this sense of calm whenever you need it. (Click to return to menu)"
        hide ellie
        show l_ellie
        jump lesson_and_tools

    label nature:
        show ellie4
        hide l_ellie
        hide screen meditation_menu
        python:
            def is_positive_float(value):
                try:
                    temp = float(value)
                    is_positive = temp > 0
                    return is_positive
                except ValueError:
                    return False

            while True:
                meditation_length = renpy.input("Sounds good! How many minutes would you like to meditate for?")

                if is_positive_float(meditation_length):
                    meditation_length = float(meditation_length)
                    break
                else:
                    renpy.say("Calm Academy", "Please enter a valid positive number.")
        hide ellie4
        show ellie
        t "Got it, [meditation_length] minutes. Grab some headphones and find a comfortable place to sit and click whenever you're ready to begin."
        t "You may click again while meditating to finish early."
        play music "audio/Meditation.mp3"
        $ renpy.movie_cutscene("All1.webm", delay=(meditation_length * 60.0), stop_music=False, loops=-1)
        stop movie
        play music "audio/Bossa.mp3"
        t "Meditation complete! Remember that you can return to this sense of calm whenever you need it. (Click to return to menu)"
        hide ellie
        show l_ellie
        jump lesson_and_tools

label tm:
    hide l_ellie
    hide screen tools_menu
    call screen planner 
    with fade
    t ""

label SAB:
    hide screen activity_menu
    with fade
    show SAB1
    t "When we evaluate our mental state, we often use the words “stress”, “anxiety”, and “burnout” interchangeably. This ambiguous language can make it difficult to address what’s really going on. (Click to continue)"
    t "This activity will help you learn more about these terms, so you're better equipped to manage your wellness."
    hide SAB1
    show screen leave
    menu SAB_Buttons:
        set menuset
        t "Learn more about stress, anxiety, and burnout by clicking the buttons. Start the final activity once you're ready!"
        "More About Stress":
            jump Stress

        "More About Anxiety":
            jump Anxiety

        "More About Burnout":
            jump Burnout

        "Final Activity!":
            jump SAB_Practice

label Stress:
    hide screen leave
    t "Stress is the overall experience of your nervous system being overwhelmed. Physical, mental, and emotional factors can all contribute to this experience."
    show stress1
    t "Take a moment to read through the causes above, and see if you can recognize any in your life."
    hide stress1
    show stress2
    t "Similar to the causes, symptoms can also be physical, mental, or emotional."
    t "Knowing common symptoms can help you identify stress early on."
    hide stress2
    menu Stress_1:
        set menuset
        t "How frequently do you feel any of these symptoms?"
        "Every day.":
            t "It's okay to feel that way. If you are experiencing severe stress that affects your functioning, is long-term, or is increasing in severity, that may be a symptom of a stress disorder."  
            t "Seeking help from a healthcare professional can help you better manage your symptoms. Recovering from stress is possible."

        "Sometimes":
            t "That's totally normal! A little bit of stress can help keep you alert and motivated."
            t "Ensure that it doesn't become too intense or frequent, or else the negative effects will outweigh the positive."

        "Almost Never":
            t "That's good to hear! It sounds like you manage your stress proactively."

        "Hmm...":
            t "It's alright if you don't know or don't want to share!"
            t "Continue to think about this question in the future, if you're not sure about the answer."
    t "Let's go over a few steps you can follow to assess your stress level."
    show stress3
    t "First, ask yourself where you feel stress in your body, and how it manifests in your life."
    hide stress3
    show stress31
    t "Next, try to assess the duration, frequency, and intensity of your symptoms. Ask yourself if the stressor is mild, moderate, severe, or catastrophic..."
    t "...and if it’s acute (eg. working on a group project with unhelpful group members), or persistent (eg. consistently struggling to meet expectations in a certain subject)."
    t "This can help put them into perspective." 
    hide stress31
    show stress32
    t "Symptoms can be further categorized based on their source (eg. family, finances, school, etc.)."
    hide stress32
    t "Finally, let's discuss how to manage stress."
    t "Self care is essential for maintaining your emotional well being and bouncing back from stressful situations."
    menu Stress_2:
        set menuset
        t "Do you practice any of these common ways of self care?"
        "Cooking or eating healthy meals":
            t "Who does't love a good meal! Proper nutrition helps all kinds of physical and mental processes."

        "Spending time with family or friends":
            t "That's great! It's important to stay connected with your support system."

        "Leisure time (eg. reading)":
            t "Awesome! Working on personal interests outside of school or work is what makes us unique and well-rounded."
    show stress4
    t "Check out this list of self-care ideas!"
    hide stress4
    show stress5
    t "Self care isn't the only way to manage stress. Here are some other ways."
    hide stress5
    menu Stress_3:
        set menuset
        t "Great job learning more about mental wellness! Did you learn anything new about stress?"
        "Yes, I understand the causes better.":
            t "That's great! It's important to recognize different stressors."

        "Yes, I understand the symptoms better.":
            t"That's great! It's important to recognize different signs of stress."

        "Nope, all review.":
            t "That's fine! It's always good to reinforce your knowledge."
    show screen leave
    jump SAB_Buttons

label Anxiety:
    hide screen leave
    menu Anxiety_1:
        set menuset
        t "Let's start with a little trivia question! What's one difference between stress and anxiety?"
        "They're the same thing":
            t "They're very similar, but not quite the same!"

        "Stress in external and anxiety is internal":
            t "Bingo!"

        "Anxiety is more intense and long-term.":
            t "That's right!"
        
        "How they're spelled, duh?":
            t "That is true..."
    show anxiety2
    t "Stress and anxiety are both uncomfortable experiences urging you to “fix” a problem."
    t "Stress can appear in our lives very suddenly, but it is usually short-term. Once the source of stress is gone, your symptoms will decline."
    t "Anxiety, on the other hand, can continue even after the stressor is gone. It is more long-term and can lead to more intense responses, such as panic attacks and anxiety attacks."
    t "Another difference between stress and anxiety is that sources of stress are typically external (eg. Needing to study for a test) and sources of anxiety are typically internal (eg. Believing you’re not capable of doing well on a test)."
    hide anxiety2
    t "Now, let's focus on anxiety specifically."
    show anxiety1
    t "Anxiety is a persistent feeling of worry or tension towards the future, triggered by either a real or perceived threat."
    t " This threat triggers an adrenaline rush which initiates the body’s fight-or-flight response, leading to various physical, mental, and behavioral symptoms."
    hide anxiety1
    menu Anxiety_2:
        set menuset
        t "Is it normal to experience anxiety?"
        "Yes, but only if you have an anxiety disorder.":
            t "True, but people without anxiety disorders can also feel anxious."
            t "Anxiety disorders are characterized by intense or frequent anxiety. If you think you are experiencing this, a healthcare professional can provide guidance." 

        "Yes, everyone can experience it.":
            t "Very true! It is normal to experience anxiety in your life."
            t "Anxiety disorders, on the other hand, are characterized by intense or frequent anxiety."
            t "If you think you are experiencing this, a healthcare professional can provide guidance."
    t "Next, let's go over some common symptoms. While going through the following information, reflect on how you personally experience anxiety."
    show anxiety3
    t "Anxiety can manifest itself physically..."
    hide anxiety3
    show anxiety31
    t "emotionally..."
    hide anxiety31
    show anxiety32
    t "mentally..."
    hide anxiety32
    show anxiety33
    t "and in other miscellaneous ways."
    hide anxiety33
    t "It is okay to feel these symptoms, and there are many ways of managing them."
    show anxiety4
    t "Some anxiety-specific strategies are keeping a worry jar or notebook, or setting a worry time (as unconventional as it sounds!)"
    t "Keeping a jounal is another good idea, as they can provide insight into what triggers your symptoms."
    t "Finally, self care can play a big role in managing anxiety. This can look different from person to person, whether it's eating healthy meals, or playing video games with friends."
    t "If your anxiety is more severe, a healthcare professional can provide a more specific plan."
    hide anxiety4
    menu Anxiety_3:
        set menuset
        t "Great job learning more about mental wellness! Did you learn anything new about anxiety?"
        "Mhm, I understand the causes better.":
            t "That's great! It's important to recognize different triggers."

        "Mhm, I understand the symptoms better.":
            t "That's great! It's important to recognize different signs of anxiety."

        "Not really.":
            t "That's fine! It's always good to reinforce your knowledge."
    show screen leave
    jump SAB_Buttons
    
label Burnout:
    hide screen leave
    t "Ack, my schedule is packed!"
    t "Studying from 5-7, school from 8-3, and extracurriculars from 4-9?! This sounds like a recipe for disaster..."
    t "or more specifically, a recipe for burnout!"
    t "Burnout is the inability to meet constant demands resulting in exhaustion and a lack of motivation. Symptoms can be mental, physical, or emotional."
    show burnout1
    t "Take a moment to read through the symptoms above, and see if you have experienced any before."
    hide burnout1
    menu Burnout_1:
        set menuset
        t "Burnout can happen to anyone. Do you know how to recover from it?"
       
        "Yup!":
            t "Awesome! That's some valuable information."
            t "I'll provide some of my own knowledge too, and you can pick out the most helpful ideas."
       
        "Nope!":
            t "That's alright!"

        "I don't know.":
            t "That's alright!"

        "Uhh.. you're really putting me on the spot, huh?":
            t "Sorry, haha! I guess it's my job to tell you, not the other way around."

    t "Let's go over five steps to recover from burnout."
    show burnout2
    t "Admitting that you are burned out is the first step to recovering. It’s okay if this feels difficult, because often the things making us feel burnt out are something important to us."
    hide burnout2
    show burnout21
    t "Next, distance yourself from the stressor. For example, you can take a day off from school, ask to postpone/omit some assignments, or take a break from stressful extracurricular activities."
    hide burnout21
    show burnout22
    t "Once some distance has been created, focus on self care and physical wellness. Get an extra hour of sleep, eat a nutritious meal, or spend quality time with your loved ones."
    hide burnout22
    show burnout23
    t "After your health starts to improve, reevaluate your goals and values. Ask yourself if you are prioritizing what is most important to you, and if your mindset is helping you or setting you back. "
    hide burnout23
    show burnout24
    t "Finally, explore concrete changes you can make to improve your wellbeing and commit to them."
    t "For example, schedule leisure time for yourself every week, or cut off relationships that burn you out."
    t "Various other stress management strategies, such as journaling, meditation, and exercise can combat burnout."
    hide burnout24
    menu Burnout_2:
        set menuset
        t "Great job learning more about mental wellness! Did you learn anything new about burnout?"
        "Yup, I understand the symptoms better.":
            t "That's great! Knowing symptoms of burnout can help you differentiate it from stress or anxiety."

        "Yup, I understand how to recover better.":
            t "That's great! Burnout is exhausting, so it can help to have a step-by-step plan."

        "No, all review.":
            t "That's fine! It's always good to reinforce your knowledge."
    show screen leave
    jump SAB_Buttons

label SAB_Practice:
    hide l_ellie
    scene messy
    with fade
    show artellie
    "It's 5 in the evening and Ellie is hard at work trying to finish up an art project."
    e "..."
    y "Hey, Ellie!"
    hide artellie
    show artellie1
    "Your friend barely looks up."
    show artellie2
    e "Oh, hey! I'm trying to finish this STUPID project. I'm going as fast as I can, but I'll never be done in time."
    hide artellie2
    y "Anything I can do to help? This room could use some cleaning."
    show artellie2
    e "I know, but I don't care what my room looks like right now. I just don't have the time!"
    hide artellie2
    show artellie1
    y "Something to eat?"
    hide artellie1
    show artellie
    e "Didn't I tell you?? I  don't have the time!!!"
    "As you look around the room, you notice empty cups of instant noodles and bags of chips strewn across the floor."
    e "I need this to be perfect, but I just can't get the colours right!"
    menu Practice_1:
        set menuset
        y "Ellie, I think you're struggling with..."
       
        "Stress":
            e "Stress? Well, why do you think that?"
        "Anxiety":
            e "Anxiety? No, this is caused by my project, which is an external factor. It's not an internal feeling, so I doubt it's anxiety."
            y "Hmm, well in that case..."
            jump Practice_1
    
        "Burnout":
            e "Burnout? No, this is a short-term feeling. I doubt it's burnout."
            y "Oh, well in that case..."
            jump Practice_1
    y "Being in a cluttered environment, eating junk food, and perfectionism can all cause stress!"
    hide artellie
    show artellie4
    e "Well, I have been pretty emotionally reactive lately, and I have this awful headache!"
    
    menu Practice_2:
        set menuset
        y "Do you..."
       
        "Feel like this often?":
            e "Not really, I'm just stressed because of this project. My symptoms aren't too intense either."
       
        "Have very intense symptoms?":
            e "No, I just feel a little off because of this project. I usually feel fine."
    
        "Have something more fun you could be working on?":
            e "Anything would be more fun than this, but procrastinating isn't the way to go."
            jump Practice_2
    
    menu Practice_3:
        set menuset
        y "Ellie, I think you should..."
       
        "Finish this project tomorrow":
            e "...but it's due tomorrow?"
            y "Oh, right! I guess that wouldn't work."
            jump Practice_3
        "Come watch a movie with me":
            e "No, if I don't work on this project then the stress won't go away."
            y "That's true. I guess procrastinating isn't a good idea."
            jump Practice_3
    
        "Work in a cleaner environment":
            e "Hmm, alright. Let's move to the living room maybe? You'll need to help me move all these paints and brushes!"
            y "Not a problem!"
            
    scene clean
    with fade
    show artellie3
    e "This area feels a lot more calm, and it's so close to the kitchen! Could you bring me a few more bags of chips?"

    menu Practice_4:
        set menuset
        y "..."
        "Sure, what flavour?":
            e "Ketchup, barbeque, sour cream and onion, anything is fine!"
            hide artellie3
            show artellie4
            e "Well, now that I think about it, I've been eating chips all day. They probably don't hold a lot of nutritional value, considering I'm still hungry and exhausted."
        "I think a healthier snack would give you more energy.":
            hide artellie3
            show artellie4
            e "Hmmm...now that I think about it, I've been eating chips all day. They probably don't hold a lot of nutritional value, considering I'm still hungry and exhausted."
    e "Let's go with a healthy snack!"
    "You return a few moments later with a plate of carrot sticks and hummus. In the meantime, Ellie has seemed to make more progress on her artwork."
    y "Feeling better? I hope the clean room is helping."
    hide artellie4
    show artellie2
    e "Yes, I feel better, but what if I feel stressed again? I doubt sitting in the living room and eating carrot sticks is the answer to all my problems."
    y "Managing stress takes constant effort. Whether it's exercising regularly, asking your family for support, or cutting down on unecessarry tasks, there's a lot of ways to reduce stress."
    y "It's up to you to decide what strategies work best, but there's lots of online and in-person tools to help!"
    hide artellie2
    show artellie4
    e "I see, thanks so much for your help. Let's get this painting finished!"
    "Congrats on completing the final activity! Future app updates will allow you to keep different Ellie costumes (eg. Artist Ellie) as a reward."
    hide screen leave
    jump lesson_and_tools   

label TM:
    hide screen activity_menu
    with fade
    show screen leave
    menu TM_Buttons:
        set menuset
        t "Click a button to learn more about time management. Start the practice activity once you're ready!"
        "Planning":
            jump Planning

        "Prioritizing and Performing":
            jump Prioritizing_and_Performing
        
        "SMART Goals":
            jump SMART

        "Practice Activity!":
            hide l_ellie
            jump TM_Practice

label Planning:
    hide screen leave
    show 3P
    t "The time management process can be divided into three steps, known as the 3Ps: Planning, performing, and prioritizing!"
    hide 3P
    show P1
    t "Let's start with the first P: Planning."
    t "Planning helps bridge the gap between where you are right now, and where you want to reach in the future."
    t "It gives you a clear sense of what needs to be done and how long it will take. At the end of the day or week, you can look back on all the things you’ve completed and feel a sense of accomplishment!"
    t "This sense of accomplishment can help you prevent or recover from burnout."
    t "Planning also helps you keep note of important deadlines and test dates. Procrastinating and receiving poor grades can cause significant stress, so it’s important to be aware of what you have to do."
    hide P1
    menu Planning_1:
        set menuset
        t "There is a difference between effective and ineffective planning. Out of these goals, which seems the most effective?"
        "Study math for 2 hours.":
            t "This is a good goal, but it's not specific enough. Which topics are you studying? What method will you use to study?"
            jump Planning_1
        "Complete 15 questions in chapter 2 by tonight.":
            t "Correct! This goal is great because it specifically tells you which questions to complete and when they need to be done."
        "Complete 15 questions in chapter 2.":
            t "This is a good goal, but it doesn't tell you when it needs to be completed."
            jump Planning_1
    show P2
    t "It's always a good idea to separate big projects into specific activities."
    hide P2 
    show P3
    t "You should also allocate a specific and realistic amount of time for these activites."
    hide P3 
    show P4
    t "Finally, try to write all of your tasks down on paper or online. Keeping it in your head can make you feel more anxious, and increases your chance of forgetting something."
    hide P4
    t "Once you're done planning, the next step is to pick which tasks to do first, aka Prioritizing!"
    menu Planning_2:
        set menuset
        t "Great job learning more about time management! Did you learn anything new about planning?"
        "Yup, I understand the importance of planning better.":
            t "That's great! Be sure to implement it into your routine, so can see the benefits first-hand!"

        "Yup, I understand what makes an effective goal.":
            t "Good to hear that! Specific and realistic goals make all the difference!"

        "No, it was all review":
            t "That's fine! It's always good to reinforce your knowledge."
    show screen leave
    jump TM_Buttons

label Prioritizing_and_Performing:
    hide screen leave
    show 3P
    t "The time management process can be divided into three steps, known as the 3Ps: Planning, performing, and prioritizing!"
    hide 3P
    show 2P1
    t "Let's focus on the last two: Prioritizing and performing."
    hide 2P1
    t "When prioritizing your tasks, you should consider their importance and urgency."
    show 2P2
    t "IMPORTANT and URGENT tasks require a response in a short amount of time. For example, a program application that's due tomorrow."
    hide 2P2
    show 2P3
    t "IMPORTANT and NONURGENT tasks must be done eventually, but not necessarily today. For example, studying for a test coming up next week."
    hide 2P3
    show 2P4
    t "URGENT but NOT IMPORTANT require immediate attention, but are not a high priority. These tasks may pile up if you say “yes” to too many people, or find your work being constantly interrupted." 
    t "For example, offering to design a poster for an informal event coming up."
    hide 2P4
    show 2P5
    t "The final category is  NONURGENT and NOT IMPORTANT. These tasks may be somewhat important, but can be done whenever. For example, organizing files on your computer."
    hide 2P5
    menu Prioritizing_and_Performing_1:
        set menuset
        t "How would you categorize the following task?: Reading a 100 page book to prepare for a discussion in English class next week."
        "Important and urgent":
            t "Hmm, I would consider it important and nonurgent. The book is fairly short so there's no need to start a week before."

        "Important and nonurgent":
            t "I agree. It's important to read the book so you're prepared, but it's a fairly short book so you don't have to start right now."

        "Urgent but not important":
            t "Hmm, I would consider it important and nonurgent. The book is fairly short so there's no need to start a week before..."
            t "But it's still an important task, because you won't be able to participate if you didn't read."

        "Nonurgent and not important":
            t "Hmm, I would consider it important and nonurgent. The book is fairly short so there's no need to start a week before..."
            t "But it's still an important task, because you won't be able to participate if you didn't read."

    t "Now that you're familiar with prioritizing, let's move on to performing."
    show 2P6
    t "Performing is the last of the 3 Ps, and it requires 100 percent of your concentration. When you're working, move to a quiet space, turn off your phone, and avoid multitasking."
    t "By eliminating distractions, you are improving the quality and quantity of your work."
    t "You should also try to follow your energy patterns and do important tasks when you feel most alert or energetic (eg. first thing in the morning, after lunch, etc.)"
    hide 2P6
    menu Prioritizing_and_Performing_2:
        set menuset
        t "When do you have the most energy to do work?"
        "Morning":
            t "Early bird gets the worm! Do you complete important tasks in the morning?"
            t "If not, try to reorder your routine so you can do more work in the morning."

        "Afternoon":
            t "Good to know! Do you complete important tasks in the afternoon?"
            t "If not, try to reorder your routine so you can do more work in the afternoon."

        "Evening":
            t "Good to know! Do you complete important tasks in the evening?"
            t "If not, try to reorder your routine so you can do more work in the evening."

        "Not sure":
            t "That's okay! Observe your energy patterns for the next few weeks and see if you can come to a conclusion."

    menu Prioritizing_and_Performing_3:
        set menuset
        t "Great job learning more about time management! Did you learn anything new about prioritizing or performing?"
        "Yes, I learned more about prioritizing.":
            t "Good to hear! Prioritizing will help make the most of your plans."

        "Yes, I learned more about performing.":
            t "Good to hear! Performing is an important but often overlooked part of time management."

        "No, I did not.":
            t "That's fine! It's always good to reinforce your knowledge."
    show screen leave
    jump TM_Buttons

label SMART:
    hide screen leave
    t "Starting a big project or studying for a final exam can seem like an overwhelming task, but breaking it down into smaller goals can make it more manageable."
    t "Let's explore what makes a goal SMART."
    show S1
    t "SMART is an acronym used to write effective goals. The S stands for specific. The objective of the goal should be narrow, or else it will be too difficult to accomplish."
    hide S1 
    show S2
    t "The M stands for measurable. It should be possible for you to judge whether the task is completed or not, or else you may spend too little or too much time working on it."
    t "For example, 'finish 20 practice problems' is measurable, but 'study for bio test' is not."
    hide S2 
    show S3
    t "The A stands for achievable. You should have adequate time and resources to complete your task. Pushing yourself too hard increases your risk of stress and burnout."
    hide S3 
    show S4
    t "The R stands for relevant. The purpose of the task should align with your priorities, and be meaningful."
    hide S4
    show S5
    t "Finally, T stands for time-bound. A good goal should have an exact time frame, so you know when it should be completed."
    hide S5 
    menu SMART_1:
        set menuset
        t "Can this goal be improved?: Practice piano scales after school."
        "It could be more MEASURABLE.":
            t "That's right! This goal doesn't define how many scales you need to practice, or how long you need to practice for."

        "It could be more ACHIEVABLE":
            t "Not quite, try again"
            jump SMART_1

        "No, it's fine as it is.":
            t "Not quite, try again"
            jump SMART_1
    menu SMART_2:
        set menuset
        t "Can this goal be improved?: Read 50 pages of novel for  English  class"
        "It could be more TIMEBOUND.":
            t "That's right! This goal doesn't say when you need to read the 50 pages."

        "It could be more RELEVANT":
            t "Not quite, try again"
            jump SMART_2

        "No, it's fine as it is.":
            t "Not quite, try again"
            jump SMART_2
    t "SMART goals make tasks specific and manageable. This helps you keep track of your progress and hold yourself accountable."
    menu SMART_3:
        set menuset
        t "Great job learning more about time management! Did you learn anything new about SMART goals?"
        "Yes, I learned what the acronym means":
            t "Good to hear! Next time you’re writing a to-do list, be sure to apply what you learned!"
        "No, I already knew what SMART goals were.":
            t "That's fine! It's always good to reinforce your knowledge."
    show screen leave
    jump TM_Buttons

label TM_Practice:
    scene cafe
    with fade
    show bakerellie
    "You and Ellie are hosting a bake sale next week to raise money for charity, but there's a lot left to do!"
    hide bakerellie
    show bakerellie5
    e "This charity is super important to me, so the sale needs to be a success!"
    menu TM_Practice1:
        set menuset
        y "I agree. Let's start by"
        "Planning what to do.":
            hide bakerellie5
            show bakerellie4
            e "Good idea!"
        "Prioritizing what to do.":
            hide bakerellie5
            show bakerellie1
            e "Prioritize what? We don't even know what to do yet!"
            y "Oh right, let's start by planning that first."
        "Baking":
            hide bakerellie5
            show bakerellie1
            e "Hold your horses! We don't even know what to bake yet. And wouldn't the food be spoiled if we started so early?"
            y "Oh right, let's start by planning that first."
    hide bakerellie5
    hide bakerellie1
    show bakerellie
    e "The first thing we need is permission to host the bake sale. Next, we'll need to advertise it."
    y "Right. Then, one night before the sale, I'll visit your house and we'll bake the items."
    y "If each item costs about $2, we should sell at least 200 units."
    menu TM_Practice2:
        set menuset
        y "We can..."
        "Bake 200 on our own.":
            hide bakerellie
            show bakerellie5
            e "Hmm... what if we run out of time? We need to make sure our goal is achievable."
            jump TM_Practice2
        "Bake 100, and buy 100.":
            hide bakerellie
            hide bakerellie5
            show bakerellie4
            e "That sounds achievable! We'll have lots of things to sell, and it won't be too much work for us."
    e "Okay, so the four main steps in our plan are: get permission, advertise, bake, and buy."
    hide screen leave
    show screen TM_drag
    show Matrix
    "You and Ellie continue to elaborate on your plan until you have a long list of things to do. Drag each task to move it to its appropriate category."
    hide screen TM_drag
    hide Matrix
    show screen leave
    hide bakerellie4
    show bakerellie
    e "Phew, now we have our priorities straight. You can email the prinicipal for permission, and I'll get started on making the posters."
    scene kitchen
    with fade
    hide bakerellie
    show bakerellie1
    "You arrive at Ellie's house next week to start baking, but you're progressing much slower than you anticipated."
    hide bakerellie1
    show bakerellie3
    e "Ugh, I'm getting so many messages asking how much the bake sale items will cost."
    e "I can't believe I forgot to write the prices on the posters!"
    e "And to top it off, we're so behind on baking! It's 7:30, and all we have is 24 muffins."
    hide bakerellie3
    show bakerellie6
    "While Ellie continues responding to the messages on her phone, a peculiar scent fills the air."
    "You look at the oven."
    y "Smoke! Ellie the cookies are burning!"
    hide bakerellie6
    show bakerellie3
    e "What! No! Why is everything going wrong!"
    "She removes the 12 burnt cookies from the oven."
    menu TM_Practice3:
        set menuset
        y "Ellie, I think..."
        "I can take care of it from here":
            e "What do you mean? We're already so behind, I can't make you do it alone."
            y "What I meant was..."
            jump TM_Practice3
        "You're distracted by the messages":
            y "If we want to do a good job of baking, then we need to give it 100 percent of our attention."
            hide bakerellie3
            show bakerellie1
            e "Sigh, okay. I'll respond to the messages later. I suppose we can't have a bake sale if we don't bake anything!"
    "You and Ellie work hard at baking for the next two hours, until you've made nearly 100 baked goods."
    hide bakerellie1
    scene cafe
    with fade
    "The bake sale next morning is a huge success!"
    show bakerellie4
    t "Thanks for your help in planning this event! I couldn't have done it alone."
    "Congrats on completing the final activity! Future app updates will allow you to keep different Ellie costumes (eg. Baker Ellie) as a reward."
    hide bakerellie4
    hide screen leave
    jump lesson_and_tools  
    
