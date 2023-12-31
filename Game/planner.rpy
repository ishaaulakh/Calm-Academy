screen planner:
    modal True
    python:
        day_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Other"]
        xalign_values = [0.04, 0.34, 0.66, 0.96, 0.04, 0.34, 0.66, 0.96]
        yalign_values = [0.2, 0.2, 0.2, 0.2, 0.96, 0.96, 0.96, 0.96]

        mon_tasks = renpy_store_get_tasks_on_day(day_list[0])
        tue_tasks = renpy_store_get_tasks_on_day(day_list[1])
        wed_tasks = renpy_store_get_tasks_on_day(day_list[2])
        thr_tasks = renpy_store_get_tasks_on_day(day_list[3])
        fri_tasks = renpy_store_get_tasks_on_day(day_list[4])
        sat_tasks = renpy_store_get_tasks_on_day(day_list[5])
        sun_tasks = renpy_store_get_tasks_on_day(day_list[6])
        other_tasks = renpy_store_get_tasks_on_day(day_list[7])

        week_tasks = [mon_tasks, tue_tasks, wed_tasks, thr_tasks, fri_tasks, sat_tasks, sun_tasks,other_tasks]
    
    frame:
        xalign 0.5 yalign 0.04
        xsize 1200
        ymaximum 100
        hbox:
            textbutton _("Back") action [ NullAction() ]
            text "Today's date is [renpy.store.formatted_date]"
            textbutton _("Clear") action [
                lambda: renpy_store_clear_task_backend(),
                renpy.restart_interaction
            ]

    for i in range(8):
        python:
            day_name = day_list[i]
            day_xalign = xalign_values[i]
            day_yalign = yalign_values[i]
        
        frame:
            xalign day_xalign
            yalign day_yalign
            xmaximum 275  
            ymaximum 300

            vbox:
                viewport:
                    draggable True
                    mousewheel True 
                    vbox:
                        text "[day_name]"
                        imagebutton:
                            id "add_"+"[day_name]"
                            idle "planner.png"
                            hover "planner.png"
                            clicked "planner.png"
                            action [Show("addTaskName",parameter=day_name), Hide("planner")]
                        for task in week_tasks[i]:
                            python:
                                task_id = task.get_id()
                                task_name = task.get_name()
                                task_duration = task.get_duration()
                                task_priority = task.get_priority()
                            hbox box_wrap True:
                                if task_priority == 1:
                                    textbutton _("[task_name]: [task_duration] hrs"):
                                        action [Hide("planner"), Show("editTask", task_id=task_id, task_name=task_name)]
                                        style "task_priority_1"
                                        text_style "task_text"
                                elif task_priority == 2:
                                    textbutton _("[task_name]: [task_duration] hrs"):
                                        action [Hide("planner"), Show("editTask", task_id=task_id, task_name=task_name)]
                                        style "task_priority_2"
                                        text_style "task_text"
                                elif task_priority == 3:
                                    textbutton _("[task_name]: [task_duration] hrs"):
                                        action [Hide("planner"), Show("editTask", task_id=task_id, task_name=task_name)]
                                        style "task_priority_3"
                                        text_style "task_text"
                                else:
                                    textbutton _("[task_name]: [task_duration] hrs"):
                                        action [Hide("planner"), Show("editTask", task_id=task_id, task_name=task_name)]
                                        style "task_priority_4"
                                        text_style "task_text"
