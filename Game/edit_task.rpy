screen editTaskName(task_id, task_name):
    modal True
    frame:
        xalign 0.5 ypos 50
        xsize 1200
        ysize 500
        vbox:
            text "Editing [task_name]"
            hbox:
                text "Enter New Task Name: "
                button:
                    id "task_name_edit"
                    xysize (250, 25)
                    action NullAction()
                    add Input(hover_color="#3399ff",size=28, color="#000", default="", changed=renpy.store.task_to_edit.set_name, length=50)

            textbutton _("Save") action [
                lambda: renpy_store_update_task_name_in_backend(renpy.store.task_to_edit.get_id(), renpy.store.task_to_edit.get_name()), 
                lambda: renpy.store.task_to_edit.reset_data(),
                Hide("editTaskName"),
                Show("planner")
            ]
            textbutton _("Back") action [ 
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
            text "Editing [task_name]"
            style_prefix "radio"
            label _("Select [task_name]'s Priority Level")
            textbutton _("Urgent and Important") action [lambda: renpy.store.task_to_edit.set_priority(1)]
            textbutton _("Urgent and Not Important") action [lambda: renpy.store.task_to_edit.set_priority(2)]
            textbutton _("Not Urgent and Important") action [lambda: renpy.store.task_to_edit.set_priority(3)]
            textbutton _("Not Urgent and Not Important") action [lambda: renpy.store.task_to_edit.set_priority(4)]

            textbutton _("Save") action [
                lambda: renpy_store_update_task_priority_in_backend(renpy.store.task_to_edit.get_id(), renpy.store.task_to_edit.get_priority()),
                lambda: renpy.store.task_to_edit.reset_data(),
                Hide("editTaskPriority"),
                Show("planner")
            ]
            textbutton _("Back") action [
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
                button:
                    id "task_duration_edit"
                    xysize (250, 25)
                    action NullAction()
                    add Input(hover_color="#3399ff",size=28, color="#000", default="", changed=renpy.store.task_to_edit.set_duration, length=5)

            textbutton _("Save") action [
                lambda: renpy_store_update_task_duration_in_backend(renpy.store.task_to_edit.get_id(), renpy.store.task_to_edit.get_duration()),
                lambda: renpy.store.task_to_edit.reset_data(),
                Hide("editTaskDuration"),
                Show("planner")
            ]

            textbutton _("Back") action [
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
            textbutton _("Delete Task") action [
                lambda: renpy_store_delete_task_in_backend(renpy.store.task_to_edit.get_id()),
                lambda: renpy.store.task_to_edit.reset_data(),
                Hide("deleteTask"),
                Show("planner")
            ]       
            textbutton _("Back") action [
                lambda: renpy.store.task_to_edit.reset_data(),
                Hide("deleteTask"),
                Show("editTask",task_id=task_id, task_name=task_name)
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
            textbutton _("Edit Name") action [Hide("editTask"), Show("editTaskName", task_id=task_id, task_name=task_name)]
            textbutton _("Edit Priority") action [Hide("editTask"), Show("editTaskPriority", task_id=task_id, task_name=task_name)]
            textbutton _("Edit Duration") action [Hide("editTask"), Show("editTaskDuration", task_id=task_id, task_name=task_name)]
            textbutton _("Delete Task") action [Hide("editTask"), Show("deleteTask", task_id=task_id, task_name=task_name)]
            textbutton _("Cancel") action [
                lambda: renpy.store.task_to_edit.reset_data(),
                Hide("editTask"),
                Show("planner")
            ]
