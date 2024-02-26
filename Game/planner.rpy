screen planner():
    modal True
    python:
        day_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Other"]
        xalign_values = [0.04, 0.347, 0.653, 0.96, 0.04, 0.347, 0.653, 0.96]
        yalign_values = [0.18, 0.18, 0.18, 0.18, 0.87, 0.87, 0.87, 0.87]

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
        xalign 0.5 yalign 0.02
        xsize 1200
        ymaximum 100
        hbox:
            imagebutton:
                    xalign 0.5
                    idle "lback.png"
                    hover "lback_hover.png"
                    action Rollback()
            text "   Today's date is [renpy.store.formatted_date]   "
            xalign 0.5
            yalign 0.03
            imagebutton:
                    xalign 0.5
                    idle "Clear.png"
                    hover "HClear.png"
                    action[Show("clearTask")]

    for i in range(8):
        python:
            day_name = day_list[i]
            day_xalign = xalign_values[i]
            day_yalign = yalign_values[i]
        
        frame:
            xalign day_xalign
            yalign day_yalign
            xmaximum 280  
            ymaximum 290

            vbox:
                viewport:
                    draggable True
                    mousewheel True 
                    vbox:
                        text "[day_name]"
                        imagebutton:
                            idle "add.png"
                            hover "add_hover.png"
                            clicked "planner.png"
                            action [Hide("planner"), Show("addTaskName",parameter=day_name)]
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
