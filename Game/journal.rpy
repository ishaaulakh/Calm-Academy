init python:    
    import os
    renpy.store.prompt_backend = [
        "Reflect on your current time management strategies. Are you breaking down your tasks into smaller goals, or do you find yourself trying to achieve everything all at once?",
        "How can you incorporate more self-care and leisure activities into your routine?",
        "What unproductive habits do you have that inhibit time management? How would you go about unlearning these habits?",
        "What qualities are you grateful to have?",
        "What can you commit to today that your future self will thank you for?",
        "When are you your most authentic self?",
        "What are three things you're grateful for?",
        "What is something in your past you once viewed as a failure, but now see as a gift?",
        "Who in your life are you grateful for (past or present)?",
        "How was your day today?",
        "Who or what made you laugh today?",
        "What's bothering you today?",
        "Rate your current stress level from 1 to 10. Why did you choose that score?",
        "What are three ways you can show yourself more compassion?",
        "Recall a moment when you overcame great stress. How did you do it and how did it make you feel?",
        "How does anxiety show up in your body? What does it feel like?",
        "How is your workload at school?",
        "What are your go-to ways of practicing self-care? Do they reduce your stress?",
        "What is your inner critic telling you right now? How would you reply to what your inner critic is saying?",
        "Who or what you can count on to help manage your stress or anxiety?",
        "What is one self-care practice you want to try but haven't tried yet? Make a plan to try it soon.",
        "Write an affirmation that can help you overcome anxious thoughts.",
        "Does physical activity lower your stress? How does it make you feel?",
        "What self-critical thoughts have you had recently? How can you reframe these thoughts to be more self-compassionate?",
        "Perfectionists often feel like they're not working hard enough because their goals are unreachable. Do you carry this attitude? Is it helping or harming you?",
        "What is one activity that brings you peace?",
        "Who or what makes you smile?",
        "What boundaries do you need to set at school, home, or work? How will these boundaries benefit you?",
        "Does procrastination often hinder you from doing school work? How can you dismantle this habit?",
    ]


    class Entry:
        def __init__(self):
            #TODO: CHAANGE DDAA NAMEE
            self.name = ""
            self.file_name = ""
            self.file_path = ""
            self.selected_prompt = ""
        def reset_data(self):
            self.name = ""
            self.selected_prompt = ""
        def ready_to_submit(self):
            if len(self.name) == 0:
                return False
            else:
                return True
        def set_name(self, newstring):
            self.name = newstring
        def set_file_name(self, newstring):
            self.file_name = newstring
        def set_file_path(self, newstring):
            self.file_path = newstring
        def set_selected_prompt(self, prompt):
            self.selected_prompt = prompt
        def get_name(self):
            return self.name
        def get_file_name(self):
            return self.file_name
        def get_file_path(self):
            return self.file_path
        def get_selected_prompt(self):
            return self.selected_prompt

    renpy.store.entry_to_add = Entry() 
    renpy.store.random_prompt = ""

    def renpy_store_submit_new_journal_entry():
        file_path = renpy.store.entry_to_add.get_file_path()
        file = open(file_path+".txt","w") 
        if file is not None:
            file.write(renpy.store.entry_to_add.get_selected_prompt())
            file.write("\n")
            file.write(renpy.store.entry_to_add.get_name())
            file.close()
        else:
            print("bad")
        # TODO: write notification

screen delete_Entry():
    modal True
    frame:
        xalign 0.5 ypos 0.3
        xsize 400
        ysize 250
        vbox:
            text "Leaving now will delete your response."
            imagebutton:
                xalign 0.5
                idle "Del.png"
                hover "HDel.png"
                action Rollback()
            imagebutton:
                xalign 0.5
                idle "Cancel.png"
                hover "HCancel.png"
                action Hide("delete_Entry")

screen Entry_saved():
    modal True
    frame:
        xalign 0.5 ypos 0.4
        xsize 300
        vbox:
            text "Entry saved!"
            imagebutton:
                idle "Okay.png"
                hover "HOkay.png"
                action Rollback()
        
screen prompt():
    modal True

    python:
        random_prompt = renpy.random.choice(renpy.store.prompt_backend)
        new_file_name = renpy.store.entry_to_add.get_file_name()
        file_path = os.path.abspath(os.path.join(config.basedir, "Game","Journal", new_file_name))
        renpy.store.entry_to_add.set_file_path(file_path)
        renpy.store.entry_to_add.set_selected_prompt(random_prompt)
    frame:
        xalign 0.5 ypos 0.1
        xsize 1200
        ysize 150
        vbox:
            text "Prompt: [random_prompt]"
            imagebutton:
                idle "Prompt.png"
                hover "Prompt.png"
                action SetVariable("random_prompt", renpy.random.choice(renpy.store.prompt_backend))

    frame: 
        xalign 0.5 ypos 0.32
        xsize 1200
        ysize 420
        viewport:
            draggable True
            mousewheel True 
            vbox:
                xsize 1200 
                hbox:
                    ysize 250
                    box_wrap True
                    text "My Response: "
                    input id "journal_input" size 28 color "#5a715e" default "" changed renpy.store.entry_to_add.set_name
                imagebutton:
                    idle "Submit.png"
                    hover "HSubmit.png"
                    action [
                        lambda: renpy_store_submit_new_journal_entry(),
                        Show("Entry_saved")
                ]
                imagebutton:
                    idle "back.png"
                    hover "back_hover.png"
                    action[Show("delete_Entry")] 
    
screen name_new_entry():
    frame:
        xalign 0.5 ypos 0.35
        xsize 1200
        vbox:
            xsize 1200
            text "Name your entry: "
            input id "file_name" size 40 color "#000" default "" changed renpy.store.entry_to_add.set_file_name length 50
            hbox:
                xalign 0.5
                imagebutton:
                    xalign 0.5
                    idle "back.png"
                    hover "back_hover.png"
                    action Rollback()
                imagebutton:
                    xalign 0.5
                    idle "Read.png"
                    hover "Read_hover.png"
                    action [Hide("name_new_entry"), Show("Library")]
                imagebutton:
                    idle "Cont.png"
                    hover "Cont_hover.png"
                    action [Hide("name_new_entry"), Show("prompt")]


screen open_file(entry):
    frame:
        xalign 0.5 ypos 0.1
        xsize 1000
        ysize 600
        vbox:
            viewport:
                draggable True
                mousewheel True
                python:
                    entry_name = entry.get_name()
                    entry_prompt = entry.get_selected_prompt()
                vbox:
                    text "[entry_prompt]"
                    text "[entry_name]"
                

screen Library():
    python: 
        folder = os.path.abspath(os.path.join(config.basedir, "Game","Journal"))
        current_entries = []

        files = os.listdir(folder)
        for file_name in files:
            file_path = os.path.join(folder, file_name)
            if os.path.isfile(file_path) and file_name.endswith('.txt'):
                entry = Entry()
                entry.set_file_name(file_name)
                entry.set_file_path(file_path)
                # read the file no
                file = open(file_path,"r") 
                if file is not None:
                    content = file.read() # Split the content into prompt and name based on the first newline character
                    if '\n' in content:
                        prompt, name = content.split('\n', 1)
                        entry.set_name(name.strip())  # Remove leading and trailing whitespaces from the name
                        entry.set_selected_prompt(prompt)
                        current_entries.append(entry)
                    file.close()
                else:
                    print("bad file")
    frame:
        xalign 0.5 yalign 0.04
        xsize 1000
        ymaximum 100
        imagebutton:
            idle "lback.png"
            hover "lback_hover.png"
            action [Hide("Library"), Show("name_new_entry"), Hide("open_file")]
    frame:
        xsize 1000
        ysize 500
        xalign 0.5
        yalign 0.4
        viewport:
            draggable True
            mousewheel True 
            scrollbars "vertical"
            vbox:
                xalign 0.5
                spacing 20
                for entry in current_entries:
                    python:
                        entry_name = entry.get_name()[:70]
                        entry_title = entry.get_file_name()[:-4] 
                    frame:
                        xsize 800
                        xpos 0.1
                        ypos 0.1  
                        vbox:
                            text "[entry_title]   "
                            text "Preview: [entry_name]" color "#b3bbb3" size 24
                            imagebutton:
                                idle "Open.png"
                                hover "HOpen.png"
                                action[Show("open_file", entry=entry)]
        

