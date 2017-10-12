transform centerleft:
    xalign 0.0
    yalign 0.5

transform centerright:
    xalign 1.0
    yalign 0.5

init python:
    import time
    import string
    import math

    def typing_game(sentence, word=None, time_limit=5.0):
        if not word:
            word = sentence
        starting_position = sentence.find(word)
        ending_position = starting_position + len(word)
        
        position = starting_position
        starting_time = time.time()

        while position < ending_position:
            # Skip spaces and punctuation signs
            if not sentence[position].isalpha():
                position += 1
                continue
            
            remaining_time = time_limit - (time.time()-starting_time)
            
            if remaining_time <= 0:
                # Time is already over, no need to instantiate the screen
                break
            
            if not renpy.call_screen("extorsion_game", sentence, position, remaining_time, starting_position, ending_position):
                # Timeout
                break

            position += 1
        
        return position == ending_position

    def custom_timer_func(st, at, limit):
        remaining_time = limit-st
        return Text('{:4.2f}'.format(remaining_time), at), 0.1
        
    composure = 0
    defiance = 0
    health = 10
    hour = 10.0
    money = 0
    
    def composure_display_func(st, at):
        return Text("{color=#ffff00}Composure: %s{/color}" % composure), 0.1
    renpy.image("composure_display", DynamicDisplayable(composure_display_func))
    
    def defiance_display_func(st, at):
        return Text("{color=#008000}Defiance: %s{/color}" % defiance), 0.1
    renpy.image("defiance_display", DynamicDisplayable(defiance_display_func))
    
    def health_display_func(st, at):
        return Text("{color=#4c4cff}Health: %s{/color}" % health), 0.1
    renpy.image("health_display", DynamicDisplayable(health_display_func))
    
    def hour_display_func(st, at):
        rounded_hour = math.floor(hour)
        minutes = (hour-rounded_hour)*60
        return Text("{color=#cccccc}Time: %s:%s{/color}" % ('{:02.0f}'.format(rounded_hour), '{:02.0f}'.format(minutes))), 0.1
    renpy.image("hour_display", DynamicDisplayable(hour_display_func))

    def money_display_func(st, at):
        return Text("{color=#fff}$%s{/color}" % money), 0.1
    renpy.image("money_display", DynamicDisplayable(money_display_func))

    def init_minigame_ui():
        renpy.show("composure_display", at_list=[topleft])
        renpy.show("defiance_display", at_list=[topright])
        renpy.show("health_display", at_list=[centerleft])
        renpy.show("hour_display", at_list=[centerright])
        renpy.show("money_display", at_list=[truecenter])

screen extorsion_game(word, index, time_limit, start, end):
    python:
        letter = word[index]

        letter_color = "#f00"
        past_letter_color = "#8b0000"
        future_letter_color = "#ff490c"
        
        # Some Python magic to color the right letters in the word
        colored_word = "%s{color=%s}%s{/color}{color=%s}%s{/color}{color=%s}%s{/color}%s" % (word[:start], past_letter_color, word[start:index], letter_color, letter, future_letter_color, word[index+1:end], word[end:])

    # Standard screen display. See https://www.renpy.org/doc/html/screens.html to customize it
    text colored_word size 120 xalign 0.5 yalign 0.5
    
    # Some key is pressed
    for another_letter in list(string.ascii_letters):
        key another_letter action NullAction()
    
    # The right key is pressed (override the previous statement)
    key letter.lower() action Return(True)
    key letter.upper() action Return(True)
    
    # Timer
    timer time_limit action Return(False)
    add DynamicDisplayable(custom_timer_func, time_limit) xalign 0.5 yalign 0.0

label extortion_original_example:
    scene black
    $ init_minigame_ui()
    
    # Set the mark's initial statistics
    $ composure = 5
    $ defiance = 0
    
    # Extra variables can be created for a specific fight if need be
    # For example, this one counts the number of times we tried to threaten this particular mark
    $ threat_attempts = 0
    
    jump extortion_original_example_loop
    
label extortion_original_example_loop:
    # Break the loop when composure is low enough or defiance high enough
    if composure < 1:
        jump extortion_original_example_success
    if defiance > 3:
        jump extortion_original_example_failure
    
    menu:
        "Seduce":
            $ defiance +=1
            "Your charm is lacking."
            
            jump extortion_original_example_loop
        "Threaten":
            $ threat_attempts += 1
            
            if 1 == threat_attempts:
                jump extortion_original_example_first_threat
            
            if typing_game(sentence="This example is long enough as it is.", word="example"):
                "It's working."
                $ composure -= 1
            else:
                "You were too slow."
                $ defiance += 1
            
            jump extortion_original_example_loop

        "Reason":
            $ defiance += 1
            "They won't listen to reason."
            
            jump extortion_original_example_loop

label extortion_original_example_first_threat:
    if typing_game(sentence="I would hate to have to dirty your furniture with blood.", word="blood"):
        $ composure -= 1
        show rosca at left
        r "I would hate to have to dirty your furniture with blood."
        "As would I."
    else:
        $ defiance += 1
        "Your blood you mean?"
    
    $ r.hide()
    window hide

    jump extortion_original_example_loop
    
label extortion_original_example_success:
    $ money += 50
    "Your money is mine, rascal."
    return

label extortion_original_example_failure:
    "Oh no, they got really angry."
    show leola at right
    l "Ah, violence, finally."
    "Awesome fight scene."
    $ health -= 1
    l "Try to do better next time ok?"
    return
