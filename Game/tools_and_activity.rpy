screen tools_menu():
    modal True
    frame:
        xalign 0.2 yalign 0.3
        xsize 240
        ysize 80
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                    xalign 0.5
                    idle "IJour.png"
                    hover "HJour.png"
                    action Jump("Journal")
    frame:
        xalign 0.5 yalign 0.3
        xsize 240
        ysize 80
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                    xalign 0.5
                    idle "IPlan.png"
                    hover "HPlan.png"
                    action Jump("tm")
    frame:
        xalign 0.8 yalign 0.3
        xsize 240
        ysize 80
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                    xalign 0.5
                    idle "IMedi.png"
                    hover "HMedi.png"
                    action Jump("Meditation")

screen activity_menu():
    modal True
    frame:
        xsize 1
        ysize 1
        xalign 0.3
        yalign 0.05
        imagebutton:
            idle "SAB.png"
            hover "HSAB.png"
            action Jump("SAB")
    frame:
        xsize 1
        ysize 1
        xalign 0.3
        yalign 0.2
        imagebutton:
            idle "TM.png"
            hover "HTM.png"
            action Jump("TM")
        
    frame:
        xsize 1
        ysize 1
        xalign 0.3
        yalign 0.35
        imagebutton:
            idle "Soon.png"
            action NullAction()

screen skip():
    zorder 99
    frame:
        xalign 0.28 yalign 0.5
        xsize 3
        ysize 1
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "Skip.png"
                hover "HSkip.png"
                action Jump("lesson_and_tools")

screen activities_or_tools():
    modal True
    frame:
        xalign 0.38 yalign 0.32
        xsize 2
        ysize 1
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "Act.png"
                hover "HAct.png"
                action Jump("activities")
    frame:
        xalign 0.62 yalign 0.32
        xsize 2
        ysize 1
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                    idle "Tool.png"
                    hover "HTool.png"
                    action Jump("tools")
        
screen leave_activity():
    frame:
        xalign 0.28 yalign 0.2
        xsize 3
        ysize 1
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "leave_activity.png"
                hover "Hleave_activity.png"
                action Jump("lesson_and_tools")

