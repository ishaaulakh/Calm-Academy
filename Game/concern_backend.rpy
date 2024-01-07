init python:
    class Concern:
        def __init__(self):
            self.name = ""
        def reset_data(self):
            self.name = ""
        def ready_to_submit(self):
            if len(self.name) == 0:
                return False
            else:
                return True
        def set_name(self, newstring):
            self.name = newstring
            print("seet naamee: ", self.name)
        def get_name(self):
            print("get_name: ", self.name)
            return self.name

    renpy.store.concern_backend = []
    renpy.store.concern_to_add = Concern() #definition

    def renpy_store_concern_reset():
        print("RESET DATATA")
        renpy.store.concern_to_add.reset_data()

    def renpy_store_add_concern_to_list():#function and variable names always have underscore not dot
        good_concern = renpy.store.concern_to_add.ready_to_submit()
        if good_concern:
            renpy.store.concern_backend.append(renpy.store.concern_to_add)
            for c in renpy.store.concern_backend:
                print("pp- ", c.get_name())
        # ELSE: ERROR SCREEN