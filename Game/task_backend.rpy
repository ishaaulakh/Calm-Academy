init python:
    import os
    import datetime

    #####################################
    ##### classes for silly backend #####
    class Task:
        def __init__(self):
            self.name = ""
            self.day = ""
            self.id = -1
            self.priority = -1
            self.duration = -1.0
            self.is_finished = False
        
        def reset_data(self):
            self.name = ""
            self.day = ""
            self.priority = -1
            self.duration = -1
            self.is_finished = False
    
        def set_name(self, newstring):
            self.name = newstring
        def set_day(self, day):
            self.day = day
        def set_id(self, id):
            self.id = id
        def set_priority(self, priority):
            self.priority = priority
        def set_duration(self, duration):
            self.duration = duration
        def set_is_finished(self, is_finished):
            self.is_finished = is_finished

        def get_name(self):
            return self.name
        def get_day(self):
            return self.day
        def get_priority(self):
            return self.priority
        def get_duration(self):
            return self.duration
        def is_task_finished(self):
            return self.is_finished
        def get_id(self):
            return self.id
    
    class TaskBackend:
        def __init__(self):
            self.task_list = []
            self.csv_file = os.path.abspath(os.path.join(config.basedir, "Game","TimeManagement","backend.csv"))

        def add_task(self, task):
            task.id = self.generate_task_id()
            self.task_list.append(task)
            with open(self.csv_file, 'a') as file:
                file.write(
                        task.name + "," +
                        task.day + "," +
                        str(task.id) + "," +
                        str(task.priority) + "," +
                        str(task.duration) + "," +
                        str(task.is_finished) + "\n"
                    )

        def remove_task(self, task_id):
            # Remove a task based on its task_id
            self.task_list = [task for task in self.task_list if task.id != task_id]
            self.save_tasks_to_csv()
        
        def clear_all_tasks(self):
            self.task_list = []
            with open(self.csv_file, 'w') as file:
                file.write("Name,Day,Task ID,Priority,Duration,Is Finished\n")

        def change_task_name(self, task_id, new_name):
            print("change_task_name")
            if len(new_name) == 0:
                return False
            for task in self.task_list:
                if task.get_id() == task_id:
                    task.set_name(new_name)
                    self.save_tasks_to_csv()
                    return True 
            return False
    
        def change_task_day(self, task_id, new_day):
            for task in self.task_list:
                if task.get_id() == task_id:
                    task.set_day(new_day)
                    self.save_tasks_to_csv()
                    return True 
            return False

        def change_task_priority(self, task_id, new_priority):
            for task in self.task_list:
                if task.get_id() == task_id:
                    task.set_priority(int(new_priority))
                    self.save_tasks_to_csv()
                    return True 
            return False

        def change_task_duration(self, task_id, new_duration):
            for task in self.task_list:
                if task.get_id() == task_id:
                    try:
                        task.set_duration(float(new_duration))
                        self.save_tasks_to_csv()
                        return True 
                    except ValueError:
                        print("Invalid duration value.")
                        return False
            return False

        def save_tasks_to_csv(self):
            # overrides the backend with current list of tasks
            with open(self.csv_file, 'w') as file:
                file.write("Name,Day,Task ID,Priority,Duration,Is Finished\n")
                for task in self.task_list:
                    file.write(
                        task.name + "," +
                        task.day + "," +
                        str(task.id) + "," +
                        str(task.priority) + "," +
                        str(task.duration) + "," +
                        str(task.is_finished) + "\n"
                    )

        def load_tasks_from_csv(self):
            with open(self.csv_file, 'r') as file:
                lines = file.readlines()
                # Skip the header row
                tasks = [self.parse_csv_row(line.strip()) for line in lines[1:]]
            self.task_list = tasks

        def parse_csv_row(self, row):
            name, day, task_id, priority, duration, is_finished = row.split(',')
            task = Task()
            task.name = name
            task.day = day
            task.id = int(task_id)
            task.priority = int(priority)
            task.duration = float(duration)
            task.is_finished = bool(is_finished)
            return task

        def generate_task_id(self):
            if not self.task_list:
                # task list is empty, this is first task
                return 1
            max_task_id = max(task.id for task in self.task_list)
            return max_task_id + 1

        def get_all_tasks(self):
            return self.task_list

        def get_all_tasks_on_day(self, day):
            tasks = [task for task in self.task_list if task.day == day]
            return sorted(tasks, key=lambda task: task.priority)


    #######################################
    ##### variables in global storage #####
    renpy.store.task_to_add = Task()
    renpy.store.task_to_edit = Task()
    renpy.store.task_backend = TaskBackend()
    renpy.store.task_backend.load_tasks_from_csv()

    today = datetime.date.today()
    renpy.store.day_of_week = today.strftime("%A")
    renpy.store.month_day = today.strftime("%B %d")
    renpy.store.formatted_date = today.strftime('%A, %B %d')

    def renpy_store_task_reset():
        renpy.store.task_to_add.reset_data()
    
    def renpy_store_task_submit():
        renpy.store.task_backend.add_task(renpy.store.task_to_add)
        renpy_store_task_reset()
    
    def renpy_store_get_tasks_on_day(day):
        renpy.store.task_backend.load_tasks_from_csv()
        return renpy.store.task_backend.get_all_tasks_on_day(day)

    def renpy_store_clear_task_backend():
        renpy.store.task_backend.clear_all_tasks()
        renpy.store.task_to_add.reset_data()
        renpy.store.task_to_edit.reset_data()

    # USED IN EDIT TASK SCREENS
    def renpy_store_delete_task_in_backend(task_id):
        print("used remove")
        renpy.store.task_backend.remove_task(task_id)

    def renpy_store_update_task_name_in_backend(task_id, new_name):
        print("new_name: ", new_name)
        renpy.store.task_backend.change_task_name(task_id, new_name)

    def renpy_store_update_task_day_in_backend(task_id, new_day):
        print("new_day: ", new_day)
        renpy.store.task_backend.change_task_day(task_id, new_day)

    def renpy_store_update_task_priority_in_backend(task_id, new_priority):
        print("new_priority: ", new_priority)
        renpy.store.task_backend.change_task_priority(task_id, new_priority)

    def renpy_store_update_task_duration_in_backend(task_id, new_duration):
        print("new duration: ", new_duration)
        renpy.store.task_backend.change_task_duration(task_id, new_duration)