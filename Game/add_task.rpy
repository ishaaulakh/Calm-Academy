screen addTaskName(parameter):
    modal True

    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 200
        vbox:
            text "[parameter]"
            hbox:
                text "Enter Task Name: "
                # input default "type here" id "task_name_input"
                button:
                    id "task_name_input"
                    xysize (250, 25)
                    action NullAction()
                    add Input(hover_color="#3399ff",size=28, color="#000", default="", changed=renpy.store.task_to_add.set_name, length=50)

            textbutton _("Next") action [
                renpy.store.task_to_add.set_day(parameter),
                Hide("addTaskName"),
                Show("addTaskPriority", parameter=parameter)
            ]
            textbutton _("Back") action [Hide("addTaskName"), Show("planner"), Function(renpy_store_task_reset)]
    
screen addTaskPriority(parameter):
    modal True
    python:
        stored_task_name = renpy.store.task_to_add.get_name()

    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 500
        vbox:
            style_prefix "radio"
            label _("Select [stored_task_name]'s Priority Level")
            textbutton _("Urgent and Important") action [lambda: renpy.store.task_to_add.set_priority(1)]
            textbutton _("Urgent and Not Important") action [lambda: renpy.store.task_to_add.set_priority(2)]
            textbutton _("Not Urgent and Important") action [lambda: renpy.store.task_to_add.set_priority(3)]
            textbutton _("Not Urgent and Not Important") action [lambda: renpy.store.task_to_add.set_priority(4)]

            textbutton _("Next") action [Hide("addTaskPriority"), Show("addTaskDuration", parameter=parameter)]
            textbutton _("Cancel") action [Hide("addTaskPriority"), Show("planner"), Function(renpy_store_task_reset)]
            textbutton _("Back") action [Hide("addTaskPriority"), Show("addTaskName", parameter=parameter)]

screen addTaskDuration(parameter):
    zorder 999
    modal True
    python:
        stored_task_name = renpy.store.task_to_add.get_name()
        stored_task_prior = renpy.store.task_to_add.get_priority()

    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 200
        vbox:
            hbox:
                label _("Okay! Now enter how many HOURS you expect to work on [stored_task_name]: ")
                button:
                    id "task_duration_input"
                    xysize (250, 25)
                    style input_box
                    action NullAction()
                    add Input(hover_color="#3399ff",size=28, color="#000", default="", changed=renpy.store.task_to_add.set_duration, length=5)

            textbutton _("Save Task") action [
                Function(renpy_store_task_submit),
                Hide("addTaskDuration"),
                Show("planner")
            ]
            textbutton _("Cancel") action [Hide("addTaskPriority"), Show("planner"), Function(renpy_store_task_reset)]
            textbutton _("Back") action [Hide("addTaskDuration"), Show("addTaskPriority", parameter=parameter)]
