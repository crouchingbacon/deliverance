init python:
    nic_route = 0
    leola_route = 0
    quota_notok = 0
    health_notok = 0
    nic_eve1 = 0
    leola_eve1 = 0

image alley = "alley.jpg"
image arcade = "arcade.jpg"
image car = "bosscaredit.jpg"
image darkstreet = "street.jpg"
image extortion = "extortionbg.jpg"
image frontseat = "shotgunnightedit.jpg"
image hallway = "dimofficepath.jpg"
image hq = "hq.jpg"
image inapartment = "apartmentedit.jpg"
image incar = "insidecar1edit.jpg"
image incafe= "darkcafe.jpg"
image juice = "juice.jpg"
image office = "officeedit.jpg"
image olddash = "olddash.jpg"
image mainstreet = "mainStreet.jpg"
image outcafe = "relax.jpg"
image outapartment = "appartment.jpg"
image police = "police.jpg"
image police2 = "police2.jpg"
image prison = "prison.jpg"
image shoot = "shoot.jpg"
image wakeup = "apartment.jpg"
image note = "note.png"

define r = Character("Rosca", color="#ed1c24", image="rosca")
define o = Character("Oberon", color="#fde600")
define nic = Character("Nic", color="#57c6d0")
define l = Character("Leola", color="#96cf9d", image="leola")
define u = Character("???", color="#FFFFFF")
define ace = Character("an Ace", color="#000000")

image rosca = "images/sprites/png/rosca.png"
image rosca yawn two= "images/sprites/png/rosca_yawn_2.png"
image rosca oi one= "images/sprites/png/rosca_oi_1.png"
image rosca oi two= "images/sprites/png/rosca_oi_2.png"
image rosca hmm two= "images/sprites/png/rosca_hmm_2.png"
image rosca surprise = "images/sprites/png/rosca_surprise.png"
image rosca surprise hat = "images/sprites/png/rosca_surprise_hat.png"
image rosca disappointed = "images/sprites/png/rosca_disappointed.png"
image rosca smug = "images/sprites/png/rosca_smug_hatless.png"
image rosca smug hat = "images/sprites/png/rosca_smug.png"
image rosca cheeky = "images/sprites/png/rosca_cheeky.png"
image rosca tsktsk hat = "images/sprites/png/rosca_tsktsk_hat.png"

image leola = im.Flip("images/sprites/png/leola.png", horizontal=True)
image nic = im.Flip("images/sprites/png/nic.png", horizontal=True)

# Missing pictures: grand door to Nic's office

label opening_scene:
    # Olive: I am comendeering the start label for debugging purposes, treat
    # this label as start instead.

    # Swears reference
    # http://www.alwaysspanish.com/2012/09/swear-in-spanish-like-natives.html

    # Plot check reference
    # https://www.kritikme.com/blog/everything-you-wanted-to-know-about-your-plot-but-were-afraid-to-ask-yourself

    # Understanding Romantic Identity
    # http://www.asexuality.org/en/topic/78157-romance-vs-romantic-identities/
    # https://www.good.is/articles/the-sexless-relationship-guru

    # Asi Es Como Te Amo
    # https://www.youtube.com/watch?v=N9JKX2ewwEI
    # Some femme fatale
    # https://www.youtube.com/watch?v=lfaE_8gEh4w

    stop music
    scene black
    play music "audio/Alone Together.mp3"
    # Message tone?
    # Flash of white, highlighting Rosca's worn face.
    # Tense music.
    # Mobile/Email-ish interface
    # A message appears.
    # play sound "audio/msg.wav"
    u "Sorry for your loss, Rosca."
    # Rosca types a message in.
    # play sound "audio/beeplo.wav"
    r "Who is this?"
    # play sound "audio/msg.wav"
    u "That's not important."
    # play sound "audio/msg.wav"
    u "But tell you what."
    # play sound "audio/msg.wav"
    u "I've got a hot tip for you."
    # play sound "audio/msg.wav"
    u "I know who killed your brother."
    # play sound "audio/beeplo.wav"
    r "Where did you get this information?"
    # No reply.
    # play sound "audio/beeplo.wav"
    r "Tell me who murdered Oberon."
    # No reply
    # play sound "audio/beeplo.wav"
    r "Please."
    # play sound "audio/beeplo.wav"
    r "Hello?"
    # play sound "audio/beeplo.wav"
    r "Please!"
    # play sound "audio/beeplo.wav"
    r "How much do you want? Name your price."
    # No reply
    # play sound "audio/msg.wav"
    u "Keep your money."
    # play sound "audio/msg.wav"
    u "You want the truth?"
    # play sound "audio/msg.wav"
    u "Meet me tonight."
    # play sound "audio/msg.wav"
    u "Down by the Arcade. Where his body was dumped."
    # play sound "audio/msg.wav"
    u "What a mess that was, huh?"
    # play sound "audio/beeplo.wav"
    r "Tell me who you are."
    # play sound "audio/msg.wav"
    u "Don't make me repeat myself."
    # play sound "audio/msg.wav"
    u "It shouldn't matter who I am, Rosca."
    # play sound "audio/msg.wav"
    u "After all, I didn't kill him."
    # play sound "audio/msg.wav"
    u "What matters is what you're going to do next."
    # play sound "audio/msg.wav"
    u "I'm coming alone."
    # play sound "audio/beeplo.wav"
    r "Do you think I'm an idiot?"
    # play sound "audio/beeplo.wav"
    r "I don't trust you."
    # play sound "audio/msg.wav"
    u "If you think I'm dangerous, then bring a friend."
    # play sound "audio/msg.wav"
    u "Bring the Aces."
    # play sound "audio/msg.wav"
    u "Hell, bring the fucking Boss."
    # play sound "audio/beeplo.wav"
    r "I'm not going."
    # play sound "audio/msg.wav"
    u "Ha! That's {i}funny{/i}."
    # play sound "audio/beeplo.wav"
    r "Don't fuck with me."
    # play sound "audio/msg.wav"
    u "Oh, I'm not fucking with you, Rosca."
    # play sound "audio/msg.wav"
    u "If you still think you can run and hide..."
    # play sound "audio/msg.wav"
    u "Then the joke's on you."
    "My hands felt cold-"
    "Nothing made sense any more."
    play sound "audio/dropphone.mp3"
    "I couldn't even hold on to the phone."
    "Lately... I've been asking myself, {i}why{/i}?"
    "{i}Why did this have to happen?{/i}"
    "My life has always felt like a house of cards."
    "Now that my brother's been pulled out, forever-"
    "Everything is falling apart faster than I can put back together."
    "Oberon did something he never should have."
    "He started getting ideas. Getting angry. Looking for trouble."
    "But I thought nothing of it."
    "After all, we ran with {i}the Black Aces{/i}."
    "Nothing and no one could touch us."
    centered "{i}I-{/i}"
    centered "{i}I should have known better.{/i}"
    stop music
    play sound "audio/typewriter.mp3"
    $ renpy.movie_cutscene("images/threedaysago.ogv")
    play sound "audio/alarm.mp3"
    #$ r.switch_mood('yawn 2')
    show rosca yawn two at left with fade
    r "Ugh."
    r "Oberon, shut that thing up, will you?"
    r "Damn it!"
    scene inapartment
    "My eyes finally creaked open. It didn't make much of a difference; the room was just as dark."
    # Click sound. Alarm clock sound stops.
    "I sat up a little too fast; bile shot up the back of my throat."
    "Last night's bender wasn't doing me any favors."
    #Light turns on in the room.
    show rosca yawn two at left with fade
    r "Coffee, I need coffee. {i}Pero ya!{/i}"
    $ color_out_auto = True
    # $ r.switch_mood('oi 1')
    show rosca oi one at left with fade
    "At that point Oberon would have caved, pouring the black liquid into a cup and shoving it into my hands."
    "Then I began to realize that he wasn't there."
    # $ r.switch_mood('hmm 2')
    # show rosca hmm two with dissolve
    show rosca hmm two
    "A note on the messy table and a half-smoked cigarette, both right by our empty change jar."
    "I bent over to read the note."
    show note
    "{i}Sorry Rosca, I've got a personal errand to run today. Don't you worry, I'll make it up to you, I promise{/i}."
    "{i}Meet me at the cafe first thing tomorrow, manita. I've got something for you that will definitely make your day{/i}."
    hide note
    r "Hijo de puta. The least he could do is send me a message on the phone instead of forcing me to read this chicken-scratch shit."
    play sound "audio/ring.mp3"
    play sound "audio/ring.mp3"
    "I dove for my phone and checked the screen to see who was calling."
    play sound "audio/ring.mp3"
    # $ r.switch_mood('surprise 1')
    show rosca surprise
    r "Mierda! Patrona sure is calling early today..."
    "I thumbed the receive button to shut the damn phone up."
    nic "Rosca. 1,000 credits. Oberon. 2,000 credits. Get to work."
    # $ r.switch_mood('disappointed 1')
    show rosca disappointed
    r "Patrona, Oberon's not around today."
    nic "Great. Then that means you're picking up 3,000 credits today."
    # $ r.switch_mood('oi 1')
    show rosca oi with dissolve
    "Come mierda, Oberon."
    nic "Are you up for it, Rosca?"
    nic "If you're not up to it, there's always-"
    # $ r.switch_mood('smug 2')
    show rosca smug with dissolve
    r "No, I'll manage. See you later, Patrona."
    nic "Good girl."
    nic "Be careful. {w} And {i}don't be late{/i}."
    "Nicasia Dillinger. I'll bet that isn't even her real name."
    "But she's la Patrona. {i}The Boss{/i}."
    "Whatever passed her lips was as good as the bitter truth."
    "I haven't had the chance to taste those lips."
    "Rumor is, {i}no one{/i} has."
    # $ r.switch_mood('cheeky 1')
    show rosca cheeky with dissolve
    r "Not for lack of trying, though."
    "After a quick shower, I put on my hat and headed over to the Arcade."
    "No time for breakfast. I never ate breakfast."
    scene mainstreet
    play sound "audio/trafficshort.wav"
    show rosca at left with moveinleft
    "From our apartment to the Arcade, the distance was barely a fifteen minute walk."
    "Patrona called it convenient, but it all depends on how you looked at it."
    "Ever heard of the phrase, {i}don't shit where you eat{/i}?"
    "Well, we lived and worked in pretty much the same neighborhood."
    "A lot of shit happened around us, all right."
    "Oberon and I mostly kept to ourselves."
    play music "audio/Upriver Funk.mp3"
    # Pass by the Streets.
    # Traffic sounds.
    show leola at right with moveinright
    l "Morning, Rosca!"
    "But we did have {i}one{/i} friend."
    l "Going anywhere dangerous today?"
    # $ r.switch_mood('smug hat 1')
    r smug hat "Why, are you bored out of your mind already?"
    # $ l.switch_mood('fiteme hat shadow 4 0')
    l "It's not like trouble ever happens around here."
    # $ r.switch_mood('smug hat 2')
    r "So you're saying I'm not working hard enough?"
    # $ l.reset_mood()
    l "Maybe."
    # $ r.switch_mood('tsktsk hat 1')
    r tsktsk hat "Your Urban Security pals don't have a clue, huh."
    r "Dead noses, all of them."
    # $ l.switch_mood('fiteme hat shadow 4 0')
    l "And why's that?"
    # $ r.switch_mood('heynow hat 3')
    r "How do you mask that dirty cop stench, when you're on first name basis with the {i}biggest criminal in town{/i}?"
    l "You know, hotshot... I could arrest you. Right here, right now."
    # $ r.switch_mood('tsktsk hat 1')
    show rosca tsktsk hat with dissolve
    r "But you won't."
    l "I {i}could{/i}."
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat with dissolve
    r "I'd like to see you try, Inspector."
    "I struck a pose, half in jest and half just to see what Leola would do."
    "She didn't move a muscle, but I could see where her eyes were going."
    "Not that she would ever do anything about it."
    "Like Patrona said: cops and Aces, oil and water."
    "No matter how dirty, we couldn't mix."
    "That didn't mean I couldn't tempt her, though."
    l "Listen, you need my help today, or what?"
    # $ l.switch_mood('whoa hat shadow 3 0')
    l "I've got better things to do than torture myself with a tease like you."
    # $ l.switch_mood('fiteme hat shadow 4 0')
    l "Let me guess... your brother left you with the bag again?"
    # $ r.switch_mood('oi hat 2')
    r "He sure did, que pendejo. I'm going to tear him a new one when he gets back."
    # $ l.switch_mood('neutral hat shadow 1 0')
    l "Listen Rosca..."
    l "I know it's just business as usual... but could you tell him to take it easy? It's getting harder to clean up after him."
    l "Just the other day, we found him beating a man he already collected from."
    # $ l.switch_mood('hmph hat shadow 2 0')
    l "A few minutes too late and it would have turned into a murder case."
    # $ r.switch_mood('surprise hat 1')
    show rosca surprise hat with dissolve
    r "..."
    l "Don't look at me like that. Of course I let him get away."
    l "This wasn't the first time. If this keeps up, I'm going to have to take him in."
    # $ r.switch_mood('tch hat 1')
    r "All right. I'll talk to him. He's just a bit too good at his job, you know?"
    l "Sure... a {i}real{/i} pro. He wasn't pulling any punches when we restrained him. Gave me a nasty bruise on the arm, too..."
    "She rolled up her sleeve and pointed to a blackened patch of sore flesh."
    l "So I gave him a kick in the balls for this."
    # $ r.switch_mood('surprise hat 2')
    show rosca surprise hat with dissolve
    r "A la madre, Leola! Doesn't it sting?"
    "Leola rolled her sleeves down and winked at me."
    l "Damn, Rosca."
    l "For a moment there, you almost sound like you were worried about me."
    # $ l.switch_mood('whoa hat shadow 3 0')
    l "I'm sure a kiss would make it feel all better."
    # $ r.switch_mood('heynow hat shade 3')
    r "..."
    # Rosca hits Leola. Punch sound.
    play sound "audio/punch.wav"
    "I hit her, right where it hurt."
    # $ l.switch_mood('hmph hat shadow 2 0')
    l "Oh, fuck! You're a real devil, you know that?"
    # $ r.switch_mood('oi hat 2')
    r "Cállate. You asked for it."
    l "Barring medical expenses from your routine abuse... you still owe me 500 credits from last night."
    # $ r.switch_mood('tch hat 1')
    r "Consider it paid."
    # $ l.switch_mood('fiteme hat shadow 4 0')
    l "Sweet. Sounds grea- {nw}"
    r "As long as we can make some credits today."
    # $ l.switch_mood('hmph hat shadow 2 0')
    l "I knew it. There's always a catch with you."
    # $ l.switch_mood('fiteme hat shadow 4 0')
    l "What's the job?"
    r "Just another walk in the Arcade. 3,000 credits. Think we can pull it off?"
    # $ l.reset_mood()
    l "Psh. Just keep glaring like that and this will be a piece of cake."
    l "Though, just in case..."
    "Leola took a brass classic out of her coat and wore it on her left fist."
    # Apparently classic is another word for knuckleduster. I thought it sounded better.
    # $ l.switch_mood('hmph hat shadow 4 2')
    l "All set. Let's go!"
    "It shone like the chrome on a newly serviced astro-sedan. Loud and bright, and everything but useful in the streets."
    # $ r.switch_mood('oi hat 2')
    r "I'm not moving until you take that thing off your hand."
    l "Why?"
    # $ r.switch_mood('tch hat 1')
    r "You're going to attract too much attention! Keep that shit in your coat until you need to use it."
    l "Fine."
    "She took it off and sighed."
    # $ l.switch_mood('hmph hat shadow 2 0')
    l "You're no fun. Besides... I've loaned you my gun. {i}What else am I supposed to use{/i}?"
    r "I don't care! That's your problem. You're supposed to be the cop, Leola. Act like one."
    # $ r.switch_mood('oi hat 2')
    r "It's not my fault you can't afford another gun. Nic pays you a premium, for fuck's sake. Where does all your money go?"
    # $ l.switch_mood('fiteme hat shadow 4 0')
    l "Whatever, kid. That's none of your business."
    l "I think this shiny baby does a good pretty good job of convincing the marks, and {i}it doesn't even have to talk{/i}."
    # $ r.switch_mood('tch hat 1')
    r "Leola. Leave that junk in your pocket and leave the thinking and talking to me."
    # $ l.reset_mood()
    l "Hmph. All right then, {i}señorita{/i}. Lead the way."
    "Pobre gringa, can't even roll her r's."
    "Still, it made me smile."
    "Maybe someday, I'd get that respect from everyone else."
    "But for now..."
    # $ r.switch_mood('heynow hat 3')
    r "Let's get to work, Inspector."
    # Transition to the Street then the Arcade
    play sound "audio/trafficshort.wav"
    scene arcade
    show rosca at left
    show leola at right
    "The Arcade was the heart of Veccio Palermo."
    "Money came all the way from here and bled out to everywhere else."
    "Me, I was just here to suck the marks dry."
    "The marks had many names for my brother and I."
    "{i}Extortionist, racketeer, {b}parasite{/b}{/i}."
    "Personally, I preferred tax collector."
    "It's a stable job."
    "After all... in life, death and taxes are the only things you could count on."
    "I just happened to work for an employer who dealt in both."
    "We've all got means of keeping the lights in our eyes."
    "This was mine."
    l "Hey Rosca, run the numbers by me, would ya?"
    # $ r.switch_mood('tch hat 1')
    r "At least twenty businesses failed to give their dues this month."
    # Might change this line depending on actual minigame output.
    r "If we can get at least four of them to pay up, 3,000 credits shouldn't be too hard."
    l "We? Let's see {i}you{/i} get one first."
    l "I'll wait here. Give me a call when things go south."

    menu:
        "Easy enough.":
            jump confident
        "You just want an excuse to use your fists. Let's keep things clean today.":
            jump guide

label guide:
    l "All right, all right. You got me."
    l "But you, being you, it shouldn't be that hard to get them to see reason."
    l "Just say the right things to make them realize that an unpaid debt to the Boss of the Black Aces brings nothing but bad luck."
    l "Let me handle the idiots who are stupid enough to try hurting you."
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat with dissolve
    r "Who's to say I can't handle myself?"
    l "Look, the last time we tried that, you ended up half-dead in a ditch."
    l "The Boss even made me pay for the hospital bills."
    l "She just about chewed my head off, that day."
    # $ r.switch_mood('surprise hat 2')
    show rosca surprise hat with dissolve
    r "Oh... I thought she covered it."
    l "She eventually did, when she realized I didn't have enough to fix your face."
    # $ r.switch_mood('tsktsk hat 1')
    show rosca tsktsk hat
    r "What can I say, she's got her priorities straight."
    l "I can't say I disagree."
    # $ l.switch_mood('fiteme hat shadow 4 2')
    l "So yeah. Leave the fighting to me, kid."
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat with dissolve
    r "All right. I'm counting on you, Leola."
    # $ l.reset_mood()
    l "When have I ever let you down?"
    l "Now tell me what you've got planned for the day."
    jump arcade1

label confident:
    l "'atta girl! Go get them."
    l "Just say the right things to make them realize that an unpaid debt to the Boss of the Black Aces brings nothing but bad luck."
    l "Let me handle the idiots who are stupid enough to try hurting you."
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat with dissolve
    r "Who's to say I can't handle myself?"
    l "Look, the last time we tried that, you ended up half-dead in a ditch."
    l "The Boss even made me pay for the hospital bills."
    l "She just about chewed my head off, that day."
    # $ r.switch_mood('surprise hat 2')
    show rosca surprise hat with dissolve
    r "Oh... I thought she covered it."
    l "She eventually did. Maybe she realized I didn't have enough to fix your face."
    # $ r.switch_mood('tsktsk hat 1')
    show rosca tsktsk hat with dissolve
    r "What can I say. She's got her priorities straight."
    l "I can't say I disagree."
    # $ l.switch_mood('fiteme hat shadow 4 2')
    l "So yeah. Leave the fighting to me, kid."
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat with dissolve
    r "All right. I'm counting on you, Leola."
    # $ l.reset_mood()
    l "When have I ever let you down?"
    l "Now tell me what you've got planned for the day."
    jump arcade1

label arcade1:
    # $ r.switch_mood('tch hat 1')
    r "Right now it's {color=#f00}10:00 AM{/color}. That leaves me {color=#f00}2 hours{/color} before lunch break."
    r "Then after {color=#f00}an hour{/color}, it's back to work, until {color=#f00}5:00 PM{/color}."
    # $ r.switch_mood('tsktsk hat 1')
    show rosca tsktsk hat with dissolve
    r "After that, I'll have to haul ass and report to Patrona."
    r "That gives me {color=#f00}6 hours{/color}."
    r "If things go smoothly, half an hour should be enough time to collect."
    # $ r.switch_mood('tch hat 2')
    r "Troublesome debtors could take me longer though."
    r "And if I'm going to need {i}your{/i} help, well, that's going to take {color=#f00}an hour{/color}."
    r "I need at least {color=#f00}3,000 credits{/color} today."
    # $ r.switch_mood('tch hat 1')
    r "Most of these people owe Patrona somewhere between {color=#f00}500 to 2,000 credits{/color}."
    r "I don't have intel on exactly how much, but if they're scared enough, they could pay more than they owe, just to keep out of trouble."
    r "If you take care of them for me, Leola, they might comply..."
    # $ r.switch_mood('oi hat 2')
    r "But if you're too rough with them, they'll pass out."
    l "Don't worry about it, Rosca. I know the drill."
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat with dissolve
    r "Good."
    r "Oberon just takes what's in their wallets, but I've got a reputation to keep."
    r "If he's going to play the brute, then I'm going to have to be a consummate professional."
    # $ r.switch_mood('tch hat 2')
    r "Like you said, I'm not as tough as I look, so fights are out of the question."
    r "Let's see. Should I check the facts again?"

    menu:
        "Better careful than sorry.":
            jump threattut
        "Nah, everything's in order.":
            jump threatbegin

label threattut:
    "It's {color=#f00}10:00 AM{/color} right now. Then I get a {color=#f00}1 hour{/color} lunch break at {color=#f00}12:00 PM{/color}."
    "Then after that, I have {color=#f00}4 hours{/color} left to work, before I have to report to Patrona at {color=#f00}5:00PM{/color}."
    "All in all, I have {color=#f00}6 hours{/color} to make the quota."
    "The time it takes to collect depends on how well I do my job."
    "If I make a mess, or if the mark's a troublesome ass, Leola's going to have to step in. That'll take {color=#f00}an hour{/color}."
    "If Leola takes care of them for me, they might comply... or get knocked out."
    "Oberon just takes what's in their wallets, but I've got a reputation to keep."
    "If he's going to play the brute, then I'm going to have to be a consummate professional."
    "I'm not much of a fighter, so brawls are out of the question."
    "And for today, I need to collect at least {color=#f00}3,000 credits{/color}."
    "Once more?"
    menu:
        "Huh, I should go over it again.":
            jump threattut
        "Nope, I'm ready.":
            jump threatbegin

label threatbegin:
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat with dissolve
    r "Well... nothing is going to happen if I just stand here."
    r "Who should I visit first? Better check the addresses."
    # Insert random addresses and names.
    # Insert game mechanic here.
    # Randomizer, patience bar, clock, etc.
    # Lunch break allows character to buy food and a lottery ticket (ex: coffee and cigarettes, etc.).
    "Minigame placeholder."
    menu:
        "C. Richards":
            jump extortion_richards
        "Iris":
            jump extortion_iris
        "Frank Okasaki":
            jump extortion_frankokasaki
        "Hatchet":
            jump extortion_hatchet

label extortion_richards_end:
    "Minigame ends."
    # when minigame ends, Rosca calls Leola
    # Show Leola's health
    # if Leola's health gets to less than 20% her relationship points with Rosca goes down
    stop music fadeout 1.0
    play music "audio/Upriver Funk.mp3"
    "Branch Placeholder: How much of Leola's health remains?"
    menu:
        "9 to 10":
            jump perfhealthday1
        "5 to 8":
            jump normhealthday1
        "0 to 4":
            jump badhealthday1

label perfhealthday1:
    scene arcade
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat at left
    show leola at right
    l "Damn, Rosca. You did pretty well today."
    l "Got me standing like a fool here, bored to all hell."
    r "I can't believe you. After all this, you're complaining?"
    l "Why do you always take things the wrong way? I was giving you a compliment."
    r "Can't help it, Leola. There's nothing right about you, cabróna."
    l "Is this how you treat the people who bust their ass for you?"
    r "Well, like you said yourself, it's not like you did much of anything."
    r "Patrona still pays you for your services, while I have to earn my keep every fucking day."
    l "Man... that {i}is{/i} tough."
    l "Hey, thanks for letting me tag along, kid."
    l "Y'know, the Boss pays me more when I'm escorting you."
    l "Maybe she's got her eye on you, Rosca."
    r "Of course she does. Who can resist this?"
    l "Sure thing, carrot-top. Your hair, it practically screams for attention."
    r "And yours fades into the background, like a washed up rag."
    r "By the way, Leola, carrots are orange, not red."
    l "Red, orange, black. It all looks the same to me."
    l "Besides, you've got to give me a break, Rosca. I can't compete with the hottest criminal in town."
    r "No mames, Leola! You're too careless with compliments."
    l "Why not? They're free."
    l "Unlike dinner."
    r "Hm? What do you mean?"
    l "Like I said, you owe me. C'mon, if you're free this evening-"
    r "That Cafe again? Jeez, Leola. You practically live there already."
    l "The best donuts in Veccio Palermo, and that's saying something. Tell me I'm wrong."
    r "Well... you're not wrong."
    r "I'll think about it."
    l "Great. Either way, you know where to find me."
    l "See ya."
    "She walked away at a leisurely pace."
    r "Good thing the marks were agreeable today. Managed to spare her from writing those bogus public security reports."
    stop music fadeout 1.0
    $ leola_route += 2
    jump visitbossday1

label normhealthday1:
    scene arcade
    # $ r.switch_mood('smug hat 1')
    show rosca smug hat at left
    show leola at right
    l "That wasn't so bad, hm?"
    l "Hey, thanks for letting me tag along, kid."
    l "Y'know, the Boss pays me more when I'm escorting you."
    l "Maybe she's got her eye on you, Rosca."
    r "Of course she does. Who can resist this?"
    l "Sure thing, carrot-top. Your hair, it practically screams for attention."
    r "And yours fades into the background, like a washed up rag."
    l "Aw, give me a break, Rosca. I can't compete with the hottest criminal in town."
    r "No mames, Leola! You're too careless with compliments."
    l "Why not? They're free."
    l "Unlike dinner."
    r "Hm? What do you mean?"
    l "Like I said, you owe me. C'mon, if you're free this evening-"
    r "That Cafe again? Jeez, Leola. You practically live there already."
    l "The best donuts in Veccio Palermo, and that's saying something. Tell me I'm wrong."
    r "Well... you're not wrong."
    r "I'll think about it."
    l "Great. Either way, you know where to find me."
    l "See ya."
    "She walked away at a brisk pace."
    r "Oh, I guess she still has to write those bogus public security reports."
    stop music fadeout 1.0
    $ leola_route += 1
    jump visitbossday1

label badhealthday1:
    scene arcade
    # $ r.switch_mood('surprise hat 2')
    show rosca surprise hat at left
    show leola at right
    l "Goddamn it Rosca, you sure have a way with words."
    l "Pissed all the marks off, and I think I'm getting pissed off at you, myself."
    l "At least Oberon could take the hits. I've got to take yours for you, and that's fine... but-"
    l "Don't sic 'em all at me!"
    l "Fuck, my body's going to be pretty sore tomorrow."
    r "I... really fucked up today."
    r "My bad, Leola."
    l "..."
    r "Look, I said I'm sorry."
    l "You're lucky you're cute-{nw}"
    r "What?"
    l "I said, you're lucky you're an Ace, else I'd remodel your face."
    l "I'm going home early to get some rest."
    r "Thanks for coming along, Leola. Really-"
    l "Yeah, yeah. Still pissed at you. Get your damn act together, Rosca."
    "She stalked off."
    r "Damn. Leola's going to be writing a fuckton of those bogus public security reports today..."
    r "Eres una pendeja, Rosca..."
    stop music fadeout 1.0
    # Lock out option to spend evening with Leola
    # Bad call Leola
    jump visitbossday1

label visitbossday1:
    r "Guess it's time to visit Patrona."
    scene mainstreet
    "I liked walking down the Streets after work."
    "Around the area, it was quiet enough for me to catch a breath, save for a few loitering deadbeats."
    "They knew enough about the Aces to stay far away from me."
    scene hq
    "And they knew enough about the Aces to stay the hell away from the big, black building right on Main Street."
    "Our headquarters."
    "It would make a fine tourist attraction... if Veccio Palermo had any visitors."
    "Patrona's office was at the Penthouse. A position of power and privilege."
    "We could tell when she was having a bad day-{w}she banned elevator access."
    "If we wanted to see her then, we had to take the stairs."
    "Fortunately, today was going well."
    "And unlike most Aces... {w}I had the keys to the elevator."
    scene hallway
    "I opened the door nice and easy, the way she liked it-"
    "And I shut it behind me with the same care."
    # door shutting sound?
    scene office
    play music "audio/Anthem.mp3"
    show rosca at left
    show nic at right
    nic "Rosca!"
    "Placeholder branch: Did Rosca finish on time?"
    menu:
        "Not late.":
            jump ontimeday1
        "Late":
            jump lateday1

label ontimeday1:
    "Patrona rose from her leather chair and leaned against her desk. She never liked to sit while talking."
    nic "Right on time! Excellent."
    r "Wouldn't dare to keep {i}you{/i} waiting, Patrona."
    nic "Good girl."
    nic "But between the both of us..."
    nic "I wouldn't mind winding the clock back, just for you."
    "Her lips closed around the cigarette as she smiled that sly smile I've seen far too often."
    "Other Aces might have left it at that, but I never let her off that easy."
    "Oh no, {i}claro que no{/i}."
    r "Ah, but by how much, Patrona? A second, a minute, an hour-"
    "She cut me off with a laugh."
    nic "Hm, that depends."
    nic "Show me what you've got...{w} then we'll talk."
    "Patrona's eyes left my gaze for only a moment, {i}but I knew where it went{/i}."
    r "Are we still talking about business, Patrona?"
    nic "Ah, but what else is there, Rosca? You tell me."
    "Like I was going to give in that easy."
    r "Oh, I guess it's nothing then."
    "That ember tip on her cigarette flashed as she took a sudden puff; stifled disappointment, perhaps?"
    nic "If you say so, doll."
    nic "Now, about that business-"
    r "Here, Patrona."
    "I showed her my work for the day."
    # Rosca shows credits.
    "Placeholder branch: Did Rosca meet the quota?"
    menu:
        "Yes":
            jump quotaokday1
        "No":
            jump quotanotokday1

label lateday1:
    "Patrona rose from her leather chair and leaned against her desk. She never liked to sit while talking."
    nic "You're late. You know how much I {i}hate{/i} waiting, Rosca."
    "If anything, Patrona was a real stickler for punctuality. She glared, eyes like daggers pointed at my face."
    "I would be lying if I said she didn't scare me."
    "But I would {i}never{/i} let her see that. {i}Nunca jamás{/i}."
    "Besides- {w}I had my ways."
    r "Oh Patrona..."
    r "What was that thing you always liked to say?"
    nic "I say a lot of things, doll. Don't make me guess."
    r "That one about... {w}good things being worth the wait."
    "Her cold stare lost its focus-"
    "Then, she laughed."
    nic "Hah! Now that's rich."
    nic "When did I ever say that? Besides-"
    nic "If you're good, then I'm a fucking saint."
    r "Saints are known for forgiveness, Patrona."
    nic "Oh, fine."
    nic "But I'll still have to punish you for making me worry-{nw}"
    "Nic coughed and glared at me."
    r "What did you say?"
    nic "Nothing."
    r "No, really, Patrona-"
    r "It's a bit difficult to understand you, when you've always got that cigarette between your lips."
    nic "If you didn't hear, then it's not important."
    "Oh I heard her, all right."
    "I just wanted her to say it, loud and clear."
    "But... some things can't be rushed, after all."
    nic "Anyway..."
    nic "I'm cutting some of your booze money."
    r "..."
    nic "Huh. Guess you're not much of a drinker."
    nic "Coffee money, then. And the smokes too."
    r "What?!"
    nic "Looks like I hit a nerve."
    r "Some saint you are, Patrona."
    nic "If you'll get on your knees, though..."
    r "You asking me to pray, or-"
    nic "Heh, Rosca. You tell me."
    "Like I was going to give in that easy."
    r "All that kneeling and praying is more trouble than it's worth. I'm not religious, Patrona."
    "That ember tip on her cigarette flashed as she took a sudden puff; stifled amusement, perhaps?"
    nic "Neither am I, doll."
    nic "Now, about that business-"
    r "Here, Patrona."
    "I showed her my work for the day."
    # Deduct 200 credits from accumulated amount.
    # Rosca shows credits.
    "Placeholder branch: Did Rosca meet the quota?"
    menu:
        "Yes":
            jump quotaokday1
        "No":
            jump quotanotokday1

label quotaokday1:
    "Placeholder branch: Did Rosca exceed quota?"
    menu:
        "Yes":
            jump quotaexceedday1
        "No":
            jump quotanormalday1

label quotaexceedday1:
    nic "I'm impressed."
    nic "You're really pulling your weight around here, Rosca."
    nic "I'm even starting to feel like I can trust you with my back."
    r "Are you sure about that, Patrona?"
    nic "It's a risk I'm willing to take, doll."
    nic "Maybe even give you a raise-"
    r "I..."
    r "What?"
    "It threw me off."
    "Did she actually... mean it? A la madre!"
    "I guess my hard work {i}was{/i} paying off."
    "Patrona peered at me and cocked her head, her half-smoked stick hanging precariously from her mouth."
    "I felt like {i}I{/i} was the stick."
    nic "Rosca."
    r "..."
    nic "Oi. Rosca!"
    r "S-si, Patrona!"
    nic "Hey, did you really earn all this?"
    nic "Look-it's like you just shut down all of a sudden."
    nic "For a smooth-talker... {w} you just dropped the ball, there."
    nic "I guess you're not ready for that raise, after all."
    "Then Patrona laughed."
    "Come mierda, I guess she was just teasing, after all."
    nic "Quit that face. Pathetic's not a good look for an Ace, Rosca."
    r "How about this, then?"
    nic "Perfect, doll."
    nic "Now... seeing as you did pretty damn well today..."
    nic "Hell-I'll admit it."
    nic "You've been doing pretty damn well for the past few months."
    $ nic_route += 1
    jump quotaday1cont


label quotaday1cont:
    nic "Anything in particular that I can do for you, Rosca?"
    r "How about-"
    r "Hmm..."
    nic "Within reason, Rosca."
    r "Hey, Patrona. That's not fair. {i}You haven't even heard my request yet{/i}."
    nic "Why are you taking so long, then?"
    r "It's not every day that your boss does you a favor."
    r "Hm."
    r "..."
    nic "..."
    nic "Rosca!"
    r "All right, I've got it!"
    nic "Out with it, then."
    r "I'd like a VIP pass to the Den. All-access, open bar, the works."
    nic "A special pass? We don't have those in the Den, doll."
    r "Don't be silly, Patrona. Of course you do."
    nic "Has someone been going around selling phony passes again?"
    nic "Give me a name... {w}{i}and I'll have their head on a fucking plate{/i}."
    nic "No refunds, though, if you were stupid enough to buy one."
    nic "It's about time you learned to be more careful with money."
    r "No, no, Patrona..."
    r "What I meant was..."
    r "I'd like you to take me there, yourself."
    nic "Hey now, that's a little-"
    r "Unreasonable?"
    nic "..."
    r "You know how the Aces give me a hard time."
    r "It's been ages since I've had a decent drink, too."
    r "If you're there to keep them at bay-"
    nic "I'll think about it."
    r "You'll {i}think{/i} about it?"
    r "Hey now-"
    r "This just might be the first time in a long time that someone's turned me down."
    r "I'm not sure I like it."
    nic "Consider it a learning experience."
    nic "You can't win 'em all."
    r "Eh, but I {i}hate{/i} losing."
    nic "C'mon, doll. You know how people talk."
    nic "If I'm seen with you, then-"
    r "Then what?"
    nic "They'll be thinking you're my plus one."
    r "Plus one? What're we talking about, Patrona-ledgers, or a night out?"
    nic "Do I have to spell it out, Rosca?"
    nic "They'll think I'm {i}seeing{/i} you."
    r "What's wrong with that? Let them talk."
    r "It's not like they ever said anything nice behind my back, anyway."
    r "Might give them something to think about, too, next time they open their damn mouths."
    nic "..."
    nic "Hm."
    r "Patrona. Please?"
    nic "Well... if it's you..."
    nic "Ah, what the hell."
    nic "I guess it's all right."
    nic "Maybe I can do something about all that hostility. What did you do to piss them off, anyway, Rosca?"
    nic "I mean, I can understand why they hate your brother, but you-"
    r "Hm?"
    nic "Well, you're pretty..."
    r "Ah!"
    "Dios mio-{w}has she finally opened her eyes?"
    nic "Likeable."
    r "Oh."
    "{i}A la madre con la Patrona.{/i}"
    nic "So. What did you do?"
    r "Patrona... some of my marks are Aces too, y'know."
    nic "Oh, right."
    nic "Well... tough luck, doll."
    r "Enough about that, though. Yes or no, Patrona?"
    "Stingy Nic gave me the smallest of nods-"
    "But a yes was a yes."
    nic "You can find me at the Den most evenings."
    nic "Give me a call when you get there, then I'll show you around."
    nic "You'll have to play the part though."
    r "What part?"
    nic "My plus one."
    r "You mean... your date?"
    nic "Don't push it, Rosca."
    r "All right, all right. That's easy enough."
    nic "You're a real piece of work, doll. Do you know what you're even getting into?"
    r "Why wouldn't I?"
    nic "Lots of snakes out there in the Den, Rosca."
    r "But you said you'd watch my back, Patrona."
    nic "When did I-"
    nic "Oh, all right. A favor is a favor."
    nic "And after all, it's just for a night."
    r "We'll see about that."
    "She leaned against her desk and started poking around the mess on her table."
    nic "Now get out of my office, will ya? Let me sign your paychecks in peace."
    r "Thanks. See you around, Patrona."
    nic "Yeah, yeah."
    $ nic_route += 1
    jump eveningday1

label quotanormalday1:
    nic "Not bad."
    nic "I guess you do deserve your paygrade."
    r "That and more, Patrona."
    r "Who knows what'll happen if you raise it?"
    nic "You've been doing pretty well in the Aces, Rosca..."
    nic "But let's not get ahead of ourselves. You're not {i}that{/i} good."
    r "Right..."
    nic "You've been doing pretty damn well though, for the past few months."
    jump quotaday1cont


label quotanotokday1:
    nic "This won't do, Rosca."
    # Sound of hand slamming on table.
    nic "You know why we wear all these fancy suits?"
    nic "It's because we run a business."
    nic "And a business that doesn't earn money is a piece of shit business."
    nic "You cost money too, y'know."
    nic "And so's your brother, running around doing god knows what, when he should be on the streets, making cred!"
    "She took a long drag on the cigarette, exhaling it in one quick sigh."
    nic "Fuck this."
    r "Sorry, Patrona. I-"
    "Her eyes flashed; I looked away. {i}I had to{/i}. If I didn't, I might have pissed myself."
    nic "Damn it, Rosca. Don't say useless things like {i}'sorry'{/i}."
    r "Tomorrow I'll-"
    "She cut me off with a click of the tongue. It might as well have been a pistol's hammer, primed to spark."
    nic "Listen, do me a favor. Just shut up and get the fuck out of my office."
    r "Si, Patrona. I'm really sor- I mean, it won't happen again!"
    "Her vicious eyes bored through mine."
    "I wasn't even sure if she was seeing {i}me{/i}, instead of the damn numbers in her head."
    "But she didn't move a muscle. That was as close to forgiveness as I was going to get."
    "All things considered, it could have been much, much worse."
    "I even knew some Aces who faced death for lesser failures."
    "That was the risk we all took, working for someone who dealt in lead and silver."
    "I hightailed it out of there before she decided to change her mind."
    # Lock out option to spend evening with Nic.
    # Bad call Nic
    jump eveningday1

label eveningday1:
    stop music fadeout 1.0
    scene black
    "After getting some groceries, I wandered back to the Headquarters and took a cat nap 'til the evening."
    "These days I could never sleep for long stretches anymore."
    "But I didn't mind. I liked the evenings. It was the only time when nothing was too noisy or bright."
    scene black
    r "Ah, night never comes fast enough."
    r "I guess I still have some free time."
    r "Pretty sure Leola’s over at the Cafe."
    r "That place might have the best pastries, but they also have, hands down, the {i}worst{/i} coffee."
    r "I owe her dinner… but donuts and coffee again? How she got so tall living on those things, it’s a mystery to me."
    r "Patrona's probably waiting at the Den."
    r "It’s a happenin’ place, the kind I never go to. And for good reason: I wouldn’t know what to do there except drink and hide."
    r "Damn Aces."
    r "But now that Patrona's got my back, I just might have a good time."
    r "Then again... I could just go straight home. I’ll be seeing them both tomorrow, anyway."
    menu:
        "Go to the Cafe.":
            jump leolaeve1
        "Visit the Den.":
            jump niceve1
        "Go home.":
            jump roscaeve1

label leolaeve1:
    # Day 1 evening with Leola.
    scene alley
    # $ l.switch_mood('smile 4 0')
    "The walk to the Cafe was long but uneventful. That old place was in the laziest part of the city."
    "Even the pickpockets here were slower than drunks. And the drunks here, well, they're the kind that lie down on the curb to wait for sunrise."
    "I guess that lent it a kind of peace."
    scene outcafe
    "Before I could even open the door, the heavy fragrance of freshly fried donuts hit me square in the gut."
    "And just like that, I was hungry."
    play music "audio/Off the Cuff.mp3"
    "A familiar face came up to open the door; Leola practically dragged me through it, then sat me down."
    scene incafe
    l "Get over here!"
    "The table was already occupied by a heaping plate of steaming donuts."
    # $ r.switch_mood('angry 5 3')
    r "Hija de puta. You couldn’t even wait until I got here?"
    l "Have mercy, Rosca. If I waited any longer, my stomach would have caved in."
    # $ r.switch_mood('nahh 5 0')
    r "That {i}thing{/i} is not a cave, Leola. It’s an abyss."
    # $ l.switch_mood('smug 4 0')
    l "Besides, it’s all on you today. Might as well take advantage of your kindness. Who knows when you’ll be this generous again?"
    # $ r.switch_mood('tch 2')
    r "We’ve been eating here every Sunday for the last three years. You, me and Oberon."
    "She rolled her eyes and bit into a donut."
    # $ l.switch_mood('thinking 2 0')
    l "Hey, you never know, kid. Maybe you’ll get your tongue in a knot then get done in by one of your debtors."
    l "Or maybe some punk Ace might forget I work for the Boss and plant a slug in my head."
    l "And there's Oberon-"
    # $ r.switch_mood('angry 5 3')
    r "Knock on wood, Leola!"
    "There was a glint in her eye as she dropped her donut and moved her hand towards me."
    # $ l.switch_mood('smile 4 0')
    l "Ha, you mean those?"
    "She was pointing to my chest."
    # $ l.switch_mood('smug 4 0')
    l "Might as well. Flat as a board."
    "They were {i}not{/i}. She just wanted an excuse to piss me off."
    "I slapped her hand away and bit savagely into a donut."
    "Always the same taste. Greasy, sweet and delicious."
    l "Hey, Rosca. You look like you just came or something. I thought you were tired of these."
    # $ r.switch_mood('smug 2')
    r "Ay, no mames, cabróna. Can we talk about something normal for once?"
    # $ l.switch_mood('smirk 5 0')
    l "Like the weather? Gee, what a lovely day for picking pockets."
    # $ r.switch_mood('heh 1 3')
    r "No! I mean, can't you talk to me like I'm a decent person?"
    # $ l.switch_mood('smile 4 0')
    l "Not if you keep looking like {i}that{/i}."
    # $ r.switch_mood('heynow 3')
    r "You're hopeless! I might as well be talking to a wall."
    "I raised my voice; no one looked at us twice. We've been here so long that our voices were part of the music."
    # $ l.switch_mood('smug 4 0')
    l "Simmer down, Rosca! Such a hothead. How does Oberon survive living with you?"
    # $ r.switch_mood('tch 1')
    r "He’s a lot smarter than you, for sure. At least Oberon doesn’t go around pissing people off with-"
    # $ r.switch_mood('tsktsk 1')
    r "Oh wait, he does."
    r "Huh. I see now. Come to think of it..."
    # $ r.switch_mood('cheeky 1')
    r "You and Oberon aren’t so different, after all."
    # $ l.switch_mood('noway 2 0')
    l "Yeah, sure! Like night and day, you mean."
    # $ r.switch_mood('tch 2')
    r "Two words. Violence and food. I can't think of anything else you guys live for."
    # $ l.switch_mood('disagree 2 0')
    l "If you think I'm anything like him, you don't know me at all."
    # $ r.switch_mood('cheeky 1')
    r "Hah, I can read you like a book. Try me."
    # $ l.switch_mood('smug 4 0')
    l "Fine!"
    # $ l.switch_mood('smile 4 0')
    l "Let's sweeten the deal though. How about a bet?"
    r "Sure. You'll regret it."
    # $ l.switch_mood('smug 4 0')
    l "If you get everything right-"
    # $ r.switch_mood('oi 2')
    r "Everything? That's not fair."
    # $ l.switch_mood('thinking 2 0')
    l "You said you could read me like a book. I think that's fair enough, kid."
    # $ l.switch_mood('smirk 5 0')
    l "Or you could just admit defeat."
    # $ r.switch_mood('oi 1')
    r "Well, what do I get if I win?"
    # $ l.switch_mood('smile 4 0')
    l "Anything you want."
    # $ r.switch_mood('smug 2')
    r "Now {i}that{/i} just has bullshit written all over it."
    # $ l.switch_mood('noway 2 0')
    l "I'm serious."
    # $ r.switch_mood('tch 2')
    r "Whatever. What if I get it wrong, though?"
    # $ l.switch_mood('smirk 5 0')
    l "You've got to-{nw}"
    # $ r.switch_mood('nahh 5 0')
    r "No, I am not getting into bed with you. Not for free, at least."
    # $ l.switch_mood('smile 4 0')
    l "How much?"
    # $ r.switch_mood('heh 1 3')
    r "Give or take, 6,000 credits."
    # $ l.switch_mood('disagree 2 0')
    l "Ah, jeez, Rosca! Give me a break."
    # $ r.switch_mood('smug 2')
    r "You can't afford me, can you?"
    # $ l.switch_mood('cross 2 0')
    l "For that kind of price, I could get three other girls, instead of just one."
    # $ r.switch_mood('angry 5 3')
    r "Hija de puta. Are you serious?"
    play sound "audio/punch.wav"
    $ l.switch_mood('noway 2 0')
    l "Ow, fuck! I was just joking..."
    l "You're scary when you're jealous."
    # $ r.switch_mood('nahh 5 0')
    r "{i}Jealous?{/i} Don't be stupid, Leola. Can we get back to the fucking game?"
    # $ l.switch_mood('smile 4 0')
    l "Heh. Boy, do you have a temper."
    # $ l.switch_mood('smug 4 0')
    l "As I was saying... if I win, then..."
    "Her eyes roved around the room, searching for something I couldn't see."
    "Or maybe she was trying to avoid my eyes?"
    "I stared her down."
    # $ l.switch_mood('smirk 5 0')
    l "I've got it!"
    r "All right, let's hear it."
    # $ l.switch_mood('smile 4 0')
    l "If I win, I get to walk you home."
    # $ r.switch_mood('tsktsk 1')
    r "Are you serious?"
    r "Well, that's a pretty cheap prize. I mean, don't you do that already?"
    # $ l.switch_mood('thinking 2 0')
    l "Yeah, but Oberon's always hanging around you. He's not here today, so I might as well take the chance, right?"
    # $ r.switch_mood('oi 2')
    r "A chance on what? That's a pretty stupid prize, if you ask me. I'll give you a chance to reconsider."
    # $ l.switch_mood('smug 4 0')
    l "Don't tell me what I want, kid."
    # $ r.switch_mood('cheeky 1')
    r "Fine then. You can walk me home."
    # $ l.switch_mood('smile 4 0')
    l "Great!"
    l "Ok, first question."
    l "What's my favorite color?"
    r "..."
    "Puta! {i}I don't have a clue{/i}."
    "...it's not like her clothes have any colors."
    menu:
        "Green.":
            jump green
        "Red.":
            jump red
        "Neither.":
            jump colorblind

label green:
    l "Nope. What gave you that idea?"
    r "Your eyes."
    l "Huh. Sometimes I even forget that it's green."
    l "Then again, it all looks the same to me."
    jump loseleoladay1

label red:
    l "Nope. What gave you that idea?"
    r "Red's a great color."
    l "I guess it looks great on you."
    l "Then again, it all looks the same to me."
    jump loseleoladay1

label colorblind:
    r "Do you really have a favorite color?"
    r "I mean... you're colorblind."
    l "...I'm surprised you remembered."
    r "That's one."
    l "Two more."
    jump q2

label q2:
    l "What's my last name?"
    "Easy. I could see her badge from here-"
    l "No cheatin', kid."
    "She blocked the badge from view."
    "I'm pretty sure it was something like a color..."
    menu:
        "Weiss.":
            jump weiss
        "Carmine.":
            jump carmine
        "Ivermann.":
            jump ivermann

label weiss:
    l "Wow. You'd think a criminal would remember the first cop who arrested her."
    r "Maybe I {i}want{/i} to forget."
    jump loseleoladay1

label ivermann:
    l "Wow. You'd think a criminal would remember the first cop who arrested her."
    r "Maybe I {i}want{/i} to forget."
    jump loseleoladay1

label carmine:
    r "How could I forget the first damn cop who arrested me."
    l "Lucky for you that I'm a friend of Nic's."
    r "Friend?"
    l "Yeah... We used to be-{nw}"
    l "You know what? Fine. Employee."
    r "{i}What?{/i} {i}You{/i} were {i}friends{/i} with Patrona?"
    l "Listen..."
    l "The Boss doesn't have friends, kid. Just people who pretend to be, because they're scared of her."
    r "I'm halfway to being Patrona, then."
    l "Hey, I'm still your friend, remember?"
    r "Yeah, yeah. Maybe you're the obstacle to my success."
    r "Well, that's two."
    l "Don't get cocky."
    l "Still got one more."
    l "What's my zodiac sign?"
    r "Hah, Leola!"
    r "This sounds an awful lot like those personal ads."
    l "Just shut up and answer the question."
    r "{i}You're going to regret this{/i}."
    # Rosca looks smug (if expression is available?)
    "Judging by her personality, it's got to be..."
    menu:
        "Gemini":
            jump gemeni
        "Leo":
            jump leo
        "Taurus":
            jump taurus

label gemeni:
    l "What? You think I'm a two-faced coward, or something?"
    r "I don't know. You're pretty adaptable."
    l "Only because you're so damn manipulative."
    r "It's called {i}charm{/i}."
    l "Pfft. Whatever."
    l "Maybe you're not as good at reading people as you think you are."
    jump loseleoladay1


label leo:
    l "What? You think I'm a narcissist, or something?"
    r "No... but you're damn stubborn, cabróna."
    l "It's called {i}determination{/i}."
    r "More nonsense coming out of your mouth, as always."
    l "Pfft. Whatever."
    l "Maybe you're not as good at reading people as you think you are."
    jump loseleoladay1

label taurus:
    l "Wow, what gave it away?"
    r "Two words."
    r "Big eater."
    r "Also, stubborn as hell."
    l "Heh, you're-{nw}"
    r "You're also pretty lazy, now that I think about it."
    r "Sleeping on the job, sometimes..."
    r "Do you even help people cross the street?"
    l "Ok, that's enough."
    l "And why would I help people cross the street?"
    r "Isn't that what cops do?"
    l "I'm a fucking Inspector, Rosca."
    r "So? You're a heartless bitch, Leola. At least respect the elderly."
    l "What are you going on about?"
    l "Besides. You didn't even talk about the good stuff."
    r "Like what?"
    l "Well... Tauruses are loyal! Independent! Uninhibited in the bed-{nw}"
    r "CÁLLATE!"
    "I took a donut and stuffed it in her big, noisy mouth. It disappeared quickly though."
    r "Zodiac signs are bullshit, anyway."
    jump winleoladay1

label loseleoladay1:
    l "Heh. You lose!"
    l "Though... I'm not sure I should be happy about that."
    l "I guess you don't know me at all."
    r "Don't be stupid, cabróna. Those things don't count for shit."
    r "How about information like your blood type? Or the location of your safehouse?"
    r "Who cares about their favorite color when they're bleedin' out on the curb?"
    l "But Rosca..."
    l "You told me to talk to you like you were a decent person."
    l "They don't know squat about things like that, kid."
    r "...Damn. You've got a point there."
    r "I guess I'm a bad girl, through and through."
    l "You're not {i}that{/i} bad."
    "She grinned at me, real sunny-like."
    "Damn, even if this woman beats the shit out of people..."
    "Really... Leola's a fucking child. Somehow, she's still {i}all right{/i} inside."
    "It's a bit dazzling, almost."
    "At least until she wiped her mouth with the back of her hand."
    "I waited for her as she finished the rest of the donuts. No leftovers."
    "She drank the awful coffee in one big gulp and stood up like a jackknife."
    "Over here, I struggled to leave the table; it still felt like I just ate bricks for dinner."
    jump getout

label getout:
    l "Hey, I think it's about time we got out of here."
    "She grabbed hold of my wrist and began to pull me out of the Cafe."
    r "Hold on- Leola, the bill!"
    l "Let's make a run for it! Three, two, one-"
    scene darkstreet
    "With me in tow, she tugged me down the street like a mad dog. I ran like hell too, and hell ain't a pleasant thing to behold."
    r "Hah- puta-"
    l "Hahaha!"
    "After what seemed like an eternity, we finally ground to a halt somewhere near the Arcade."
    r "Hahh-"
    r "You... fucking... idiot!"
    l "Stop smoking, kid. It's really bad for your endurance."
    r "Why'd you piss 'em off? Shit... now we have to go find some other place to hang out."
    l "Don't worry about it."
    r "What?"
    l "..."
    "Her mouth twitched as she fought to keep back a laugh."
    l "I already paid for everything before you got there."
    r "What."
    r "You made me run {w}THE WHOLE FUCKING WAY {w}just for NOTHING?"
    r "..."
    "I didn't even have the energy to hit her. She kept on talking as I tried to remember how to breathe."
    l "Hey, I got a bonus today. Thought it would be worthwhile to spend some of it to see you smile."
    l "I know you're worried about Oberon."
    l "But I'm watching his back, too."
    "She was still holding me, all the while. I'd almost forgotten."
    "The warmth of her fingers moved from my wrist, and into my palm."
    "Leola held my hand."
    "I let my fingers hang limp, frozen by indecision."
    "Before I could hold her tight, she let go."
    "I had to meet her halfway, somehow-"
    "To say that this was ok-"
    "That we weren't breaking any rules."
    "I caught her arm, holding it hostage."
    l "Ack! Rosca, you're hurtin' me."
    r "Quit whining and carry me already."
    l "What?"
    r "You owe me that much, you crazy bitch. I could have died, running all the way here!"
    l "Fair enough."
    # Show special event CG of Leola carrying Rosca
    "With one smooth motion, she lifted me into her arms. To be honest, I wasn't expecting her to do anything."
    "But Leola was stronger than I expected. And more obedient, too."
    r "Thanks."
    l "No worries. You can rest easy now."
    r "Take me home. You know where the keys are."
    l "Heh. That sounds like an indecent proposal."
    r "Ha! You're too much of a pussy to actually {i}do{/i} anything about it, anyway."
    l "Hey now, don't call me that!"
    r "A big fucking pussy? That?"
    l "Stop it! Next time, I'll bring some soap to wash that filthy mouth of yours, kid."
    r "Whatever. Quit dodging the fucking bullet, cabróna."
    r "If you aren't one, prove it."
    stop music
    r "Kiss me."
    "We both froze. Maybe hell froze over, too."
    "{i}I didn't mean to say it{/i}. The words just flew right out of my mouth."
    l "...huh?"
    "Her arms stiffened, bracing against some invisible weight, as if I grew a thousand times heavier in that split second."
    "But I couldn't bring myself to stop there."
    "So I closed my eyes, waiting for her to lay one on me."
    scene black
    "Leola stood still for so long, I was worried she was going to drop me."
    "But she didn't-"
    play music "audio/Blanc.mp3"
    "Instead, she kissed me."
    "Leola kissed me so softly, our lips barely touched."
    "I could tell that she wanted more."
    "I could tell, because of how slowly she pulled away-"
    "This was how it was with Leola..."
    "But- {w}was this how it should always be?"
    scene darkstreet
    r "WHY DID YOU DO THAT?"
    l "Hell... even I'm still asking myself that question."
    l "But, well-"
    l "You told me to!"
    "Her face was flushed and she could barely look me in the eyes."
    "Leola's eyes-"
    "They glowed like distant fireflies, lost in the night."
    r "..."
    r "This doesn't mean anything, does it?"
    "Her lips moved and I could see it-"
    "A worn smile, outlined by that warm, green light."
    "She knew what she had to say."
    l "Not a damn thing, kid."
    l "Just one of your stupid dares."
    r "So... {w}we're clear."
    l "Crystal."
    r "...{w}I still think you're a pussy though."
    l "Wha- Don't call me that!"
    r "Ha, you call that a kiss, cabróna?"
    l "Want me to try again?"
    "{i}Yes. {w}No. {w}{b}I don't know{/b}.{/i}"
    "I laughed and turned away."
    "I {i}had{/i} to. For the first time, I couldn't look her in the eyes."
    "It scared me..."
    "That I was starting to take the fucking joke to heart."
    r "Leola, please... just take me home."
    l "All right."
    scene black
    "I should have climbed off her arms that night... and gone home alone."
    "Instead, I closed my eyes and pretended to fall asleep in her arms, like the damn fool I was."
    scene inapartment
    "Leola tucked me into bed and left me well enough to myself."
    "But I couldn't sleep-"
    "My mind raced with thoughts about what would have happened if she stayed for the night."
    "I didn't get much rest, that damned evening."
    stop music fadeout 1.0
    # Leola RV + 2
    jump day2

label winleoladay1:
    l "Damn it. You win."
    l "Though... I can't say I'm not happy."
    l "I guess you {i}can{/i} read me like a book."
    l "I don't mind. I've got nothing to hide."
    "She grinned at me, real sunny-like."
    "Damn, even if this woman beats the shit out of people..."
    "Really... Leola's a fucking child. Somehow, she's still {i}all right{/i} inside."
    "It's a bit dazzling, almost."
    "At least until she wiped her mouth with the back of her hand."
    l "Ok, you've got me. What do you want?"
    r "I'll save that win. Never know when it'll come in handy."
    l "Wha- That's really boring."
    r "Or practical. You never specified the terms of agreement."
    l "Well, I guess that's fair."
    l "All right, Rosca. One I.O.U. It's a deal."
    l "Put it 'ere!"
    "Leola shook my hand with a firm grip. Her palm was surprisingly soft, for someone who pounded skulls for a living."
    r "There. Agreed."
    l "Great!"
    # Leola RV +1 (also has effect on ending)
    jump getout

label niceve1:
    # Day 1 evening with Nic.
    # Play ambient city noise. Loud people etc.
    "I headed on to the Den."
    "The streets grew narrower with each step, and the shadows, thicker."
    "It took me a few dead ends to remember the right turns to take, but I found my way."
    "I just had to follow the trail of broken glass, crumpled beer cans..."
    play music "audio/Halftime Tango.mp3"
    "And of course, the music."
    "The Den was located downtown, where all the bars and bistros were."
    "It's a sanctuary of sorts for the Black Aces."
    "The Aces were a wild crowd, it went without saying."
    "Live weapons were allowed inside the establishment, because it made everyone feel {i}safer{/i}."
    "If someone were stupid enough to fire a shot though... I don't think anyone would survive."
    "A fucking bloodbath waiting to happen, really."
    "Somehow, Patrona kept the peace."
    "She's the only reason I can think of to explain why no one's died in there. {w}Yet."
    "Most Aces had some kind of pedigree. Connections. Resources."
    "They were a pack of stuck-up putos who wouldn't talk to anyone that didn't look like they could mooch a drink off of."
    "Tough luck for us, Oberon and I-"
    "We moved into the city with nothing but the devil's luck and the shirts on our backs."
    "After spending the day with angry marks, the last thing I wanted to do was to rub elbows with with snobs and fuckers."
    "It didn't help that some of the Aces {i}used to be marks{/i}."
    "But, after a hard day..."
    "The one thing I really needed was a good, old fashioned drink."
    "Patrona seemed to like us though. I often wondered why."
    "Then again, trying to understand Patrona was about as useful as trying to see in the dark."
    "It was much easier to please her instead."
    "I passed the low entrance and flashed my card over the scanner."
    play sound "audio/bleephi.wav"
    nic "Hey, Rosca. I {i}knew{/i} you'd be here."
    nic "I told you to call {i}first{/i}."
    r "W-whoa-"
    "I nearly pissed myself."
    r "Evening, Patrona."
    "She peered at me and frowned."
    nic "Rosca... you all right? You're looking a little pale."
    r "How long have you been standing there, Patrona?"
    nic "I followed you all the way from the Arcade, actually."
    r "What?!"
    nic "Yeah. You didn't notice?"
    nic "Give me a break. You've got to be kidding, right?"
    nic "I mean, you were walking into all those dead ends just to throw me off."
    nic "But I don't give up easy, heh."
    r "..."
    nic "Oh no, you're serious..."
    nic "{i}How are you still alive right now{/i}?"
    nic "Leola sure has her work cut out for her. I guess that bitch deserves her fees after all."
    r "You know... {i}the bitch{/i} you're referring to saved my ass more than once."
    nic "Good. {i}That's what I pay her to do{/i}."
    r "Patrona, she-{nw}"
    nic "Yeah, yeah. Enough about her."
    "Was that... jealousy I was hearing?"
    "I couldn't understand why... but it thrilled me to hear that rasp of jealousy in Nic's voice-"
    "Or was she just pretending?"
    "I tried to care, but the difference didn't matter much to me."
    nic "I'd rather hear you talk about yourself, doll."
    nic "And call me Nic. It's after hours."
    nic "Unless this is some cheap trick to get me to pay you overtime, hm?"
    r "Just show me where the bar is, and we're good, Nic."
    nic "A straight shooter. I like that about you."
    nic "Let's get you a drink, shall we?"
    "I felt an arm wrap around my waist. It was Patrona's arm-"
    nic "Remember. We've got to look the part."
    r "Jeez, Nic. It's not {i}that{/i} hard."
    "Maybe the reminder was more for herself, than for me."
    "Nic paused to light her cigarette."
    "As soon as she put it on her lips, someone lit it for her, no questions asked."
    "I realized that a throng of people had gathered around us."
    "We were blocking the door, after all."
    "But no one dared to ask Patrona to step aside."
    nic "Hey now, doll. Take a look at that."
    "With a jerk of her head, she pointed at someone in the crowd."
    nic "See? She's definitely got it bad for you."
    "I searched the shadowy sea of faces."
    "True enough-"
    "A pair of eyes connected with mine, staring at me, holding my gaze a little too long."
    "I was surprised that Nic had a knack for spotting things like that-"
    "When she couldn't see all the signs I was throwing her way."
    nic "That girl's a real piece of work, hm?"
    nic "Flirting with her Boss' date. Practically {i}suicidal{/i}."
    r "You sound like you're going to issue a hit on her."
    "Nic smiled at the woman in question."
    "{i}That{/i} was enough to send {i}her{/i} walking briskly towards the exit."
    r "She can't help it, Nic. It's not her fault that you've got a hot date."
    r "Tell me you won't... {w}you won't actually hurt her, right?"
    "Nic only smiled back. Always, that big, sly grin."
    nic "..."
    "She laughed and leaned close, stopping short of nuzzling my cheek."
    "Nic only whispered, but from the sides, it probably looked like something else."
    nic "What do you think I am?"
    nic "Some crook?"
    r "Hah!"
    "A few Aces started staring. Pointing, even."
    "I could hear the low murmur of questions they were asking among themselves."
    "{i}Just who the hell is this red-head, cozying up to the Boss?{/i}"
    "{i}Troublesome bitch. What was her name again?{/i}"
    "{i}What's the Boss doing, bringing the fucking leech here?{/i}"
    "Pinned under their gaze, I could feel my face grow warm, {i}puta madre{/i}."
    r "Ah-"
    nic "Don't worry about it."
    "Nic held me closer and turned to the Aces."
    nic "I'd hate to inconvenience the lot of you, folks..."
    nic "So if any of you fuckers have a problem with Rosca here-"
    nic "Someone better speak up now, so we can find elsewhere to spend the evening."
    "The crowd fell silent. Apparently, no one thought today was a good day to die."
    nic "I thought so."
    "Nic shrugged and smiled at me."
    nic "Relax."
    r "Look at them. They're shanking me with their eyes."
    nic "I won't let them fuck you around, Rosca."
    r "You better not."
    nic "Ah, forget about them. Let's go get you that drink."
    "The room was filled with smoke-my fingers itched to light one up for myself."
    play sound "<loop 1.0>audio/barambience.mp3"
    "We finally made it to the bar, pushing past a crowd."
    "Nic leapt over the bar table, somehow managing that without knocking any of the glasses off."
    nic "Let me make one for you myself."
    r "I didn't know you made your own drinks, Nic."
    nic "Look. I'm a kingpin, not a princess."
    nic "I'm not above making my own drinks. They taste better, too."
    nic "But enough about that."
    nic "Here's the menu."
    "She handed me a worn down piece of paper; a few drinks caught my eye."
    r "Let's see... I'll have one-"
    menu:
        "Bloody Murder.":
            jump notastebm
        "Black Widow.":
            jump notastebw
        "Glass of milk":
            jump notastem

label notastebm:
    nic "That's the worst thing off the menu. You don't want to drink {i}that{/i}."
    nic "It's called {i}Bloody Murder{/i} for a reason."
    r "And what reason is that?"
    nic "Because it cuts like a knife down the throat and leaves you broken in the morning."
    r "{i}Why{/i} is that even on the menu?"
    nic "Some people want to be broken. If that's their idea of a good time, I won't hold them back."
    "Now {i}there{/i} was an opening, if I ever saw one."
    r "Well... what if it's my idea of a good time?"
    "Her eyes lit up at those words. Who knows what images were running through her head at the moment?"
    "I wonder... if they were the same as mine?"
    "Judging by the way she leaned closer, I'd say yes."
    nic "So... you like bein' broken?"
    menu:
        "I already am.":
            jump holdthatthought
        "Only if you're doing the breaking.":
            jump holdthatthought

label holdthatthought:
    "Before I could reply, she held a finger up to my lips."
    nic "On second thought..."
    nic "I think it's better to leave that a mystery, hm?"
    nic "I'd rather find out without you tellin' me."
    nic "Oh, and about that drink..."
    play sound "audio/martinishake.wav"
    "Nic turned away from me and began to make a cocktail."
    "She chose the bottles with abandon, barely looking at the labels, as if she already knew where everything was from years of practice."
    play sound "audio/icesound.wav"
    "Finally, she returned to me and set her creation on the table."
    nic "Here, try this instead."
    jump sapphire

label notastebw:
    nic "You've got a tacky taste in liquor, Rosca."
    nic "The only people who drink Black Widows are old, toothless fuckers without a thought left in their heads."
    r "It sounds like you have a specific fucker in mind."
    nic "My old man. He made it for himself all the time."
    "Sometimes, it's hard to believe that Patrona ever was a child."
    nic "Got his mind numb enough that one day he decided to shoot himself in the face-"
    nic "With me as an audience of one."
    "I didn't quite know what to say to that."
    r "..."
    r "Damn, Nic. I-"
    nic "You're sorry? I already told you not to say useless shit like that."
    r "..."
    nic "And don't worry. He's alive and well, somewhere."
    nic "The fucking gun wasn't loaded."
    "She laughed."
    nic "Still want to drink a Black Widow?"
    r "{i}Why{/i} is that even on the menu?"
    nic "Some people will do anything to forget the past. If that's their idea of a good time, I'm not holding them back."
    r "Huh... what if that's my idea of a good time?"
    "She laughed at me."
    nic "Really, Rosca. You're only twenty-three. You barely {i}have{/i} a past."
    nic "What is it that you want so badly to forget?"
    r "I..."
    menu:
        "I want to forget some of the things I've done for the Aces.":
            jump holdthatthought
        "Actually, it's not just the past... Fuck tomorrows, too.":
            jump holdthatthought

label notastem:
    "She narrowed her eyes at me and snatched the menu away."
    nic "That's not on the list."
    r "Yeah, I know. But I want one, Nic."
    nic "You think I'm going to let your first drink with me in the Den be a glass of fuckin' milk?"
    nic "{i}Over my dead body.{/i}"
    r "It was a joke..."
    nic "You've got a poor taste in jokes, too."
    "Oh, now {i}there{/i} was an opening, if I ever saw one."
    r "Fine then. You got a better one, Nic?"
    nic "Huh? What do you mean?"
    r "Tell me a joke."
    nic "You puttin' me on the spot, hm?"
    r "It's only that if you're feeling the pressure."
    nic "No sweat."
    nic "Ok. Here it is."
    nic "What do the Aces... {w}and a pussy... {w}have in common?"
    r "No offense, Nic..."
    r "But is {i}that{/i} all you ever think about?"
    nic "Of course not. What gave you that impression?"
    r "Well... people talk. And isn't everyone interested in, well-"
    nic "Stop right there, Rosca."
    nic "Listen. I've got three things to say to ya."
    nic "First-"
    nic "By everyone, I think you mean {i}yourself{/i}."
    nic "Second: don't believe everything you hear."
    nic "I don't know what you think I do, exactly-"
    nic "Well... you're better off not knowing, really."
    nic "But you don't become the Boss by fucking around..."
    r "What, literally, or-"
    "She cut me off with a glare."
    nic "Third-"
    nic "Well..."
    nic "Congratulations."
    r "Eh? What for?"
    nic "You just killed the damn punchline."
    r "Ah..."
    r "..."
    r "A la madre, what was the joke again?"
    nic "Some date you are."
    nic "What do the Aces... {w}and a pussy... {w}have in common?"
    r "Damn... I don't even know what kind of answer to give you."
    "Nic stuck out her tongue."
    "I still didn't get it."
    nic "That's all it takes to get into deep shit, doll."
    r "What?"
    nic "A slip of the tongue."
    "It took a moment for me to piece it together."
    r "Oh."
    r "Damn.{w} Hahaha!"
    r "Are you speaking from experience, Nic?"
    nic "Not answering that question, Rosca."
    nic "Now, how's about we shut you up with something good to drink?"
    play sound "audio/martinishake.wav"
    "Nic turned away from me and began to make a cocktail."
    "She chose the bottles with abandon, barely looking at the labels, as if she already knew where everything was from years of practice."
    play sound "audio/icesound.wav"
    "Finally, she returned to me, and set her creation on the table."
    nic "Here, try this instead."
    jump sapphire

label sapphire:
    show juice
    "On the bartop was a thin glass filled with what looked to me like molten sapphire."
    "It was almost too beautiful to drink."
    "I never imagined the Boss of the Black Aces could make something as delicate as this."
    hide juice
    r "Wow... Jeez, Nic. That's a work of art."
    nic "So are you, doll."
    "She threw me a cheeky grin."
    "I rolled my eyes."
    "Can't have her thinking I was {i}too{/i} easy."
    r "So... what's this one called?"
    nic "It doesn't have a name yet. Made it on the fly."
    nic "Well, aren't you going to take a sip?"
    menu:
        "Drink it.":
            jump drinkit
        "Don't drink it.":
            jump nodrink

label drinkit:
    "The sip I took turned into a swig. It was the most refreshing drink I've ever had."
    "My lips tingled with a strange warmth-"
    "And my tongue..."
    "Ah. Delicious. {w}{i}Almost like a drunk lover's kiss{i}."
    nic "Not bad, hm?"
    r "Damn, Nic. After this, how do you expect me to go back to drinking water..."
    r "{i}Just what did you put in this thing?{/i}"
    nic "That's a secret."
    nic "Did you like it?"
    r "Fuck yeah."
    nic "Of course you did."
    nic "Hm, I think I'll call it... Rosca's Juice."
    nic "Made it just for you. You should feel honored."
    r "What?!"
    r "That sounds kind of-"
    r "Heh, if you know what I mean..."
    nic "Oh I do, doll... {w}but that's not what {i}I{/i} mean."
    r "What? C'mon Nic... You told me to play the part."
    r "I can't do it all by myself."
    nic "I think you're having too much fun, is all."
    nic "So, what do you really think of the name?"
    r "How about Boss' Juice?"
    r "I'd like a taste of {i}that{/i}."
    nic "Talk about sucking up to the boss."
    nic "That's not how I roll, though."
    r "I find that hard to believe."
    nic "Hush, now."
    "She touched my jaw with a finger, trailing it along the edge."
    "I gasped, shivering."
    r "Mierda, Nic! Your hands are cold!"
    "{i}That{/i} wasn't why {i}I{/i} shivered, though."
    nic "Well, yeah... that's what happens when you touch ice."
    "I slipped out of her grasp and caught her hand."
    "Her eyes widened in surprise, and that sly smile of hers only grew."
    "She laughed, {i}really laughed{/i}, for the first time that evening."
    "I... don't think I've ever heard her laugh like that before."
    "I wanted to make sure it happened more often from now on."
    r "I'm not sure if that's all you want, Nic."
    nic "It really is, doll. I so solemnly swear."
    r "I don't believe you."
    nic "It's the truth. You better believe it."
    "She raised the shaker."
    nic "Want more of the same?"
    r "I won't say no."
    r "Could you consider changing the drink's name, though?"
    nic "It depends. Give me one good reason."
    r "It's embarrassing."
    nic "And why's that?"
    r "...it makes me feel like I'm on the goddamn menu."
    nic "Well, shit. You know I {i}hate{/i} sharing."
    nic "But... if that's what it takes to see your face around here more often-"
    nic "Then yes. You're on the menu."
    jump bangbang

label nodrink:
    nic "Are you shittin' me?"
    "All things considered, she almost looked shocked that I was turning her offer down."
    r "No, but-{nw}"
    nic "Just taste it, Rosca. Best decision of your life, I promise."
    "Well, it's not like I could say no to her, anyway."
    menu:
        "Just drink it.":
            jump drinkit

label bangbang:
    play sound "audio/martinishake.wav"
    play sound "audio/icesound.wav"
    "She made herself the same drink, except in red."
    "I'm pretty sure I knew what she meant by {i}that{/i}."
    "At least, I wanted to believe that's what she meant."
    "We drank in silence, taking in the atmosphere. Nic threw me a smile every now and then."
    "Despite all odds, I was {i}actually{/i} having a good time."
    "Of course, Patrona couldn't stay with me the whole evening."
    "It wasn't long before a pack of Aces stole her from me, taking her to the far end of the room."
    "I could hear them talk, though I wasn't too sure what they were talking about."
    "Sometimes, it sounded like a heated argument was taking place. But then they would laugh."
    "Nic's grin though-it looked strained."
    "I wanted to save her from those awful bores-"
    "But I couldn't just jump in without an invite. I saw the way they all looked at me. And I didn't want to embarrass Patrona."
    "Once in a while, her glance would fall my way from afar, and she would throw me a wink, or a smile."
    "I didn't know how many drinks I'd had... while I waited-"
    "I was starting to see double when she finally made her way back to me."
    nic "Rosca."
    r "..."
    nic "C'mon now. I think you've had about enough."
    r "Some date you are."
    nic "Hm?"
    r "You know, if you leave me out here too long, that woman just might come back and snatch me up."
    "I saw her eyes scan the room for the briefest moment."
    nic "She should be long gone by now."
    nic "'sides, do you really want a woman who backs down at a threat?"
    r "Well, I wouldn't mind that so long as she kept me company, Nic."
    r "If I wanted to get drunk by myself, I would have stayed home."
    nic "You're going to have to let that slide, Rosca."
    nic "Maybe it doesn't look like it... but this is still work, doll."
    nic "Keeping everyone happy isn't easy."
    r "You call that an excuse? Not good enough, Nic."
    r "Everyone includes {i}me{/i}, you know."
    "I tried to lean on her shoulder, but all I managed to do was slip out of the barstool-"
    r "Shit-!"
    "Nic caught me just in time, though."
    nic "Damn."
    nic "You're a mess, Rosca."
    r "Just so you know, this is all your fault."
    nic "Maybe I should just take you home... before you fall asleep on me."
    nic "Hold on. Let me get the car-"
    "Nic began to walk to the door."
    r "{i}Let me get the car-{/i}"
    r "A la madre, Nic."
    "And just like that, I was alone again."
    "I entertained myself by watching the faces in the shadowy room."
    "I've been working for the Aces three years now... but I still didn't know any of them."
    "Not that I cared. A pack of putos. Fuckers, all of them."
    "But then-"
    "I recognized one."
    "It was {i}that{/i} woman, coming around."
    "Her face-I couldn't really see too well, on account of all the drinks I've had."
    "I was willing to bet she was gorgeous, though-"
    "So, I grinned at her. Nic was taking her sweet time, anyway."
    "I {i}think{/i} she smiled back."
    r "Hey Nic! Look who's here."
    "Nothing like a little competition to spur her on."
    "She stopped dead in her tracks and glanced back at me."
    r "Ha! Made you look-"
    # eye closeup?
    "Ah-"
    "{i}Then{/i} Nic started running in my direction."
    "{i}Really running.{/i}"
    "If she's always wanted me {i}that{/i} badly, well..."
    "She's done a damn good job at hiding it all this time."
    "Her hand was in her coat now-"
    "No, wait."
    "Why would she-"
    stop music fadeout 1.0
    play music "audio/Dead Noise.mp3"
    nic "Ros-"
    nic "-ca!"
    nic "-et down!"
    "I didn't know what-"
    nic "ROSCA! GET THE FUCK DOWN!"
    "I followed her gaze, back to the woman, then I saw it-"
    show shoot
    "A gun pointed at my face."
    play sound "audio/nicgun.wav"
    r "Fuck!"
    scene black
    "Shots were fired-"
    "I fell to the floor{w}, waiting for the pain to come."
    "Warm, sticky fluid seeped into my clothes. That sharp, rusty scent-"
    "Was I dying-{w}and just too lushed up {w}to feel the pain?"
    nic "-sca."
    nic "ROSCA, HEY!"
    stop music
    scene black
    "I opened my eyes. It was Nic."
    "It took a while for my legs to stop shaking long enough for me to stand up straight."
    nic "ROSCA! ARE YOU HURT?"
    "I felt myself up, slowly realizing that the blood wasn't mine."
    r "N-no... I'm fine."
    nic "That's good..."
    "I turned to Nic."
    "Her hand was hidden in her coat. I didn't have to see it to know that it was a gun."
    "I could still smell the charred powder from the blast."
    "And then... {w}there was that body on the floor."
    r "Nic. What..."
    play sound "audio/nicgun.wav"
    "She shot the body again."
    play sound "audio/nicgun.wav"
    "And again."
    play sound "audio/nicgun.wav"
    "Then she fired her gun in the air."
    "Nobody moved a muscle."
    r "..."
    nic "Party's over. Get the fuck out."
    "That's when everybody ran."
    "I would have gone away with them-"
    "It's just that...{w} I couldn't walk a straight line to save my life at this point."
    "Nic turned to me. Her eyes..."
    "They were tainted with something I thought I'd never see in la Patrona-"
    "Fear."
    "She was shaking-"
    "It was almost like she didn't even recognize me."
    "I... {w}I had never seen her so remotely out of control."
    "Not just of herself. This whole situation-"
    nic "Shit."
    r "Nic, I-"
    nic "She-"
    nic "Rosca, I'm-"
    nic "I'm sorry, I..."
    nic "I SHOULD HAVE KILLED THAT BITCH THE SECOND SHE LOOKED AT YOU!"
    r "Nic, please..."
    r "You couldn't have known."
    nic "..."
    nic "No, Rosca! EVEN WORSE! {w} I WAS {i}CARELESS{/i}!"
    nic "I thought she would leave after I gave her a fuckin' hint-"
    nic "I let this happen. I should have-{nw}"
    r "Who cares, Nic... It's over."
    nic "THAT COULD HAVE BEEN YOU ON THE FUCKIN' FLOOR!"
    nic "It could have been you..."
    r "... I'm still here, aren't I?"
    r "You saved me, Nic."
    r "I knew you would, anyway."
    nic "That's... not true."
    nic "I almost {i}KILLED{/i} you, Rosca."
    nic "{i}I should never have let you in here{/i}."
    nic "I thought this would help things but..."
    play sound "audio/dropphone.mp3"
    "The gun slipped from Nic's hand-"
    "And she grabbed me by the arm so tight, it {i}hurt{/i}."
    nic "I SHOULD'VE..."
    nic "Damn..."
    r "Nic..."
    r "You're hurting me-!"
    "She stopped herself and grit her teeth."
    nic "I turned my back for one second, and..."
    nic "This bitch slips in-"
    nic "Now the Aces are scared shitless!"
    nic "The peace... I couldn't keep the peace-"
    nic "FUCK! AH-"
    "She staggered backwards, shoulders slumped with a weight I could not see."
    "But I could feel it-"
    "Those thoughts that were so full of fear and hate-"
    "And all towards herself."
    "Nic's pride made sure they never made it out of her mouth, but..."
    "I could feel it."
    "She was tearing herself apart, inside."
    "I couldn't take it."
    "I couldn't take it any more."
    play music "audio/Blanc.mp3"
    "I wrapped my arms around her-"
    r "Puta madre-shut up, Nic!"
    r "Just shut the fuck up!"
    nic "Don't tell me to shut up, Rosca!"
    nic "You know... {w}you know it's true."
    nic "In the end...{w} and always when it matters most... {w}I'm useless."
    r "Hija de puta, Nic..."
    r "Open your eyes!"
    "She opened her one good eye."
    r "...you're not useless!"
    r "You give us all a reason to get up in the damn morning!"
    r "Like anyone else is going to give us fuckups a job..."
    r "Or buy us our homes..."
    r "And spend every miserable evening... {w}fighting to keep a den of snakes from eating each other alive!"
    r "You're la Patrona, Nic!"
    r "I don't care what they say."
    r "You're a fucking saint to me. {w} And don't you {i}dare{/i} forget that."
    nic "..."
    nic "A saint, huh."
    "{i}There it was{/i}. {w}That sly grin."
    nic "...that's rich, Rosca. It really is."
    "I always forgot that Nic was shorter than me... but this close-"
    "It was the first time I had seen her this close."
    "Her face was hidden in shadows, just like the rest of the room."
    "But beneath her hat, Nic's eye still flickered with light."
    "Like a split-second muzzle flash, frozen in time."
    "I wanted to see more of that light."
    nic "Hey!"
    "I took her hat off."
    r "Ah, it was getting in the way..."
    nic "Rosca..."
    r "Cállate, por favor."
    r "Just... {w}hold me tight, Nic."
    "I leaned into her, feeling the heat soak through our clothes."
    "Her hands slowly ran over my back, her breath hot on my neck."
    "But then-"
    "Nic pulled away, bewildered."
    nic "Rosca..."
    r "{i}Dios mio{/i}-"
    nic "What are we doing-"
    r "I just-"
    nic "Rosca-"
    r "Nic, please... I'm begging you."
    r "Can't we just stay like this... a little while longer?"
    nic "That's... not how I-"
    r "Please-"
    nic "..."
    r "Won't you-"
    nic "I know what you want, doll."
    "She sighed, giving me a grudging kiss on the mouth."
    "A kiss so light, I almost didn't feel it happen."
    "Then she pushed me away."
    r "Wha-"
    nic "But you're drunk, Rosca."
    nic "And I'm..."
    nic "I'm not."
    nic "Look. I'll drive you home."
    "Her eyes fell to the corpse on the floor, still bleeding out."
    nic "Damn... I've still got to take care of that mess somehow..."
    nic "I guess she'll have to go in the trunk."
    r "I'll help you out, Patrona."
    nic "Are you kidding me? You can barely stand."
    nic "And it's not your kill. Leave it to me."
    "She wrapped her arms around me once more, helping me up."
    nic "Hey, Rosca..."
    nic "Thank you."
    r "What for?"
    nic "For..."
    nic "I don't know.{w} I don't know what this is."
    r "We don't have to know, Nic. {w}Así es... como te amo."
    nic "..."
    nic "What does that mean?"
    r "It's a secret."
    r "Besides... you'll find out yourself, someday."
    "I hoped she would. Until then, though-"
    nic "..."
    nic "If you say so, Rosca."
    scene car
    "She brought me to her car-"
    "I waited for her in the front seat, as she fixed the mess in the back."
    "That dead body in the trunk... it could have been me."
    "But I was still here, though."
    "Maybe it was because I had someone to look after."
    "And someone who was also looking out for me."
    nic "Let's get you home."
    scene incar
    play sound "audio/carengine.wav"
    "Nic drove me home that evening. We sped past the city in silence."
    "Veccio Palermo looked different from inside a bullet-proof sedan."
    scene frontseat
    "A la madre-"
    "The streetlights, the shop signs, the old houses-they almost looked beautiful."
    "Maybe... it was because I was closed off enough from the world..."
    "That I didn't have to look over my shoulder after every fucking step."
    "I felt safe."
    scene outapartment
    "Nic stopped in front of the apartment and helped me in."
    scene inapartment
    "Somehow, we made it to the bed without falling over each other."
    "Nic placed the blankets over me and sat down on the ugly couch by the bed."
    "I felt like a child under the covers."
    scene black
    "I closed my eyes..."
    "Slipping in and out of sleep, mind racing and hazy with an ungodly mix of adrenaline and alcohol."
    "The last thing I could remember was the sound of her driving off at four in the morning-"
    "The smell of smoke in the air-"
    "And that ghost of a kiss."
    $ nic_eve1 += 1
    stop music
    jump day2

label roscaeve1:
    $ l.visible = False
    $ nic.visible = False
    r "Hijo de puta. Oberon isn't back yet."
    r "I guess I'll have to show up early in the Cafe tomorrow."
    "I heated up some leftovers from last night's dinner and swallowed them down with old beer."
    "Somehow, the quiet hung around like an uninvited guest."
    "I didn't like it, so I started to hum."
    "Oberon would have hated that."
    "But-"
    play sound "audio/loudbang.mp3"
    "{w}That shot that rang out in the dark-"
    "If Oberon were here, he'd call it a firecracker and laugh."
    "If Oberon were here..."
    r "Que te jodan, Oberon... leaving me worried like this."
    play sound "audio/policechatter.wav"
    "I paced about the cramped room, turning the cop scanner on and reaching for Leola's gun-"
    "The gun that she lent me, after the first time I was assaulted on the job."
    "Then I looked out the dark window, turned the scanner off..."
    play sound "audio/policescanner.wav"
    "And... promptly sat my ass back down."
    "It's wasn't like I could go out there to look for him on my own."
    "Big words and a sweet mouth don't go far when faced with a rock-hard fist."
    "I toyed with the phone."
    r "Maybe I should ask Patrona if she's heard anything about him."
    r "Or I could try asking Leola if any of the cops caught up with him."
    r "Then again, maybe I should just wait 'til tomorrow. He said he'd meet me at the Cafe."
    menu:
        "Call Leola":
            jump callleoladay1
        "Call Nic":
            jump callnicday1
        "Don't call anyone.":
            jump nocallday1

label callleoladay1:
    play sound "audio/phonedial.wav"
    play sound "audio/calling.mp3"
    "It took a few rings before she picked up."
    r "Leola..."
    "The line stayed silent."
    stop sound
    r "Leola!"
    "I yelled into the phone; she was probably just trying to piss me off again."
    l "Shit, Rosca. Do you know what time it is?"
    "My nerves were shot enough that I didn't notice how late it already was."
    "Her voice was raspy, as if she'd just finished downing a cup of stale coffee with too much grounds in it."
    "I waited for her to clear her throat."
    l "So, what's eating at you, kid?"
    r "Oberon hasn't come back yet."
    l "Maybe he's tired of living with an insomniac."
    r "I'm sorry, I shouldn't have called."
    l "Naw, Rosca. It's ok, I'm up anyway."
    l "I was sleeping on the job, pulling a late shift tonight."
    r "Oh. Damn, that's pretty shitty."
    l "We all have to eat, Rosca."
    l "Besides, the scumbags all come out at this hour. More fun for me."
    r "And maybe Oberon's one of those scumbags?"
    l "Hey, that bruise still hurts. If I see him, I'll be sure to give it to him twice as hard and send him home, crying for his big sis."
    "She laughed at the thought; I heard her take a big swig of something. Maybe it {i}was{/i} stale coffee."
    r "Say..."
    r "Leola, did you pick to work overtime tonight just to look for him?"
    l "Wha-"
    "She took a sharp breath and started coughing. I managed to catch her off guard; I could almost see her cheeks turn red."
    r "I guess if you found him, then that would mean I'd be indebted to you."
    r "And then, you'd make me do something we'd both regret, wouldn't we?"
    r "You better get those handcuffs ready, Inspector. I don't play nice in be-"
    "She finally recovered enough to break into a guffaw."
    l "Better not finish that sentence, Rosca. I know how you talk to your marks."
    l "You lookin' to bleed me dry too? You really are full of it."
    l "Though... I am staking out, just in case."
    r "You sure have your priorities straight."
    r "... but thanks. I mean it."
    l "Hey, it's nothing, Rosca. Just doing my job."
    l "Besides, it's not like you've got other friends, you poor bastards."
    "If we were damned to have just her, then I guess we lucked out, me and Oberon."
    r "You know, frankness isn't always an endearing quality, Leola."
    l "Not here to endear myself to anyone, kid."
    r "It's just... please... tell me right away if you find him, Leola."
    l "I will. He's my friend too, you know?"
    l "Now please, get off the phone, Rosca, and get some rest."
    r "Good night, Leola."
    r "And Leola...!"
    l "Huh? What now?"
    r "Cuídate."
    l "What?"
    r "Take care."
    l "Oh. Of course."
    # Call ends with a beep.
    r "She's right."
    r "Time to get some rest, then."
    scene black
    # Sleep.
    # mild bonus for minigame?
    # Leola RV +1
    jump day2

label callnicday1:
    play sound "audio/phonedial.wav"
    play sound "audio/calling.mp3"
    "Patrona picked up surprisingly quickly. Even faster than during the day."
    stop sound
    r "Uh, evening-"
    nic "Yeah? Who is this?"
    r "...take a wild guess, Patrona."
    nic "Oh, Rosca! Of course."
    nic "Did you... and then... did she... ha! There's... finally he got the... people missing... yeah."
    "I could barely hear her; it sounded like she was trapped in a crowd of people shouting and laughing to lively music."
    "Then it hit me. She was at some kind of party."
    "It's been so long since I've been to one, I didn't even know what fun sounded like anymore."
    nic "So what's happened? I mean, you don't call the fuckin' Boss of the Black Aces if nothing's happened."
    "She was shouting into the phone and sounded a bit too chirpy for the hour."
    r "Ah Patrona, have you heard anything about Oberon?"
    nic "Nope. Have you?"
    "I haven't, which is exactly why I called, but she didn't seem to realize that."
    r "No..."
    nic "Well, if you have, I better be the first to know. That punk deserves a fist up his ass for shirking work."
    r "Patrona, uh, where are you?"
    nic "At the Den, where else?"
    nic "Don't worry about your brother, Rosca. If he's tough enough to piss me off, he's more than capable of surviving a night out on his own."
    nic "He's an Ace. Don't worry about it."
    r "You're right. Thanks Patrona."
    nic "I'm always right."
    nic "And call me Nic. It's after hours."
    nic "Where are you, anyway... Nic?"
    r "I'm at home."
    nic "Oh. Well, that's interesting."
    r "Really?"
    nic "Of course not."
    nic "That's a shame. You're wasting your youth, kid."
    r "Well, it takes sleep to keep looking young."
    nic "Let's worry about that when we get there, heh."
    r "Hey Nic, do you ever sleep?"
    nic "Sometimes. It's a tragic waste of time, I'm telling you."
    r "I guess I should let you get back to what you're doing then..."
    "I was about to hang up, but she started speaking again."
    "My thumb froze."
    "I was just about to hang up on the Boss of the Black Aces; almost signed my death sentence there."
    "The sounds from the other end were quieter now. Almost as if she moved away from the crowd, just to hear a little better."
    "Her voice was softer, too."
    nic "Hey Rosca."
    r "What?"
    nic "Take care."
    r "I-"
    "Before I could speak, the other line grew noisy with shouts."
    nic "Damn! There's a couple of fuckers here that I've got to have a word with."
    nic "Be seeing you tomorrow."
    r "Hold on-"
    "The line died before I could finish my sentence."
    r "Well..."
    r "That wasn't very helpful..."
    r "But it distracted me enough to stop worrying."
    r "I guess it's time to get some rest."
    scene black
    # Nic RV +1
    jump day2

label nocallday1:
    r "It's late. I guess..."
    r "I shouldn't bother anyone."
    r "I'll just try to get some rest."
    scene black
    # big minigame bonus
    jump day2

label day2:
    play sound "audio/typewriter.mp3"
    $ renpy.movie_cutscene("images/twodaysago.ogv")
    play sound "audio/alarm.mp3"
    scene inapartment
    $ nic.visible = False
    r "Ugh..."
    r "Fuck me."
    "Early mornings were the worst."
    "I fought to keep my eyes open-"
    "There was an appointment I couldn't miss today."
    r "That surprise better be a good one, pendejo."
    r "If it's another heaping plate of donuts, I'll put a hole in you myself."
    scene mainstreet
    "It was a bad hour. The city was crawling with the State's dogs."
    "If Leola were with me now, they wouldn't even give me a second look."
    "But she wouldn't be seeing me 'til midday."
    "A wrong word here, a careless glance there-"
    "That's all it took to start trouble with those goons."
    "I was forced to use the darker alleyways. Lucky enough, it was still daytime."
    "I've been down the different paths to the Cafe so many times."
    "I could tell which route I was taking even if I had my eyes closed all the way."
    "Soon enough, I found myself at that Cafe."
    "That sentimental, run-down, shambling excuse for a Cafe."
    # Simulate walking with scene changes?
    play music "audio/Light Faith.mp3"
    "And it didn't take much looking before I saw {i}manito{/i}."
    "This early in the morning and already arguing with a waiter-"
    "{b}{i}Cabrón{/i}{/b}."
    "I rushed in."
    r "Oberon! {i}Quit it{/i}. You're embarrassing us."
    "He lowered his fist, eyebrows still stuck in a position of anger."
    o "I was just kidding around, manita."
    o "Besides, he almost messed your flowers up."
    o "I've got to fix that somehow, right?"
    r "{i}What are you going on about{/i}, pendejo?"
    "I looked at the man Oberon had been harassing; his skin was taking on a shade of white."
    "My brother's idea of a fix needed a repair, itself."
    r "Let him go, Oberon. I'm already here, let's cut the shit."
    "He handed me a bouquet of fresh-cut flowers."
    r "..."
    r "You brought me out here, for flowers?"
    o "Here, take a whiff."
    "I smelled it to humor him-"
    "But the hair on the back of my neck rose as soon as I sniffed the flowers."
    r "These flowers are for funerals! Pendejo!"
    #Oberon makes confused face
    o "Oh... are they? Flowers are still flowers, anyway."
    o "C'mon, at least give your little brother a hug."
    r "Ugh, no! You force me to wake up at the crack of dawn-"
    o "Seven in the morning is hardly the crack of dawn, manita."
    r "Cállate! I barely got any sleep."
    r "Do you have any idea how worried I was?"
    r "Hijo de puta."
    o "Sorry, manita. I was just-"
    r "You know what, I don't even want to know."
    r "Now... tell me why we're here, Oberon."
    o "Hah! Wow, good one."
    "He started laughing at me, softly at first, then his voice rose into a barking mad crescendo."
    r "Puta madre, have you lost your fucking mind?"
    r "Please tell me you're not high right now."
    r "Tell me now, or I swear, I'll-"
    o "Relax! Ah-"
    o "Ahaha-"
    r "..."
    "Shit. I thought this was it. Oberon was going to tell me that he was an addict."
    "He was going to ask me for money, I could feel it."
    o "How could you forget?"
    r "..."
    r "..."
    r "Forget what?"
    o "{i}Feliz cumpleaños, Rosca!{/i}"
    r "...oh."
    r "Is it really-"
    "I... really... forgot."
    o "If there's anything you should remember around here, it's your birthday."
    o "That's the only day in a year that you get to make a wish, Rosca."
    o "Just a cake, and a candle, and your breath-"
    o "And the world could be yours, manita."
    "He glared at me-"
    "No, at someone behind me."
    "On cue, that waiter from earlier stepped forward and placed a plate in front of me."
    "On it was a donut, with one big, fat candle in the hole."
    r "..."
    r "You call this a cake, cabrón?"
    o "Sometimes you've got to improvise, Rosca!"
    r "..."
    r "Oberon-"
    "My throat felt coarse, struggling with words I haven't said in a long time."
    o "Blow the candle, manita!"
    o "Or else-"
    o "I'll {w}start {w}{i}singing{/i}."
    "I guess I didn't have to say anything at all."
    "I blew the candle, hard."
    "Then I realized- {w}I was in such a hurry, I blew it out before even thinking of a wish."
    "What a waste."
    "Still, I had to thank him."
    r "Gracias... manito."
    o "Aw, cabróna! You're making me blush."
    o "I was starting to think that your mouth was only filled with curses."
    o "The other Aces are starting to call you diablo rojo, you know."
    r "I don't care what those putos think. They can fuck themselves for all I care."
    r "Besides, I-"
    o "Yeah, I know. You've only got eyes for las chicas."
    o "Tell me, have you and Leola done it yet?"
    r "What?! Quit talking trash on my birthday, pendejo."
    o "All right, if you say so."
    o "I think she's a good choice though... You've got taste, manita."
    o "Long, toned legs that go on forever... {b}{i}Ay, esta tan buena{/i}{/b}!"
    r "Hijo de puta, if you don't shut up now, I'll-"
    o "Tranquila, manita! I won't stand between you two. I was just making an {i}observation{/i}."
    r "Make another observation like that, and I'll gouge your eyes out while you sleep."
    o "And you wonder why I didn't come home."
    r "Just... don't mess it up for us. She's the {i}only{/i} person who has our backs, manito."
    r "Well, other than Patrona."
    "His eyes flashed when I mentioned her."
    r "And for the record, she's... interesting, too."
    o "If you're looking to fuck a diablo, maybe."
    o "I'm not blind, manita. I've seen the way she looks at you, but-"
    o "It's a bad idea, Rosca. Patrona's only using us."
    r "You don't know her like I do, Oberon."
    r "And so what? She's la Patrona. {i}The Boss{/i}, puta madre. Nic sure as hell didn't get there doing charity work."
    o "{i}Nic{/i}? You're on first name basis now, huh."
    r "Besides... don't you see an opportunity here? If we've got Patrona-"
    o "{i}Estás loca{/i}, manita! You'll never 'get' her."
    r "Watch me."
    r "And don't tell me what to do, pendejo. I'm still older than you."
    o "I won't let this go, Rosca. Doesn't it bother you, the way things are?"
    r "Why should it? It's the same with them 'honest' folk."
    r "They have a boss too. And their boss has a boss. On and on. Everyone using each other to make more money."
    r "That's the way things are, Oberon. It's called employment."
    r "Only difference is that places like Patrona's doesn't need health inspections once in a while."
    o "It's not the same, Rosca."
    o "We {i}hurt{/i} people."
    r "So? Hypocrite."
    r "I've never seen you happier than after a good, old-fashioned beatdown."
    o "You're right. It makes me feel alive."
    o "But you're different."
    o "You're no fighter, Rosca."
    r "As everyone loves to remind me. I can't fight. So what?"
    o "Do you like... huh, what was that you called it-"
    o "Ah. {i}Tax collecting{/i}."
    r "It pays the bills, Oberon."
    o "I don't think you have it in you to enjoy it."
    o "Do you know why?"
    r "Of course."
    r "Like millions of other people on this wretched earth, I'd rather sleep in than argue with deadbeats."
    r "Lucky for us, I'm pretty good at it though."
    o "You've always been a good liar, manita. But please, just for once-"
    o "Don't lie to yourself."
    o "You're miserable."
    o "You can't stand it, because you still care about what's right, Rosca."
    r "Come mierda, Oberon! Tell that fairytale to the people I collected from yesterday."
    r "It might at least give them a good laugh."
    o "Do you want to keep living like this?"
    stop music fadeout 1.0
    "My brother's careless smile disappeared, replaced by a thin, serious line."
    r "I-"
    play sound "audio/ring.mp3"
    o "Answer my question."
    r "Oberon, I-"
    play sound "audio/ring.mp3"
    o "Answer me!"
    play sound "audio/ring.mp3"
    r "I... I have to take this call. It's... Patrona."
    "I reached for the phone."
    r "Good morning, Patrona."
    nic "Took you a while to pick up. You still asleep?"
    r "No, I'm at the Cafe."
    nic "Well, look at you. An early riser."
    nic "You're going to go places, doll."
    r "Thanks, Patrona."
    nic 'Any word about Oberon yet?'
    "I glanced at him. His face was still stuck in a dark frown."
    "I scowled back."
    r "No..."
    nic "Hm. I see."
    nic "Well, you know how this works by now."
    nic "On account of his absence, you're going to have to collect 4,000 credits today."
    r "Whoa there. That's a lot more than yesterday."
    nic "There's a good reason for that, Rosca."
    "An actual explanation for why I had to bust my ass twice as hard today - that was unusual."
    r "What is it, Patrona?"
    nic "I've considered moving you up the ranks."
    r "Oh, I get your drift. A promotion?"
    nic "I like the way you operate, Rosca. Smooth, clean and ruthless. It's about time you got yours, hm?"
    r "A la ma- Ah, I don't know what to say-"
    nic "Of course, that promotion ain't happening if you don't make it rain, doll."
    r "I'll make it pour, Patrona!"
    nic "Heh. You're a fiery one, aren't you?"
    nic "Make me proud."
    nic "Wouldn't want the Aces to be grumblin' now, accusing ol' Nic to be handing out favors to hot pieces like you."
    nic "Between the both of us though, I'd hand you that promotion, in a snap."
    r "I won't let you down. Just you watch me, Patrona."
    nic "Oh I'll be watching, all right. Get it done then come see me, you hear?"
    "The phone clicked shut. Today was off to a great start."
    "I guess I didn't need to make a wish after all."
    "It was like the universe already knew what I wanted and finally decided to give it to me on bended knee."
    r "No mames, Oberon! Patrona's moving me up the ranks!"
    o "Rosca, listen."
    r "This is great news- maybe we'll be able to get out of that fucking dump of an apartment."
    o "Rosca-"
    r "And you could get a better job-"
    "Oberon slammed his fist on the table."
    o "CÁLLATE JODER, ROSCA!"
    r "..."
    o "Look."
    o "Forget the fucking flowers."
    o "Forget the cake."
    o "Here's the real gift I have for you."
    "He handed me an envelope. It was heavy with paper; a packet of documents."
    o "Everything you need for a new life."
    o "It's all in there."
    r "What is this-"
    "I tore open the packet. A passport and some fancy official-looking, stamped papers fell into my lap."
    o "Get out of here, Rosca."
    r "How did you get all this-"
    o "Don't ask me that. It's not important."
    r "Oberon-"
    o "I told you right? One day, I'd get us out of here."
    o "I've been saving up, looking for someone who could help us."
    r "Saving up? Our fucking jar on the coffee table begs to differ."
    r "Where did you get the money for all this? Tell me!"
    r "Did you steal it from your quota?"
    o "No. Let's just say... I worked twice as hard."
    r "Leola told me-"
    o "Esa cabróna... I told her to keep it to herself."
    r "Well, it's good that she didn't! This is {i}insane{/i}."
    o "And staying in this shithole makes sense?"
    r "Why not?! We get by. Things are looking up now!"
    r "Where else could we go?"
    r "Do you think it's that easy, leaving Veccio Palermo?"
    r "The Aces don't take kindly to traitors and deserters."
    o "I've thought about that. It's exactly why I'm staying here."
    r "Ok. Oberon-"
    r "Tell me, please-"
    r "WHAT FUCKING WALL DID YOU HIT YOUR HEAD ON-"
    o "Rosca-"
    r "TO THINK THAT I WOULD LEAVE YOU BEHIND-"
    r "BY {i}YOUR{/i} FUCKING {i}SELF{/i}?"
    o "Rosca, let's face it."
    o "Out there, there's no place for monsters like me."
    o "You though... you still have a chance."
    o "You don't have to forgive me, Rosca, for what I did in the past."
    o "I had to do something. Papá, Mamá- I had to put them out of their misery."
    r "Oberon, please! That's behind us now."
    r "And... {w}you did the right thing."
    o "Don't lie, Rosca. I know... deep in your heart, that you'll never forgive me."
    r "Oberon, that's not true!"
    o "We both know that only monsters can survive in Veccio Palermo."
    o "But... there are places out there, where it doesn't take a gun to deliver justice."
    r "Cállate, Oberon-"
    o "Goddamn it, Rosca! Maybe things could be different."
    r "No."
    o "Rosca, listen to me-"
    r "{b}I already have a life.{/b} Here.{w} With you. {w}With Leola. {w}With Patrona."
    r "{i}Take that away.... and I've got nothing else, Oberon.{/i}"
    r "You're asking me to leave that all behind?"
    o "This isn't who you have to be, Rosca."
    r "{i}I know who I am.{/i}"
    r "I'm an Ace."
    r "You're an Ace, too."
    r "...and we're late for work."
    "I stood up from the table, leaving his gift behind."
    "Oberon stayed put."
    "Then he shouted at me, just before I could reach the door."
    o "You're making a mistake, Rosca!"
    r "It's my mistake to make, not yours!"
    "I gave him the finger and walked out the Cafe, pretending not to hear the rest."
    r "I..."
    r "{i}I belong here{/i}."
    $ l.visible = True
    $ nic.visible = True

    scene street
    # Scene the Streets
    play sound "audio/trafficshort.wav"
    "My feet carried me into the Arcade; I didn't even have to think."
    "Leola was in her usual spot, waiting for me."
    "{i}Just like clockwork.{/i}"
    play music "audio/Upriver Funk.mp3"
    l "Rosca!"
    r "..."
    l "H-hey, you're looking mighty pissed off today."
    r "Don't talk to me."
    l "What happened, Rosca?"
    r "I SAID, DON'T TALK TO ME!"
    "My voice rang out in the street but people barely turned their head to look at us."
    "A mean-looking cop and an angry crook: {i}like they wanted any part of that trouble{/i}."
    r "Ah-"
    r "Leola..."
    "Her mouth opened and closed, full of questions, but not one made it out of her lips."
    l "All right. I won't pry."
    r "Let's just get down to business."
    l "Are you sure you can do this today?"
    r "Of course."
    l "Because if you can't, just round up your worst clients, and I'll pay them a visit, myself."
    l "Y'know, the ones that don't care about talking."
    r "Stop it."
    r "I don't know if you're being kind or if you just want an excuse to go on a bloody fucking rampage."
    l "Hmm. How about both?"
    r "I told you. If you want to work with me, we do our best to keep it clean."
    l "All right, I'll be good."
    r "Let's go."
    # transition to Arcade
    l "So, 3,000 credits again?"
    r "..."
    r "4,000."
    l "Shit! What happened? Do you and Oberon have a debt to the Boss that I don't know about?"
    r "No, it's not that."
    r "Patrona said she was considering me for a promotion."
    r "I guess this is some kind of test."
    l "Oh."
    l "..."
    l "Congratulations?"
    r "Thanks for the support, Leola."
    l "You're not stupid. You know what happens to people who fail the Aces."
    l "More responsibility doesn't mean an easier life."
    r "Come mierda, I haven't even started the test... and here you are, already calling me a failure."
    r "Don't jinx this for me!"
    l "All right, all right. Good luck with your promotion, jeez."
    r "You don't understand, Leola. I want to have enough money to afford something other than donuts on my birthday."
    l '...'
    l "Oh... {w} shit!"
    l "It was {i}today{/i}, wasn't it."
    l "Happy birthday, Rosca!"
    l "Damn, I knew I messed up somewhere. I forgot to greet you, is that why you were so pissed off earlier?"
    r "Leola, even I forgot, until some puto cabrón reminded me."
    l "Huh? Who-"
    r "Oberon."
    l "He's back! How was he-"
    r "Still as stupid as ever. The usual."
    l "Heh. Big ol' Oberon. Well, we should get together and celebrate!"
    r "Why? It's no big deal."
    l "What?! But it's the only day in a year that you-{nw}"
    r "Stop right there."
    r "If I hear that wish bullshit one more time, I swear, I'm going to {i}shoot{/i} someone."
    # l "See, this is why I don't lend you my gun."
    # r "You'd be a fool for lending it to me in the first place."
    # l "You're right. I don't think the judge would believe I was innocent even if I showed him a photo of you pulling the trigger."
    l "It wouldn't hurt to be a little less cynical on your birthday, kid."
    l "I mean... if you keep frowning like that, you'll look like a fucking raisin when you're fifty."
    "I laughed for the first time that day."
    r "Leola, take a moment and ask yourself this, all right?"
    r "Who the fuck wants to live to fifty in Veccio Palermo?"
    l "I wouldn't mind."
    r "Well, you're going to get to fifty faster than me, anyway."
    r "Guess I can keep you some company, until then."
    l "Gee, thanks. I guess I'll make sure at least one person comes to your funeral."
    r "Can we get to work before Patrona finds a reason to hold one in my honor?"
    "Minigame placeholder."
    jump extortiond2end

label extortiond2end:
    "Minigame ends."
    # when minigame ends, Rosca calls Leola
    # Show Leola's health
    # if Leola's health gets to less than 20% her relationship points with Rosca goes down
    stop music fadeout 1.0
    play music "audio/Upriver Funk.mp3"
    "Branch Placeholder: How much of Leola's health remains?"
    menu:
        "90 to 100":
            jump perfhealthday2
        "21 to 89":
            jump normhealthday2
        "20 to 0":
            jump badhealthday2

label perfhealthday2:
    l "Rosca, you have to tell me, {i}right now-{/i}"
    l "What's your secret?"
    l "It looks to me like they're just handing you the money without a fight! All you had to do was {i}ask{/i}."
    l "The Boss didn't know it then, but she hired a real hustler the day she hired you."
    r "It's called being professional, Leola. Something I don't think you understand."
    l "Hey, you never gave me a chance to be {i}professional{/i} today."
    r "That's not what I meant."
    l "Eh? You're not making sense, kid."
    r "I mean, if you were a good cop, you wouldn't be doing this at all."
    l "Hah! Rosca-"
    l "Good cop is just another name for clay pigeon in these parts."
    l "Besides, if I did my job properly, you'd be rotting in some cell by now."
    "I thought back to the day we first met. The memory was still as fresh as a crisp new pack of smokes."
    "And like that pack, I couldn't help but touch on it from time to time."
    "It calmed me, somehow... that a bad day could turn into an opportunity, with a spark of luck."
    r "I don't deserve that talk from you."
    r "You couldn't even tell the difference from someone feeling you up, and someone trying to plant a note in your pocket."
    r "Some inspector you are."
    l "For the record, I thought you were trying to steal my wallet."
    l "And I would have let you get away with it, if you didn't fuck things up."
    r "That was my first job. And your pockets were so damn tight, it was ridiculous!"
    l "Why couldn't you just tell me what was in the note, anyway?"
    r "I was told that it was for your eyes only."
    l "Well, why couldn't you just hand it over, like a sensible person?"
    r "...I was just trying to have some fun."
    l "Heh. That so? Well, I had fun too."
    r "Yeah, until your chief came around. {w} Then you arrested me to save your ass from being accused of loitering on the job."
    l "One of my more brilliant moments, really."
    r "The only good thing that came out of that was being introduced to Patrona."
    l "What about meeting me?"
    r "You fucking arrested me. So, no."
    r "But why'd you introduce me, anyway?"
    l "Hey, you looked like you were up to the job."
    l "The way you swore at me when I hauled you into the Security Headquarters; I could tell you had a way with words."
    r "Well... thanks to you, I now have a permanent record."
    l "Just sexual assault and theft, nothing too serious."
    r "It's a screwed up world when the crook's {i}actually innocent{/i}."
    l "Hey, I had to give you a resume, Rosca. The Boss doesn't hire clean hands."
    r "No wonder she hired you."
    l "I wouldn't say that's why, but sure, let's leave it at that."
    r "So why-{nw}"
    r "You know what, I won't pry. Sounds like more trouble than it's worth."
    l "Heh, admit it, you're dying to ask. Go on now-"
    r "I really don't care, Leola."
    l "Damned killjoy. Well... if you're free later this evening, you know where to find me, Rosca."
    l "Maybe I'll treat you to something, too, since it's your birthday and all."
    l "And bring Oberon along, will you? That bastard owes me an apology."
    l "See you around."
    "She walked away with a leisurely pace."
    "With no assault reports to write, her afternoon's practically free."
    r "{i}Que chingóna, that Leola.{/i}"
    jump visitbossday2


label normhealthday2:
    l "Hey, you made the quota. Good job."
    r "Yeah. Not a bad haul, if I say so myself."
    l "I had some fun too. That's always a good thing, heh."
    r "Hey Leola... have you ever thought about going straight?"
    l "What?!"
    l "But-"
    l "No, I can't, Rosca. You're... {w}asking me... {w}to give up women?!"
    l "You might as well ask me to stop breathing."
    r "THAT'S NOT WHAT I MEANT!"
    play sound "audio/punch.wav"
    "I hit her square on the arm. The old bruise probably hasn't healed yet, and it sure as hell won't heal any faster now."
    l "Fuck! Will you {i}please{/i} stop hitting me {i}there{/i}?"
    l "I was only trying to lighten the mood..."
    r "Well, you're just pissing me off, cabróna."
    l "Fine. What did you mean, then?"
    r "I mean, if you were a good cop, you wouldn't be doing this at all."
    l "{i}This?{/i}"
    r "Working for the Aces."
    l "Hah! Rosca-"
    l "Good cop is just another name for clay pigeon in these parts."
    l "Besides, if I did my job properly, you'd be rotting in some cell by now."
    "I thought back to the day we first met. The memory was still as fresh as a crisp new pack of smokes."
    "And like that pack, I couldn't help but touch on it from time to time."
    "It calmed me, somehow... that a bad day could turn into an opportunity, with a spark of luck."
    r "I don't deserve that talk from you."
    r "You couldn't even tell the difference from someone feeling you up, and someone trying to plant a note in your pocket."
    r "Some inspector you are."
    l "For the record, I thought you were trying to steal my wallet."
    l "And I would have let you get away with it, if you didn't fuck things up."
    r "That was my first job. And your pockets were so damn tight, it was ridiculous!"
    l "Why couldn't you just tell me what was in the note, anyway?"
    r "I was told that it was for your eyes only."
    l "Well, why couldn't you just hand it over, like a sensible person?"
    r "...I was just trying to have some fun."
    l "Heh. That so? Well, I had fun too."
    r "Yeah, until your chief came around. {w} Then you arrested me to save your ass from being accused of loitering on the job."
    l "One of my more brilliant moments."
    r "The only good thing that came out of that was being introduced to Patrona."
    l "What about meeting me?"
    r "You fucking arrested me. So, no."
    r "But why'd you introduce me, anyway?"
    l "Hey, you looked like you were up to the job."
    l "The way you swore at me when I hauled you into the Security Headquarters; I could tell you had a way with words."
    r "Well... thanks to you, I now have a permanent record."
    l "Just sexual assault and theft, nothing too serious."
    r "It's a screwed up world when the crook's {i}actually innocent{/i}."
    l "Hey, I had to give you a resume, Rosca. The Boss doesn't hire clean hands."
    r "No wonder she hired you."
    l "I wouldn't say that's why, but sure, let's leave it at that."
    r "So why-{nw}"
    r "You know what, I won't pry. Sounds like more trouble than it's worth."
    l "Heh, admit it, you're dying to ask. Go on now-"
    r "I really don't care, Leola."
    l "Damned killjoy. Well... if you're free later this evening, you know where to find me, Rosca."
    l "Maybe I'll treat you to something, too, since it's your birthday and all."
    l "And bring Oberon along, will you? That bastard owes me an apology."
    l "See you around."
    "She walked away with a rushed pace."
    "A few assault reports to write, and her afternoon's free."
    r "{i}Que chingóna, that Leola.{/i}"
    jump visitbossday2

label badhealthday2:
    l "Hey Rosca..."
    l "Tell me."
    l "You're not this bad on purpose, are you?"
    l "I mean, if you hate me that much, just fucking tell me to my face."
    r "Joder, Leola... I'm sorry-"
    l "I'll take some hits, sure, but I'm not in this business to get killed."
    l "If you don't shape up, I just might find someone else to work with."
    r "Well, I won't blame you."
    r "If you want to find another partner... I'll respect your decision."
    l "Fuck it, {i}I don't want anyone else{/i}. {nw}"
    r "What?"
    l "I said, don't fuck it up for anyone else, you hear?"
    l "{i}Well shit{/i}. My body's going to be a garden patch of bruises thanks to {i}you{/i}."
    l "I'm going home early to get some rest."
    r "Wait! Leola-"
    "She walked away with a limp, pointedly ignoring me."
    "There were a pile of assault reports waiting to be written, and Leola would have to write them all herself."
    r "Today was a real mess... Damn."
    r "Eres una pendeja, Rosca."
    # Lock out option to spend evening with Leola
    jump visitbossday2    

label visitbossday2:
    scene hq
    show rosca at left
    show nic at right
    stop music fadeout 1.0
    play sound "audio/trafficshort.wav"
    r "Well... now that the work's done, I guess it's time to visit Patrona."
    "I walked down the Streets, pushing past the ever-present crowd."
    "With a tip of the hat, I looked some of them in the eye; they knew enough to back off."
    "And the closer I got to the Headquarters, the faster people made way."
    "Finally, I reached her office."
    "I opened the door with care."
    play music "audio/Anthem.mp3"
    "Already, she was standing there, having a smoke. A haze of gray clouded the room."
    nic "Rosca."
    "Placeholder branch: Did Rosca finish on time?"
    menu:
        "Not late.":
            jump ontimeday2
        "Late":
            jump lateday2

label ontimeday2:
    r "Afternoon, Patrona."
    "She glanced at the clock on her desk and grinned."
    nic "Right on time. Excellent."
    nic "How did your day go?"
    r "It was all right."
    nic "Really, now."
    r "As fine as any other day in Veccio Palermo can be, Patrona."
    "Her lips twitched, holding back a laugh."
    nic "You and I both know that's bullshit, Rosca. I know what it's like out there."
    nic "That said... {w}I do appreciate your tact, doll."
    nic "Knowing the right thing to say and the right time to say it can make all the difference."
    nic "Doubly true when you're caught up in a bad situation."
    r "But this isn't one of those situations, is it, Patrona?"
    nic "Hah, of course not."
    nic "I'm starting to think you {i}do{/i} deserve that promotion."
    "A smile passed my lips, despite my best efforts to tamp it down."
    nic "But first, let's see what you've got for me."
    "I showed her today's haul."
    "Placeholder branch: Did Rosca meet the quota?"
    menu:
        "Yes":
            jump quotaokday2
        "No":
            jump quotanotokday2


label lateday2:
    r "Good aftern-"
    nic "Save the sweet talk for later, Rosca. You're late."
    "Come mierda. Of all the days to be late..."
    nic "You're this close to pissing me off, Rosca. Can't you read the fucking time?"
    r "Ah-"
    nic "If that's an excuse you're about to give me, it better be a {i}damn good one{/i}."
    nic "You're full of it-"
    nic "Makin' me sit here and wait, while who the fuck knows what's going on out there-"
    "If I didn't know any better... I'd say she was worried-"
    "About me."
    if nic_eve1 == 1:
        jump lateday2special
    else:
        jump lateday2regular


label lateday2regular:
    "But I knew better than to bring that up."
    r "I, uh-"
    menu:
        "It's all Leola's fault.":
            jump blameleola
    
        "This is Oberon's fault.":
            jump blameoberon

label lateday2special:
    "If condition test placeholder."
    return

label blameleola:
    "I'm sorry, Leola... but I need this promotion."
    nic "{i}That. Bitch{/i}. Is she causing you trouble, Rosca?"
    nic "Just say the word, and I'll have her {i}replaced{/i}."
    nic "Plenty of other dogs out there. Much cheaper to work with, too."
    "Already, her hand was halfway to the phone-"
    "Mierda! Patrona had at least three sicarios on speed dial at any given moment."
    "Leola didn't deserve {i}that{/i}."
    r "No, no! It's nothing like that Patrona."
    "I reached over and caught her hand, praying that she didn't notice how cold my fingers were."
    nic "What the hell?"
    "I caught her off-guard."
    nic "...don't touch me."
    "So she said-{w}the edge fell from her voice, though."
    nic "Don't cover for that bitch."
    r "Patrona... that's a whole lot of trouble you're asking for. She's an Inspector."
    nic "And I'm the Boss."
    r "It's still trouble, Patrona."
    nic "Don't tell me what to do."
    r "Besides, you know how Leola is. Once she gets started, she won't stop talking."
    nic "You're late because the both of you had a chat?"
    r "It was a one-sided chat, Patrona. Besides... you know I can't help it."
    r "I'm a good listener."
    nic "..."
    nic "A good listener, huh."
    nic "Well... you listen up now."
    jump lateday2cont

label blameoberon:
    "I'm sorry, Oberon... but {i}we{/i} need this promotion."
    nic "What? But he wasn't even there."
    r "Exactly."
    nic "You know what, Rosca-"
    nic "I see what you're getting at."
    nic "But life isn't fair, and a team is a team."
    nic "If he fails to deliver, either you pick up the slack or go home, Rosca."
    nic "Don't complain to me about the numbers after you've accepted the job."
    nic "Understood?"
    r "Yes, Patrona."
    jump lateday2cont

label lateday2cont:
    nic "I'll be taking the penalty from your miscellaneous fees."
    nic "It's not like you're putting it to good use, anyway."
    r "You're being cold, Patrona."
    nic "Well, you're not giving me much of a reason to warm up to you today."
    r "..."
    nic "So. How did your day go?"
    r "It was all right."
    nic "Really, now."
    r "As fine as any other day in Veccio Palermo can be, Patrona."
    nic "You and I both know that's bullshit, Rosca. I know what it's like out there."
    nic "That said... I appreciate your tact, doll."
    nic "Knowing the right thing to say and the right time to say it makes all the difference."
    nic "I'm starting to think you do deserve that promotion."
    "A smile passed my lips, despite my best efforts to tamp it down."
    nic "Then again... you {i}were{/i} late."
    "{i}Puta madre, this tension!{/i}"
    nic "But first, let's see what you've got for me."
    "So I showed her today's haul."
    "Placeholder branch: Did Rosca meet the quota?"
    menu:
        "Yes":
            jump quotaokday2
        "No":
            jump quotanotokday2

label quotaokday2:
    "Placeholder branch: Did Rosca exceed quota?"
    menu:
        "Yes":
            jump quotaexceedday2
        "No":
            jump quotanormalday2

label quotaexceedday2:
    nic "A beautiful job you did today, Rosca."
    "She took a step back, as if to take me in, the whole of me."
    nic "That's it, right there, the person I've been looking for all this time."
    nic "The position is yours."
    jump quotaday2cont

label quotaday2cont:
    r "A la madre, Patrona!"
    "At least if I died right now, they would have to put me up with a respectable funeral."
    "I was fucking {i}made{/i}."
    nic "That really is some mouth you have there, doll."
    r "..."
    nic "Then again, now that you're a cut above the rest, I say we can dispense with the courtesy, once in a while."
    r "I... but wow, I-"
    "My mouth opened and closed like I was a fish out of water; I had to light a smoke to keep myself from looking like a total fool."
    "I wanted Patrona to see me as cutthroat Ace, Patrona in the making, and her future señora all rolled into one."
    "The growing smirk on her lips reduced me to something closer to a fucking mute."
    nic "I take it that this is good news to you?"
    "I took a deep breath and calmed myself down. I was awake. This really was happening."
    r "Best day of my life, Patrona."
    nic "Don't overdo it, doll."
    nic "Though... I noticed. You still haven't asked me anything about the job."
    nic "Are you going to take it blindly, just like that?"
    nic "Then again, on that day when you joined the Aces... you didn't really know what you were getting into, did you."
    r "Well, Patrona-"
    nic "Call me Nic. You've earned it."
    r "Si, Nic. I figured it would just be more of the same, right?"
    nic "Well, something like that. Basically, the promotion means you get to keep more of what you make."
    "At that point, I was just waiting for the catch. There had to be a catch."
    nic "The thing is-"
    "Ah, there it was."
    nic "If you're going to take on this responsibility, then your quota also rises."
    nic "And... as soon as you take on this job, I'm issuing a hit on the person whose job you're taking."
    r "What?"
    nic "It's no one you know, so don't worry about it."
    r "..."
    nic "So is that a yes?"
    "She already had her hand on the phone."
    r "I-"
    nic "Great."
    r "Wait Nic, I-"
    play sound "audio/ring.mp3"
    play sound "audio/ring.mp3"
    nic "Hey Paco."
    nic "Yeah, it's about time. Take him out."
    "She ended the call just as fast as she'd made it. As if she had just ordered {i}takeout{/i}."
    nic "There. It's done."
    r "..."
    "I wondered who it was, the poor devil."
    nic "I know what you're thinking, Rosca. Well, let me tell you right now..."
    nic "You hear that little voice in your head, the one that tells you that something is wrong or right?"
    nic "From now on, you tell her this-"
    r "Patrona..."
    nic "Listen, Rosca. I'm trying to help you here. Don't fuckin' interrupt me when I'm trying to teach you something important."
    r "..."
    nic "As I was saying."
    nic "That voice. Tell it to go die in a fucking ditch, you got that?"
    r "..."
    nic "Look. There are only two things you should concern yourself with every day."
    r "And those are?"
    nic "Loyalty and common sense. Everything else is secondary."
    nic "You know what happens to those who cross the Aces, Rosca."
    nic "There's only so much I can do, watching out for you..."
    nic "Don't make decisions that you know will end with you bleeding out on the pavement."
    nic "As for common sense..."
    nic "Well, I think you're plenty smart, Rosca."
    nic "Oberon though."
    nic "He's becoming a pain. Reign him in, will you?"
    r "I will, Nic."
    nic "Good."
    nic "Well, what are you doing this evening?"
    r "I don't know yet."
    nic "Then... spend the evening with me."
    nic "I'll be stuck in the office 'til midnight."
    nic "Fucking paychecks. I need someone to sign them for me."
    nic "You're the only one I trust enough to forge my signature."
    r "A load of fun, I'm sure."
    nic "Maybe, if you like bonuses."
    r "I'll think about it."
    nic "You like giving everybody a hard time, don't you."
    r "Not everybody, Nic."
    nic "Just me, then?"
    r "Of course."
    nic "You know, I hate it when people lie to me."
    r "That's a dangerous accusation."
    nic "Heh, I guess that wasn't fair of me."
    nic "Hey listen..."
    nic "If you need anything-"
    nic "My doors are always open to you, Rosca."
    nic "Like I said, you've earned it."
    r "I won't let you down, Patrona."
    nic "Good."
    nic "Well, I've got some loose ends to tie. Come back later."
    r "If I come back at all."
    nic "Get out of here, Rosca."
    "I left her office."
    jump eveningday2

label quotanormalday2:
    nic "Not bad, Rosca."
    nic "I know you could do a little better, but I'd say this is good enough."
    nic "Well, what can I say-"
    nic "The position is yours."
    jump quotaday2cont


label quotanotokday2:
    nic "What the fuck-"
    nic "I ask you to do one thing, Rosca."
    nic "I even offer you a promotion."
    nic "And you're showing me... that this is the best you can do?"
    r "..."
    nic "Listen to me."
    nic "I've said this before."
    nic "Do you know why we wear all these fancy suits?"
    nic "It's because we run a fucking {i}business{/i}."
    nic "And a business that doesn't earn money is a piece of shit business."
    nic "Every day you piss away is a dent on our resources."
    nic "So unless you want to end up like one of those marks you know so well..."
    nic "Do your goddamn job, Rosca."
    nic "Before I send the bitches after your good for nothing brother."
    "She took a long drag on the cigarette, exhaling it in one quick sigh."
    nic "Fuck this."
    r "Sorry, Patrona. I-"
    "Her eyes flashed; I looked away. I had to. If I didn't, I might have pissed myself."
    nic "Damn it, Rosca. Don't say useless things like {i}'sorry'{/i}."
    r "Tomorrow I'll-"
    "She cut me off with a click of the tongue. It might as well have been the crack of a whip, breaking skin."
    nic "Listen, do me a favor. Just shut up and get the fuck out of my office."
    r "Si, Patrona. I'm really sor- I mean, it won't happen again!"
    "Her vicious eyes bored through mine."
    "I wasn't even sure if she was seeing {i}me{/i}, instead of the damn numbers in her head."
    "But she didn't move a muscle. That was as close to forgiveness as I was going to get."
    r "Today was a fluke, Patrona..."
    nic "It better be."
    nic "Because if you're the fluke, then we're going to have a real problem on our hands."
    r "It won't happen again."
    nic "Get out of here."
    "I reached for the door and bolted out of her office."
    jump eveningday2


label eveningday2:
    "Some days, I wish night came faster than it did."
    menu:
        "Visit the Cafe":
            jump leolaeve2
    
        "Head to Nic's office.":
            jump niceve2

        "Go home.":
            jump roscaeve2

label leolaeve2:
    # CHECK IF LEOLA WAS CHOSEN EVE1- will affect some dialogue choices?
    # rosca goes to cafe, but leola's already waiting for her outside
    # Rosca accompanies leola on a stakeout
    # as a pretend hooker / cop informant
    # they eat fuckin' donuts again lololol
    # leola brings out bad coffee
    # leola reveals her views on justice
    # segway into old friendship of nic and leola
    # also beer
    # the two make out
    # leola gets called away by superior / radio / emergency
    # leola doesn't shirk work (when jfc she should have)
    # rosca jokes about her finally being a good cop for once
    # rosca doesn't really care, she just thinks leola's cute when she think she sounds smart
    # ofc rosca tells her to take care when she goes off
    # in spanish??
    # rosca goes home
    scene alley
    scene outcafe
    scene incafe
    jump oberoneve

label niceve2:
    # CHECK IF NIC WAS CHOSEN EVE1- will affect some dialogue choices?
    # nic is hard at work at her desk
    # when Rosca comes in she calls her over
    # gives her instructions on what to do
    # at first Rosca messes up
    # then they get into a flow
    # Nic shares a drink with Rosca (classy vintage, etc)
    # segway into old friendship of nic and leola
    # drinking game????
    # nic gets a bit red in the face, kind of drunk
    # lol rosca is a better drinker
    # rosca starts being a bit lewd
    # the two make out, hot scene
    # but when rosca asks for it, nic stops
    # explains her ace-feelings, panics a bit, thinks rosca will laugh at her
    # but suprise-! rosca is totes understanding
    # nic volunteers to drive rosca home
    # but rosca reminds her she is drunk
    # rosca goes home
    jump oberoneve

label oberoneve:
    # Oberon wakes up
    # Rosca decides to make a meal
    # The two have a talk
    # Touching and funny at first
    # But it turns into an argument
    # Oberon runs out into the night
    jump day3

label roscaeve2:
    # Rosca heads straight home, is greeted by the sight of Oberon sleeping.
    # She decides to take a smoke and reminisce about their past
    # Reveal some details as to why they left
    # And why Oberon had to kill their parents
    # Starts to make a call
    # But this wakes Oberon up-
    "Placeholder"
    jump oberoneve

label day3:
    play sound "audio/typewriter.mp3"
    $ renpy.movie_cutscene("images/onedayago.ogv")

label extortiond3end:
    "Minigame ends."
    # when minigame ends, Rosca calls Leola
    # Show Leola's health
    # if Leola's health gets to less than 20% her relationship points with Rosca goes down
    stop music fadeout 1.0
    play music "audio/Upriver Funk.mp3"
    "Branch Placeholder: How much of Leola's health remains?"
    menu:
        "9 to 10":
            jump perfhealthday3
        "5 to 8":
            jump normhealthday3
        "0 to 4":
            jump badhealthday3

label perfhealthday3:
    "Placeholder."
    jump eveningday3

label normhealthday3:
    "Placeholder"
    jump eveningday3

label badhealthday3:
    "Placeholder"
    jump eveningday3

label day4:
