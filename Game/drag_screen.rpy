screen addConcernName:
    modal True
    frame:
        xalign 0.5 ypos 1
        xsize 1200
        ysize 500
        vbox:
            hbox:
                text "Enter Concern:"
                input id "concern_name_input" hover_color "#3399ff" size 28 color "#000" default "" changed renpy.store.concern_to_add.set_name
            textbutton _("Submit") action [
                Function(renpy_store_add_concern_to_list),
                Hide("addConcernName"),
                Show("drag")
            ]
            textbutton _("Cancel") action [
                Function(renpy_store_concern_reset),
                Hide("addConcernName"),
                Show("drag")
            ]

screen drag:
    frame:
        xalign 0.5 yalign 0.04
        xsize 1200
        ymaximum 100
        hbox:
            textbutton _("Back") action Rollback()
            textbutton _("Clear") action [
                lambda: renpy_store_clear_concern_backend(),
                renpy.restart_interaction
            ]
    for concern in renpy.store.concern_backend:
        python:
            concern_name = concern.get_name()
            print("concern_name: ", concern_name)
            print("renpy.store.concern_backend len", len(renpy.store.concern_backend))
            print("renpy.store.concern_backend[0]", renpy.store.concern_backend[0].get_name())
        drag:
            xpos renpy.random.randint(0, 800)
            ypos renpy.random.randint(0, 800)
            frame:
                xpadding 3
                ypadding 5
                text "[concern_name]"
    frame:
        xalign 0.5 yalign 0.5
        xsize 1200
        ymaximum 500
        hbox:
            textbutton _("Add Concern") action [Hide("drag"), Show("addConcernName")]
