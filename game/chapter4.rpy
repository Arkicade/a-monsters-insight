label d3_win:
    stop music fadeout 2.0
    play sound "audio/sfx/magic.wav"
    $ showtext = False
    $ showtext2 = False
    $ showinput = False
    window hide
    $ quick_menu = False

    call screen deu_victory() with dissolve
    #$rrow.xp = 900
    #$rrow.yp = 1000

    #$ quick_menu = True

    $ search = _return
    $ search = search.lower()

    $ deulithoteq_sig = search
    jump d3_done

label d3_done:
    stop ambient fadeout 2.0
    $save_name = "-- end of dialogue 3 --"
    hide screen deu_door
    hide sewer onlayer back with dissolve
    mc "With my mark imprinted on Deulithoteq's mind, it acts like a \"signature\" of some sorts."
    mc "Meaning that I can siphon their mental energy at anytime, as long as the connection is maintained."
    "Congratulations!{w} You've successfully won Deulithoteq's favour!"
    jump check_end

label d3_draft:
    window hide
    $ quick_menu = False

    call screen deu_victory() with dissolve
    #$rrow.xp = 900
    #$rrow.yp = 1000

    #$ quick_menu = True

    $ search = _return
    $ search = search.lower()

    $ deulithoteq_sig = search
    jump d3_draft_done

label d3_draft_done:
    stop ambient fadeout 2.0
    $save_name = "-- end of dialogue 3 --"
    hide screen deu_door
    hide sewer onlayer back with dissolve
    mc "With my mark imprinted on Deulithoteq's mind, it acts like a \"signature\" of some sorts."
    mc "Meaning that I'll be free from them as long as I uphold the terms of the CONTRACT written in silk..."
    mc "... as Deulithoteq upholds the PACT that I made in its mind."
    "Congratulations!{w} You've successfully escaped Deulithoteq!"
    "Although you failed to win its favour, this still isn't a LOSE situation."
    jump check_end

label check_end:
    $ quick_menu = True
    show solas onlayer back with dissolve
    play ambient "audio/sfx/solas.wav" fadein 1.0
    mc "After our conversation, I quickly exited Deulithoteq's underground to get up on the surface of Solas."
    mc "It was scorching, humid and dead into the middle of the night."
    mc "People passed by but nobody looked,{w} all of them should've been Deulithoteq's earwurm lackeys."
    mc "However, they seemed to resemble inconspicuous monsters,{w} anodyne,{w} hardly noticeable."
    mc "Their figures melt into the atmosphere as the sand mist melts into the dark blotched sky."
    mc "I suppose this is what I wanted but there's this feeling where I don't know what's going to happen next."
    mc "There's no fear, no anticipation, no curiosity.{w} Just the feeling of emptiness that needs to be filled."
    mc "I turn to see the sun-dial eye planted in the middle of Solas."
    mc "There was a tingling in my feet and an emptiness encompassing the air."
    mc "The midwinter sandstorm is approaching soon."
    mc "...{w} I knew then that I had to go."
    $save_name = "-- epilogue --"
    if fernweh_outcome == "win" and cormeum_outcome == "win" and deulithoteq_outcome == "win":
        jump end_rule
    elif deulithoteq_outcome == "win":
        jump end_fool
    elif fernweh_outcome == "win" and cormeum_outcome == "win" and deulithoteq_outcome == "draft":
        jump end_gris
    else:
        jump end_veneer

label end_rule:
    ### you're the bestt
    mc "After sun eye turned to the west, I went aboard the Solas Eye Line to go back home."
    hide solas onlayer back with dissolve
    stop ambient
    play nature "audio/sfx/train.mp3"
    mc "The ride wasn't all that pleasant,{w} but it was the only place that I could feel like there was serenity in my life."
    mc "Home could be calm too, but taking care of Keychee can be time-consuming."
    stop nature fadeout 2.0
    show homeb onlayer farback
    show homef onlayer back with dissolve
    play ambient "audio/sfx/basement.mp3"
    play music "audio/music/Confused.wav"
    mc "By the time I was back in Barraken, Keychee was already fast asleep."
    mc "I went over to the drawers, and started mixing ingredients in..."
    mc "..."
    mc "What am I doing?"
    mc "After EVERYTHING that's happened these past few days, I'm just sitting here... alone."
    mc "Making myself a meal?"
    mc "I've just earnt the favours of two of the Great Terrors of OUTERWORLD."
    mc "And managed to successfully outdo my greatest threat to my whole career."
    mc "...{w} I should celebrate!"
    mc "But with what?"
    mc "I don't have any equipment or funds to do anything {i}too{/i} lavish."
    stop music fadeout 2.0
    mc "No.{w} I know what I need to do."
    stop ambient fadeout 2.0
    hide homeb onlayer farback
    hide homef onlayer back with dissolve
    mc "From here on out,{w} I'm drafting a list of names and I'm checking them off one by one."
    play music "audio/music/Gaining.wav" fadein 13.0
    mc "This list will hold the names of Great Terrors, Old Terrors, Dark Terrors..."
    mc "And whoever stands in my way."
    mc "Oh I'll celebrate alright!"
    mc "My victories will pave the way for my celebration."
    mc "I'll celebrate by scratching off these names one by one."
    mc "Slowly but surely having all of them within the palm of my hands."
    mc "I'll celebrate by having people kneel at my feet."
    mc "They'll be honoured to even witness my presence.{w} They'll gaze upon my visage and call my domains works of art."
    mc "They'll loathe the days that they thought I was nothing."
    mc "...{w} Hahaha..."
    mc "I'll celebrate by ruling this OUTERWORLD!"
    mc "And it'll be on my own, with no strings attatched,{w} no one to answer to."
    mc "And no one who'll ever dare disobey my order."
    window hide
    $ quick_menu = False
    show on_moon_particle onlayer inyourface
    show sun_front onlayer front with dissolve
    show sun_back onlayer back with dissolve
    $renpy.pause(2, hard=True)
    $ persistent.sun = True
    ending "SUN END:{w} On the path to rule"
    stop music fadeout 1.0
    hide on_moon_particle onlayer inyourface
    hide sun_front onlayer front with dissolve
    hide sun_back onlayer back with dissolve
    jump credits

label end_gris:
    # end up being the right hand man of deulithoteq
    # l'eminence gris
    mc "I ran as fast as I could to the Solas Eye Line,{w} dodging people as I moved past them."
    play music "audio/sfx/train.mp3"
    mc "Once I was aboard the line, I closed my eyes and leaned into my seat."
    stop ambient
    hide solas onlayer back with dissolve
    ## black hide solas
    mc "In my sleep I saw dreams of my death today,{w} one that I've managed to successfully escape today."
    mc "But over the course of the ride, I was haunted by walking spectres of the future."
    mc "What's going to happen next?"
    mc "I don't think I'll ever know,{w} but I need to shape a future that will suit me best."
    stop music fadeout 2.0
    show homeb onlayer farback
    show homef onlayer back with dissolve
    play ambient "audio/sfx/basement.mp3"
    play music "audio/music/Confused.wav"
    mc "By the time I got home, there was already a note from Deulithoteq beckoning me again."
    mc "Something about... gathering INSIGHT on Tashen of Tallis."
    mc "I gave Keychee some food and souvenirs of the Solas eye line before leaving."
    mc "After all, I have to answer their call."
    hide homef onlayer back with dissolve
    hide homeb onlayer farback with dissolve
    stop ambient fadeout 2.0
    ending "A few weeks pass by..."
    # sewer bg
    play ambient "audio/sfx/sewer.mp3"
    show sewer onlayer farback with dissolve
    mc "I decided to make best with the situation of Deulithoteq's contract."
    show deu onlayer front with dissolve
    mc "Through dedication and diligence, I quickly became Deulithoteq's most powerful ally and most valuable \"asset\"."
    hide deu onlayer front with dissolve
    show wurm1 onlayer front with dissolve
    show wurm2 onlayer front with dissolve
    mc "Thereby earning the respect of it along with all of the other earwurms."
    mc "They are unexpectedly kind and trusting of me."
    mc "Some of the earwurms even take care of Keychee whilst I'm away doing INSIGHT work for Deulithoteq."
    hide wurm2 onlayer front with dissolve
    hide wurm1 onlayer front with dissolve
    mc "Of course, I have my own line of work too...{w} still have my clients after all."
    mc "Moreover, I collect souls for my own siphon needs as I did before."
    mc "The difference is now I have an additional commitment."
    mc "Much to my surprise, I found the job to be quite rewarding and over time, Deulithoteq became a trusted co-worker."
    mc "The reason I use \"co-worker\" instead of \"boss\" is something I keep to myself."
    mc "For you see, with Deulithoteq's rise in power lead to the rise of my own power."
    mc "My name and Deulithoteq's have travelled around the OUTERWORLD,{w} and when they reach of the ears of others..."
    stop ambient
    mc "They hear this."
    play ambient "audio/sfx/mouth.wav"
    hide sewer onlayer farback with dissolve
    mc "{i}\"Yes, Deulithoteq is the master, its eminence over all information of the OUTERWORLD. \"{/i}"
    mc "{i}\"But you see, there's a second master too.{w} One whose machinations lay concealed...{w} whose power is drawn behind a curtain.\"{/i}"
    mc "{i}\"One who Deulithoteq will listen to without fail.\"{/i}"
    mc "{i}\"There's the grey eminence.{w} A monster who ports a strange visage and a silver tongue.\"{/i}"
    mc "{i}\"They're the one who's behind every decision Deulithoteq makes.\"{/i}"
    mc "{i}\"So...{w} you want all the knowledge in this world?\"{/i}"
    mc "{i}\"Then bow before the Silver-tongued.\"{/i}"
    $ quick_menu = False
    stop ambient fadeout 2.0
    window hide
    show on_moon_particle onlayer front
    show gris_front onlayer front with dissolve
    show gris_far onlayer farback with dissolve
    show gris_back onlayer back with dissolve
    $renpy.pause(2, hard=True)
    $ persistent.moon = True
    ending "MOON END:{w} L'eminence Grise"
    stop music fadeout 1.0
    hide gris_far onlayer farback with dissolve
    hide gris_back onlayer back with dissolve
    hide gris_front onlayer front with dissolve
    jump credits

label end_fool:
    ## rivalry between you and Deulithoteq, Lupin and Zenigatta
    ## fun ending
    hide solas onlayer back with dissolve
    stop ambient
    mc "It was a long walk back home,{w} luckily I managed to hide inside a passing vehicle to make the trip easier."
    show homeb onlayer farback
    show homef onlayer back
    play ambient "audio/sfx/basement.mp3"
    play music "audio/music/Confused.wav"
    show keychee hands nosquint blinkhands hands_smile onlayer front with dissolve
    k "Silver-tongued!{w} I was wondering when you'd come back."
    mc_s "Deulithoteq took a while but I've got it in the bag!"
    hide keychee hands nosquint blinkhands hands_smile onlayer front
    show keychee hands blinkhands nomouth onlayer front
    k "Wait I'm sorry... what happened?"
    mc_s "Apparently they wanted to get some INFORMATION out of me, but it turns out I ended up being their siphon."
    k "I thought you were only focusing on great terrors?"
    mc_s "I was... and still plan to do so my small friend."
    mc_s "But I couldn't resist the opportunity that was right in front of me!"
    hide keychee hands blinkhands nomouth onlayer front
    show keychee down blinkdown onlayer front
    mc "I start laughing."
    mc_s "Honest to Holle, I didn't think I could've pulled it off."
    mc_s "I guess I can be a little greedy sometimes."
    hide keychee down blinkdown onlayer front
    show keychee down blinkdown down_open onlayer front
    k "But it was still extremely risky!{w} We shouldn't tempt fate-"
    mc_s "What on earth do you think Deulithoteq could possibly to do me?"
    k "Well let's see... it knows your address, your sources and..."
    mc_s "Also you."
    hide keychee down blinkdown down_open onlayer front
    show keychee hands handssquint blinkhands onlayer front with vpunch
    k "WHAT? It knows about ME TOO?"
    k "Hey silver-tongued, it was nice knowing you."
    k "But I think I need to be someone else's parasite-"
    k "Nyeh-"
    hide keychee hands handssquint blinkhands onlayer front with vpunch
    mc "Keychee bangs against the jar to try and budge it out of the door."
    mc "...{w} the jar barely even \"shuffles\" a centimetre."
    mc_s "...{w} Keychee you're not getting out of here."
    mc "The parasite sighs."
    show keychee down downsquint blinkdown onlayer front with dissolve
    k "I know."
    hide keychee down downsquint blinkdown onlayer front
    show keychee down nosquint blinkdown down_open onlayer front
    k "Maybe you're right."
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down nosquint blinkdown down_smirk onlayer front
    k "Besides,{w} what can that earwurm do anyway?"
    hide keychee down nosquint blinkdown down_smirk onlayer front with dissolve
    hide homef onlayer back
    hide homeb onlayer farback
    stop ambient
    ending "A few days go by..."
    show solas onlayer back with dissolve
    play ambient "audio/sfx/solas.wav"
    mc "Atop the Solasian Oculus Spire,{w} Khwarzinki the Clairvoyant, the head honcho of Solas, reigns supreme."
    mc "I feel the gelid, crisp sand and dust press against my skin."
    mc "Wrapping the weaves of my scarf against my body, I look up to the tower."
    mc "I'm almost so close I could taste it!"
    mc "Kwarzinki is my first Old Terror that I've managed to get a hold of."
    mc "There's no difference in power between Great and Old Terrors.{w} It's a matter of what they survey."
    mc "Great Terrors are responsible for people."
    mc "Dark Terrors are responsible for concepts."
    mc "... and Old Terrors{w} are responsible for lands and regions."
    mc "Turns out Kwarzinki and an associate of Fernweh's were quite close."
    mc "If I get my fingers around Kwarzinki, it could mean my hands all over Solas!"
    "Just as you're about to open the Spire's gates,{w} you feel a grip on your back."
    stop music fadeout 2.0
    mc_s "...{w}...I."
    d "We meet again Silver-tongue."
    # show deulithoteq sprite here
    play music "audio/music/Deulithoteq.wav" fadein 5.0
    show deu onlayer front with dissolve
    mc_s "Deulithoteq?!{w} What are you doing here?"
    hide deu onlayer front
    show deu_down onlayer front
    d "I could ask you the same thing, but we already know what's going to happen."
    d "Kwarzinki asked us both to come at the same time because it wants to choose one of us over the other."
    hide deu_down onlayer front
    show deu_side onlayer front
    d "Only one of us can gain it's favour."
    mc "I start grinning."
    mc_s "I've already beaten you once before,{w} shouldn't be hard to do the same again!"
    hide deu_side onlayer front
    show deu_smile onlayer front
    d "Well guess what Silver-tongue?{w} I've learnt from your tricks..."
    d "You won't outsmart me again."
    mc_s "We'll see about that."
    hide deu_smile onlayer front
    show deu onlayer front
    play sound "audio/sfx/oculus.mp3"
    "Suddenly,{w} the Oculus spire's gates open:{w} beckoning the both of you to enter the tower."
    "The two of you turn to face each other."
    hide deu onlayer front with dissolve
    hide solas onlayer back with dissolve
    stop ambient fadeout 2.0
    mc_s "May the best monster win."
    d "Heh...{w} may the best monster win."
    "And with that, you both take a step inside."
    $ quick_menu = False
    window hide
    show blue_p onlayer inyourface
    show fool_back onlayer back with dissolve
    show fool_front onlayer front with dissolve
    $renpy.pause(2, hard=True)
    $ persistent.moon = True
    ending "MOON END:{w} Fall for it twice and you're a fool"
    stop music fadeout 1.0
    hide blue_p onlayer inyourface
    hide fool_back onlayer back
    hide fool_front onlayer front
    jump credits

label end_veneer:
    hide solas onlayer back with dissolve
    stop ambient
    mc "It was a long walk back home,{w} luckily I managed to hide inside a passing vehicle to make the trip easier."
    mc "But by the time I got back home,{w} things were everything but easy."
    show homeb onlayer farback
    show homef onlayer back with dissolve
    play ambient "audio/sfx/basement.mp3"
    play music "audio/music/Sad.wav" fadein 1.0
    mc "My house was in complete disarray;{w} the dilapidated floorboards have fell through,{w} the kitchen drawers were broken..."
    mc "...{w} and there was a shattered glass jar on the floor."
    mc_s "Keychee..."
    mc "I searched around the Barraken complex,{w} but nobody saw the parasite leave."
    mc "..."
    mc "The Freske juice was left untouched.{w} I took a sip."
    hide homeb onlayer farback
    hide homef onlayer back
    mc "... and fell asleep."
    show silkerf onlayer back with fade
    show silker onlayer farback with dissolve
    mc "The next day I woke up and packed a bag ready to go to Moowrongo"
    mc "I went over to the Zilker store to see if the G'narg knew where Keychee went."
    mc "Worryingly enough, the G'narg hasn't heard from it since Keychee \"moved\" into my place."
    mc "With not much else to do,{w} I lingered around town and started shopping for things I knew I couldn't afford."
    mc "I just wanted to see what things would look like on my body."
    hide silkerf onlayer back
    hide silker onlayer farback
    stop ambient fadeout 2.0
    "Over the next few days, you stuck to your usual routine."
    "You would scavenge in Melduvia for scraps of food,{w} cook,{w} and read your favourite zines."
    "You weren't so good at keeping track on who was due next,{w} so you started appearing at your clients' houses when you needed energy."
    "Many of them tried to escape or bail to say that it was due a different day,{w} but you didn't care."
    "There was still the dream of conquering the great terrors,{w} and you did it once!"
    "But you had to set your ambitions to be more realistic, and thus, you decided to scale down."
    "You kept your siphoning list small and within Barraken,{w} occasionally venturing into Lusin-scape."
    "Perhaps if you got enough funds from Deulithoteq someday,{w} you could pursue that dream again."
    "So you focused on the dreams that seemed within reach{w} but were ultimately elusive."
    "You started experimenting with changing your form, warping your voice,{w} anything to make you better."
    "But there was always something better than you.{w} Something more beautiful."
    show homeb onlayer farback
    show homef onlayer back with dissolve
    stop music fadeout 2.0
    play ambient "audio/sfx/basement.mp3"
    "One day when you were baking Guulings, you got a message."
    d "{i}\"I have a job that I want you to do.\"{/i}"
    mc "If it's Deulithoteq,{w} I always have to prioritise it first."
    mc "Always answer the call."
    "It was a job regarding picking up information on the demi-terror Tashen."
    "And you were briefly reminded of that dream you once had."
    stop ambient
    hide homef onlayer back with dissolve
    hide homeb onlayer farback
    show sewer onlayer back with dissolve
    play ambient "audio/sfx/sewer.mp3"
    "By the time you arrived to Deulithoteq, you had...{w} an specific request in mind."
    mc_s "Master Deulithoteq,{w} I humbly ask for your aid."
    show deu_up onlayer front with dissolve
    d "In exchange for Tashen's INSIGHT?"
    mc_s "No,{w} it's something to do out of the kindness of your heart."
    hide deu_up onlayer front
    show deu_smile onlayer front
    d "Hahaha..."
    mc_s "And it could potentially make Tashen's blackmail a lot easier."
    hide deu_smile onlayer front
    show deu onlayer front
    d "And what would that be?"
    mc_s "You see the weaver's silk you have?"
    hide deu onlayer front
    hide sewer onlayer back
    stop ambient fadeout 2.0
    ######### dark
    mc_s "Could you make me a new face?"
    $ persistent.blood = True
    ending "BLOOD END:{w} Re-mending your veneer"
    jump credits

label credits:
    hide screen deu_door
    window hide
    $save_name = "-- credits --"
    $ quick_menu = False
    play sound "audio/sfx/title.mp3"
    show mock_zoom
    $renpy.pause(4, hard=True)
    hide mock_zoom with dissolve
    play music "audio/sfx/credits.wav"
    show on_moon_particle onlayer particle
    show credits1 onlayer credit with dissolve
    $renpy.pause(4.5, hard=True)
    show credits2 onlayer credit
    hide credits1 onlayer credit
    $renpy.pause(5.5, hard=True)
    show credits3 onlayer credit
    hide credits2 onlayer credit
    $renpy.pause(5, hard=True)
    show credits4 onlayer credit
    hide credits3 onlayer credit
    $renpy.pause(4, hard=True)
    show credits5 onlayer credit
    hide credits4 onlayer credit
    $renpy.pause(3, hard=True)
    show credits7 onlayer credit
    hide credits5 onlayer credit
    $renpy.pause(3.5, hard=True)
    show credits6 onlayer credit
    hide credits7 onlayer credit
    $renpy.pause(5, hard=True)
    hide credits6 onlayer credit with dissolve
    $ quick_menu = True
    stop music fadeout 2.0
    return


label endgame:
    if persistent.doneritual:
        play ambient "audio/sfx/basement.mp3"
        $ quick_menu = False
        $save_name = "-- INSIGHT --"
        show on_moon_particle onlayer inyourface with dissolve
        show on_moon_particle onlayer inyourface with dissolve
        mc_narr "That...{w} thing is still here."
        mc_narr "But I don't want to see it anymore."
        stop music fadeout 2.0
        mc_narr "Let's look at other things instead."
        ending "CGs in the game:"
        window hide
        show on_moon_particle onlayer inyourface
        show sun_front onlayer front with dissolve
        show sun_back onlayer back with dissolve
        $renpy.pause(2, hard=True)
        $ persistent.sun = True
        ending "SUN END:{w} On the path to rule"
        window hide
        hide on_moon_particle onlayer inyourface
        hide sun_front onlayer front with dissolve
        hide sun_back onlayer back with dissolve
        show on_moon_particle onlayer front
        show gris_front onlayer front with dissolve
        show gris_far onlayer farback with dissolve
        show gris_back onlayer back with dissolve
        $renpy.pause(2, hard=True)
        $ persistent.moon = True
        ending "MOON END:{w} L'eminence Grise"
        window hide
        hide gris_far onlayer farback with dissolve
        hide gris_back onlayer back with dissolve
        hide gris_front onlayer front with dissolve
        show blue_p onlayer inyourface
        show fool_back onlayer back with dissolve
        show fool_front onlayer front with dissolve
        $renpy.pause(2, hard=True)
        $ persistent.moon = True
        ending "MOON END:{w} Fall for it twice and you're a fool"
        window hide
        hide blue_p onlayer inyourface
        hide fool_back onlayer back
        hide fool_front onlayer front
        show flower_far onlayer farback with dissolve
        show flower_back onlayer back
        show lily_p onlayer back
        show flower_front onlayer front with dissolve
        show around_particle onlayer back
        show flower_face onlayer inyourface with dissolve
        show lily_p2 onlayer inyourface
        $renpy.pause(2, hard=True)
        $ persistent.void = True
        ending "VOID END:{w} Calla Lily"
        window hide
        hide flower_far onlayer farback with dissolve
        hide flower_back onlayer back
        hide lily_p onlayer back
        hide flower_front onlayer front with dissolve
        hide around_particle onlayer back
        hide flower_face onlayer inyourface with dissolve
        hide lily_p2 onlayer inyourface
        show who_back onlayer back with dissolve
        show who_front onlayer front with dissolve
        $renpy.pause(2, hard=True)
        $ persistent.void = True
        ending "VOID END:{w} What was your name again?"
        window hide
        hide who_back onlayer back with dissolve
        hide who_front onlayer front with dissolve
        ending "There are also 2 BLOOD ENDs."
        ending "BLOOD END:{w} Re-mending your veneer"
        ending "BLOOD END:{w} Achilles’ Heel"
        show credits6 onlayer credit with dissolve
        $renpy.pause(5, hard=True)
        hide credits6 onlayer credit with dissolve
        ending "See more of arkicade's {a=https://arkicade.itch.io/}games here.{/a}"
        ending "Have a listen to LGM's {a=https://lgmsoundsgoodman.itch.io/}music here.{/a}"
        ending "See Sayumi101's other {a=https://sayumi101.itch.io/}projects here.{/a}"
        ending "Thank you so much for playing and for getting this far."
        ending "I hope you've enjoyed this game :)"
    else:
        play nature "audio/sfx/whisper.mp3"
        play ambient "audio/sfx/basement.mp3"
        $ quick_menu = False
        $save_name = "-- INSIGHT --"
        show on_moon_particle onlayer inyourface with dissolve
        show on_moon_particle onlayer inyourface with dissolve
        show mater onlayer back with dissolve
        mo "..."
        mo "...{w} So after everything, you want to come back here?"
        mo "Why?"
        mc_narr "..."
        mo "You shouldn't be here."
        mo "If anything, you despise everything that I am."
        mo "So why come back?"
        mo "...{w} hahAHHA."
        mo "I should've known better.{w} You're always going to be pathetic."
        mo "And nothing will ever change that."
        mo "..."
        mo "Why do you have that face?"
        mc_narr "What face?"
        mo "The one you have,{w} normally it's so disgusting..."
        mo "And it still is."
        mo "But this one isn't in tears.{w} Or completely dejected."
        mo "If anything you're...{w} smiling?"
        mo "I don't-{nw}"
        mc_narr "It's because I'm going to get rid of you."
        mo "... seriously?"
        mo "HAHAHA you can't get rid of me!"
        mo "I'm EVERYTHING TO YOU,{w} I'm the reason you exist."
        mo "I'm the reason why you push yourself."
        mo "Why you're worth anything more than a WRETCH!"
        mc_narr "It is true that I cannot kill you."
        mc_narr "But I can change you,{w} erode you with time."
        mo "You can't change who you are silver-tongued."
        mo "You just have to live with yourself."
        mo "Oh sure you've tried to ignore me a couple of times."
        mo "But you'll always be tempted, and I'll always be there..."
        mc_narr "If there's anything I learnt it's this."
        mc_narr "It's never about who you ARE,{w} it's who you PRETEND to be."
        mc_narr "If I pretend to be sophisticated, I AM sophisticated."
        mc_narr "If I pretend to be powerful, I AM powerful."
        mc_narr "Actions define us in the eyes of others..."
        mc_narr "Not the stupid wriggling thoughts like you-"
        hide mater onlayer back with vpunch
        mo "SHUT UP!"
        show mater onlayer back with dissolve
        mo "You're JUST BITTER!"
        mo "Oh yess yess so VERY VERY bitter!"
        mo "And I'll tell you why."
        mo "Because when you discovered you had the power of INSIGHT..."
        mo "You thought hey..."
        mo "I wonder what's inside MY mind?"
        mo "..."
        mo "And then you found me."
        mo "YOU FOUND{w} ONLY ME."
        mo "HAHAHhAHAahahHAHHAHAhahahHAHHAHAHAAHHAhahah{nw}"
        mo "Conspicio Mater ohhh it lives on through US!"
        mo "Conspicio Mater will never be dead no."
        mo "As long as the last siphon lives."
        mo "We'll be here."
        mc_narr "You see, that's what I always thought too."
        mc_narr "But then I saw how easily I can change people."
        mc_narr "And I thought it could be easier..."
        mc_narr "...if I tried to change myself."
        mc_narr "And this place needs an overhaul anyways."
        mo "...{w} so you think you're doing this now?"
        mc_narr "Not \"RIGHT NOW\" no."
        mc_narr "It's going to take a lot of time."
        mc_narr "I just thought I'd give you the warning."
        mc_narr "And be better than whatever you were to me..."
        mo "..."
        mo "...{w} You should've never looked in your mind."
        mo "It was always forbidden."
        mc_narr "...{w} I know."
        mc_narr "But really, who decides what's forbidden anyways?"
        mo "The Conspicio Mater."
        stop nature fadeout 2.0
        mc_narr "...{w} hahaha."
        stop ambient
        $ persistent.doneritual = True
    #play ambient "audio/sfx/basement.mp3"
    return
