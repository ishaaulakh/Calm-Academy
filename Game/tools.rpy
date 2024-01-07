screen tools_menu:
    frame:
        xalign 0.2 yalign 0.3
        xsize 240
        ysize 80
        hbox:
            xalign 0.5
            yalign 0.5
            textbutton _("Guided Journal") action Jump("Journal"):
                xalign 0.5
    frame:
        xalign 0.5 yalign 0.3
        xsize 240
        ysize 80
        hbox:
            xalign 0.5
            yalign 0.5
            textbutton _("Planner") action Jump("tm"):
                xalign 0.5
    frame:
        xalign 0.8 yalign 0.3
        xsize 240
        ysize 80
        hbox:
            xalign 0.5
            yalign 0.5
            textbutton _("Meditation") action Jump("Meditation"):
                xalign 0.5