screen leave():
    zorder 9000
    frame:
        xalign 0.11 yalign 0.07
        xsize 3
        ysize 1
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "leave_activity.png"
                hover "Hleave_activity.png"
                action [Hide("leave"), Jump("lesson_and_tools")]

screen TM_drag():
    fixed:
        drag:
            xpos 0.1
            ypos 0.2
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Get permission to host bake sale"
        drag:
            xpos 0.1
            ypos 0.3
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Advertise bake sale"
        drag:
            xpos 0.1
            ypos 0.4
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Buy baking ingredients"
        drag:
            xpos 0.1
            ypos 0.5
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Bake 100 goods"
        drag:
            xpos 0.5
            ypos 0.2
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Buy 100 pre-made goods"
        drag:
            xpos 0.5
            ypos 0.3
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Add extra decorations to the goods"
        drag:
            xpos 0.5
            ypos 0.4
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Design personalized thank you note"
        drag:
            xpos 0.5
            ypos 0.5
            drag_raise True
            draggable True
            frame: 
                xpadding 10
                ypadding 10
                text "Respond to unimportant questions"
        
        
            