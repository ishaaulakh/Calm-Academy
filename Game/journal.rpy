init python:
    import os
    renpy.store.prompt_backend = [
        "Reflect on your current time management strategies. Are you breaking down your tasks into smaller goals, or do you find yourself trying to achieve everything all at once?",
        "How can you incorporate more self care and leisure activities into your routine?",
        "What unproductive habits do you have that inhibit time management? How would you go about unlearning these habits?",
        "What qualities am I grateful to have?",
        "What can I commit to today that my future self will thank me for?",
        "When are you your most authentic self?",
        "What are three things you're grateful for?",
        "What is something in your past you once viewed as a failue, but now see as a gift?",
        "Who in your life are you grateful for (past or present)?"
        
    ]

    class Entry:
        def __init__(self):
            #TODO: CHAANGE DDAA NAMEE
            self.name = ""
            self.file_name = ""
            self.file_path = ""
        def reset_data(self):
            self.name = ""
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
        def get_name(self):
            return self.name
        def get_file_name(self):
            return self.file_name
        def get_file_path(self):
            return self.file_path

    renpy.store.entry_to_add = Entry() 
    renpy.store.random_prompt = ""

    def renpy_store_submit_new_journal_entry():
        file_path = renpy.store.entry_to_add.get_file_path()
        file = open(file_path+".txt","w") 
        if file is not None:
            file.write(renpy.store.entry_to_add.get_name())
            file.close()
        else:
            print("baad")
        # TODO: write notification

screen delete_Entry:
    modal True
    frame:
        xalign 0.5 ypos 0.3
        xsize 300
        ysize 200
        vbox:
            text "Leaving now will delete your response."
            textbutton _("Delete") action Rollback()

screen Entry_saved:
    modal True
    frame:
        xalign 0.5 ypos 0.3
        xsize 300
        ysize 200
        vbox:
            text "Entry saved!"
            textbutton _("Return to Menu") action Rollback()
        
screen prompt:
    modal True

    python:
        renpy.store.random_prompt = renpy.random.choice(renpy.store.prompt_backend)
        new_file_name = renpy.store.entry_to_add.get_file_name()
        file_path = os.path.abspath(os.path.join(config.basedir, "Game","Journal", new_file_name))
        renpy.store.entry_to_add.set_file_path(file_path)
    frame:
        xalign 0.5 ypos 0.1
        xsize 1200
        ysize 150
        vbox:
            text "Prompt: [random_prompt]"
            textbutton _("Generate New Prompt") action SetVariable("random_prompt", renpy.random.choice(renpy.store.prompt_backend))

    frame: 
        xalign 0.5 ypos 0.32
        xsize 1200
        ysize 450
        viewport:
            draggable True
            mousewheel True 
            vbox:
                xsize 1200 
                hbox:
                    box_wrap True
                    text "My Response: "
                    input id "journal_input" size 28 color "#5a715e" default "" changed renpy.store.entry_to_add.set_name
                textbutton _("Submit") action [
                lambda: renpy_store_submit_new_journal_entry(),
                Show("Entry_saved")
                ]
                textbutton _("Back") action[Show("delete_Entry")] 
    
screen name_new_entry:
    frame:
        xalign 0.5 ypos 0.35
        xsize 1200
        ysize 150
        vbox:
            xsize 1200
            text "Name your entry: "
            input id "file_name" size 28 color "#000" default "" changed renpy.store.entry_to_add.set_file_name length 50
            hbox:
                textbutton _("Back") action Rollback()
                textbutton _("Continue") action [Hide("name_new_entry"), Show("prompt")]
                textbutton _("Read a Previous Entry") action [Hide("name_new_entry"), Show("Library")]


screen open_file(entry):
    frame:
        xalign 0.5 ypos 0.1
        xsize 1200
        ysize 450
        viewport:
            draggable True
            mousewheel True
            python:
                entry_name = entry.get_name()
            text "[entry_name]"

screen Library:
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
                # read the file now
                file = open(file_path,"r") 
                if file is not None:
                    content = file.read()
                    entry.set_name(content)
                    current_entries.append(entry)
                    print("starting file dump")
                    print(content)
                    file.close()
                else:
                    print("baad")

    frame:
        viewport:
            draggable True
            mousewheel True 
            vbox:
                xsize 300
                spacing 10
                for entry in current_entries:
                    python:
                        entry_name = entry.get_name()[:70]
                        entry_title = entry.get_file_name()[:-4] 
                    frame:
                        xsize 1265
                        ysize 120
                        align (0.5, 0)
                        vbox:
                            text "Entry Title: [entry_title]   "
                            text "Preview: [entry_name]" color "#b3bbb3" size 24
                            textbutton _("Open") action[Show("open_file", entry=entry)]
