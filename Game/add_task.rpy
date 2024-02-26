screen task_submit_error():
    zorder 1000
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xsize 500
        ysize 200
        vbox:
            text "Error in Task Input. Ensure you have set a name, priority level, and input a numerical duration."
            imagebutton:
                idle "Okay.png"
                hover "HOkay.png"
                action [Hide("task_submit_error"), Show("planner"), Function(renpy_store_task_reset)]
                xalign 0.5

screen addTaskName(parameter):
    modal True
    frame:
        xalign 0.5 ypos 50
        xsize 1000
        ysize 500
        vbox:
            text "[parameter]"
            hbox:
                text "Enter Task Name: "
                input id "task_name_input" hover_color "#3399ff" size 28 color "#000" default "" changed renpy.store.task_to_add.set_name length 50
            imagebutton:
                    idle "Cont.png"
                    hover "Cont_hover.png"
                    action [
                        renpy.store.task_to_add.set_day(parameter),
                        Hide("addTaskName"),
                        Show("addTaskPriority", parameter=parameter)
                    ]
            imagebutton:
                idle "back.png"
                hover "back_hover.png"
                action [Hide("addTaskName"), Show("planner"), Function(renpy_store_task_reset)]
    
screen addTaskPriority(parameter):
    modal True
    
    python:
        stored_task_name = renpy.store.task_to_add.get_name()
    frame:
        xalign 0.5 ypos 50
        xsize 1000
        ysize 500
        hbox:
            vbox:
                xsize 500
                style_prefix "radio"
                label _("Select [stored_task_name]'s Priority Level")
                textbutton _("Urgent and Important") action [[lambda: renpy.store.task_to_add.set_priority(1)], Show("lil_guy1"), Hide("lil_guy2"), Hide("lil_guy3"), Hide("lil_guy4")]
                textbutton _("Not Urgent and Important") action [lambda: renpy.store.task_to_add.set_priority(2), Show("lil_guy3"), Hide("lil_guy1"), Hide("lil_guy2"), Hide("lil_guy4")]
                textbutton _("Urgent and Not Important") action [lambda: renpy.store.task_to_add.set_priority(3), Show("lil_guy2"), Hide("lil_guy1"), Hide("lil_guy3"), Hide("lil_guy4")] 
                textbutton _("Not Urgent and Not Important") action [lambda: renpy.store.task_to_add.set_priority(4), Show("lil_guy4"), Hide("lil_guy1"), Hide("lil_guy3"), Hide("lil_guy2")]
                imagebutton:
                        idle "Cont.png"
                        hover "Cont_hover.png"
                        action [Hide("addTaskPriority"), Show("addTaskDuration", parameter=parameter)]
                imagebutton:
                    idle "cancel.png"
                    hover "hcancel.png"
                    action [Hide("addTaskPriority"), Show("planner"), Function(renpy_store_task_reset)]
                imagebutton:
                    idle "back.png"
                    hover "back_hover.png"
                    action [Hide("addTaskPriority"), Show("addTaskName", parameter=parameter)]
            imagebutton:
                idle "PCC.png"
                action NullAction()


screen addTaskDuration(parameter):
    zorder 999
    modal True
    python:
        stored_task_name = renpy.store.task_to_add.get_name()
        stored_task_prior = renpy.store.task_to_add.get_priority()

    frame:
        xalign 0.5 ypos 50
        xsize 1000
        vbox:
            hbox:
                label _("How many HOURS do you expect to work on [stored_task_name]: ")
                input id "task_duration_input" size 28 color "#000" default "" changed renpy.store.task_to_add.set_duration length 5
            imagebutton:
                    idle "save.png"
                    hover "hsave.png"
                    action [
                    Function(renpy_store_task_submit),
                    Hide("addTaskDuration"),
                    Show("planner")
                ]
            imagebutton:
                idle "cancel.png"
                hover "hcancel.png"
                action [Hide("addTaskDuration"), Show("planner"), Function(renpy_store_task_reset)]
            imagebutton:
                idle "back.png"
                hover "back_hover.png"
                action [Hide("addTaskDuration"), Show("addTaskPriority", parameter=parameter)]
            


