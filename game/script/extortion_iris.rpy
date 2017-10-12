define iris = Character("Iris", color="#GGG")

label extortion_iris:
    stop music
    play music "audio/The Hustle.mp3"
    scene extortion
    show rosca at left
    $ init_minigame_ui()
    
    # Set the mark's initial statistics
    $ composure = 5
    $ defiance = 0
    
    # Extra variables can be created for a specific fight if need be
    # For iris, this one counts the number of times we tried to threaten this particular mark
    $ threat_attempts = 0

    r "Iris."
    r "Looks like you've fallen on hard times, girl."
    r "You're about to fall on harder ones, if you don't give us what's ours."
    iris "Give me a break, sugar."
    iris "Surely... it's not wrong to enjoy life once in a little while."
    iris "And hey, maybe I can do something for you, baby."

    hide rosca with dissolve
    
    jump extortion_iris_loop
    
label extortion_iris_loop:
    # Break the loop when composure is low enough or defiance high enough
    if composure < 1:
        jump extortion_iris_success
    if defiance > 3:
        jump extortion_iris_failure
    
    menu:
        "Seduce":
            $ defiance +=1
            "My charms won't work on this one."
            
            jump extortion_iris_loop
        "Threaten":
            $ threat_attempts += 1
            
            if 1 == threat_attempts:
                jump extortion_iris_first_threat

            if 2 == threat_attempts:
                jump extortion_iris_second_threat

            if 3 == threat_attempts:
                jump extortion_iris_third_threat

            if 4 == threat_attempts:
                jump extortion_iris_fourth_threat

            if 5 == threat_attempts:
                jump extortion_iris_fifth_threat

            if typing_game(sentence="This iris is long enough as it is.", word="iris"):
                "It's working."
                $ composure -= 1
            else:
                "Too slow!"
                $ defiance += 1
            
            jump extortion_iris_loop

        "Reason":
            $ defiance += 1
            "They won't listen to reason."
            
            jump extortion_iris_loop

label extortion_iris_first_threat:
    if typing_game(sentence="Blood is a pain to wash out, isn't it?", word="pain"):
        $ composure -= 1
        show rosca at left with dissolve
        r "But maybe you'll get good at washing it out. You keep getting into all sorts of trouble with us, anyway."
        richards "I didn't do anything wrong!"
    else:
        $ defiance += 1
        richards "Was that a threat? You look like the wind could blow you over."
    
    hide rosca with dissolve
    window hide

    jump extortion_iris_loop

label extortion_iris_second_threat:
    if typing_game(sentence="Lead or silver, pendejo. Your choice.", word="silver"):
        $ composure -= 1
        show rosca at left with dissolve
        r "And there's only one right answer."
        richards "That's not much of a choice you're giving me."
    else:
        $ defiance += 1
        richards "The money's gone. You're wasting your time, girl."
    
    hide rosca with dissolve
    window hide

    jump extortion_iris_loop

label extortion_iris_third_threat:
    if typing_game(sentence="You're making a big mistake.", word="mistake"):
        $ composure -= 1
        show rosca at left with dissolve
        r "Think about what you're doing, pal."
        richards "..."
    else:
        $ defiance += 1
        richards "All I'm thinking about is bashing your face in, you bitch."
    
    hide rosca with dissolve
    window hide

    jump extortion_iris_loop

label extortion_iris_fourth_threat:
    if typing_game(sentence="I heard your daughter had a beautiful wedding.", word="daughter"):
        $ composure -= 1
        show rosca at left with dissolve
        r "Why weren't we invited? We were the sponsors, after all."
        richards "Don't bring her into this, {i}please{/i}! I'm begging you!"
    else:
        $ defiance += 1
        richards "If you touch one hair on her head, you'll regret it, bitch."
    
    hide rosca with dissolve
    window hide

    jump extortion_iris_loop

label extortion_iris_fifth_threat:
    if typing_game(sentence="A man only has ten fingers.", word="fingers"):
        $ composure -= 1
        show rosca at left with dissolve
        r "I think in your case... it's ten too many. Don't you agree?"
        richards "You're messed up..."
    else:
        $ defiance += 1
        richards "Yeah, give me a trim on the toenails too, while you're at it."
    
    hide rosca with dissolve
    window hide

    jump extortion_iris_loop
    
label extortion_iris_success:
    $ money += 50
    "Your money is mine, rascal."
    jump extortiond1end

label extortion_iris_failure:
    "Fuck, I pissed them off."
    r "Leola!"
    show leola at right with moveinright
    l "I've got this."
    hide rosca with moveoutleft
    "I left the room and let Leola go to work."
    $ health -= 1
    l "All taken care of, kid."
    l "Try to do better next time, ok?"
    scene black
    jump extortiond1end
