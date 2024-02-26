screen meditation_menu():
    modal True
    frame:
        xsize 1
        ysize 1
        xalign 0.3
        yalign 0.05
        imagebutton:
            idle "Box.png"
            hover "HBox.png"
            action Jump("boxBreathing")
    frame:
        xsize 1
        ysize 1
        xalign 0.3
        yalign 0.2
        imagebutton:
            idle "Deep.png"
            hover "HDeep.png"
            action Jump("deepBreathing")
    frame:
        xsize 1
        ysize 1
        xalign 0.3
        yalign 0.35
        imagebutton:
            idle "Nature.png"
            hover "HNature.png"
            action Jump("nature")
