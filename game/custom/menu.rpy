init:
    $ qm_baiyu = False
    $ qm_screen = False
    
    transform qm_spin:
        subpixel True
        yalign 0.75
        xalign 0.95
        rotate 0
        on hover:
            linear 3.0 rotate 360
            rotate 0
            repeat
        on idle:
            linear 3.0 rotate 0
    
    transform qm_eff:
        xoffset 50
        on show:
            alpha 0.0
            easein 1.0 xoffset 0 alpha 1.0
        on hide:
            easeout 1.0 xoffset 50 alpha 0.0


screen default_quick_menu():
    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("History") action ShowMenu('history')
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Prefs") action ShowMenu('preferences')

screen baiyu_quick_menu():
    hbox:
        style_prefix "quick"

        xalign 0.8
        yalign 0.97

        textbutton _("Rollback") action Rollback() at qm_eff
        textbutton _("History") action ShowMenu('history') at qm_eff


screen quick_menu():
    zorder 100
    if quick_menu:
        if qm_baiyu:
            if qm_screen:
                imagebutton auto "gui/button/hide_menu_%s.png" focus_mask True action [Hide("baiyu_quick_menu"), SetVariable("qm_screen", False)] at qm_spin
            else:
                imagebutton auto "gui/button/show_menu_%s.png" focus_mask True action [Show("baiyu_quick_menu"), SetVariable("qm_screen", True)] at qm_spin
        else:
            use default_quick_menu