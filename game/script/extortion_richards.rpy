define richards = Character("Richards", color="#FFF")

label extortion_richards:
    stop music
    play music "audio/The Hustle.mp3"
    scene extortion
    show rosca at left
    $ init_minigame_ui()
    
    # Set the mark's initial statistics
    $ composure = 5
    $ defiance = 0
    
    # Extra variables can be created for a specific fight if need be
    # For richards, this one counts the number of times we tried to threaten this particular mark
    $ threat_attempts = 0

    # 3 different approaches?

    menu:
        "How should I begin?"
    
        "Put him at ease.":
            jump seduce_richards
    
        "Intimidate him.":
            jump intimidate_richards

        "Get straight to the point.":
            jump straightforward_richards

label seduce_richards:
    r "Chris, baby-"
    richards "Oh, don't you dare open that sweet mouth, Rosca."
    richards "It's done nothing but cause me trouble."
    r "But... you {i}like{/i} trouble, don't you?"
    richards "C'mon now, how about you sit on my lap, while we discuss this?"
    richards "Seeing as you're here, well... I'm in deep shit already."
    richards "Might as well enjoy it."
    l "Hey-"
    richards "What's it to ya, bitch?"
    richards "Hey Rosca, who's this mouthy friend of yours?"
    l "..."
    r "Hush, Leola."
    r "Sorry baby, my associate forgets her place, sometimes."
    r "Besides, Chris..."
    r "This isn't {i}that{/i} kind of meeting. You haven't even paid your debts yet."
    r "Fact is... you can't afford me, cabrón."
    richards "Ah, what a shame!"
    r "Now, now. Don't cry."
    richards "Hah, I'm trying not to."
    r "How about you hand the cash over and send me on my way?"
    r "I'll throw in a kiss, gratis."
    richards "Well... I'm sorry, Rosca... but there's nothing to hand over."
    richards "How about you come back in a week?"
    r "You said that last time."
    richards "Anything to keep you coming back, love."
    r "Oh no, baby. You can't keep doing this."
    r "I won't have anything to come back to, if you keep this up."
    jump extortion_richards_loop

label intimidate_richards:
    r "Mr. Richards."
    richards "Hey, you used to call me Chris. Why so stiff all of a-"
    r "Let's cut the shit."
    r "You already know why I'm paying you a visit."
    r "Now... hand over the money and-"
    richards "And no one gets hurt?"
    richards "That's {i}bullshit{/i}, and you know it. I'm a dead man twice over..."
    richards "Nic used to come see me herself. But now that she's sending a runt like you..."
    richards "And that beanstalk of a bitch over there..."
    richards "Nic must be done talking, huh."
    richards "Ah, luck's a fickle mistress, Rosca. I haven't won a bet in weeks."
    r "Patrona can't wait for lady luck to pay your debts for you."
    r "You can always get a job. Luck's got nothing to do with it, Richards."
    richards "You're no gambler, you wouldn't understand."
    richards "Here, how about a drink-"
    r "I said, cut the shit. Let's talk about the money, Richards."
    richards "Then there's nothing to talk about."
    r "We'll see about that."
    
    hide rosca with dissolve
    
    jump extortion_richards_loop

label straightforward_richards:
    r "Chris Richards."
    richards "Yes, that's my name. Just Chris is fine enough."
    richards "Now, what can I do for you, love?"
    r "Right now, it's more of... what you can do for yourself, Richards."
    r "Patrona just wants the money back. No more, no less."
    richards "Tell her she'll get it soon enough."
    r "She's tired of waiting, Richards."
    richards "And that's why she sent you, instead of coming over herself."
    richards "Well... maybe I'm a dead man, after all."
    r "I'm only here to take what is due."
    jump extortion_richards_loop
    
label extortion_richards_loop:
    # Break the loop when composure is low enough or defiance high enough
    if composure < 1:
        jump extortion_richards_success
    if defiance > 3:
        jump extortion_richards_failure
    
    menu:
        "Seduce":
            $ seduce_attempts += 1

            if 1 == seduce_attempts:
                jump exortion_richards_first_seduce

            if 2 == seduce_attempts:
                jump extortion_richards_second_seduce

            if 3 == seduce_attempts:
                jump extortion_richards_third_seduce

            if 4 == seduce_attempts:
                jump extortion_richards_fourth_seduce

            if 5 == seduce_attempts:
                jump extortion_richards_fifth_seduce

            if typing_game(sentence="Don't make me beg, Richards.", word="Richards"):
                "Hah! What a pig."
                $ composure -= 1
            else:
                "Tch, my charms aren't working on this one."
                $ defiance += 1
            
            jump extortion_richards_loop

            # $ defiance +=1
            # "My charms won't work on this one."
            
            jump extortion_richards_loop
        "Threaten":
            $ threat_attempts += 1
            
            if 1 == threat_attempts:
                jump extortion_richards_first_threat

            if 2 == threat_attempts:
                jump extortion_richards_second_threat

            if 3 == threat_attempts:
                jump extortion_richards_third_threat

            if 4 == threat_attempts:
                jump extortion_richards_fourth_threat

            if 5 == threat_attempts:
                jump extortion_richards_fifth_threat

            if typing_game(sentence="Ah, Monica... Such a lovely name, isn't it. Ever heard her scream?", word="Monica"):
                r "Hijo de puta. Look at you, shaking like a leaf. Pathetic."
                $ composure -= 1
            else:
                "Why isn't he giving up?!"
                $ defiance += 1
            
            jump extortion_richards_loop

        "Reason":
            if 1 == reason_attempts:
                jump exortion_richards_first_reason

            if 2 == reason_attempts:
                jump extortion_richards_second_reason

            if 3 == reason_attempts:
                jump extortion_richards_third_reason

            if 4 == reason_attempts:
                jump extortion_richards_fourth_reason

            if 5 == reason_attempts:
                jump extortion_richards_fifth_reason

            if typing_game(sentence="This has gone on long enough, Richards.", word="Richards"):
                "Finally talked some sense into him."
                $ composure -= 1
            else:
                "Why won't he listen to reason?!"
                $ defiance += 1
            
            jump extortion_richards_loop

            # $ defiance += 1
            # "They won't listen to reason."
            
            jump extortion_richards_loop

label extortion_richards_first_threat:
    r "You're looking pretty filthy these days. You really let yourself go, Richards."
    richards "What's it to you?"
    r "Ever had to wash your own clothes, old man?"
    richards "Every damn day after I gave my daughter away."
    r "Then you ought to know..."
    if typing_game(sentence="Blood is a pain to wash out, isn't it?", word="pain"):
        $ composure -= 1
        show rosca at left with dissolve
        r "Don't worry, Richards."
        r "With practice... you'll get good at washing it out of your shirts soon enough."
        r "You keep getting into all sorts of trouble with us, anyway."
        richards "...are you threatening me?"
        r "There's nothing to be afraid of, if you do the right thing."
        richards "I want to, Rosca. Believe me."
        richards "But I can't."
        richards "I'm not running away. I'm going to pay Nic back."
        richards "I just need a bit more time..."
    else:
        $ defiance += 1
        richards "Look, kid. I could snap your neck without trying."
        richards "And believe me, I'll-"
        l "{i}Back {w}off{/i}, {w}{b}fucker{/b}."
        richards "..."
        richards "Hey... that badge-"
        richards "Y-you're..."
        r "I wouldn't get on her bad side, if I were you."
        richards "Bah-"
        richards "All you bitches have are bad sides, anyway-"
        r "You better watch that mouth, hijo, if you want to keep those teeth."
    hide rosca with dissolve
    window hide

    jump extortion_richards_loop

label extortion_richards_second_threat:
    if typing_game(sentence="You've got a simple choice, Richards: lead or silver?", word="lead"):
        $ composure -= 1
        show rosca at left with dissolve
        richards "That's not much of a choice you're giving me."
        richards "What if you've got a silver bullet?"
        r "I'll personally dig it out of your skull once we're done."
        r "Like we'd be wasting any more silver on you."
        richards "The money's gone. You're wasting your time, girl."
        r "If that's true..."
        r "Then...{w} are you ready{w} to die?"
        richards "..."
        r "Uno."
        richards "..."
        # hand banging table
        r "Dos."
        richards "..."
        # sound of gun being cocked
        r "Tres!"
        richards "Wait! H-hold on..."
        r "Tch. Thought so. Spineless fucker."
        r "Now again... the money."
    else:
        $ defiance += 1
        richards "Gold, then."
        r "That's not one of the choices."
        richards "Those choices were daft, love."
        richards "And so are you."
        r "Tch."
    hide rosca with dissolve
    window hide

    jump extortion_richards_loop

label extortion_richards_third_threat:
    if typing_game(sentence="You're making a big mistake.", word="mistake"):
        $ composure -= 1
        show rosca at left with dissolve
        r "Think about what you're doing, pal."
        r "If only you did what you were supposed to, you wouldn't be in this mess, Richards."
        richards "I did what any father would do."
        r "I couldn't give less of a fuck about what you did."
        richards "..."
    else:
        $ defiance += 1
        richards "Who did you sell your soul to, you heartless bitch?"
        r "At least I'm not in debt."
        richards "The devil's going to come for you, girl."
        r "And {i}you{/i} are going to end up in the {b}dump{/b} if you keep talking like that."
        richards "..."
    
    hide rosca with dissolve
    window hide

    jump extortion_richards_loop

label extortion_richards_fourth_threat:
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

    jump extortion_richards_loop

label extortion_richards_fifth_threat:
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

    jump extortion_richards_loop

label extortion_richards_first_seduce:
    if typing_game(sentence="Listen, Richards. Why don't you tell me all about it?", word="Richards"):
        $ composure -= 1
        show rosca at left with dissolve
        r "And there's only one right answer."
        richards "That's not much of a choice you're giving me."
    else:
        $ defiance += 1
        richards "The money's gone. You're wasting your time, girl."
    
    hide rosca with dissolve
    window hide

    jump extortion_richards_loop

label extortion_richards_second_seduce:
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

    jump extortion_richards_loop

label extortion_richards_third_seduce:
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

    jump extortion_richards_loop

label extortion_richards_fourth_seduce:
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

    jump extortion_richards_loop

label extortion_richards_fifth_seduce:
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

    jump extortion_richards_loop

label extortion_richards_first_reason:
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

    jump extortion_richards_loop

label extortion_richards_second_reason:
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

    jump extortion_richards_loop

label extortion_richards_third_reason:
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

    jump extortion_richards_loop

label extortion_richards_fourth_reason:
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

    jump extortion_richards_loop

label extortion_richards_fifth_reason:
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

    jump extortion_richards_loop
    
label extortion_richards_success:
    $ money += 50
    "Your money is mine, rascal."
    jump extortiond1end

label extortion_richards_failure:
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
    jump extortion_richards_end
