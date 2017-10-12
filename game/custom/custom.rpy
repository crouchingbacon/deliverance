init -1 python:    
    import time
    
    color_out_auto = True
    characters_to_color_out = [{'tag': "rosca", 'color': "#ed1c24"}, {'tag': "leola", 'color': "#96cf9d"}, {'tag': "nic", 'color': "#57c6d0"}, {'tag': "oberon", 'color': "#fde600"}]

    def get_original_image(tag):
        return renpy.game.context().scene_lists.get_displayable_by_tag("master", tag).children[0]
    
    def color_out_everyone(except_tags=[]):
        for char in characters_to_color_out:
            tag = char['tag']
            color = char['color']
            
            if tag not in except_tags:
                color_out(tag, color)

    def color_out(tag, color=None):
        tag = tag.lower()
        
        if not renpy.showing(tag):
            return
        
        if not color:
            color = next(char for char in characters_to_color_out if char['tag'] == tag)['color']
        
        original_image = get_original_image(tag)
        if isinstance(original_image, renpy.display.im.MatrixColor):
            # Already colored out
            return

        rgb = Color(color).rgb
        colored_out_image = im.MatrixColor(original_image, im.matrix.tint(rgb[0]*0.75, rgb[1]*0.75, rgb[2]*0.75))
        renpy.transition(dissolve)
        renpy.show(tag, what=colored_out_image)

    def uncolor(tag):
        tag = tag.lower()
        
        if not renpy.showing(tag):
            return
            
        current_image = get_original_image(tag)
        if not isinstance(current_image, renpy.display.im.MatrixColor):
            # Not colored, nothing to do
            return
        
        original_image = current_image.image
        renpy.transition(dissolve)
        renpy.show(tag, what=original_image)

    def CustomCharacterCallback(event, interact=True, char=None, **kwargs):
        if not color_out_auto:
            return
            
        if not char:
            return
        if not char.name:
            return

        if event == "begin":
            color_out_everyone(except_tags=[char.name.lower()])
            uncolor(char.name.lower())

    class Character(ADVCharacter):
        def __init__(self, name, color=None, **kwargs):
            cb = renpy.curry(CustomCharacterCallback)(char=self)
            super(Character, self).__init__(name, color=color, ctc="ctc", ctc_position="fixed", callback=cb, **kwargs)

image ctc:
    "gui/ctc.png"
    alpha 0.0
    pause 0.5
    block:
        linear 0.4 alpha 1.0
        pause 0.1
        linear 0.4 alpha 0.2
        pause 0.1
        repeat

define narrator = Character(None)
default preferences.text_cps = 60

image bg shot_missed:
    "#ed1c24"
    linear 0.2 alpha 0.0

image shot_oberon = AlphaMask("bg shot_missed", "oberon")

default shots_fired = 0

default shootout_dt = None
label start_shootout:
    if shootout_dt == None:
        $ shootout_dt = time.time()
    elif time.time() - shootout_dt > shootout_timeout:
        jump shootout_end_out_of_time
    label shootout_loop:
    scene black
    show nic:
        pos (200, 200)
    show oberon at left

    call screen shootout_screen

label shot_oberon:
    show shot_oberon at left
    $ shots_fired += 1
    jump shootout_end_oberon_shot

label shot_nic:
    call shootout_shot_nic
    jump start_shootout

label shot_missed:
    scene black
    show bg shot_missed
    show nic:
        pos (200, 200)
    show oberon at left
    $ shots_fired += 1
    call shootout_shot_missed
    if shots_fired >= 6:
        jump shootout_end_out_of_bullets
    else:
        jump start_shootout

screen shootout_screen():
    timer 0.5 action Jump("start_shootout")
    imagebutton:
        idle "black"
        action [Jump('shot_missed')]

    imagebutton:
        idle "images/nic.png"
        pos (200, 200)
        action [Jump('shot_nic')]
        focus_mask True
    imagebutton:
        idle "images/oberon.png"
        action [Jump('shot_oberon')]
        focus_mask True
label shootout:
    $ config.mouse = {'default':[('images/reticle.png', 60, 60)]}
    call start_shootout

label end_shootout:
    $ config.mouse = None
    return
label start:
    jump opening_scene
