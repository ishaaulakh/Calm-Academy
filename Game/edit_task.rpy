screen editTaskName(task_id, task_name):
    modal True
    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 500
        vbox:
            xsize 1200
            text "Editing [task_name]"
            hbox:
                text "Enter New Task Name: "
                input id "task_name_edit" hover_color "#3399ff" size 28 color "#000" default "" changed renpy.store.task_to_edit.set_name length 50
            imagebutton:
                idle "Save.png"
                hover "HSave.png"
                action [
                    lambda: renpy_store_update_task_name_in_backend(renpy.store.task_to_edit.get_id(), renpy.store.task_to_edit.get_name()), 
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("editTaskName"),
                    Show("planner")
                ]
            imagebutton:
                idle "back.png"
                hover "back_hover.png"
                action [ 
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("editTaskName"),
                    Show("editTask", task_id=task_id, task_name=task_name)
            ]

screen editTaskPriority(task_id, task_name):
    modal True
    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 500
        vbox:
            xsize 1200
            text "Editing [task_name]" 
            style_prefix "radio"
            label _("Select [task_name]'s Priority Level") 

            textbutton _("Urgent and Important") action [[lambda: renpy.store.task_to_edit.set_priority(1)], Show("lil_guy1"), Hide("lil_guy2"), Hide("lil_guy3"), Hide("lil_guy4")]
            textbutton _("Urgent and Not Important") action [lambda: renpy.store.task_to_edit.set_priority(2), Show("lil_guy2"), Hide("lil_guy1"), Hide("lil_guy3"), Hide("lil_guy4")] 
            textbutton _("Not Urgent and Important") action [lambda: renpy.store.task_to_edit.set_priority(3), Show("lil_guy3"), Hide("lil_guy1"), Hide("lil_guy2"), Hide("lil_guy4")]
            textbutton _("Not Urgent and Not Important") action [lambda: renpy.store.task_to_edit.set_priority(4), Show("lil_guy4"), Hide("lil_guy1"), Hide("lil_guy3"), Hide("lil_guy2")]

            imagebutton:
                idle "Save.png"
                hover "HSave.png"
                action [
                    lambda: renpy_store_update_task_priority_in_backend(renpy.store.task_to_edit.get_id(), renpy.store.task_to_edit.get_priority()),
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("editTaskPriority"),
                    Show("planner")
                ]
            imagebutton:
                idle "back.png"
                hover "back_hover.png"
                action [
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("editTaskPriority"),
                    Show("editTask", task_id=task_id, task_name=task_name)
                ]

screen editTaskDuration(task_id, task_name):
    modal True
    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 500
        vbox:
            text "Editing [task_name]"
            hbox:
                text "Enter New Task Duration: "
                input id "task_duration_edit" hover_color "#3399ff" size 28 color "#000" default "" changed renpy.store.task_to_edit.set_duration length 5
            imagebutton:
                idle "Save.png"
                hover "HSave.png"
                action [
                    lambda: renpy_store_update_task_duration_in_backend(renpy.store.task_to_edit.get_id(), renpy.store.task_to_edit.get_duration()),
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("editTaskDuration"),
                    Show("planner")
                ]
            imagebutton:
                idle "back.png"
                hover "back_hover.png"
                action [
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("editTaskDuration"),
                    Show("editTask", task_id=task_id, task_name=task_name)
                ]

screen deleteTask(task_id, task_name):
    modal True
    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 500
        vbox:
            text "Are you sure you want to delete this task?"
            imagebutton:
                    idle "Delete.png"
                    hover "HDelete.png"
                    action [
                    lambda: renpy_store_delete_task_in_backend(renpy.store.task_to_edit.get_id()),
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("deleteTask"),
                    Show("planner")
                ]       
            imagebutton:
                idle "back.png"
                hover "back_hover.png"
                action [
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("deleteTask"),
                    Show("editTask",task_id=task_id, task_name=task_name)
                ]


screen clearTask():
    modal True
    frame:
        xalign 0.5 ypos 0.03
        xsize 1200
        ysize 200
        vbox:
            text "Are you sure you want to clear all tasks?"
            textbutton _("Clear All") action [
                lambda: renpy_store_clear_task_backend(),
                renpy.restart_interaction,
                Hide("clearTask"),
                Show("planner")
            ]       
            imagebutton:
                idle "back.png"
                hover "back_hover.png"
                action [
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("clearTask"),
                    Show("planner")
                ]

screen editTask(task_id, task_name):
    modal True
    python:
        renpy.store.task_to_edit.set_id(task_id)

    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 500
        vbox:
            text "Edit Properties of [task_name]"
            hbox:
                imagebutton:
                        idle "EName.png"
                        hover "HEName.png"
                        action [Hide("editTask"), Show("editTaskName", task_id=task_id, task_name=task_name)]
                imagebutton:
                        idle "EPrio.png"
                        hover "HEPrio.png"
                        action [Hide("editTask"), Show("editTaskPriority", task_id=task_id, task_name=task_name)]
                imagebutton:
                    idle "EDura.png"
                    hover "HEDura.png"
                    action [Hide("editTask"), Show("editTaskDuration", task_id=task_id, task_name=task_name)]
                imagebutton:
                    idle "Delete.png"
                    hover "HDelete.png"
                    action [Hide("editTask"), Show("deleteTask", task_id=task_id, task_name=task_name)]
            imagebutton:
                idle "cancel.png"
                hover "hcancel.png"
                action [
                    lambda: renpy.store.task_to_edit.reset_data(),
                    Hide("editTask"),
                    Show("planner")
                ]
