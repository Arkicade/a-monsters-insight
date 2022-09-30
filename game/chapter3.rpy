label d2_win:
    stop music fadeout 2.0
    play sound "audio/sfx/magic.wav"
    $ showtext = False
    $ showtext2 = False
    $ showinput = False
    window hide
    $ quick_menu = False

    call screen cormeum_victory() with dissolve
    #$rrow.xp = 900
    #$rrow.yp = 1000

    #$ quick_menu = True

    $ search = _return
    $ search = search.lower()

    $ cormeum_sig = search
    jump d2_done


label d2_done:
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    stop nature fadeout 2.0
    hide screen cor_door with dissolve
    hide cardianf onlayer back
    hide cardianb onlayer farback with dissolve
    $save_name = "-- end of dialogue 2 --"
    $cormeum_outcome = "win"
    mc "With my mark imprinted on Cor Meum's mind, it acts like a \"signature\" of some sorts."
    mc "Meaning that I can siphon their mental energy at anytime, as long as the connection is maintained."
    "Congratulations!{w} You've successfully won Cor Meum's favour!"
    "...or whatever is left of them."
    jump chapter3

label chapter3:
    hide screen cor_door
    $ showtext = False
    $ showtext2 = False
    $ showinput = False
    $ temp_charisma = 0
    $ temp_reputable = 0
    $ temp_supreme = 0
    $ temp_knowledge = 0
    $ temp_intellect = 0
    $ inventory = []
    "Here, we can save your progress by overriding the save in the first file slot."
    "Would you like to save?"
    window hide
    menu:
        "Yes (save file to slot 1)":
            #$renpy.save("chapter2", save_name)
            play sound "audio/sfx/save.wav"
            $ purge_saves()
            "Your game has been saved..."
        "No (do not save file to slot 1)":
            "So be it."

    $save_name = "-- reading a zine --"
    $ quick_menu = False
    play sound "audio/sfx/title.mp3"
    show on_moon_particle onlayer inyourface
    show chapter3 with dissolve
    $renpy.pause(5, hard=True)
    hide chapter3 with dissolve
    $ quick_menu = True
    hide on_moon_particle onlayer inyourface
    mc "After stepping outside the Cardian,{w} I felt my body go under."
    mc "I was out of breath, and everything seemed to be slipping away from me."
    mc "...{w} Was I drowning?"
    mc "Thoughts in my head rush back to me."
    mc "Yes... the Cardian."
    mc "It was a spherical capsule in the sky."
    mc "Did I just plummet to my death?"
    mc "The sheer force of falling should've killed me,{w} at least the water was here to break my fall."
    mc "...{w} this is suffocating... almost unbearable."
    mc "I can still breathe,{w} but the fact that I can't see anything is killing me."
    mc "It feels as if you've been wrapped up, restricted."
    mc "I have to swim out of here."
    show riverlong onlayer back with dissolve
    show blue_p onlayer inyourface with dissolve
    play nature "audio/sfx/river.mp3"
    "You rise up to the surface of the water to find yourself, once again, at the Melduvian river."
    mc "I must've been here for a while if the river all the way from Moowrongo made its way here..."
    hide riverlong onlayer back with dissolve
    hide blue_p onlayer inyourface with dissolve
    stop nature fadeout 2.0
    "A short hike later..."
    show homeb onlayer farback
    show homef onlayer back
    play ambient "audio/sfx/basement.mp3"
    show keychee down nosquint blinkdown down_smirk onlayer front with dissolve
    k "Silver-tongued thank goodness you're here!"
    hide keychee down nosquint blinkdown down_smirk onlayer front
    show keychee down nosquint blinkdown down_open onlayer front
    k "There's something you need to see-"
    mc_s "I almost DIED today Keychee..."
    if cormeum_outcome == "lose":
        mc_s "TWICE!"
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down downsquint blinkdown nomouth onlayer front
    mc_s "So I'm not in the mood for any more of your reprimands or your opinions."
    show keychee down downsquint blinkdown down_open onlayer front
    k "But silver-tongued!"
    mc_s "I'm going to sleep."
    mc_s "I didn't even have the chance to take a nap in between yesterday and today."
    hide keychee down downsquint blinkdown down_open onlayer front
    show keychee up nosquint blinkup onlayer front
    k "Wait don't go to sleep! I'll make you breakfast!"
    mc_s "You can't Keychee, you're stuck in a jar remember?"
    "You yawn."
    mc_s "What I need is a shower and a nap-"
    k "No silver-tongued look!"
    hide keychee up nosquint blinkup onlayer front with hpunch
    mc "Keychee shoves its jar across the counter so it can move closer to me."
    show keychee up blinkup onlayer inyourface
    play music "audio/music/Dirt.wav" fadein 1.0
    k "You see this? You're in the AVANT news!"
    hide keychee up blinkup onlayer inyourface
    show keychee up blinkup up_closed onlayer inyourface
    mc_s "What?{w} I'm not newsworthy."
    mc_s "Also I've never heard of them before, probably some independent... underground zine."
    if cormeum_outcome == "win":
        hide keychee up blinkup up_closed onlayer inyourface
        show keychee up blinkup nomouth onlayer front
        k "Well it reported your new alliance with Cor Meum."
        mc_s "What?"
        k "Look!"
        hide keychee up blinkup nomouth onlayer front
        show keychee down blinkdown onlayer front
        show zine_cor onlayer inyourface with dissolve
        play sound "audio/sfx/page.mp3"
        mc "I move the zine towards me and start skimming through the dirty and tarnished papers."
        mc "Yep, that's definitely me... and that's Cor Meum."
        mc "How could they have known about it so soon?"
        mc "It must've been the time it took for me to get out of the river and walk back home."
        mc_s "But that's impossible."
        hide keychee down blinkdown onlayer front
        show keychee down blinkdown down_open onlayer front
        k "What is?"
        mc_s "Keychee, how do you think they knew of my conversation with Cor Meum?"
        k "I...{w} are the details accurate?"
        hide keychee down blinkdown down_open onlayer front
        show keychee down blinkdown nomouth onlayer front
        mc_s "Hmm..."
        mc "I pick up the zine off the counter."
        hide zine_cor onlayer inyourface with dissolve

    else:
        hide keychee up blinkup up_closed onlayer inyourface
        show keychee up blinkup nomouth onlayer front
        k "Well it reported your new alliance with Fernweh."
        mc_s "What?"
        k "See for yourself!"
        show zine_fer onlayer inyourface with dissolve
        play sound "audio/sfx/page.mp3"
        hide keychee up blinkup nomouth onlayer front
        show keychee down blinkdown nomouth onlayer front
        mc "I the zine towards me and start skimming through the dirty and tarnished papers."
        mc "Yep, that's definitely me... and that's Fernweh"
        mc_s "Who could've possibly known about our conversation?"
        mc_s "We had it in the CHASM, meaning only lost souls could go there."
        mc_s "And unless they were called by Fernweh themselves, they wouldn't be able to move freely as I did."
        mc "I pick up the zine off the counter."
        hide zine_fer onlayer inyourface with dissolve

    mc "After further observation I realise that all the details were kept relatively vague."
    mc "{i}\"A conversation had taken place.\" \"There was some conflict.\" \"Parties involved came to an agreement.\"{/i}"
    mc "There's no actual DEFINITIVE information written in this entire thing!"
    mc_s "The fact that they know this is itself a bad sign."
    mc "Wait,{w} who wrote this article?"
    $ met_deu = True
    play sound "audio/sfx/page.mp3"
    mc_s "{i}\"Deulithoteq\"{/i}."
    mc_s "{i}\"The one who knows all\"{/i}?"
    hide keychee down blinkdown nomouth onlayer front
    show keychee down blinkdown down_open onlayer inyourface
    k "Heard of them before?"
    hide keychee down blinkdown down_open onlayer inyourface
    show keychee down blinkdown nomouth onlayer inyourface
    mc_s "...{w} never actually?"
    mc_s "I thought I would have most, if not all, of the great terrors pegged."
    mc_s "If I don't know them, they're not worth my time."
    hide keychee down blinkdown nomouth onlayer inyourface
    show keychee down downsquint blinkdown down_smirk onlayer inyourface
    k "...{w} isn't that what a lot of people would assume about you too?"
    mc_s "The difference is I'm TRYING to stay discrete."
    mc_s "Clearly this Doolithek wants to get their name in the spotlight."
    hide keychee down downsquint blinkdown down_smirk onlayer inyourface
    show keychee up upsquint blinkup onlayer inyourface
    k "You're failing on the discrete part."
    mc_s "I wouldn't call it failing.{w} Be honest Keychee nobody reads the AVANT news."
    hide keychee up upsquint blinkup onlayer inyourface
    show keychee up nosquint blinkup up_closed onlayer inyourface
    k "..."
    mc_s "Listen, I'm going to go shower..."
    mc_s "Hello Keychee?"
    hide keychee up nosquint blinkup up_closed onlayer inyourface with dissolve
    play sound "audio/sfx/flip.mp3"
    mc "The little parasite moves its tail out of the hole in the jar to start flipping through the pages."
    show keychee hands blinkhands nomouth onlayer inyourface
    k "Wait, this is literally just a copy of the same page."
    mc_s "You see how unprofessional they are?"
    k "Silver-tongued, I don't even think this is a real zine."
    k "All of the news they have is outdated, wait!"
    k "This page is straight out ripped off from Doompocalypse!"
    hide keychee hands blinkhands nomouth onlayer inyourface
    show keychee hands blinkhands hands_smile onlayer inyourface
    mc_s "What are you... wait you have a point."
    hide keychee hands blinkhands hands_smile onlayer inyourface
    show keychee down blinkdown nomouth onlayer inyourface
    mc "This zine isn't just messy, it's almost incoherent."
    play sound "audio/sfx/flip.mp3"
    mc "I keep flipping through the pages until I reach the final one."
    play sound "audio/sfx/flip.mp3"
    mc "With it is a date, time, location and a message."
    mc_s "{i}\"I'll be waiting. - Deulithoteq\"{/i}"
    mc_s "HA! What kind of ominous message is that?"
    hide keychee down blinkdown nomouth onlayer inyourface
    show keychee down downsquint blinkdown down_open onlayer inyourface
    k "Silver-tongued! Do not take this lightly!"
    k "This being KNEW of your conversations, and KNOWS where you live."
    mc_s "So...{w}what?"
    mc_s "They're just a journalist they can't hurt me."
    hide keychee down downsquint blinkdown down_open onlayer inyourface
    show keychee down nosquint blinkdown down_open onlayer inyourface
    k "I don't think they're a journalist, all of this is a cover up."
    mc_s "I could look into it with Globin.{w} She'll tell me if this Dolintoq is someone I should keep an eye on."
    k "...{w} that reminds me."
    hide keychee down nosquint blinkdown down_open onlayer inyourface
    show keychee up blinkup nomouth onlayer inyourface
    k "Silver-tongued,{w} Globin says she doesn't wish to associate with you for today."
    mc_s "I'm sorry WHAT?"
    mc_s "Not \"associate\" with me? What kind of nonsense-{nw}"
    mc_s "Fine, academics are always going to be elitist."
    mc_s "I'll ask your G'narg friend at the Zilker."
    hide keychee up blinkup nomouth onlayer inyourface
    show keychee up upsquint blinkup nomouth onlayer inyourface
    k "He... says he doesn't want to associate with you either."
    mc_s "Hold on, why all of a sudden do they want to withhold information?"
    hide keychee up upsquint blinkup nomouth onlayer  inyourface
    show keychee down nosquint blinkdown onlayer inyourface
    mc_s "They were my sources! I haven't changed or done anything."
    hide keychee down nosquint blinkdown onlayer inyourface
    show keychee down blinkdown down_open onlayer inyourface
    k "True I... don't know what to say.{w} I'm sorry."
    mc_s "Unless... it wasn't me who changed, but them."
    mc_s "Wait, what if Doonigotok bought them out?"
    mc_s "THE LITTLE VERMINS!"
    hide keychee down blinkdown down_open onlayer inyourface
    show keychee down downsquint blinkdown nomouth onlayer inyourface
    mc "I smashed my hand on the counter and Keychee's jar slips off the table."
    play sound "audio/sfx/break.mp3"
    hide keychee down downsquint blinkdown nomouth onlayer inyourface with vpunch
    mc "I catch it in the nick of time."
    mc_s "Excuse me Kecyhee."
    show keychee hands handssquint blinkhands onlayer front with vpunch
    k "I ALMOST DIED."
    mc_s "Looks like we're both going to be someone else's meat unless we get a step ahead."
    mc_s "Daringoteen wishes to play this little game huh?"
    mc_s "Buying out my sources and asking me for a meeting."
    mc_s "What could they possibly want?"
    hide keychee hands handssquint blinkhands onlayer front
    show keychee hands nosquint blinkhands onlayer front
    k "I don't have a clue!{w} It couldn't be money... or any artifacts."
    k "Frankly you don't have anything, you're completely broke."
    stop music fadeout 2.0
    mc_s "That's what I'm going to have to solve once I get there."
    mc_s "But, before I do.{w} I'm showering."
    hide keychee hands nosquint blinkhands onlayer front
    show keychee down nosquint blinkdown down_smirk onlayer front
    k "Can you give me some juice before you go?"
    mc_s "Sure."
    mc "I take from FRESKE juice form before and pour it through the hole in Keychee's jar."
    mc_s "Tell me when to stop."
    hide keychee down nosquint blinkdown down_smirk onlayer front
    show keychee down blinkdown down_open onlayer front
    k "OK..."
    hide keychee down blinkdown down_open onlayer front
    show keychee down blinkdown down_open juice_1 onlayer front
    play nature "audio/sfx/pour.mp3"
    mc_s "Now?"
    k "No keep going please."
    hide keychee down blinkdown down_open juice_1 onlayer front
    show keychee down blinkdown nomouth juice_2 onlayer front
    k "...{w}...{w}..."
    hide keychee down blinkdown nomouth juice_2 nlayer front
    show keychee down downsquint blinkdown down_open juice_3 onlayer front
    stop nature
    k "Stop! Okay STOP!"
    mc_s "Yeesh okay I'm stopping."
    hide keychee down downsquint blinkdown down_open juice_3 onlayer front
    show keychee down nosquint blinkdown down_smirk juice_3 onlayer front
    mc "Keychee starts licking the FRESKE juice that's all around in the jar."
    mc "It even starts swimming inside it."
    hide keychee down nosquint blinkdown down_smirk juice_3 onlayer front with dissolve
    "..."
    $save_name = "-- prep for dialogue 3 --"
    play music "audio/music/Menu.wav"
    "After you've washed yourself off, you know you have to start prep for your little..."
    "...{w} \"talk\" with Deulithoteq."
    show screen setup_text("Strategy update")
    ending "Deulithoteq is a strange one."
    ending "You don't know anything about it."
    ending "Appearing to be trustworthy could never help."
    ending "And showing that you KNOW more than it can work too..."
    ending "Perhaps you could intimidate it?"
    ending "Or try to befriend it?"
    ending "Maybe you shouldn't try to be too friendly..."
    ending "If you find some dirt on it."
    ending "Perception could also help."
    menu:
        "On this evening, you decide to..."
        "Read and raise stats (there's nothing else you can do)":
            if mode == "challenge":
                $ points += 2
            else:
                $ points += 3
            "As much as it pains you, it doesn't look like you have any other choice."
            "You have [points] points left to spend."
            $ quick_menu = False
            $ extra_menu = False
            window hide
            show newspaper_bg onlayer inyourface with dissolve
            call screen stat_screen with dissolve
            hide newspaper_bg onlayer inyourface with dissolve
            "You read the papers, trying to find out anything regarding the person who wrote the AVANT article."
            "But it seems like they erased all of their tracks."
            "Or Keychee is right, and the newspaper was just a coverup for something more sinister..."
            $ quick_menu = True
            $ extra_menu = True
            hide homef onlayer back
            hide homeb onlayer farback with fade
            jump start_d3


########################################################################################
#############################################################################################
########################################################################################################
################ A C T U A L    D I A L O G U E    S T A R T S     H E R E #############################
########################################################################################
#############################################################################################
########################################################################################################

label start_d3:
    stop music fadeout 2.0
    $save_name = "-- start of dialogue 3 --"
    "Your preparation time for the Dialogue is up."
    "Now,{w} the silver-tongued will attempt to {b}win{/b} the favour of the interlocutor:{w} Deulithoteq, the one who hears all."
    #### transition
    #### BIG TITLE TRANSITION SCREEN:
    #### Deulithoteq, the one who hears all
    show solas onlayer back with dissolve
    play ambient "audio/sfx/solas.wav" fadein 1.0
    mc "After a couple of hours, I reach the midtown of Solas, the listed location of where I was supposed to be."
    mc "Strangely enough, or perhaps unsurprisingly,{w} nobody in near sight can be seen."
    mc "I'm an hours walk away from the nearest location warper, and caught in an obscure, closed-off location."
    mc "I was early, sure, but I wanted to seem at least competent.{w} Or maybe I should've shown up late to seem like I don't care?"
    mc "What does it matter? The choice has already been made."
    mc "But the most frightening thing is I exactly know how I'm going to handle this."
    mc "I virtually know nothing about them, but they seem to know almost everything about me."
    mc "...{w} ALMOST."
    mc "I need to deduce exactly how much they know and why they've come after me."
    "Suddenly, you hear a knock on 5 doors.{w} On all of the buildings that surround you?"
    mc "What's happening?"
    "Then, an EARWURM approaches you from an underneath tunnel."
    if "earwurm" not in keywords:
        show screen unlock_text("New keyword: EARWURM")
        $ keywords.append("earwurm")
        $ deu_keywords.append("earwurm")
    show wurm1 onlayer front with dissolve
    ear "Please, follow me silver-tongued."
    mc_s "Umm... down there?"
    ear "My sincerest apologies, you aren't an ooze-based organism so you can't slip under."
    ear "Go inside the building two ways up from your right."
    ear "Head straight through the door that's covered in black.{w} Take the ladders down."
    ear "You'll find me underground and I can guide you to the Master."
    hide wurm1 onlayer front with dissolve
    mc "The master eh?{w} Haha, Deulithoteq is going on a little bit of a power trip I see..."
    mc_s "No problem."
    stop ambient
    hide solas onlayer back with dissolve
    play ambient "audio/sfx/sewer.mp3" fadein 1.0
    $renpy.pause(2, hard=True)
    show sewer onlayer back with dissolve
    show on_moon_particle onlayer inyourface with dissolve
    "After navigating through the doors and tunnels you meet with a new earwurm along with the one at Solas."
    show wurm1 onlayer front with dissolve
    show wurm2 onlayer front with dissolve
    ear "Glad to see our GUEST, is still here, we will show you to the Master."
    "You continue walking down through some tunnels filled in an inky sea."
    "There's specks of orange and red sand along the floor and walls where earworms dive in and out."
    "Surprisingly, there's also signs of green fauna in this place."
    "And above in the glass tubes, you can see creatures of the night floating and swimming around."
    "For a supposed nobody, Deulithoteq sure has money to spend."
    "The earwurms that guided you here silently dismiss themselves."
    hide wurm1 onlayer front with dissolve
    hide wurm2 onlayer front with dissolve
    mc "Then, in front of me,{w} finally, the monster of the hour rises before me."
    show deu_up onlayer front with dissolve
    play music "audio/music/Deulithoteq.wav"
    play nature "audio/sfx/destroy.wav"
    play sound "audio/sfx/quake.mp3"
    "Deulithoteq bursts through the ink and wraps its tail around the walls of sand."
    "It resembles a giant earwurm except it seems to be mutating into a Farfallen."
    "As it whips its tail around, trying to escape the quicksand, you notice how Deulithoteq TOWERS over you."
    hide deu_up onlayer front with dissolve
    show deu onlayer front with dissolve
    show screen deu_door with dissolve
    stop nature fadeout 2.0
    "It makes a rattling noise with its mouth and the tendril-gills on the side of its face start shaking."
    play sound "audio/sfx/beast.mp3"
    "It sounds of brass shells knocking up against a metal maze."
    "But you don't know if it's going to fire."
    menu:
        mc_s "So..."
        "So nice to finally meet you Deulithoteq (+ reputable)":
            #charisma
            $ temp_reputable += 1
            d "Huhuhuhuhhh..."
            "It chuckles in a low reverberating voice."
            d "The pleasure is all mine."
            d "I've heard a great deal about you y'know?"
            mc_s "I can tell."
        "What's the deal? (+ supreme)":
            #supreme
            $ temp_supreme += 1
            d "..."
            mc_s "Look, I'm not here to beat around some bushes."
            mc_s "You broke into my house, demanded that I come to this remote location."
            mc_s "So... what gives?{w} You need something settled?"
            d "Not settled.{w} We just need to get one thing started."
        "You've got an... interesting place (- charisma)":
            #reputable
            $ temp_charisma -= 1
            $ deulithoteq_door -= 1
            d "...{w}What are you implying about it?"
            mc_s "It's hidden well beyond underground, about miles from any recognisable place."
            mc_s "You've structured it in such a way that makes it encompass this entire small town."
            mc_s "And its designed to be perfect for Wurms like yourself to travel."
            d "Well colour me surprised.{w} Looks like someone can see."
            mc "Clearly patronizing me,{w} don't have the time to argue with it."
        "How's the weather been? (+ charisma)":
            #charisma plus
            $ temp_charisma += 1
            d "In this sewer? Not any better than whatever is going on up there."
            play sound "audio/sfx/beast.mp3"
            mc "Its voice is so deep that it shakes the ground I stand on."
            mc_s "Oh really? haha...{w} I thought the sand would deal nicely with your... skin..."
            d "It's rough and coarse and gets everywhere.{w} Not as nice as you'd think."
    hide deu onlayer front
    show deu_side onlayer front
    d "I'm not surprised if you were to have some...questions."
    d "But unfortunately it is I who is going to be questioning you."
    mc_s "Me?{w} Last time I recall I haven't been going around committing crimes."
    mc_s "I'm a malformed siphon, something {i}hardly{/i} worth mentioning."
    show screen cue_text("Deulithoteq's skin is brimming.\n   Confident body language.") with dissolve
    hide deu_side onlayer front
    show deu_smile onlayer front
    d "Well you're in luck, because someone took notice."
    hide screen cue_text with dissolve
    mc "The whole POINT was that I didn't want to be noticed,{w} at least not yet."
    mc "I don't know if I or it should be the one making demands."
    mc "But judging by Doolingotok's stature,{w} it definitely has the physical advantage over me."
    mc "Oh well, just have to make sure I don't lose my cool."
    mc_s "As long as the questions are anodyne I could hardly care less."
    hide deu_smile onlayer front
    show deu onlayer front
    d "Fair enough,{w} so, I wanted to know a little bit about your conversation with Fernweh."
    mc_s "And the reason I should tell you is...?"
    hide deu onlayer front
    show deu_down onlayer front
    d "Because you're not leaving until you do."
    mc "The tunnel entrance that I came from was suddenly blocked by blank ink and orange sand."
    mc "I could hear the earwurms enclosing the way out with some arcane magic."
    d "So tell me..."
    hide deu_down onlayer front
    show deu onlayer front
    menu:
        d "What happened?"
        "None of your business (+ supreme)":
            #supreme
            $ temp_supreme += 1
            $ deulithoteq_door -= 1
            d "Excuse me?{w} I thought I could ask-{nw}"
            mc_s "ANODYNE questions.{w} It's disrespectful to discuss what Fernweh confided in me."
            hide deu onlayer front
            show deu_side onlayer front
            d "...{w} so that was a PRIVATE conversation?"
            mc_s "It's one that's sensitive to Fernweh's feelings which I promised not to disclose."
            d "Hmm last time I checked Fernweh didn't have such a strong relationship with you..."
            d "Hell, there was no relationship at all to speak of."
            d "Why would they tell you something that you couldn't tell me?{w} Hmm?"
            hide deu_side onlayer front
            show deu onlayer front
            mc_s "Figure it out for yourself."
            mc "It's better if I just put my guard up."
        "We just had friendly conversation (- reputable)":
            #reputable minus
            $ temp_reputable -= 1
            d "Oh really?{w} Well what kind of \"friendly\" things did you two talk about?"
            mc_s "Honestly, nothing worth mentioning."
            mc_s "Discussion of their meaning in life, the nature of LOST souls..."
            mc_s "You know, armchair philosophy."
            hide deu onlayer front
            show deu_side onlayer front
            d "Riiight."
            hide deu_side onlayer front
            show deu onlayer front
            mc "It {i}definitely{/i} seems unconvinced.{w} But what else can I do?"
        "They summoned me to their home... (+ reputable)":
            #reputable plus
            $ temp_reputable += 1
            mc_s "Because apparently the CHASM called for me."
            hide deu onlayer front
            show deu_up onlayer front
            d "Wait!{w} It did?"
            mc_s "Doesn't have any inherit meaning except that I may be a LOST SOUL."
            d "What?"
            mc "I try to muster a laugh."
            mc_s "What? You didn't think I'd be so straightforward."
            mc_s "Besides, LOST or not, it doesn't matter now."
            mc_s "Anything that should've happened to me was sorted then and there."
            hide deu_up onlayer front
            show deu_down onlayer front
            d "And Fernweh though it was okay to let a LOST SOUL like you go?"
            mc_s "I {i}may{/i} have been LOST or not."
            mc_s "Fernweh made the call that I wasn't."
            hide deu_down onlayer front
            show deu onlayer front
            d "...{w} Interesting."
        "What else would a LOST SOUL do but visit Fernweh? (+ charisma)":
            #charisma plus
            $ temp_charisma += 1
            hide deu onlayer front
            show deu_side onlayer front
            d "You... are a LOST SOUL?"
            mc_s "Yeah and one that made it out too!"
            mc_s "Turns out Fernweh is going a little easier on their constitution on what a \"LOST being\" means."
            mc_s "So I once made the cut, but I don't make it anymore."
            d "... and why is that?"
            mc_s "Because in that miraculous... magical moment, I found my true life's purpose."
            mc_s "And that is...{w} to eat my breakfast which I so sorely miss."
            mc_s "So if you could just let me go...{w} that would be {i}really{/i} sweet of you~"
            hide deu_side onlayer front
            show deu onlayer front
            d "Not. A. Chance."
            mc "Being snarky doesn't work?{w} Fine."

    d "But that wasn't the {i}only{/i} high profile person you came across...{w} no..."
    hide deu onlayer front
    show deu_down onlayer front
    d "The following day, you were invited to the Cardian which hosts Cor Meum,{w} the HEART of the Vena Cava."
    d "And what's shocking is that you somehow LEFT that place without having been assimilated."
    d "You would've been the first person to do so,{w} (second if you count CEREBRUM)."
    menu:
        d "So what happened when you were talking to Cor Meum?"
        "They invited me over so we could see eye to eye (+ reputable  + knowledge)":
            #reputable
            $ temp_reputable += 1
            $ temp_intellect += 1
            d "About...?"
            mc_s "Well they wanted some changes for the Cor Meum structure."
            mc_s "Normally a collective would just... consult itself.{w} But they were wise enough to realise they needed fresh eyes."
            mc_s "Specifically from a singleton perspective."
            mc_s "We mostly had chats about the differences between collective and singleton lifestyles."
            mc_s "I suggested possible improvements."
            hide deu_down onlayer front
            show deu_side onlayer front
            d "Which were?"
            mc_s "Oh! Too many to name and too specific to Cor Meum."
            mc_s "Say, if I write a book on this would you buy it?"
            hide deu_side onlayer front
            show deu_down onlayer front
            d "Most likely not."
            mc_s "But you should really support independent creators!"
            d "..."
        "I went over because I wanted to join the Vena Cava (+ charisma)":
            #charisma
            $ temp_charisma += 1
            hide deu_down onlayer front
            show deu_side onlayer front
            d "And you've returned unassimilated,{w} why?"
            mc_s "Well it was only my {i}orientation{/i} just to get used to the system."
            mc_s "I'll be swiftly joining them soon,{w} have to deal with admin is all."
            d "Last time I checked, joining a collective didn't require so much bureaucracy."
            mc_s "Times have changed my friend."
            d "Have they?"
            mc "It's definitely onto me lying, but what else can I do except go along with it."
            mc_s "I say you and I should take a hike out of this filthy place, and you can see how much has really changed."
            hide deu_side onlayer front
            show deu_down onlayer front
            d "...{w} I'd rather not."
        "This shouldn't concern you (+ supreme)":
            #supreme
            $ temp_supreme += 1
            hide deu_down onlayer front
            show deu_side onlayer front
            d "I don't think whether it concerns me or not matters,{w} what {i}does{/i} matter is that I'm asking you."
            mc "I smile."
            mc_s "Well that's a shame because I don't know if you're going to get a clear-cut answer."
            mc_s "It was a rather... private conversation, and Cor Meum would hate it if I went and told others about it."
            d "Well Cor Meum isn't here-"
            mc_s "I'm a monster of my word,{w} and I know where to draw the lines."
            mc_s "You're overstepping here Doolingotok."
            hide deu_side onlayer front
            show deu_down onlayer front
            d "...{w} It's Deulithoteq."
            d "And if you don't want to tell me,{w} I'll find out one way or another."
        "I... I mean I don't know (- supreme)":
            #supreme minus
            $ temp_supreme -= 1
            d "... you don't?"
            mc_s "Why, they asked me to go...{w} or was it I who brough myself there?"
            mc_s "Getting involved in a collective conscious means I can scarcely remember what's my actions..."
            mc_s "... and what the actions of the Vena Cava were."
            mc_s "There was a lot of bloodshed, ringing in the ears, demands made."
            mc_s "Oh it's too horrible and frightening to remember!"
            mc "Sure it's an act, and I can see it's not buying it.{w} But I need to sell something."

    d "..."
    hide deu_down onlayer front
    show deu onlayer front
    mc "It takes a brief pause, staring at me.{w} Almost like how it beckons the silence between us to speak for it."
    mc "There's a gravity to this moment that wasn't there before."
    mc "There's going to be no more niceties from here."
    mc "It opens its jaws."
    hide deu onlayer front
    show deu_frown onlayer front
    d "I don't think you understand the weight of the situation you're in."
    # CUE
    # POINTER for almost
    if perception > 0:
        show screen testing_text("Test: Perception -> Success", True)
        show screen cue_text("Deulithoteq's teeth are bruxing.\n   It's nervous and worried.") with dissolve
        d "I know {a=call:d3_p1}ALMOST{/a} everything about you."
    else:
        show screen testing_text("Test: Perception -> Failed", False)
        d "I know almost everything about you."
    ### if there's a pointer here THEN be sure to hide the cue_text screen within the pointer
    d "That \"AVANT\" zine had its content filled with information about you."
    if perception > 1:
        hide screen cue_text with dissolve
    hide deu_frown onlayer front
    show deu_side onlayer front
    d "You must've read it, given that the location, time and date of our meeting was written at the back."
    d "So you must've seen what was flipped through."
    mc_s "So?"
    hide deu_side onlayer front
    show deu_frown onlayer front
    d "I didn't know I'd have to spell this out for you,{w} but I'm the one in charge here and I want to make that very clear."
    d "Everything and anything you say can and will be used against you."
    mc "Yeesh, it doesn't need to be so aggressive about it though."
    if perception > 1:
        show screen cue_text("Deulithoteq's skin is twisting.\n   Is it confident or cautious?") with dissolve
    hide deu_frown onlayer front
    show deu_smile onlayer front
    d "In essence, I have the power to RUIN you."
    if perception > 1:
        hide screen cue_text
    d "If you want to walk away from here, free of consequence..."
    hide deu_smile onlayer front
    show deu_frown onlayer front
    d "...the only thing you have to do is comply with what I'm saying."
    menu:
        d "Do you understand?"
        "I do (+ reputable)":
            $ temp_reputable += 1
            #reputable
            d "Hmm... good."
            mc "The best thing I can do right now is just tacitly agree."
            mc "The last thing I want happening is for Dewlingatek to get aggressive."
            "Because that could possibly result in your death."
        "I think it's you who's misunderstanding something (+ supreme  + intellect)":
            #supreme
            $ temp_supreme += 1
            $ temp_intellect += 1
            d "What?"
            ## perception check
            mc_s "You're right that I {i}did{/i} in fact read the contents of the zine."
            mc_s "But there was nothing defamatory or anything scandalous related to me."
            mc_s "I met up with Fernweh,{w} who cares?"
            mc_s "I wanted to join the Vena Cava collective,{w} so does millions of other monsters...?"
            mc_s "I fail to see what you have over me."
            hide deu_frown onlayer front
            show deu_down onlayer front
            d "I-"
            mc_s "Sure of course I'll comply with your questions,{w} because I have nothing to hide."
            mc "In this situation I NEED to gain power over this... thing."
            hide deu_down onlayer front
            show deu_frown onlayer front
            mc "If I establish early on that I'm not going \"quiet\" into that good night,{w} I'll have leverage."
        "... (Don't say anything: - reputable)":
            #reputable minus
            $ temp_reputable -= 1
            d "..."
            hide deu_frown onlayer front
            show deu_smile onlayer front
            d "Huhuhuhhh... choosing not to say anything?"
            d "You must be so frightened... or maybe you don't know what to say."
            d "So what is it?{w} A tacit agreement?{w} Or is it a silent defiance?"
            d "You choose."
            hide deu_smile onlayer front
            show deu_frown onlayer front
            mc_s "...{w} Or maybe you figure it out yourself."
        "Oh! Are you implying I didn't understand the situation before? (+ charisma)":
            #charisma
            $ temp_charisma += 1
            mc_s "No need to {i}spell{/i} it out for me, I wasn't born yesterday Dewlingatok-"
            hide deu_frown onlayer front
            show deu_down onlayer front
            d "Deulithoteq."
            mc_s "Yeah whatever,{w} listen you have to lay out your position I understand."
            mc_s "But don't patronize me okay?{w} Because I think we could learn a little thing about each other/"
            mc_s "I think I'll let myself get comfortable."
            mc "I seat myself in some hard crystallized sand, coated in a layer of gooey ink."
            hide deu_down onlayer front
            show deu_frown onlayer front
            mc "It hardly constitutes as a chair, but it's the most comfortable I can be."

    d "Suit yourself."
    jump phase2_d3

label phase2_d3:
    $save_name = "-- dialogue 3 --"
    hide deu_frown onlayer front
    show deu_up onlayer front
    mc "Oh no.{w} I can see CLEAR as day what it's trying to do."
    mc "Underground network,{w} buying out all of my sources,{w} demanding to answer its questions."
    mc "I somehow got involved in some family crime syndicate?"
    mc "But how?{w} All I did was siphon peoples' souls, I didn't get involved in crime."
    mc "Globin is a research scientist, she wouldn't be involved in this sort of lifestyle."
    mc "The G'narg at Zilker could've fabricated some story about me getting involved in crime."
    mc "But why would he?{w} We hardly met!"
    mc "Unless this isn't about crime at all..."
    mc "The best I can do is sit and wait."
    mc_s "So what happens now?"
    hide deu_up onlayer front
    show deu_side onlayer front
    d "...{w} I'd like to get to know you a little bit better."
    d "Specifically...{w} hmm...{w} I don't know what to start out with first..."
    hide deu_side onlayer front
    show deu_smile onlayer front
    d "How about your parents?"
    mc_s "I'm sorry, my what?"
    hide deu_smile onlayer front
    show deu onlayer front
    d "Parents,{w} the guardians who raised you."
    d "The beings that, through some process, birthed you into existence."
    mc_s "Yeah I don't {i}have{/i} one of those."
    hide deu onlayer front
    show deu_sad onlayer front
    d "What? So were you born from the Void?{w} Formed from The Nothing?"
    mc_s "No.{w} I was-{nw}"
    mc_s "Wait, why are you asking me any of this?"
    show screen cue_text("Deulithoteq's tendrils are spinning.\n   It's growing impatient...") with dissolve
    hide deu_sad onlayer front
    show deu_frown onlayer front
    d "I'm doing the question asking here,{w} remember?"
    hide screen cue_text with dissolve
    hide deu_frown onlayer front
    show deu_side onlayer front
    d "So, your parents-{nw}"
    mc_s "I'm not associated with them anymore."
    menu:
        d "Oh, could you tell me why that is?"
        "Tell the truth (+ reputable)":
            #reputable
            $ temp_reputable += 1
            $ deulithoteq_door += 1
            mc_s "I was born malformed,{w} misshapen,{w} or whatever else you want to call it."
            mc_s "The... Conspicio Mater.{w} It is like a vat of nutrients that forms all of our kind."
            hide deu_side onlayer front
            show deu_down onlayer front
            d "And what kind is-"
            mc_s "Usually they allow us to properly form, and then let us go into the big bright world."
            mc_s "But for me...{w} they figured it would be better if I didn't follow that path."
            mc_s "..."
            mc "What am I doing?{w} I'm not entitled to tell this guy anything."
            mc_s "So yeah, that's why I'm not associated with them, I'm not talking to them."
            hide deu_down onlayer front
            show deu_sad onlayer front
            d "My apologies-"
            mc "Trying to empathize with me? Not a chance."
            hide deu_sad onlayer front
            show deu_down onlayer front
            mc "I see right through you,{w} you're doing the EXACT same thing I'm doing."
        "Lie - I decided to part ways (+ charisma  - reputable?)":
            #charisma
            #minus reputable, no consequence if you pass a charisma test
            $ temp_charisma += 1
            if charisma < 2:
                $ temp_reputable -= 1
            mc_s "I thought that my parents were too controlling of me."
            mc_s "Still care for them though,{w} but I thought it would be best to leave them."
            mc_s "They have a lot of growing to do, but doesn't everyone?"
            hide deu_side onlayer front
            show deu_down onlayer front
            d "What made you want to leave?"
            mc_s "Sometimes when you're born, you come with a certain baggage."
            mc_s "But I needed to drop it off so that I could run faster."
            mc_s "You understand?"
            d "Alright..."
        "Lie - They banished me (+ supreme  - reputable?)":
            #supreme
            #minus reputable, no consequence if you pass a reputable test
            $ temp_supreme += 1
            if (supreme + temp_supreme) < 2:
                $ temp_supreme -= 1
            mc_s "I was born with a blessing and a curse of my strength."
            mc_s "Many of my siblings ended up falling victim to it, in my ignorance as a child."
            mc_s "At first they didn't mind,{w} but it grew too much when I tried to usurp them."
            mc_s "Thus, because they were terrified of what I could do, they banished me out of fear."
            hide deu_side onlayer front
            show deu_sad onlayer front
            d "Wait... so you murdered your siblings, and it was only when you planned to kill your parents-"
            mc_s "Us monsters have different cultures from one another."
            mc_s "It is natural to battle with your siblings to claim superiority."
            mc_s "And it is a tradition in my family to kill the weaker siblings off so that the strongest one remains."
            hide deu_sad onlayer front
            show deu_down onlayer front
            d "...{w} I see."

    d "Next, I was hoping you could tell me more about that pet you keep in your apartment."
    mc "You could hardly call it that."
    hide deu_down onlayer front
    show deu onlayer front
    d "It seems to resemble the Fructa-Gluc parasite species,{w} why do you have one just lying around?"
    mc_s "I don't have it {i}lying around{/i}, I keep it safely kept in a jar."
    d "But why would you KEEP it with you?"
    mc_s "I was going to eat it, but I wasn't particularly hungry that day."
    mc_s "So I just kept it around and got used to it."
    menu:
        d "Would you ever use it on someone else?"
        "Tell the truth (+ reputable)":
            $ temp_reputable += 1
            #reputable
            mc_s "You know what, that thought has never really crossed my mind..."
            hide deu onlayer front
            show deu_side onlayer front
            d "Really?"
            mc_s "It's like a vermin, it remains in the house but I never really acknowledge its existence."
            mc_s "I don't see any potential source of use from it, and it doesn't bother me in return."
            hide deu_side onlayer front
            show deu_down onlayer front
            d "...{w} turn your body around."
            mc_s "What?"
            mc "Seriously? This guy thinks I'm infected from the parasite?"
            "You unwillingly turn around your body, lift all of your limbs for Deulithoteq to see."
            hide deu_down onlayer front
            show deu onlayer front
            d "Sorry, just had to make sure."
        "Lie - Yes (+ supreme)":
            #supreme
            $ temp_supreme += 1
            $ deulithoteq_door += 1
            mc_s "If it needed to be done,{w} without hesitation."
            hide deu onlayer front
            show deu_side onlayer front
            d "What do you mean \"if it needed to be done\"?"
            mc_s "If the parasite were ever in danger of dying without the nutrients of another being,{w} I would find it one."
            mc_s "However, we've been getting by just fine without the need for it."
            mc_s "Well...unless..."
            mc_s "If someone ever stood in my way,{w} threatened me and my home."
            mc "... or Keychee."
            hide deu_side onlayer front
            show deu onlayer front
            d "Would you never use it on someone else for leverage or gain?"
            mc_s "Oh please,{w} I'm not so cheap to use such tactics."
        "Lie - No (+ charisma)":
            #charisma
            $ temp_charisma += 1
            mc_s "That parasite attached itself to me once,{w} why would I ever want to inflict that kind of pain on someone else?"
            d "So you would never use it, even if you had something to gain from it-"
            mc_s "It's not just me I'd have to consider,{w} but also whether the parasite would attach itself."
            mc_s "Point is I could never see a situation where I'd use it."
            mc_s "And I don't want to."

    hide deu onlayer front
    show deu_sad onlayer front
    d "So that parasite is not used as any kind of weapon?"
    mc_s "No, I'd never inflict on it that kind of responsibility."
    mc "I don't exactly like referring to Keychee as {i}\"that parasite\"{/i}."
    mc "But the moment this bile finds out I'm slightly interested in Keychee's wellbeing,{w} it'll only be in harms way."
    mc_s "It's not exactly that {i}thing{/i} would even listen to me."
    hide deu_sad onlayer front
    show deu_side onlayer front
    d "Hmm..."
    hide deu_side onlayer front
    show deu_up onlayer front
    mc "Then,{w} I see it take out a piece of Vellum from the ashes of sand.{w} You could still smell the veal that it came from."
    mc "Using one of its tendrils, it starts writing down information on the vellum canvas."
    d "And finally...{w} let's get to the point."
    stop music
    d "Your power of INSIGHT."
    d "Can you-{nw}"
    mc "How... how does it know?"
    mc "Since when-{nw}"
    mc "I don't understand. I never said-{nw}"
    play music "audio/music/Tension.wav"
    "The lights are off.{w} Your mind starts to close in and your sensations numb."
    "You don't feel scared, frightened..."
    "Not even surprised or shocked or curious."
    "Just.{w} Confusion, ringing in your head, fading in and out."
    mc "No.{w} FOCUS."
    hide deu_up onlayer front
    show deu onlayer front
    d "You know as well as I do that there are gifted monsters, granted special abilities unique to their kind."
    d "There have been legendary ones such as the UNCONTESTED STRENGTH{w} or the power of CLAIRVOYANCE."
    d "Most monster species have subpar powers such as the power of MISERY or the power of INVISIBILITY."
    d "But I don't think I've ever heard of the power of INSIGHT before,{w} and more interesting than that..."
    ### CUE deulithoteq is LYING
    hide deu onlayer front
    show deu_down onlayer front
    if perception > 1:
        show screen cue_text("Deulithoteq's skin is peeling.\n   It's deceiving you.") with dissolve
    d "I've never heard of the species that is associated with that power."
    if perception > 1:
        hide screen cue_text with dissolve
    menu:
        d "So tell me silver-tongued, what ARE you and what can your power really do?"
        "How would I know? (+ reputable)":
            #reputable
            $ temp_reputable += 1
            mc_s "Remember when I said I don't associate with my parents anymore?"
            mc_s "Yeah, that's probably why I know little to nothing of my origin or powers."
            mc "This, of course, is a lie.{w} But the last thing I need is Doolingodong knowing about my INSIGHT."
            mc "Or about me being a siphon..."
            hide deu_down onlayer front
            show deu_smile onlayer front
            d "But surely you must've used it at some points if you have referenced it."
            mc_s "References to abstract concepts mean nothing, it's just a codeword I developed for my tactics."
            hide deu_smile onlayer front
            show deu_side onlayer front
            d "Tactics?"
            mc_s "You know the core components that go into a conversation?"
            mc_s "The things that go in when you want to convince a person to do something?"
            mc_s "Kind of what you're doing actually..."
            mc_s "Getting the presence of your character right,{w} knowing all the prescience beforehand,{w} and having good perception."
            mc_s "That's when you've got good INSIGHT."
            mc "I take a pause and flop myself down into the floor to relax."
            mc_s "Unfortunately my dear friend, you don't seem to be a really friendly companion.{w} Work on being more charismatic."
            d "..."
        "My power wasn't {i}given{/i} to me (+ supreme  + knowledge)":
            #supreme
            $ temp_supreme += 1
            $ temp_knowledge += 1
            mc_s "I EARNT it and LEARNT it myself you see."
            hide deu_down onlayer front
            show deu_sad onlayer front
            d "But I thought-"
            mc_s "You thought incorrectly,{w} every monster is made out of their actions and words."
            mc_s "The building blocks of us are only a starting point."
            mc_s "So this \"power\" you speak of is just something that I'm fascinated by."
            hide deu_sad onlayer front
            show deu_side onlayer front
            d "And that is?"
            mc_s "I... like people. Talking to them, trying to understand what they're thinking."
            mc_s "The \"power of INSIGHT\" is just an expression for that."
            hide deu_side onlayer front
            show deu_down onlayer front
            d "It doesn't mean that it's attached to any supernatural ability."
            mc_s "Precisely."
            mc "...not true.{w} But you roll with what you've said."
            mc_s "It's my little lucky charm,{w} it's how I get things done... people made."
            mc_s "Or how people like you get ruined.{w} Or when I know someone's crossing a line."
            mc_s "No, I'd figure we're way past that liminal now."
            hide deu_down onlayer front
            show deu_side onlayer front
            d "..."
        "I am not a part of any {i}species{/i}... (- charisma  + intellect)":
            #charisma minus
            $ temp_charisma -= 1
            $ temp_intellect += 1
            mc_s "No one claimed me, and I never knew who my parents were get it?"
            mc_s "So to be honest, I wouldn't know.{w} And to be frank, I would never want to know."
            mc_s "If you want to do the research into it that's fine, don't expect to drag me into this."
            hide deu_down onlayer front
            show deu_smile onlayer front
            d "Aren't you the least bit curious to know where you came from and the legacy behind it?"
            d "Didn't your parents ever explain to you these things?"
            mc_s "They chose not to,{w} and I didn't stick long enough to find out."
            mc_s "Barely knew them..."
            mc "That was because the one that {i}birthed{/i} me soon after tried to murder me."
            "But you don't want to talk about that."
            hide deu_smile onlayer front
            show deu_side onlayer front
            d "You're definitely a part of something though, otherwise why would you have that power?"
            mc_s "The power isn't exactly a supernatural or some arcane magic."
            mc_s "It's more of something I made up for myself rather than something that's a non-abstract ability."
            mc "This of course, is a lie.{w} My INSIGHT does work."
            mc "But of everything that I am, the last thing this Dewlingatog needs to know is the ability that I have."
        "Wouldn't it be more fun if you found out? (+ charisma)":
            #charisma
            $ temp_charisma += 1
            $ deulithoteq_door -= 1
            d "Oh please, not this again."
            mc_s "What? You're already bombarding me with questions? Why not ask a few more?"
            hide deu_down onlayer front
            show deu_frown onlayer front
            d "Silver-tongued."
            d "I'm sorry if you feel-"
            mc_s "Oh don't be sorry, keep going.{w} If you cared about my {i}feelings{/i} you would've let me go."
            mc_s "You would've not broken into my house.{w} You wouldn't have invaded my privacy or threatened me..."
            mc_s "...{w} if you cared about my {i}feelings{/i}."
            d "..."
            mc "I can feel the tension in Dewlithotech growing. Can't make it too mad."
            mc "I muster a laugh and ease into a chair in the floor."
            hide deu_frown onlayer front
            show deu_side onlayer front
            mc_s "Haha! Oh come on I'm joking. I'm JOKING."
            mc_s "Seriously though, I would've told you if I knew.{w} So that's why I ask if you can figure it out yourself."
            mc_s "Do me a favour and give me a call if you could, that would be nice."

    stop music fadeout 2.0
    mc_s "And also, one other thing."
    mc_s "And what's with all the questions? Are you writing some lucubration on me?"
    mc_s "At least let me get some of the academic funds, or compensate me for this time."
    hide deu_side onlayer front
    show deu_smile onlayer front
    play music "audio/music/Losing.wav"
    d "So you aren't even remotely aware of what an {i}anomaly{/i} you are?"
    mc_s "I'm not a product of nature nor any sort of {i}defect{/i}-"
    hide deu_smile onlayer front
    show deu_up onlayer front
    d "I NEVER said the word defect,{w} I said that you're something out of the ordinary."
    d "It doesn't insinuate that you're better or worse than anybody else."
    hide deu_up onlayer front
    show deu_smile onlayer front
    d "You're just channelling your own insecurities in my words."
    mc_s "Tch."
    hide deu_smile onlayer front
    show deu_sad onlayer front
    d "Why do you feel like you're inferior-"
    mc_s "I don't remember you introducing yourself as my therapist."
    hide deu_sad onlayer front
    show deu_down onlayer front
    mc_s "Because if you are, this has to be the most unconvincing sell you've ever made."
    mc "Although now with these questions, things do start to make sense."
    mc "So we can eliminate the possibility of it thinking that I'm a part of some crime syndicate."
    mc "No, it seems to be more interested in my past.{w} Who I am as a species member, my parents and my powers."
    mc "There's either some secret artifact related to my species or..."
    mc "But no, why would they ask about Keychee?"
    mc "Keychee is not related to any grand history.{w} Hell, Deuleethotek seemed to be more informed as to what Keychee was over me."
    mc "It knew the specific type of parasite Keychee is."
    mc "The only connecting factor...{w} is me."
    mc "But why would it concern itself with a nobody like me?"
    mc "Unless..."
    hide deu_down onlayer front
    show deu onlayer front
    d "Also, I noticed you didn't answer my earlier question on INSIGHT."
    d "You just kind of blanked out."
    hide deu onlayer front
    show deu_frown onlayer front
    d "So I would like to ask again about your power of INSIGHT-"
    mc "Sometimes you just get bombarded with too many questions that it becomes more than enough."
    mc "Come ON we don't have to do this!"
    mc "Listen to this guy, has the audacity to tell me what do to."
    mc "Asking ME questions.{w} Think it's the one in control?"
    mc "This stops here."
    "Now is the time to use the power of INSIGHT to enter Deulithoteq's mind."
    stop music fadeout 2.0
    "Find the KEYWORD that could help you."
    play music "audio/music/Insight.wav"
    hide deu_frown onlayer front with dissolve
    jump phase3_d3

label phase3_d3:
    #### code an INSIGHT section here
    ### INSIGHT: NEW KEYWORD TIME
    ### need to ensure player has READ the "Cor" section first of phase 4 before
    ### moving here otherwise they won't have the information
    window hide
    $ quick_menu = False

    call screen deu_twomind(d3_surveiltime()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()


    if search == "surveil":
        mc "The power of SURVEIL?"
        mc "So THAT's how this wurm knows of all my conversations!"
        mc "It was never there,{w} it could just overhear the last few seconds of the dialogue."
        jump phase3_d3_afterinsight

    elif search == "backspace":
        window show
        $showinput = False
        "Wait, I know the answer is hiding in plain sight."
        "The answer is there... {u}UNDERLINED AND UPPERCASE{/u}."
    else:
        $showinput = False
        "Wait, I know the answer is hiding in plain sight."
        "The answer is there... {u}UNDERLINED AND UPPERCASE{/u}."


    jump phase3_d3

label phase3_d3_afterinsight:
    stop music fadeout 2.0
    if "surveil" not in keywords:
        show screen unlock_text("New keyword: SURVEIL")
        $ keywords.append("surveil")
        $ deu_keywords.append("surveil")
    show deu_frown onlayer front with dissolve
    d "URggh-{w} sorry one second."
    hide deu_frown onlayer front
    show deu_up onlayer front
    "Deulithoteq's body starts squirming around, going in and out of the floor of the tunnel."
    "The orange sand and ink start to blend together and swim past the earwurm's body."
    play sound "audio/sfx/shargoth.mp3"
    "It falls into the floor and then comes directly out of the ceiling again.{w} Almost like it was transporting."
    hide deu_up onlayer front
    show deu_frown onlayer front with vpunch
    play nature "audio/sfx/destroy.wav"
    play sound "audio/sfx/quake.mp3"
    d "ARGhh what's this ringing in my ear?"
    play sound "audio/sfx/beast.mp3"
    d "(X)(X)"
    show wurm1 onlayer inyourface with dissolve
    show wurm2 onlayer inyourface with dissolve
    "Two smaller earwurms appear before Deulithoteq, crawling from the ceiling."
    play sound "audio/sfx/shargoth.mp3"
    d "(X)(X)(X)(X)(X)(X)"
    ear "Yes right away Master!"
    ear "(X)"
    stop sound
    stop nature fadeout 2.0
    "And then they disappear."
    hide wurm1 onlayer inyourface with dissolve
    hide wurm2 onlayer inyourface with dissolve
    mc "I can't understand what they're saying in that greasy deep language,{w} but I'm guessing it's some archaic Earwurm stuff."
    mc "Maybe Araknissen?"
    hide deu_frown onlayer front
    show deu_sad onlayer front
    d "I apologize,{w} but I'm feeling quite unwell as you can probably see."
    mc "Oh it's going to feel more unwell after I spill the news."
    mc_s "Don't worry, these kind of things happen with age."
    hide deu_sad onlayer front
    show deu_side onlayer front
    d "???"
    mc_s "Trust me I'd know."
    mc_s "But speaking of my knowledge, you know what else I do know?"
    mc_s "I'll spare you the trouble of any meaningless persiflage."
    play music "audio/music/Confused.wav"
    mc_s "You may know a lot about me, but you're mistaken if you don't think I didn't come here prepared."
    mc_s "Why don't YOU tell me about your power?"
    mc_s "You know,{w} the power of SURVEIL?"
    show screen cue_text("Deulithoteq's teeth are bruxing\n     vociferously. It's panicking.") with dissolve
    d "I don't know what you're-"
    hide deu_side onlayer front
    show deu_up onlayer front
    d "Arghh!"
    hide screen cue_text with dissolve
    d "I DON'T know WHAT-{nw}"
    mc_s "Don't play dumb with me, you went on this whole tangent about me needing to comply and answer your questions."
    mc_s "What happened to that noble honesty hmm?{w} So if you're going to bring up my past I have a right to bring up yours."
    mc_s "You and I both know that each power is assigned to a specific species."
    mc_s "Last time I checked, Earwurms weren't naturally gifted with the power of SURVEIL."
    mc_s "So what's happening with that?{w} What ARE YOU Dewlithutek-"
    hide deu_up onlayer front
    show deu_frown onlayer front
    d "The name is DEULITHOTEQ.{w} Last time silver-tongue."
    d "And if you can... recall..{w} urhg."
    hide deu_frown onlayer front
    show deu_up onlayer front
    mc "My use of INSIGHT on people leave mostly the consistent side effects of fatigue, pain in the head, chills, nausea..."
    mc "But it seems that Deulithoteq in particular is suffering the worst parts of the side effects."
    mc_s "You're not really in a condition to talk back to me now."
    mc_s "But if I can tell you about my INSIGHT, you can tell me about your SURVEIL can you?"
    hide deu_up onlayer front
    show deu_down onlayer front
    d "...{w} you... already know what it is don't you?"
    d "Why do you need to hear it from me-{w} ARUHGHhh{nw}"
    hide deu_down onlayer front
    show deu_up onlayer front
    mc "The power of SURVEIL:{w} the ability to record the last few seconds of any conversation."
    mc "There are boundaries on distance and a limit cap on the number of recordings."
    mc "But it means that Deulithoteq...{w} hey I got the name right!"
    mc "Anyways,{w} I'm guessing this is the means through which Deulithoteq knew of my conversations."
    mc "And it's why it has been particularly vague of the details, and asked me for information regarding it."
    mc "Moreover, it doesn't seem like I'm the only person Deulithoteq does this whole \"interrogation\" shtick on."
    mc "I saw a number of other people that have been recorded in Deulithoteq's mind."
    mc "But I need to know why it's keeping track on a bunch of {i}seemingly{/i} random nobodies."
    "Whilst you're in thought,{w} you notice Deulithoteq slowly recovering from the aftereffects."
    hide deu_up onlayer front with dissolve
    play nature "audio/sfx/destroy.wav"
    "It stops wriggling in the dirt and begins to rise up in front of you."
    "You stand in front of its gaping jaw."
    show deu_frown onlayer front with dissolve
    stop nature fadeout 2.0
    d "We're not having this conversation anymore."
    mc_s "We ARE if you don't want to experience that pain again..."
    d "..."
    hide deu_frown onlayer front
    show deu_side onlayer front
    d "Tch.{w} Of course I should've known you were the cause of it."
    play sound "audio/sfx/shargoth.mp3"
    d "If you do that again I WILL...{w}...urgh."
    hide deu_side onlayer front
    show deu_up onlayer front
    mc "Truth be told, I actually can't do INSIGHT straight after unless I want to experience some mental strain."
    mc "Using INSIGHT too many times costs me a certain amount of my siphoned energy."
    mc "I'm expected to get some more..."
    "That's when a thought crossed your mind."
    mc "Wait!{w} If Deulithoteq wants something from me, then at least I can get something in exchange."
    mc "What if I ask it to make me its siphon?"
    mc "Granted, that wasn't the first objective for this conversation.{w} But given the direction this is going..."
    mc "We both have a certain leverage over each other, but I have something to gain if its Deulithoteq's mental energy."
    mc "Granted, it may be a bit weak due to it suffering the effects far more than usual.{w} But at least it's something."
    mc "But I should also focus on not losing anything important to Deulithoteq in the process too."
    stop music fadeout 2.0
    mc_s "Don't worry, it {i}was{/i} an accident the first time I used it."
    mc_s "More of like an instinctual reaction when a predator seems near,{w} I just..."
    mc "What am I making up this time?"
    mc_s "I emit an aura that causes a pain in your head, chills nausea and... well whatever else you're experiencing."
    hide deu_up onlayer front
    show deu onlayer front
    d "And you did this when you were scared."
    mc_s "When I felt attacked."
    if perception > 1:
        show screen cue_text("Deulithoteq's tendrils are spinning.\n   It's deceiving you.") with dissolve
    d "I'm not trying to hurt you."
    if perception > 1:
        hide screen cue_text with dissolve
    mc_s "But you're certainly capable, and you've blocked the exit and you've made threats about it."
    hide deu onlayer front
    show deu_smile onlayer front
    d "Those... were just vague gestures to threats!{w} They weren't... actual threats on your life."
    mc "Trying to retread its words?{w} Maybe this shows that its tacitly acknowledging my potential."
    hide deu_smile onlayer front
    show deu_side onlayer front
    d "Didn't know about that whole \"aura\" emission thing."
    mc_s "Listen,{w} I'll gladly tell you anything you want to hear."
    mc_s "I'll comply."
    mc "As long as it suits me."
    mc_s "But I have to know that this is a situation of mutual trust,{w} that this isn't one sided."
    mc_s "So if you're going to {i}get to know me{/i}..."
    mc "For whatever reason that I need to figure out as well."
    mc_s "Then I have a right to {i}get to know{/i} you as well see?"
    hide deu_side onlayer front
    show deu_down onlayer front
    play music "audio/music/Deulithoteq.wav"
    d "So the questioned has become the questioner?"
    mc_s "...{w} yes."
    hide deu_down onlayer front
    show deu onlayer front
    d "Fine, ask me what you want."
    d "But, unfortunately, there won't be much to tell."
    "The Questioning will now begin."
    "Use the KEYWORDs you have so far to ask Deulithoteq about them."
    "Or perhaps you can ask about non-KEYWORDs too?"
    "Be warned because ONCE you've asked a question about a KEYWORD, that's it."
    "You cannot go back to it."
    jump phase4_d3

label phase4_d3:
    ## rest of the conversation should be talking of Deulithoteq's history
    ## how it sells and uses information
    ## about IO, about the power of SURVEIL etc.
    ### PICK UP KEYWORDS by using the two keywords first
    ### also put in POINTERS later
    d "Do you have anything else left to ask?"
    call screen questioning_input("phase7_d3")

    $ question = _return
    $ question = question.lower()
    if question =="surveil":
        if "surveil" in keywords and deuQsurveil == False:
            jump d3_Qsurveil
        elif deuQsurveil:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "earwurm":
        if "earwurm" in keywords and deuQwurm == False:
            jump d3_Qwurm
        elif deuQwurm:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."

    elif question == "recruit":
        if "recruit" in keywords:
            jump d3_Qrecruit
        else:
            "You don't have this KEYWORD."

    elif question == "contract":
        if "contract" in keywords and deuQcontract == False:
            jump d3_Qcontract
        elif deuQcontract:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."

    elif question == "information":
        if "information" in keywords and deuQinformation == False:
            jump d3_Qinformation
        elif deuQinformation:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."

    elif question == "secret":
        if "secret" in keywords:
            jump d3_Qsecret
        else:
            "You don't have this KEYWORD."

    elif question == "goal":
        if "goal" in keywords:
            jump d3_Qgoal
        else:
            "You don't have this KEYWORD."

    elif question == "mutant":
        if "mutant" in keywords and deuQmutant == False:
            jump d3_Qmutant
        elif deuQmutant:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    else:
        d "I'm sorry, what was that?"

    jump phase4_d3



#############################
################## H I R E
############################

label phase6_d3_lackey:
    ### INSIGHT: NEW KEYWORD HIRE
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_1() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_lackey_d2

    elif search == "room2":
        jump phase6_d3_lackey_d3
    else:
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    jump phase7_d3

label phase6_d3_lackey_d2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_2(d3_hire2()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_lackey

    elif search == "room2":
        if "key_1" in inventory:
            jump phase6_d3_lackey_d4
        else:
            "You don't have the key to access this door."
            jump phase6_d3_lackey_d2

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        "Incorrect answer."

    jump phase7_d3

label phase6_d3_lackey_d3:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_3(d3_hire3()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_lackey

    elif search == "room2":
        if "key_2" in inventory:
            jump phase6_d3_lackey_d5
        else:
            "You don't have the key to access this door."
            jump phase6_d3_lackey_d3

    elif search == "brazen":
        if "key_1" not in inventory:
            play sound "audio/sfx/key.wav"
            "You obtained the first key."
            ### temporary key placeholder
            $inventory.append("key_1")
            $showinput = False
        jump phase6_d3_lackey_d3

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_lackey_d3

    jump phase7_d3

label phase6_d3_lackey_d4:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_4(d3_hire4()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room2":
        jump phase6_d3_lackey

    elif search == "room":
        jump phase6_d3_lackey_d2

    elif search == "commission":
        if "key_2" not in inventory:
            play sound "audio/sfx/key.wav"
            "You got the second key."
            ### temporary key placeholder
            $inventory.append("key_2")
            $showinput = False
        jump phase6_d3_lackey_d4

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_lackey_d4

    jump phase7_d3

label phase6_d3_lackey_d5:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_5(d3_hire5()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room2":
        jump phase6_d3_lackey_d6

    elif search == "room":
        jump phase6_d3_lackey_d3

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_lackey_d5

    jump phase7_d3

label phase6_d3_lackey_d6:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_6() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_lackey

    elif search == "room2":
        jump phase6_d3_lackey_d5

    elif search == "hire":
        jump phase6_d3_hire

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        "Despite all the searching, you couldn't find the answer..."

    jump phase7_d3

label phase6_d3_hire:
    stop music fadeout 2.0
    hide screen text_timer
    ### this results in a WIN or a DRAFT outcome depending on the menu and stats
    "As soon as you exit the mind of Deulithoteq, you hear a bellowing roar erupt from its mouth."
    play sound "audio/sfx/beast.mp3"
    "It vociferously thrashes the wall of ink and sand as it had done before the first time you used INSIGHT."
    "The more you use it, the greater the effect it seems to leave on the mind you enter."
    "But even you feel slightly drained from using it twice within one sitting."
    "The power of INSIGHT, like all powers, doesn't come without a price."
    show deu_up onlayer front with vpunch
    play nature "audio/sfx/quake.mp3"
    play sound "audio/sfx/shargoth.mp3"
    d "ARGHHHHhh again with the pain?!"
    show wurm1 onlayer front with dissolve
    show wurm2 onlayer front with dissolve
    mc "From the rooms, I see the earwurms that had come before begin to aid Deulithoteq's symptoms."
    mc "Larvae would chew off at the tendrils and a multicoloured moisture was applied to its skin."
    mc "The earwurms would be busy pushing sand off and on Deulithoteq's head while speaking in that archaic language as before."
    mc "Perhaps it was some kind of healing ritual for earwurms... but it seems to be working."
    d "Enough! You are dismissed."
    stop nature fadeout 2.0
    stop sound fadeout 1.0
    mc "The earwurms bid a farewell and dive back into the ink of the walls and ceilings."
    hide wurm2 onlayer front with dissolve
    hide wurm1 onlayer front with dissolve
    hide deu_up onlayer front
    show deu_smile onlayer front
    d "Oh haHAHAHA not you! You are NOT going anywhere."
    mc "It points all of its tendrils at me."
    d "The {b}exact same pain{/b} twice in a row and it {i}only{/i} occurs when you're here?"
    hide deu_smile onlayer front
    show deu_frown onlayer front
    d "I don't think this is a coincidence would you say?"
    mc_s "Deulithoteq! I think this must all be some kind of misunderstanding-"
    d "Misunderstanding WHAT?"
    mc_s "Perhaps you suffer two incidents of the same pain concurrently..."
    mc_s "... because you are afflicted by some sort of illness?{w} An unnoticed disease?"
    hide deu_frown onlayer front
    show deu_smile onlayer front
    play sound "audio/sfx/shargoth.mp3"
    d "AHAHAHAHA...{w} AHAAHAHAHHAHAHAAH HUHUHUHUH{nw}"
    mc "Its roar rings against my ears, drowning my voice in the hollow..."
    stop sound
    mc "Rendering everything it has said in comparison as a whisper."
    hide deu_smile onlayer front
    show deu_sad onlayer front
    play music "audio/music/Confused.wav"

    d "The only {b}DISEASE{/b} I see here, is your delusion Silver-tongued."
    mc "So denying it only makes things worse. I guess the best thing I can do is be honest."
    mc_s "...{w} Y'know what?{w} Fair enough."
    mc_s "No more condescension. Got it."
    mc_s "So I'll tell it like it is."
    mc "Now here's the line you cross between reality and... {i}creative{/i} liberties."
    mc_s "Yes I caused your pain, BUT it was to demonstrate something."
    mc_s "I can do it again, and your earwurms can't heal you every single time."
    mc_s "Because every single time I do {i}it{/i}, the side effects will only get worse for you."
    mc_s "Until... there will be no more you at all."
    hide deu_sad onlayer front
    show deu_down onlayer front
    d "..."
    mc "Without a moment's hesitation, Deulithoteq speaks the language of the wurms again to summon them."
    play sound "audio/sfx/shargoth.mp3"
    d "(X) (X) (X) (X) (X)."
    mc "This could only be a bad thing."
    mc_s "Ho-Hold on there, I never said anything about me {i}following{/i} through with doing it again!"
    hide deu_down onlayer front
    show deu_side onlayer front
    d "Oh there's no need for me to guess if you'll \"do it again\" if there is no {i}you{/i}.{w} Capiche?"
    d "Say any last words Silver-tongued-{nw}"
    mc_s "You see that's funny because I don't think you'd want me dead."
    hide deu_side onlayer front
    show deu_smile onlayer front
    d "AHAHHAAHA{nw}"
    d "Oh yes, I {i}VERY{/i} much want that to be the case."
    mc "It guffaws at me more; almost in tears because of how ridiculous it thinks this whole situation is."
    mc "From the grin on its face, I think it'll take immense pleasure in seeing my death right now."
    mc "But we need to stay away from that outcome."
    mc_s "I mean, wouldn't it be foolish to murder the greatest asset you have?"
    hide deu_smile onlayer front
    show deu_frown onlayer front
    if (charisma + temp_charisma) > 2:
        show screen testing_text("Test: Charisma -> Success", True)
        d "... I'm sorry {b}my{/b} greatest asset?"
    else:
        show screen testing_text("Test: Charisma -> Failed", False)
        $ deulithoteq_door -= 7
        d "The AUDACITY of you..."
        d "My GREATEST ASSET?"
        d "I'll have you know that I have better..."
        hide deu_frown onlayer front
        show deu onlayer front
        d "Sorry little silver-tongued, but you'll have to find someone ELSE who's buying what you're selling."
        jump phase7_d3
    mc_s "To tell you the truth, I wasn't being completely transparent about the power of INSIGHT."
    mc_s "Isn't that what you asked me to explain? For me to come all the way here?"
    mc_s "So now I'm here, ready to disclose the proper details-"
    stop music fadeout 2.0
    d "So you were lying before."
    mc_s "...{w} yes."
    hide deu_frown onlayer front
    show deu_down onlayer front
    d "Did I not say to specifically comply?"
    d "And compliance encompasses telling the truth does it not?"
    if (knowledge + temp_knowledge) > 2 and (reputable + temp_reputable) > 2:
        play music "audio/music/Gaining.wav" fadein 1.0
    else:
        play music "audio/music/Losing.wav" fadein 1.0
    mc_s "Yes yes yes but the past is the past!"
    mc_s "And to be fair, I wasn't lying as much as I was choosing not to disclose certain details."
    hide deu_down onlayer front
    show deu_sad onlayer front
    d "That...{w} still counts as lying...{w}?"
    d "I think it should count as lying."
    mc_s "I say it shouldn't."
    mc_s "Listen Deulithoteq, you have a process of RECRUITMENT where you HIRE earwurms to get you INFORMATION."
    mc_s "That's the monad of your business."
    mc_s "But! I can elevate this business as your {b}best{/b} scout yet."
    mc_s "You may be asking what I have over other RECRUITs,{w} and that's my power of INSIGHT."
    hide deu_sad onlayer front
    show deu_frown onlayer front
    if (knowledge + temp_knowledge) > 2:
        show screen testing_text("Test: Knowledge -> Success", True)
        d "...{w} and what does your INSIGHT do?"
    else:
        show screen testing_text("Test: Knowledge -> Failed", False)
        $ deulithoteq_door -= 10
        d "Guess what? I'm not interested."
        hide deu_frown onlayer front
        show deu onlayer front
        d "Sorry little silver-tongued, but you'll have to find someone else who's buying what you're selling."
        jump phase7_d3
    mc_s "Apart from causing headaches,{w} which I sincerely apologise for by the way...{w}"
    mc_s "The power of INSIGHT allows me to get a look into the minds of others."
    mc_s "Which means that-{nw}"
    hide deu_frown onlayer front
    show deu_side onlayer front
    d "Hold on, looking into other peoples' minds?{w} What does that entail?"
    mc "Good! I have its attention."
    "You think to yourself in order to compose your thoughts."
    "Deulithoteq, strangely, has the patience to let you finish doing so."
    mc_s "It's not as simple as a \"jump right in and look around\" type of process."
    mc_s "Because everyone's mind is so vast, it can feel like entering an infinite abyss and drowning in all the information."
    mc_s "Which is why, before I enter, I need a few \"target points\" to look for so that I don't get lost and stay on track."
    mc_s "I call these \"target points\" KEYWORDS."
    mc_s "It's similar to how a cave-divers are attached to ropes (or distance lines) so that if they go too deep..."
    mc_s "Then they can tug on the rope and climb their way back out of the cave."
    mc_s "For me, I need KEYWORDS to be my \"safety rope\" but also as starting points as to where I should look."
    mc_s "Pinning it down to \"memories\", \"values\", \"relationships\" are still to vague, broad and abstract."
    mc_s "I need to look for something specific."
    hide deu_side onlayer front
    show deu onlayer front
    if (reputable + temp_reputable) > 2:
        show screen testing_text("Test: Reputable -> Success", True)
        d "And you are telling me all this... because?"
    else:
        show screen testing_text("Test: Reputable -> Failed", False)
        $ deulithoteq_door -= 10
        d "Okay, I'm just going to cut you off right there."
        d "Listen here, you can try to embellish how great your \"powers\" are but I'm not buying it..."
        d "Seems to good to be true, and you could easily have another power such as...{w} being able to create massive headaches?"
        d "And you're just trying to convince me that a lowlife like you can READ peoples' minds?"
        jump phase7_d3
    mc_s "Because as long as I have a good starting point, I can extract INFORMATION from {b}anyone{/b} without them even noticing."
    "You walk forwards, extend your burnt arm in the direction of Deulithoetq"
    mc_s "And if I could work for you...{w} then you're guaranteed to get {b}any{/b} INFORMATION from anyone."
    d "So you're asking me to hire you?{w} You do know what happens if you break any CONTRACT-{nw}"
    mc_s "That's why I'm also asking for some of my own demands."
    hide deu onlayer front
    show deu_smile onlayer front
    d "AHAHaha of course of course.{w} Well what is it?"
    "You unintentionally smile."
    mc_s "Oh it isn't much,{w} I need mental energy in order to survive."
    mc_s "So my form of \"payment\" would have to come in this form... so I could keep living."
    hide deu_smile onlayer front
    show deu_side onlayer front
    d "And this isn't something money can buy?"
    mc_s "AHaha! Oh I WISH!{w} My life would be so much easier."
    mc_s "But no, I would need to get the energy from... here."
    mc "I gesture all around me to draw attention to the lack of anyone else in the room."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "So you want MY power in exchange for me getting a valuable asset-"
    mc_s "The MOST valuable asset you'll ever earn."
    d "But you're not even-{nw}"
    mc_s "If you're going to discredit me as \"not worth all the fuss\" then why did you abduct me here in the first place?"
    hide deu_down onlayer front
    show deu onlayer front
    d "You came here of your own volition."
    mc_s "Because I was being threatened."
    mc_s "And I also knew I was going to be killed, abducted etc. if I didn't come here myself."
    d "Well I think that-{nw}"
    mc_s "Listen the past is the past!{w} Yesterday is kidnapping, tomorrow is camaraderie and eternal friendship."
    mc_s "Or in this case, a mutually beneficial agreement I'd say."
    hide deu onlayer front
    show deu_side onlayer front
    d "...{w} Well it doesn't have to be my lifeforce does it?"
    d "I just need to get you {i}someone's{/i} every month correct?"
    mc_s "Well... not completely correct."
    mc_s "Believe it or not INSIGHT comes with a downside,{w} when it comes to energy transactions like that..."
    mc_s "I would need an agreement of the person I gather the lifeforce from."
    mc_s "So if you abducted someone here and asked me to take their soul,{w} I couldn't do it IF they never gave their accord."
    mc_s "I'd need \"permission\" so to speak."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "Hmm..."
    mc "Deulithoteq wraps its tail around its torso, sliding past the scales like a mosaic."
    mc "I could hear the rattling of the skin as it hissed in thought."
    d "Then what about my earwurms?{w} How would they fare?"
    mc_s "For?"
    hide deu_down onlayer front
    show deu onlayer front
    menu:
        d "What if I let you take the mental energy from my earwurms instead of me?"
        "I think we could come to an agreement (?)":
            # no passed check needed
            $deulithoteq_outcome = "draft"
            d "So we're good?"
            mc_s "I think we are!"
            d "I'll amend the CONTRACTs of all the other earwurms and I'll draft a new one for you."
        "I think you're the only one who could give the supply I need (?)":
            # need reputable to pass this check
            if (reputable + temp_reputable) > 3:
                show screen testing_text("Test: Reputable -> Success", True)
                ### this would be a WIN outcome
                d "...{w} I doubt that's true."
                $deulithoteq_outcome = "win"
                d "But, I don't see the downside to this, as long as I remain the one in control."
                "You stand confused but before you say anything you bite your tongue."
                d "Which is why I'm going to draft a new CONTRACT for you and me in order to make it fair."
            else:
                show screen testing_text("Test: Reputable -> Failed", False)
                d "I'm sorry but I don't think such a thing would be possible."
                $deulithoteq_outcome = "draft"
                mc "Deulithoteq reaches for an arcane weapon shrouded by the orange sand."
                mc "I hear clicking as it prepares for the weapon to maim me."
                mc_s "I-If that's going to be the case then I wouldn't mind the earwurms... for now."
                d "Glad to hear you're willing to make compromises!"
    hide deu onlayer front
    show deu_up onlayer front
    stop music fadeout 2.0
    mc "Delicately, the spool of weaver's silk descends from the ceiling,{w} glowing with arcane magic."
    mc "Deulithoteq gathers its tendrils, now interwoven with the silver spool, to work with the wooden board mechanism."
    mc "I'm guessing this is how threading or making transcriptions can be done using the silk fabric."
    mc "And this is the drafting process of the contract."
    mc "Well I suppose if Deulithoteq is going to draft my CONTRACT outside,{w} I need to finalise the details on the inside."
    "Using your power of INSIGHT, enter the mind of Deulithoteq."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    hide deu_up onlayer front with dissolve
    if deulithoteq_outcome == "win":
        jump d3_win
    else:
        jump d3_draft


#############################
################## P O W E R
############################

label phase6_d3_S2:
    ### INSIGHT: NEW KEYWORD HIRE
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_1() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S2_d2

    elif search == "room2":
        jump phase6_d3_S2_d3
    else:
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    jump phase7_d3

label phase6_d3_S2_d2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_2(d3_power2()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S2

    elif search == "room2":
        if "key_1" in inventory:
            jump phase6_d3_S2_d4
        else:
            "You don't have the key to access this door."
            jump phase6_d3_S2_d2

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        "Incorrect answer."

    jump phase7_d3

label phase6_d3_S2_d3:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_3(d3_power3()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S2

    elif search == "room2":
        if "key_2" in inventory:
            jump phase6_d3_S2_d5
        else:
            "You don't have the key to access this door."
            jump phase6_d3_S2_d3

    elif search == "caveat":
        if "key_1" not in inventory:
            play sound "audio/sfx/key.wav"
            "You obtained the first key."
            ### temporary key placeholder
            $inventory.append("key_1")
            $showinput = False
        jump phase6_d3_S2_d3

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_S2_d3

    jump phase7_d3

label phase6_d3_S2_d4:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_4(d3_power4()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room2":
        jump phase6_d3_S2

    elif search == "room":
        jump phase6_d3_S2_d2

    elif search == "obscurity":
        if "key_2" not in inventory:
            play sound "audio/sfx/key.wav"
            "You got the second key."
            ### temporary key placeholder
            $inventory.append("key_2")
            $showinput = False
        jump phase6_d3_S2_d4

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_S2_d4

    jump phase7_d3

label phase6_d3_S2_d5:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_5(d3_power5()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room2":
        jump phase6_d3_S2_d6

    elif search == "room":
        jump phase6_d3_S2_d3

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_S2_d5

    jump phase7_d3

label phase6_d3_S2_d6:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_6() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S2

    elif search == "room2":
        jump phase6_d3_S2_d5

    elif search == "power":
        jump phase6_d3_power

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        "Despite all the searching, you couldn't find the answer..."

    jump phase7_d3

label phase6_d3_power:
    stop music fadeout 2.0
    hide screen text_timer
    ### this results in a DRAFT outcome
    "As soon as you exit the mind of Deulithoteq, you hear a bellowing roar erupt from its mouth."
    play sound "audio/sfx/beast.mp3"
    "It vociferously thrashes the wall of ink and sand as it had done before the first time you used INSIGHT."
    "The more you use it, the greater the effect it seems to leave on the mind you enter."
    "But even you feel slightly drained from using it twice within one sitting."
    "The power of INSIGHT, like all powers, doesn't come without a price."
    show deu_up onlayer front with vpunch
    play sound "audio/sfx/quake.mp3"
    d "ARGHHHHhh again with the pain?!"
    show wurm1 onlayer front with dissolve
    show wurm2 onlayer front with dissolve
    mc "From the rooms, I see the earwurms that had come before begin to aid Deulithoteq's symptoms."
    mc "Larvae would chew off at the tendrils and a multicoloured moisture was applied to its skin."
    mc "The earwurms would be busy pushing sand off and on Deulithoteq's head while speaking in that archaic language as before."
    mc "Perhaps it was some kind of healing ritual for earwurms... but it seems to be working."
    hide deu_up onlayer front
    show deu_side onlayer front
    play sound "audio/sfx/shargoth.mp3"
    d "(X) (X) (X) (X)."
    ear "(X) (X)"
    mc "And just like that, the earwurms are dismissed from the room."
    hide wurm1 onlayer front with dissolve
    hide wurm2 onlayer front with dissolve
    mc "As they exit, they leave a soft arcane trail behind them;{w} glittering under the shine of the moon."
    mc "Deulithoteq's tendrils start to ease and relax, but it is still visibly sweating and fatigued."
    mc "...{w} A few moments of silence pass in between us."
    "You start to think about what to say next.{w} And then it comes to you."
    mc_s "Deulithoteq, I hope you would indulge me for a bit, regarding your business."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "..."
    mc "It's too tired to say anything, so it gives a small nod with its head."
    mc_s "You spoke of the nature of SECRETS, that people would go to lengths to protect them;{w} that's how you got your POWER."
    mc_s "But after taking a look inside your mind-"
    hide deu_down onlayer front
    show deu_sad onlayer front
    d "Wait you did...{w} URGHhhhhhhh{nw}"
    d ".... hrughhh...{w} what?"
    mc_s "That's...{w} actually what my power of INSIGHT does."
    play music "audio/music/Confused.wav"
    mc_s "But I noticed that you've been falling a bit behind in terms of business,{w} and even now you're wasting time with me."
    hide deu_sad onlayer front
    show deu_smile onlayer front
    d "Ha... haha.{w} We may have dips but that's...{w}..."
    d "... hardly relevant.{w} Heard of the business cycle before?"
    mc_s "I don't think this is just a part of a blip,{w} I think it enlightens something deeper about your situation."
    mc_s "It shows that this world is moving past such archaic ways of thinking."
    hide deu_smile onlayer front
    show deu_frown onlayer front
    d "You seriously think knowledge has no POWER?"
    d "That's...{w} how people ascend.{w} Through education, skills, or bribery."
    d "That's how power is made-{w} URGHHHhh...{nw}"
    mc_s "Be careful, you're straining your voice."
    hide deu_frown onlayer front
    show deu_side onlayer front
    d "..."
    mc_s "Listen, the fact of the matter is, your model can't work on greater terrors."
    mc_s "As someone who's spoken to them,{w} if you held any SECRETs of them then these terrors would bury you into the ground."
    mc_s "It's much easier to murder you versus caving into your demands."
    mc_s "And I know that your only abilities are the power of SURVEIL and the silk CONTRACTs you weave."
    mc_s "These powers pale in comparison to the ability of the great terrors"
    mc_s "So for these reasons, you can {b}never{/b} have leverage over great terrors for this reason."
    mc_s "This leaves you only with clients who cannot overpower you, or are too ignorant to realise the easy way out."
    mc_s "And sure, you could exploit them for money,{w} but that money will never be enough to alleviate you from this position."
    hide deu_side onlayer front
    show deu_down onlayer front
    stop music fadeout 1.0
    "Deulithoteq coughs and spits on the ground."
    hide deu_down onlayer front
    show deu_frown onlayer front
    "It turns to stare at you with a disgusted face."
    if (intellect + temp_intellect) > 1 and (supreme + temp_supreme) > 3:
        play music "audio/music/Gaining.wav" fadein 1.0
    else:
        play music "audio/music/Losing.wav" fadein 1.0
    mc_s "So...{w} it's not to insinuate you're unsuccessful, on the contrary!"
    mc_s "You own this entire town and can afford to live very comfortably."
    mc_s "...{w} but for the problems you have this isn't the kind of power you're seeking."
    mc_s "The more you stretch out to other \"higher standing\" clients, the more you risk your cover being exposed."
    mc_s "The greater chance this whole things fall apart."
    mc_s "But if you stay with people who are desperate and helpless, there's only so much as you can grow."
    mc_s "You say that knowledge is POWER,{w} but I don't think that's the case."
    mc_s "When you're locked behind bars,{w} thrown into the abyss,{w} or are being threatened with your own life..."
    mc_s "Knowledge can't save you."
    mc_s "When you're surrounded with people who don't care what you do to them,{w} your knowledge doesn't hold power over them."
    mc_s "And these kind of destitute people populate the majority of the clients you seek."
    mc_s "Those who are utterly hopeless."
    hide deu_frown onlayer front
    show deu_sad onlayer front
    d "But I still hold POWER with this knowledge that I have.{w} URgh..."
    d "I may not always have leverage over others,{w} but this POWER I have will continue to exist."
    mc_s "But you-"
    d "I'm not seeking to conquer the world,{w} I just need to conquer what's in sight."
    hide deu_sad onlayer front
    show deu_smile onlayer front
    d "As long as people are buying what I'm selling, it doesn't matter that there are people immune to SECRETs being exposed."
    if (intellect + temp_intellect) > 2:
        show screen testing_text("Test: Intellect -> Success", True)
        d "I'm going to keep on making my income for as long as I live."
    else:
        show screen testing_text("Test: Intellect -> Failed", False)
        $ deulithoteq_door -= 7
        hide deu_smile onlayer front
        show deu_frown onlayer front
        d "I mean frankly the AUDACITY of you to say that my business isn't sustainable."
        d "That I'm a slowly dying breed of corporations?"
        d "Tch."
        hide deu_frown onlayer front
        jump phase8_d3
    mc_s "..."
    hide deu_smile onlayer front
    show deu_side onlayer front
    mc "There's some truth to what Deulithoteq is saying, it can always thrive off of those who are susceptible to blackmail."
    mc "I think I need to go back to the point before:{w} about how this business could become obsolete."
    mc_s "But you can't always make future predictions based on past data.{w} At some point you won't have enough clients to sustain your business."
    mc_s "If even the {i}slightest{/i} mistake happens, or there's one whistle-blower, what's going to save you?"
    mc_s "As I've said before:{w} when you're locked behind bars,{w} thrown into the abyss,{w} or are being threatened with your own life..."
    mc_s "Your so-called \"knowledge\" fails to hold leverage over those who lock you up."
    mc_s "You will no longer be able to feed your earwurms, and after you get out you will be ruined because there's no opportunity for future employment."
    mc_s "At least not when your history is regarding blackmail."
    mc_s "You'll most likely lose all of your sources too because they have to cover their tracks after your mishap."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "How... URGHhh can you be so sure I'll make a mistake?"
    mc "I shouldn't be going down this track, no instead I need to provide an alternative!"
    mc_s "It's not about \"making a future mistake\",{w} I'm saying you should quit whilst your still ahead."
    if (supreme + temp_supreme) > 3:
        show screen testing_text("Test: Supreme -> Success", True)
        d "So... I should just... retire? Is that what you're saying?"
    else:
        show screen testing_text("Test: Supreme -> Failed", False)
        $ deulithoteq_door -= 9
        hide deu_down onlayer front
        show deu_frown onlayer front
        d "So... I should just... retire? Is that what you're saying?"
        mc_s "Wait no that's not what I meant-"
        d "Tch."
        hide deu_frown onlayer front
        jump phase8_d3
    mc_s "Not retire.{w} No, but pursue a different form of employment."
    mc_s "You see, POWER is knowledge exerted.{w} The ability to act on knowledge is POWER."
    mc_s "There are a bunch of superfluous, meaningless INFORMATION that you've gathered and stored in your network."
    mc_s "I can tell because I saw your mind."
    mc_s "That's a great inefficiency,{w} even this conversation with me has gotten you NOTHING to use."
    mc_s "But you can only use this POWER if you move up on the ladder."
    hide deu_down onlayer front
    show deu_side onlayer front
    d "And elevate my status to what?"
    mc_s "...{w} Finance? Banking?"
    mc_s "Something that deals with money?"
    mc_s "Great terrors have multiple forms of power that deem them to be \"terrors\"."
    mc_s "Wealth, strength, knowledge, network, divine and the cult of following."
    mc_s "So far you've only been exploiting your knowledge, but if you managed to accumulate more wealth..."
    mc_s "Then you could say... buy a greater cult of following.{w} Invest in your arcane magic skills to grow greater in strength."
    mc_s "And THEN, you would be in a position to exert your knowledge as true POWER over the great terrors."
    mc_s "For you see, knowledge is power only {b}relative{/b} to your standing within society."
    mc_s "The greater your position and status,{w} the greater rewards you reap from more knowledge."
    mc_s "This makes INFORMATION gathering more valuable, more efficient and grants you more POWER."
    hide deu_side onlayer front
    show deu onlayer front
    if (charisma + temp_charisma) < 2:
        show screen testing_text("Test: Negative Charisma -> Success", True)
        d "..."
    else:
        stop music fadeout 2.0
        show screen testing_text("Test: Negative Charisma -> Failed", False)
        $ deulithoteq_door -= 5
    if deulithoteq_door < 1:
        d "..."
        d "Oh.... Ohhhh I now see what you're trying to do."
        hide deu onlayer front
        show deu_smile onlayer front
        d "Haha... very funny silver-tongued."
        mc_s "???"
        mc "Its tail swerves a path encompassing my surroundings."
        hide deu_smile onlayer front
        show deu_down onlayer front
        mc "I'm trapped."
        d "Convince me to switch careers so that you can get off scot-free?"
        hide deu_down onlayer front
        show deu onlayer front
        d "I'm sorry, but your little \"charming\" dance made it so I could see right through you."
        jump phase7_d3
    hide deu onlayer front
    show deu_down onlayer front
    "Deulithoteq pauses in silence."
    "At first, it seems to be excited...{w} elated even at this prospect."
    "But then it turns to you; suspicious."
    d "You clearly want something out of this... don't you?"
    mc_s "I'm just presenting a better way to expand your business than just keep doing the same thing over and over."
    mc_s "Build your network of earwurms to accumulate \"dirt\", gather vulnerable victims, blackmail them, gain rewards.{w} Rinse and repeat."
    mc_s "But this routine can only-"
    hide deu_down onlayer front
    show deu_side onlayer front
    d "Yes yes I see your point.{w} So what do you want from me?"
    mc_s "Nothing...{w} except for my life and to let me go?"
    d "..."
    hide deu_side onlayer front
    show deu onlayer front
    d "I'll draft a CONTRACT so that as long I live you will answer to my call, then you're free to live."
    mc_s "Ah yes thank you!"
    stop music fadeout 2.0
    mc "Unfortunately, I'm not in a position to ask for any of their mental energy.{w} Or request to be their siphon."
    mc "But I didn't come here to seek that, I just came here to know what was going on and to leave in one piece."
    mc "Now I know that it wanted to dig up dirt on me,{w} and now I get to leave with my life."
    mc "Delicately, the spool of weaver's silk descends from the ceiling,{w} glowing with arcane magic."
    mc "Deulithoteq gathers its tendrils, now interwoven with the silver spool, to work with the wooden board mechanism."
    mc "I'm guessing this is how threading or making transcriptions can be done using the silk fabric."
    mc "And this is the drafting process of the contract."
    mc "Well I suppose if Deulithoteq is going to draft my CONTRACT outside,{w} I need to finalise the details on the inside."
    hide deu onlayer front with dissolve
    $deulithoteq_outcome = "draft"
    "Using your power of INSIGHT, enter the mind of Deulithoteq."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    jump d3_draft


#############################
################## S I P H O N
############################

label phase6_d3_S3:
    ### INSIGHT: NEW KEYWORD HIRE
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_1() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S3_d2

    elif search == "room2":
        jump phase6_d3_S3_d3
    else:
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    jump phase7_d3

label phase6_d3_S3_d2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_2(d3_siphon2()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S3

    elif search == "room2":
        if "key_1" in inventory:
            jump phase6_d3_S3_d4
        else:
            "You don't have the key to access this door."
            jump phase6_d3_S3_d2

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        "Incorrect answer."

    jump phase7_d3

label phase6_d3_S3_d3:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_3(d3_siphon3()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S3

    elif search == "room2":
        if "key_2" in inventory:
            jump phase6_d3_S3_d5
        else:
            "You don't have the key to access this door."
            jump phase6_d3_S3_d3

    elif search == "chronic":
        if "key_1" not in inventory:
            play sound "audio/sfx/key.wav"
            "You obtained the first key."
            ### temporary key placeholder
            $inventory.append("key_1")
            $showinput = False
        jump phase6_d3_S3_d3

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_S3_d3

    jump phase7_d3

label phase6_d3_S3_d4:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_4(d3_siphon4()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room2":
        jump phase6_d3_S3

    elif search == "room":
        jump phase6_d3_S3_d2

    elif search == "catharsis":
        if "key_2" not in inventory:
            play sound "audio/sfx/key.wav"
            "You got the second key."
            ### temporary key placeholder
            $inventory.append("key_2")
            $showinput = False
        jump phase6_d3_S3_d4

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_S3_d4

    jump phase7_d3

label phase6_d3_S3_d5:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_5(d3_siphon5()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room2":
        jump phase6_d3_S3_d6

    elif search == "room":
        jump phase6_d3_S3_d3

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d3_S3_d5

    jump phase7_d3

label phase6_d3_S3_d6:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen deulithoteq_hire_6() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d3_S3

    elif search == "room2":
        jump phase6_d3_S3_d5

    elif search == "siphon":
        jump phase6_d3_siphon

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        "Despite all the searching, you couldn't find the answer..."

    jump phase7_d3

label phase6_d3_siphon:
    stop music fadeout 2.0
    hide screen text_timer
    ### this results in a WIN outcome
    "As soon as you exit the mind of Deulithoteq, you hear a bellowing roar erupt from its mouth."
    play sound "audio/sfx/beast.mp3"
    "It vociferously thrashes the wall of ink and sand as it had done before the first time you used INSIGHT."
    "The more you use it, the greater the effect it seems to leave on the mind you enter."
    "But even you feel slightly drained from using it twice within one sitting."
    "The power of INSIGHT, like all powers, doesn't come without a price."
    show deu_up onlayer front with vpunch
    play sound "audio/sfx/quake.mp3"
    d "ARGHHHHhh again with the pain?!"
    mc "Almost at once, the earwurms who've escorted me begin to aid Deulithoteq's symptoms."
    show wurm1 onlayer front with dissolve
    show wurm2 onlayer front with dissolve
    mc "Larvae would chew off at the tendrils and a multicoloured moisture was applied to its skin."
    mc "The earwurms would be busy pushing sand off and on Deulithoteq's head while speaking in that archaic language as before."
    mc "Perhaps it was some kind of healing ritual for earwurms... but it seems to be working."
    hide deu_up onlayer front
    show deu_side onlayer front
    play sound "audio/sfx/shargoth.mp3"
    d "...{w} (X) (X) (X) (X) (X)."
    ear "(X) (X)"
    mc "And then the earwurms wriggle into the walls,{w} leaving Deulithoteq and I alone."
    hide wurm1 onlayer front with dissolve
    hide wurm2 onlayer front with dissolve
    mc "I know I just saw that Deulithoteq is seeking something regarding {b}SIPHONs{/b} in general."
    mc "But if it wants that INFORMATION from me, it'll be hard-pressed to find it."
    mc "I haven't associated with my kind in years...{w} decades."
    mc "But why SIPHONs of all beings?{w} It could be about our gifted power of INSIGHT."
    mc "But no, Deulithoteq doesn't know {b}what{/b} INSIGHT actually does.{w} So it couldn't be about exploiting it."
    mc "It also lied about not knowing {i}what{/i} species I was, but it clearly seems to know that I'm a siphon."
    mc "Or it could be about a specific SIPHON that had wronged Deulithoteq in the past-"
    "As you go through all the possibilities as to why Deulithoteq would be interested in SIPHONs,{w} you realise something."
    mc "I could do all this speculating as much as I want, but I'll never know unless I ask it directly."
    hide deu_side onlayer front
    show deu_sad onlayer front
    d "Ugh..."
    play sound "audio/sfx/beast.mp3"
    "Deulithoteq lets out a growl, still trying to recover from your use of INSIGHT on it."
    stop sound
    mc_s "Deulithoteq, listen-"
    hide deu_sad onlayer front
    show deu_frown onlayer front with vpunch
    play nature "audio/sfx/destroy.wav"
    d "Stop talking.{w} This kind of pain never happens to me."
    d "I know you had something to do with it-{nw}"
    hide deu_frown onlayer front
    show deu_up onlayer front with vpunch
    d "GAH!{w} Urghhhh...."
    "It just barely has the strength to carry out a conversation with you."
    mc_s "Well you want to know what I know?{w} Let me tell you..."
    mc_s "I know what the whole reason for your business is."
    stop nature fadeout 2.0
    hide deu_up onlayer front
    show deu onlayer front
    d "I already told you, it's my form of income."
    play music "audio/music/Confused.wav"
    d "You're harping on about nothing."
    mc_s "I know it's something to do with SIPHONs."
    mc_s "That's why you brought me here isn't it?"
    hide deu onlayer front
    show deu_side onlayer front
    d "A SIPHON...{w} never heard of it."
    mc "Is it seriously going to play ignorant now?"
    mc_s "You can stop with the superfluous lies.{w} I {b}literally{/b} just saw it inside your mind."
    hide deu_side onlayer front
    show deu_sad onlayer front
    d "You saw what?"
    mc_s "I don't know if it's some sort of personal vendetta, an academic lucubration or just plain curiosity."
    mc_s "So why don't we cut to the chase and you can just tell me what this is all about...{w} hm?"
    d "..."
    mc "Deulithoteq lets out a gentle laugh.{w} It seems strangely at ease for someone who's just been confronted."
    hide deu_sad onlayer front
    show deu onlayer front
    d "Is that what your INSIGHT does?{w} Look into the minds of others?"
    mc_s "So you {b}are{/b} interested in SIPHONs..."
    d "You're prevaricating."
    mc_s "So are you."
    d "..."
    mc_s "I also saw that you aren't particularly fond of them either... that I cannot decipher why."
    mc_s "So instead of you trying to squeeze it out of me, why don't you {b}directly{/b} ask what you want?"
    hide deu onlayer front
    show deu_down onlayer front
    if (intellect + temp_intellect) > 2:
        show screen testing_text("Test: Intellect -> Success", True)
        mc "Unless the thing it wants is something I would never agree to do."
        d "You leave me no choice."
    else:
        show screen testing_text("Test: Intellect -> Failed", False)
        $ deulithoteq_door -= 9
        hide deu_down onlayer front
        show deu_frown onlayer front
        d "How about you stop accusing me of LYING for one?"
        d "You pathetic piece of BILE! Did you really think that you could psychoanalyze me because ya felt like it?"
        d "Tch."
        hide deu_frown onlayer front
        jump phase8_d3
    hide deu_down onlayer front
    show deu onlayer front
    d "How about this,{w} you either lead me to the Conspicio Mater or you'll never live another day."
    mc_s "The... Conspicio Mater? What do you have with them-"
    d "I'm not demanding you to ask questions, I'm demanding you to disclose the location of Conspicio Mater."
    mc_s "Wait...{w} Oh...{w} you don't know do you?"
    d "Of course I wouldn't KNOW!{w} That's why I'm-{nw}"
    hide deu onlayer front
    show deu_frown onlayer front with vpunch
    play nature "audio/sfx/destroy.wav"
    stop music fadeout 1.0
    d "ENOUGH!{w} Tell me where the Conspicio Mater is or..."
    mc_s "I honestly don't know where they are."
    d "LIES! ALL SIPHONs in existence are able to echolocate the Conspicio Mater, that's how the network of INFORMATION travels."
    mc "Deulithoteq did its due diligence in its research regarding my kind, I'll give it that."
    stop nature fadeout 2.

    if (knowledge + temp_knowledge) > 1 and (reputable + temp_reputable) > 3:
        play music "audio/music/Gaining.wav" fadein 1.0
    else:
        play music "audio/music/Losing.wav" fadein 1.0

    mc_s "But it should tell you something that even {b}I{/b} don't know where they are."
    hide deu_frown onlayer front
    show deu_down onlayer front
    d "It tells me nothing."
    "You sigh."
    mc_s "Then let me spell it out for you."
    mc_s "If I, a SIPHON, cannot locate them, then that means there's {b}nothing{/b} to locate."
    hide deu_down onlayer front
    show deu_sad onlayer front
    d "...{w} what?"
    mc_s "It means that the Conspicio Mater is gone.{w} They've been gone for years Deulithoteq."
    d "..."
    "The behemoth of an Earwurm freezes, teeth gnashing and body shaking."
    "Deulithoteq's skin rotates and shifts around its cylindrical form,{w} rusting away and its tendrils curl up."
    "It's frozen."
    mc_s "Deulithtoq you heard me when-{nw}"
    d "..."
    d "...{w} I know. I know."
    hide deu_sad onlayer front
    show deu_down onlayer front with vpunch
    play nature "audio/sfx/destroy.wav"
    d "Of COURSE!{w} That's why I haven't been able to track down a single SIPHON in all these years..."
    mc "It looks as if it finally achieved some clarity, but at a cost."
    mc "Melancholy wouldn't be the right word to describe it, but frustration, confusion..."
    stop nature fadeout 2.0
    mc "Almost like the pinnacle of its discovery was left on a bathos;{w} an anti climax."
    d "..."
    hide deu_down onlayer front
    show deu_side onlayer front
    d "So...{w} you're telling me that you're the last of your kind?"
    mc_s "I'm not making any {b}definitive{/b} statements like that.{w} But I wouldn't be surprised if I never saw another SIPHON again."
    d "You're all that's left of an ENTIRE civilization."
    mc_s "I mean we weren't a {i}civilization{/i} as much as a bunch of primitive insects living in dirt."
    d "You don't understand what your kind has done to others."
    mc_s "No kidding I wouldn't know!{w} I was excommunicated the day I was born."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "You were?"
    mc_s "Yes I told you I barely knew them."
    d "But... why?"
    mc_s "Because I was {i}malformed{/i}."
    hide deu_down onlayer front
    show deu onlayer front
    d "Defective?"
    mc_s "No, it wasn't anything to do with me being \"weak\" or because I was unable to do things."
    mc_s "..."
    mc_s "Simply put, they just didn't like the way I looked.{w} I was \"disgusting\"."
    hide deu onlayer front
    show deu_side onlayer front
    d "???"
    mc_s "But that's enough about me.{w} So you can be clear as to what you-{nw}"
    hide deu_side onlayer front
    show deu_sad onlayer front
    d "You are of no use to me then.{w} Prepare any final words you wish to speak."
    mc_s "Hold on!{w} Just because the Conspicio Mater is dead doesn't mean that inflow of INFORMATION is!"
    d "..."
    hide deu_sad onlayer front
    show deu onlayer front
    d "...{w} what about {i}agreements{/i} that were made?"
    mc "So... Deulithoteq {b}IS{/b} interested in a specific piece of knowledge held by the SIPHONs."
    mc "Wait I remember something in the INSIGHT!{w} Wasn't it...something about a PACT?"
    mc "But SIPHONs can only form PACTS if they want energy removed from one vessel into their own."
    mc_s "You must be interested in a PACT that was made between a SIPHON and another being."
    hide deu onlayer front
    show deu_side onlayer front
    d "Yes."
    mc_s "Given that this SIPHON is most likely dead, the Conspicio Mater would normally deal with such matters."
    mc_s "But now that they're dead too, it looks like you need me to fulfill the role."
    hide deu_side onlayer front
    show deu_up onlayer front
    d "What role?"
    mc_s "Any SIPHON can usurp another's position in the PACT if that SIPHON is dead."
    mc_s "Normally, the Conspicio Mater who's the all-powerful SIPHON would do such a task."
    mc_s "But I'm the only one who could do so now."
    mc_s "So I think it's best that you drop your weapon-"
    hide deu_up onlayer front
    show deu onlayer front
    d "But can you undo it?{w} Change it?{w} Rewrite it?"
    if (knowledge + temp_knowledge) > 2:
        show screen testing_text("Test: Knowledge -> Success", True)
        mc_s "...{w} Yes."
    else:
        show screen testing_text("Test: Knowledge -> Failed", False)
        mc_s "I'm... not sure..."
        $ deulithoteq_door -= 6
        hide deu onlayer front
        show deu_frown onlayer front with vpunch
        play nature "audio/sfx/destroy.wav"
        d "What do you mean \"not sure\"?{w} Aren't you the last member of their SPECIES?"
        d "Shouldn't you KNOW this kind of stuff huh?"
        stop nature
        mc_s "I... should..."
        "Deulithoteq sighs."
        hide deu_frown onlayer front
        show deu onlayer front
        d "Alright, fine... whatever."
        jump phase7_d3
    d "..."
    "Deulithoteq undoes the silk weapon it was spooling as you were talking."
    "It takes a deep sigh."
    hide deu onlayer front
    show deu_side onlayer front
    d "...{w}I need you to annul the PACT I made with the SIPHON."
    mc_s "Of mental-energy lending?{w} Sure."
    d "Thank you I-{nw}"
    hide deu_side onlayer front
    show deu_frown onlayer front
    mc_s "ONLY if you meet certain conditions."
    mc_s "First, you are to {i}never{/i} threaten my life or kill me."
    mc_s "You cannot even order other people to put my life in harm or assassinate me."
    hide deu_frown onlayer front
    show deu_smile onlayer front
    d "Done. So can we-"
    hide deu_smile onlayer front
    show deu_sad onlayer front
    mc_s "Secondly, all the unspent energy that should've been absorbed by the dead SIPHON go to me."
    d "I don't understand."
    mc_s "All this time, the mental energy you've been losing should've gone into the hands of the SIPHON."
    mc_s "I'm redirecting this new energy back to me."
    hide deu_sad onlayer front
    show deu onlayer front
    if (reputable + temp_reputable) > 3:
        show screen testing_text("Test: Reputable -> Success", True)
        d "...{w} as long as you don't take any more of my soul from here."
    else:
        show screen testing_text("Test: Reputable -> Failed", False)
        d "Actually... forget it."
        $ deulithoteq_door -= 6
        hide deu onlayer front
        show deu_side onlayer front
        d "I don't know if I could trust you of all people with such a deal anyways."
        mc_s "What are you talking about? Of course you can trust me-"
        hide deu_side onlayer front
        show deu_smile onlayer front
        d "Being sweet-toothed and charming is nice and all,{w} but I can't work with people who're all smiles and no BITE."
        hide deu_smile onlayer front
        show deu_frown onlayer front
        d "I know the second this is over you'd want to screw me over somehow."
        mc "Wait! There's gotta be something I can do to convince it-"
        hide deu_frown onlayer front
        show deu onlayer front
        d "So with that out of the way, I think we're done here."
        jump phase7_d3
    mc "Ugh, I'd rather I take the energy.{w} But why would Deulithoteq agree to do this if it's the same thing..."
    mc "... except the SIPHON is different?"
    mc_s "I could absorb energy from you at a lower rate."
    hide deu onlayer front
    show deu_sad onlayer front
    d "How much lower?"
    mc_s "Fifteen percent of the original take-out amount?"
    hide deu_sad onlayer front
    show deu_frown onlayer front
    d "Forty percent."
    mc_s "Twenty."
    hide deu_frown onlayer front
    show deu_smile onlayer front
    d "Thirty percent is my final offer."
    mc_s "...{w} done."
    d "Then I'll make a new condition of my own."
    mc_s "Which is?"
    hide deu_smile onlayer front
    show deu_frown onlayer front
    d "You are to {b}NEVER{/b} use INSIGHT on me ever again."
    mc_s "Done."
    stop music fadeout 2.0
    mc "That's why Deulithoteq responded so badly to the use of INSIGHT,{w} because it's mental energy has been strained all these years."
    mc_s "Unfortunately, to \"seal the deal\" I have to use INSIGHT to go into your mind."
    hide deu_frown onlayer front
    show deu_up onlayer front
    d "I can just draft the contract in silk."
    mc_s "It's better if we have both copies."
    d "...{w} (X) (X) (X) (X) (X)."
    play sound "audio/sfx/shargoth.mp3"
    "Deulithoteq calls out its earwurms again."
    hide deu_up onlayer front
    show deu onlayer front
    d "They're just here to help ease the pain."
    d "Consider this contract sealed."
    $deulithoteq_outcome = "win"
    hide deu onlayer front with dissolve
    "Using your power of INSIGHT, enter the mind of Deulithoteq."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    jump d3_win



label insight_time_up_d3:
    stop music fadeout 2.0
    mc "ARRghhh-{w} I can't...{nw}"
    "Spending too much time in the mind of another person can cause strain on your mental energy."
    "Unfortunately, it looks like your time is up in navigating Cor Meum's mind."
    mc "Wait! If I only had more time-{nw}"
    mc "..."
    mc "After having left Deulithoteq's mind,{w} I saw the earwurm in front of me bash violently against the ground."
    d "ARRrghh!"
    mc "It doesn't seem to be taking INSIGHT so well.{w} Maybe some of the worst symptoms I saw."
    mc "But there's nothing I can do except patiently wait until this blows over."
    mc "..."
    "After a few minutes of waiting, Deulithoteq scrambles out of the ground to face you."
    "It turns to you, exhausted,{w} and asks..."
    jump phase7_d3

label phase7_d3:
    stop music fadeout 2.0
    $save_name = "-- end of dialogue 3 --"
    hide screen deu_door with dissolve
    d "So I presume we don't need to have any further discussion... no?"
    mc_s "Well I mean...{w} I suppose..."
    mc "No point in asking to be their siphon,{w} I don't have enough leverage to do so."
    mc "Guess that means I leave empty-handed, without any mental energy."
    mc "Oh well, at least I can leave in one-"
    hide deu onlayer front
    show deu_side onlayer front
    d "\"I suppose\"? I suppose what?"
    mc_s "Oh no no it's nothing!{w} Now if you could let me go that would be great."
    hide deu_side onlayer front
    show deu_smile onlayer front
    play music "audio/music/Tension.wav"
    d "AhahahAHa..."
    "Deulithoteq remains silent for a moment, before erupting in laughter."
    play sound "audio/sfx/beast.mp3"
    d "AAHAHHAHAHAHAAHAHAH!"
    "The guffaw shrills and rings against your ears, whilst having a present underlying deep boom."
    "It smiles and begins to drill on its teeth."
    hide deu_smile onlayer front
    show deu_down onlayer front
    stop sound
    d "Did you seriously think I was just going to let you go?"
    mc_s "I mean-{nw}"
    hide deu_down onlayer front
    show deu_smile onlayer front
    d "No really?{w} Oh you're PRICELESS... hilarious I might say."
    hide deu_smile onlayer front
    show deu onlayer front
    d "So walk me through my plan, tell me about it."
    d "I went out of my WAY to find you, bring you here, ask you questions that resulted in unhelpful answers..."
    hide deu onlayer front
    show deu_frown onlayer front
    d "And then I just let you go?"
    d "As if nothing had happened at all?"
    mc_s "..."
    mc "It's right, I was stupid to think that it would just let me walk free."
    mc "I got caught up in all the casual persiflage I forgot the real context of this meeting."
    mc "It was my mishap and I shouldn't let it happen again."
    mc "...{w} if there IS another again."
    mc_s "So... what happens now?"
    ### if you have one win Deulithoteq keeps you trapped as a prisoner
    ### if you have 2 wins Deulithoteq will keep an implant device on you
    ### it'll hire you for unpaid work essentially
    if fernweh_outcome == "win" and cormeum_outcome == "win":
        jump end_achilles
    elif fernweh_outcome == "win" or cormeum_outcome == "win":
        jump end_rabbit

label phase8_d3:
    stop music fadeout 2.0
    #### hide WHATEVER before you make the call to phase 8
    show deu_sad onlayer front
    d "Frankly, I've had enough of hearing your nonsense."
    play music "audio/music/Losing.wav"
    d "You are NOT in a position to be asking ME for anything."
    d "To be making demands from ME."
    hide deu_sad onlayer front
    show deu_frown onlayer front with vpunch
    play nature "audio/sfx/destroy.wav"
    d "Did you hear what I said at the beginning?"
    d "I AM the one in charge here and I wanted to make that very clear."
    d "Everything and anything you say can and will be used against you."
    d "I WILL RUIN YOU. The more you keep on talking the more I'm losing my PATIENCE!"
    d "..."
    "Deulithoteq takes a deep breath."
    stop nature fadeout 2.0
    hide deu_frown onlayer front
    show deu_down onlayer front
    d "Listen I'm not one to get overly exacerbated over insignificant things."
    mc_s "Guess I might not be so \"insignificant\" then hmm?"
    d "Ugh..."
    "It rolls over in the sand."
    hide deu_down onlayer front
    show deu_smile onlayer front
    d "How about this, I'll tell you what to do."
    d "And you can be a good little WRETCH and follow my lead?"
    hide deu_smile onlayer front
    show deu_frown onlayer front
    d "What do you say?"
    mc_s "...{w} what's going to happen now?"

    if fernweh_outcome == "win" and cormeum_outcome == "win":
        jump end_achilles
    elif fernweh_outcome == "win" or cormeum_outcome == "win":
        jump end_rabbit


label end_rabbit:
    stop music fadeout 2.0
    $save_name = "-- epilogue --"
    d "What happens now?{w} What happens NOW?"
    hide deu_frown onlayer front
    show deu_smile onlayer front
    d "AHAHaha..."
    ### black screen
    hide deu_smile onlayer front
    hide sewer onlayer back
    show black onlayer front
    d "Oh wouldn't you like to know?"
    "..."
    stop ambient
    play music "audio/music/Sad.wav" fadein 1.0
    mc "After Deulithoteq claimed me as a wurm, I've been doing its dirty bidding since."
    mc "Of course I'm clearly superior compared to the other earwurms in terms of INFORMATION collecting and efficiency."
    mc "But that hardly matters."
    mc "It claimed me as a prisoner whilst it treat the other earwurms like family."
    mc "Sometimes it whispers to me about a curse and how I need to uplift it."
    mc "Something about a SIPHON in the past that had wronged it."
    mc "But when I ask for a follow up, Deulithoteq grows cold and distant."
    mc "It sees me as an employee and nothing more."
    mc "And often keeps me down here, away from my home."
    mc "I haven't seen Keychee since..."
    mc "..."
    stop music fadeout 2.0
    mc "I crave for the day that I could have my freedom as I once did."
    mc "But each day,{w} I get closer and closer to planning my escape."
    mc "This is the day that I do it, or die trying."
    $ quick_menu = False
    play ambient "audio/sfx/basement.mp3"
    window hide
    hide black onlayer front
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
    stop ambient fadeout 2.0
    hide flower_far onlayer farback with dissolve
    hide flower_back onlayer back
    hide lily_p onlayer back
    hide flower_front onlayer front with dissolve
    hide around_particle onlayer back
    hide flower_face onlayer inyourface with dissolve
    hide lily_p2 onlayer inyourface
    jump credits

label end_achilles:
    stop music fadeout 2.0
    $save_name = "-- epilogue --"
    hide deu_frown onlayer front
    show deu_side onlayer front
    d "It's simple really,{w} I'm going to leave an implant inside of you."
    d "I know where you'll be at all times and I'll be calling you for... \"favours\"."
    d "You've been successful before with great terrors in doing your bidding, so I'll count on you for being a... useful resource."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "Feel free to live as you please,{w} but know that you'll always answer to me if I ever call."
    ## effect
    mc_s "Hold on a second,{w} I think we could negotiate the-"
    mc_s "AH!"
    "You feel a pulsating pain rippling through your arm."
    "You feel like you can't breathe."
    hide deu_down onlayer front
    hide sewer onlayer back
    show black onlayer front
    "You close your eyes."
    "You..."
    "..."
    hide black onlayer front
    show sewer onlayer back with dissolve
    "After you open your eyes,{w} you find Deulithoteq's tail gripped around your neck and earwurms holding your legs down."
    "It's so clear now, your arm's bleeding with silk swimming in and out of your blood vessels."
    "Arcane magic dances all around you."
    "This is must be the \"weaving\" process of forming CONTRACTs.{w} You've never witnessed it done with silk before."
    show deu_smile onlayer front with dissolve
    d "Remember, if you disobey our agreement, the silk inside here will snap your veins, as you slowly bleed from the inside."
    d "You'll bleed out in minutes and soon be dead."
    mc_s "Urgh...{w} and... what do you-"
    d "Oh me?{w} Nothing, I don't have to uphold anything."
    hide deu_smile onlayer front
    show deu_frown onlayer front
    d "It's on YOU to ensure that you'll ALWAYS prioritise me over everything else."
    d "Also you should close your eyes again..."
    # black screen
    hide sewer onlayer back
    hide deu_frown onlayer front
    show black onlayer front
    d "This may hurt."
    play sound "audio/sfx/magic.wav"
    "..."
    mc "It feels like it's been hours but I know only a few minutes have passed."
    mc "My arm won't stop pulsing, but I'm slowly getting used to the slippery silk navigate up and down my veins."
    mc "I open my eyes."
    hide black onlayer front
    show sewer onlayer back with dissolve
    mc "I see that the exterior of my arm has changed to,{w} now it's been engraved with archaic arcane symbols."
    mc "No doubt in Deulithoteq's language that it spoke to the earwurms in."
    "After a long waiting,{w} Deulithoteq unlocks the arcane fuelled barriers,{w} signalling you to leave."
    show deu_side onlayer front with dissolve
    play music "audio/music/Sad.wav" fadein 2.0
    d "My earwurms will escort you out oh and also..."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "If you want to have a chat about anything, here's my business card."
    menu:
        "Take Deulithoteq's business card (?)":
            mc_s "Pleasure... doing business with you."
            d "No no please, the pleasure is all mine!"
            d "I've seen your work with Fernweh and Cor Meum,{w} keep this up and you'll be moving on to great things."
        "Slap it away and spit on the ground (?)":
            "You do just that,{w} but Deulithoteq seems completely unphased by it."
            d "Well,{w} you could just always touch the markings on your silk if you want to be summoned here."
            d "Now begone with you."


    hide deu_down onlayer front with dissolve
    show wurm1 onlayer front with dissolve
    show wurm2 onlayer front with dissolve
    "Earwurms emerge from the ground and nib at your feet.{w} An earwurm at the front guides you to go outside."
    "You climb outside the way you came."
    hide wurm1 onlayer front with dissolve
    hide wurm2 onlayer front with dissolve
    hide sewer onlayer back with dissolve
    show solas onlayer back with dissolve
    "You take a long walk back home from Solas."
    hide solas onlayer back with dissolve
    show homeb onlayer farback
    show homef onlayer back with dissolve
    "By the time you come home, Keychee is already napping."
    "You make yourself a snack and sit on the ground to try and relax.{w} Or forget what just happened."
    "The burden and stress of the future weighs on you,{w} but you're determined to fight it."
    mc "Of course... if only I asked to be hired on my own terms...{w} then maybe I wouldn't have ended up here."
    mc "But no matter,{w} this is how things are, and I can still move up in the world{w}...?"
    mc "Even if I'm dragged down by a chain."
    mc "A permanent servant to Deulithoteq."
    mc "Hmm... guess I'll have to resolve that one day."
    hide homeb onlayer farback
    hide homef onlayer back with dissolve
    stop music
    mc "Won't I?"
    $ persistent.blood = True
    ending "BLOOD END:{w} Achilles’ Heel"
    jump credits


############ add more questions here
############### at least 1, up to 3 maximum
label d3_Qsurveil:
    ### NOTES: make people LIE more often
    # strategy 2
    mc_s "Your power of SURVEIL, what does it do?"
    hide deu onlayer front
    show deu_smile onlayer front
    d "If you're asking me then you probably know...{w} but I'll amuse you."
    hide deu_smile onlayer front
    show deu_down onlayer front
    d "The power of SURVEIL allows me to hear the last few seconds of a conversation."
    d "If I'm feeling good, it can even be the last few minutes."
    mc "So this is definitely how it {i}knew{/i} of my conversations with Fernweh and Cor Meum."
    mc_s "For the conversation, do you have to \"lock on\" a specific target?"
    hide deu_down onlayer front
    show deu_side onlayer front
    d "As in?"
    mc_s "Do you get to {i}choose{/i} the person you listen in on?"
    ## CUE here, it's lying
    if perception > 1:
        show screen cue_text("Deulithoteq's tendrils are spinning.\n   It's deceiving you.") with dissolve
    d "No,{w} most often with the distance caps I just randomly hear whatever passes by."
    if perception > 1:
        hide screen cue_text with dissolve
    ## maybe do a perception test here
    hide deu_side onlayer front
    show deu_down onlayer front
    d "The power of surveil isn't my main mechanism for gathering INFORMATION anyways."
    mc_s "..."
    mc "Main mechanism? So is it Deulithoteq's job to get INFORMATION or something?"
    mc "So, all the bombardment of questions is about gathering INFORMATION about myself."
    mc "But I have no intrinsic value,{w} my origins are worth nothing."
    mc "I made it purposefully difficult to find,{w} but Deulithoteq's been doing a pretty good job of digging it up."
    mc "Granted it has the power of SURVEIL, but SURVEIL alone didn't disclose my sources of Globin and the G'narg."
    mc "Deulithoteq's SURVEIL couldn't have disclosed the location of my house."
    if "information" not in keywords:
        show screen unlock_text("New keyword: INFORMATION")
        $ keywords.append("information")
        $ deu_keywords.append("information")
    mc_s "So...{w} what was the \"main mechanism\" for gathering all that INFORMATION?"
    hide deu_down onlayer front
    show deu onlayer front
    d "What? You want to be an inside trader?"
    mc_s "No, I'm just curious."
    d "It's always good to be careful about your curiosity silver-tongued."
    $deuQsurveil = True
    jump phase4_d3

label d3_Qwurm:
    d "What about them?"
    menu:
        "What do your earwurms do for you? (route ???)":
            #strategy 1
            hide deu onlayer front
            show deu_smile onlayer front
            d "My EARWURMS are like the backbone of my company."
            d "Without them none of this would be possible..."
            mc "Wait, Deulithoteq runs a company?"
            mc_s "Since when were you a CEO?"
            hide deu_smile onlayer front
            show deu_side onlayer front
            d "I'm a self-made {i}entrepreneur{/i}, the EARWURMS are like my employees."
            mc_s "\"{i}Like{/i} your employees.\"{w} They either are or are not your employees."
            mc_s "Do you even pay corporation tax?"
            d "..."
            mc "Of course,{w} this guy is just getting more dubious by the second."
            mc "But if... whatever you call this is a business that means..."
            mc_s "If you run a business you must be in the market for something{w} no?"
            hide deu_side onlayer front
            show deu_down onlayer front
            d "Elaborate."
            mc_s "Well you know how all things are like in markets,{w} demand and supply."
            mc_s "Then there's equilibrium which is where you meet and that's how prices are made-"
            hide deu_down onlayer front
            show deu onlayer front
            d "Less... elaborate please.{w} Get to the point."
            mc_s "If you're running business, then what's your supply?"
            mc_s "What are you selling?"
            if "information" not in keywords:
                show screen unlock_text("New keyword: INFORMATION")
                $ keywords.append("information")
                $ deu_keywords.append("information")
            hide deu onlayer front
            show deu_up onlayer front
            d "INFORMATION,{w} I sell INFORMATION."
            mc_s "..."
            mc "So all the bombardment of questions is about gathering INFORMATION about myself."
            mc "But I have no intrinsic value,{w} my origins are worth nothing."
            mc "So if Deulithoteq wants to sell my background story..."
            mc "... then who's buying?"
            mc_s "...{w}Who's your demand?"
            hide deu_up onlayer front
            show deu_sad onlayer front
            d "I can never disclose details regarding my clients."
            hide deu_sad onlayer front
            show deu onlayer front
            d "I'm a professional, and as someone who's also in the {i}business{/i} of gathering INFORMATION like myself."
            d "You must understand the need to be professional too, hmm?"
            mc_s "Fair enough."
        "Are you an earwurm? (route ???)":
            #strategy 3
            hide deu onlayer front
            show deu_sad onlayer front
            d "I don't know.{w} Is the sky black? Is water wet?"
            mc_s "I know you're being sarcastic, but you can't deny that there are...differences between you and the EARWURM population."
            mc_s "They're small, wriggly and insignificant,{w} you stand as... a behemoth compared to them."
            mc_s "Last time I checked they also don't have those tendrils that you have attached to your face."
            hide deu_sad onlayer front
            show deu_side onlayer front
            d "Since when were you a biologist?"
            mc_s "I'm not, but doesn't that make your distinct features all the more odd?"
            mc_s "That someone, completely ordinary like me, can recognise those differences."
            hide deu_side onlayer front
            show deu_down onlayer front
            d "...{w} I mean, what else would I be,{w} if not an earwurm?"
            menu:
                "Something deformed (+ supreme)":
                    #supreme
                    #strategy 3
                    hide deu_down onlayer front
                    show deu_frown onlayer front
                    d "I'm sorry... what?"
                    mc_s "It's not something to necessarily be ashamed of,{w} take me for instance."
                    if reputable > 2 or supreme > 2:
                        show screen testing_text("Test: Reputable/Supreme -> Success", True)
                        if "mutant" not in keywords:
                            show screen unlock_text("New keyword: MUTANT")
                            $ keywords.append("mutant")
                            $ deu_keywords.append("mutant")
                        mc_s "I'm something of a \"mutant\" or \"deformed\" thing too!"
                    else:
                        show screen testing_text("Test: Reputable/Supreme -> Failed", False)
                        "I'm a mutant too."
                    d "I thought you didn't know {i}anything{/i} regarding your origins."
                    mc_s "True, but I did know this."
                    mc_s "During my {i}youth{/i}, I was frequently reminded that I was malformed... or misshapen."
                    hide deu_frown onlayer front
                    show deu_down onlayer front
                    d "It must've been a disgrace to endure it."
                    mc_s "Ha! Hardly, they were merely stating the truth.{w} And there's no reason why I should take offence to it."
                    mc "...{w} can we just move on now?"
                    hide deu_down onlayer front
                    show deu onlayer front
                    mc "Wait I can't say that."
                "I'm not sure... (- reputable)":
                    #minus reputable
                    hide deu_down onlayer front
                    show deu_side onlayer front
                    d "So you suppose that I should just stick with what I know?"
                    ### CUE LYING!!!
                    if perception > 0:
                        show screen cue_text("Deulithoteq's teeth are bruxing.\n   It's nervous and worried.") with dissolve
                    d "And that is earwurms, they have been my kin since birth."
                    if perception > 1:
                        show screen testing_text("Test: Perception -> Success", True)
                        d "I was born out of the {a=jump:d3_p4}SAME{/a} hive as the rest of them."
                    else:
                        show screen testing_text("Test: Perception -> Failed", False)
                        d "I was born out of the same hive as the rest of them."
                    if perception > 0:
                        hide screen cue_text with dissolve
                    mc_s "...{w} Are you sure you could fit in the hive?"
                    mc_s "You seem rather large for that."
                    #### CUE
                    hide deu_side onlayer front
                    show deu_smile onlayer front
                    if perception > 2:
                        show screen cue_text("Deulithoteq's teeth are bruxing.\n   It's nervous and worried.") with dissolve
                    d "Haha, I guess I must've been a miniscule larva at the time."
                    if perception > 2:
                        hide screen cue_text with dissolve
                    hide deu_smile onlayer front
                    show deu onlayer front
                    d "It's called \"aging\" with time."
            mc "Speaking of all of this,{w} it's a bit strange how different Deulithoteq is."
            mc "I wonder what made it this way..."

    $deuQwurm = True

    jump phase4_d3

label d3_Qrecruit:
    ### this will lead down strategy 1
    mc_s "What's the process of RECRUITment like?"
    d "Well, it's mostly done through recommendations and \"a good word\" being put in for you."
    mc "So it's essentially nepotism."
    mc_s "That means that someone who has no affiliation with your business... can't really get a job here."
    mc_s "Because the only means of doing so is through \"good praise\" given by one of the existing employees?"
    hide deu onlayer front
    show deu_frown onlayer front
    d "It's like this for a reason."
    ### CUE
    if perception > 0:
        show screen cue_text("Deulithoteq avoids your gaze.\n   It's apathetic and it doesn't seem like\n     anyone's really close here.") with dissolve
    d "We're... a tight knit family here.{w} You know how outsiders can be, they mess up the whole dynamic."
    if perception > 0:
        hide screen cue_text with dissolve
    #mc "I didn't really get the impression that anyone here was really close..."
    hide deu_frown onlayer front
    show deu_smile onlayer front
    d "Besides,{w} it's not as if anyone is deliberately looking for this kind of line of work."
    hide deu_smile onlayer front
    show deu_down onlayer front
    d "It gets messy sometimes and most people are not really fit for the job."
    mc_s "So, who {i}IS{/i} the kind of person that's \"fit for the job\"?"
    mc_s "What are you looking for beyond just... {i}good words{/i}?"
    hide deu_down onlayer front
    show deu_side onlayer front
    d "For one:{w} doing their due diligence.{w} Making sure not a single stone is left unturned."
    d "Everything needs to be done properly, precisely and they'd need to be on top of the game at all times."
    d "Even for simpler cases."
    hide deu_side onlayer front
    show deu onlayer front
    d "Second:{w} resourcefulness.{w} Hard work doesn't get you everywhere, sometimes you need to know the right people."
    d "And you need to be able to improvise and attain new resources quickly."
    d "Third...{w} hmm..."
    hide deu onlayer front
    show deu_smile onlayer front
    d "I suppose not being a narcissistic douche counts as well."
    mc "So someone who's willing to endure hard labour, smart and... tolerable?"
    mc_s "Sounds like a fair set of criteria."
    hide deu_smile onlayer front
    show deu_down onlayer front
    d "But at the end of the day it isn't about being \"fair\" it's about what {i}I{/i} would want in someone."
    d "That doesn't always align with what the earwurms want or who they'd expect to get chosen."
    d "It's a hard process, but I'm not trying to make it deliberately so."
    d "I'm just doing my job."
    "In that moment you were struck with an idea.{w} One that {i}could{/i} get you out of this situation."
    mc "I want to be Deulithoteq's siphon,{w} it's never going to let that happen under normal circumstances."
    mc "But... if there was some kind of exchange or CONTRACT we made,{w} if there was something it could gain..."
    mc "Then it would be on my side."
    mc "And what does it need more than INFORMATION?{w} And the primary way, from the sounds of it, of acquiring INFORMATION..."
    mc "... are from those earwurm lackeys it hires."
    "This means you could win Deulithoteq's favour...{w} but at a price."
    #### make a switch between strategy 1 or 2 here?
    #### in a menu?
    mc "So if Deulithoteq hired ME in exchange for me being it's siphon,{w} then I'd say it would be a pretty good deal."
    mc "The question is,{w} what would convince it to hire me?"
    hide deu_down onlayer front
    show deu onlayer front
    d "The question is now...{w} what's your job?"
    mc_s "My job?{w} Well I'd love to tell you all about it!"
    stop music fadeout 2.0
    mc "I'd actually {i}not{/i} want to do that."
    mc "But I think I have the perfect excuse out,{w} if I get to see Deulithoteq's mind..."
    hide deu onlayer front with dissolve
    play sound "audio/sfx/hand.wav"
    show banner_back onlayer back with dissolve
    show banner_front onlayer front with dissolve
    $renpy.pause(0.2, hard=True)
    show hand_zoom onlayer inyourface
    $renpy.pause(1.0, hard=True)
    play music "audio/music/Dirt.wav"
    if insight_timer:
        show screen text_timer(duration=620.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d3" )
    hide hand_zoom onlayer inyourface
    hide banner_front onlayer front
    hide banner_back onlayer back
    ########### INSIGHT SECTION
    jump phase6_d3_lackey

label d3_Qcontract:
    # strategy 1
    mc_s "You said something earlier about CONTRACTs you form with your earwurms?"
    hide deu onlayer front
    show deu_side onlayer front
    d "Oh no, not exclusively my earwurms,{w} it also applies to all the clients, and other sources that work for me."
    if "recruit" not in keywords:
        show screen unlock_text("New keyword: RECRUIT")
        $ keywords.append("recruit")
        $ deu_keywords.append("recruit")
    d "I draft them whenever I RECRUIT a new earwurm."
    mc_s "The same CONTRACT?"
    hide deu_side onlayer front
    show deu_down onlayer front
    d "No, the process of how CONTRACTs are drafted."
    mc "Suddenly, from the ceiling a spool of weaver's silk untangles itself,{w} glowing with arcane magic."
    mc "Most likely the same type used to seal the exit behind me."
    mc "Pressed up against the silk is a web of silver and a wooden board mechanism."
    mc "This is how threading or making transcriptions can be done using the silk fabric."
    mc "But here, I can see remnants of blood,{w} hands,{w} and an enigmatic language transcribed."
    show screen cue_text("Deulithoteq's skin is melting.\n   It speaks with passion and enthusiasm.") with dissolve
    hide deu_down onlayer front
    show deu_up onlayer front
    d "Here, I weave all of my CONTRACTs personally."
    d "Most of the time, there's a copy of the silk transcript with me."
    d "And then there's one embroidered into the vessel of my client."
    hide screen cue_text with dissolve
    mc_s "I'm sorry... but did-"
    d "Oh don't worry, it's mostly harmless."
    hide deu_up onlayer front
    show deu_down onlayer front
    d "The weaving process can be... painful, but it's mostly inscribed using arcane markings that come from the silk."
    mc "So this weaver's silk is the source of a lot of the power here."
    d "This is done so that if the client breaks their end of the contract..."
    hide deu_down onlayer front
    show deu onlayer front
    d "The woven silk that was {i}embroidered{/i} into their body breaks their veins, strangles them or {i}untangle{/i} them."
    mc "Essentially, it's murder by silk in your skin if you disobey the CONTRACT."
    mc_s "Got it."
    $deuQcontract = True
    jump phase4_d3


label d3_Qinformation:
    # strategy 2/3 and strategy 1
    d "What about it?"
    menu:
        "Why do you supply INFORMATION? (+ reputable)":
            #strategy 2/3
            #reputable
            $ temp_reputable += 1
            mc_s "Of all things, surely there must be better forms of monetary compensation."
            mc_s "I doubt INFORMATION pays well."
            d "You'd be surprised..."
        "How much is your collected INFORMATION worth? (+ charisma)":
            #strategy 1
            #charisma
            $ temp_charisma += 1
            d "You'd be surprised that it would be a good form of compensation!"
        "How do you make sure none of your INFORMATION gets leaked? (+ intellect)":
            d "It's simple..."
            if perception > 1:
                show screen testing_text("Test: Perception -> Success", True)
                d "I sign a {a=call:d3_p3}CONTRACT{/a} with all of my earwurms so that they can't break it."
            else:
                show screen testing_text("Test: Perception -> Failed", False)
                d "I sign a contract with all of my earwurms so that they can't break it."

    hide deu onlayer front
    show deu_up onlayer front
    mc "It flicks its tail from the ground."
    if perception > 1:
        show screen testing_text("Test: Perception -> Success", True)
        d "But I also have my own needs, {a=jump:d3_p5}GOALS{/a} and ambitions."
    else:
        show screen testing_text("Test: Perception -> Failed", False)
        d "But I also have my own needs, goals and ambitions."

    mc_s "And what are those?"
    # CUE
    show screen cue_text("Deulithoteq's teeth are bruxing.\n   It's hiding something.") with dissolve
    hide deu_up onlayer front
    show deu_frown onlayer front
    d "Irrelevant to you."
    hide screen cue_text with dissolve
    hide deu_frown onlayer front
    show deu_smile onlayer front
    d "But surely you must know more than anyone else the power that INFORMATION holds."
    d "You seek it intensely whether it's your prying questions for me, or whether it's in pursuit of another interlocutor."
    mc "Wait, how much is it revealing on what it knows about me?"
    hide deu_smile onlayer front
    show deu onlayer front
    d "I can't say what goal you seek, that's not my place to say, but INFORMATION has two kinds of values."
    d "There's the whole aphorism \"knowledge is power\" or \"scientia potentia est\"."
    hide deu onlayer front
    show deu_side onlayer front
    d "Because INFORMATION can be seen as a gateway to softlocked opportunities."
    d "With knowledge, you become more informed of the world you're living in, you're able to understand it better."
    d "With greater understanding means greater ability to manipulate the will of this world."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "{i}Knowledge is power{/i} through the insight it gives and the opportunities it makes."
    d "It \"enlightens\" us if you will."
    d "But there's another... particular kind of information which gives a different form of empowerment."
    mc "It smirks."
    hide deu_down onlayer front
    show deu_smile onlayer front
    d "And those are the kinds of INFORMATION that no one wants to know about,{w} the ones meant to be kept hidden."
    if "secret" not in keywords:
        show screen unlock_text("New keyword: SECRET")
        $ keywords.append("secret")
        $ deu_keywords.append("secret")
    d "SECRETS if you will,{w} and the defining characteristic of a SECRET is that someone wants to bury it forever."
    d "Make sure nobody knows..."
    hide deu_smile onlayer front
    show deu onlayer front
    d "..."
    mc "Making sure SECRETs it discovers stay that way,{w} I think there's another word for it."
    mc "Oh right, blackmail."
    mc "So this piece of bile, thinks it can dig up my own SECRETs and then sell it back to me?"
    mc "I doubt it."
    mc "But then again, why is Deulithoteq telling me all of this?{w} Is this some kind of double...triple bluff..."
    mc "Reverse psychology thing?"
    mc_s "So I'm guessing you want me to disclose my greatest fears and deepest most repressed SECRETs?"
    hide deu onlayer front
    show deu_smile onlayer front
    d "Haha!{w} Get a hold of yourself, this isn't some {i}sleepover{/i} silver-tongued."
    ### CUE
    if perception > 1:
        show screen cue_text("Deulithoteq's teeth are bruxing.\n   It's nervous and worried.") with dissolve
    hide deu_smile onlayer front
    show deu onlayer front
    d "Your SECRETs are worth very little next to nothing to me."
    if perception > 1:
        hide screen cue_text with dissolve
    $deuQinformation = True
    jump phase4_d3


label d3_Qsecret:
    ### this will lead down strategy 2
    d "The nature of SECRETs?{w} Well I'm pretty certain I'd stated it before."
    hide deu onlayer front
    show deu_side onlayer front
    d "But SECRETs are, by their definition, meant to be known only by a handful of people."
    d "When it becomes common knowledge or exposed to the public, it ceases to be a SECRET."
    d "And it often beckons the question... {i}\"why are SECRETs known by a handful of individuals?\"{/i}"
    d "And that's because either one or multiple SECRET keepers have agreed to let the SECRET remain unknown."
    hide deu_side onlayer front
    show deu_down onlayer front
    d "No one keeps something hidden for benign reasons.{w} If there's something to hide, there's dirt to dig."
    d "And the reason it's hidden is because it could tarnish the name of these individuals,{w} could ruin a family..."
    "It forms a sinister slated smile across its face.{w} And you could hear the raspy chuckles as its teeth peaked out."
    hide deu_down onlayer front
    show deu_smile onlayer front
    d "It could even break apart nations."
    d "So that is why there are always going to be people who exploit this, and use this for their advantage."
    "It turns to you."
    hide deu_smile onlayer front
    show deu onlayer front
    d "For power."
    d "Is that not were you doing when talking to Fernweh and Cor Meum?"
    d "You've said that you'd {i}rather{/i} not disclose what happened or you give me something that's clearly false."
    d "That's because as the SECRET keeper now, you hold leverage over both of them and can extort power from them too."
    mc_s "I'm sorry what-"
    hide deu onlayer front
    show deu_side onlayer front
    d "You can keep up your naive act to others, but don't {i}patronize{/i} me."
    d "This is why I'm being blunt with you and not wasting your time."
    mc "Interesting, Deulithoteq holds me in a... somewhat high regard.{w} Considering I'm doing the same work as them."
    menu:
        mc "But do I want this to be the case?"
        "I want it to see me in a high regard (need reputable)":
            mc "But if that's going to be the case..."
            if "recruit" in keywords:
                mc "Who else does Deulithoteq hold in high regards?"
                mc "..."
                hide deu_side onlayer front
                show deu onlayer front
                mc "Perhaps the earwurms that it recruits...{w} hmm..."
                mc_s "Actually I was wondering if you could tell me what the RECRUITment process was like?"
                jump d3_Qrecruit
            else:
                mc "Ugh I have nowhere to go with this."
                mc "I'll put a pin in it for later."
        "I want it to see me as complicit (no effect)":
            mc "It's better that I keep expectations low, before I deal a final blow."
            mc "The more it talks about itself, the less I have to give away."
            mc "And the last thing I want is to be seen as a threat,{w} otherwise I would never leave this place."
    #### make a switch between strategy 1 or 2 here?
    #### in a menu?
    mc "If they're here they most likely want to uncover everything that I do,{w} which cannot be known by anyone."
    mc_s "Are you sure about that?"
    hide deu_side onlayer front
    show deu onlayer front
    d "About what?"
    mc_s "The sustainability and power of this whole business?"
    hide deu onlayer front
    show deu_frown onlayer front
    d "What are you insinuating?"
    stop music fadeout 2.0
    mc "I'm not so sure quite yet,{w} but I'll find a way."
    mc "If I can just take a peak inside your mind..."
    ##### INSIGHT SECTION HERE
    hide deu_frown onlayer front with dissolve
    play sound "audio/sfx/hand.wav"
    show banner_back onlayer back with dissolve
    show banner_front onlayer front with dissolve
    $renpy.pause(0.2, hard=True)
    show hand_zoom onlayer inyourface
    $renpy.pause(1.0, hard=True)
    play music "audio/music/Dirt.wav"
    if insight_timer:
        show screen text_timer(duration=620.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d3" )
    hide hand_zoom onlayer inyourface
    hide banner_front onlayer front
    hide banner_back onlayer back
    jump phase6_d3_S2

label d3_Qgoal:
    ### this will lead down strategy 3
    d "I'm sorry I don't know what you mean?"
    mc_s "I'm asking what DRIVES you to do this?"
    hide deu onlayer front
    show deu_smile onlayer front
    d "Haha what DRIVES me?"
    mc_s "Your GOAL?"
    d "..."
    hide deu_smile onlayer front with dissolve
    mc "Deulithoteq melts into the ground and wriggles its tail."
    show deu_up onlayer front with vpunch
    play nature "audio/sfx/destroy.wav"
    d "Why, it's my line of business! It generates my income..."
    hide deu_up onlayer front with dissolve
    stop nature
    mc "Slowly, its body lunges out of the ground and moves closer to my face."
    show deu onlayer front with dissolve
    d "It's how I'm still alive."
    mc_s "Well...{w} I don't think that's awfully convincing."
    mc_s "Nobody pursues a path of information-gathering without having ulterior motives."
    mc_s "Sure you could talk of {i}needing an income{/i}, but there are multiple other avenues for self-employment."
    mc_s "Doing this job even when you earn a comfortable amount means you're out for something..."
    mc_s "Hell, you even own this entire town in Solas,{w} you have an interconnected network of loyal earwurms to do your bidding."
    mc_s "I'd like to think you're a {i}humble{/i} monster, you don't need much."
    mc_s "You don't need anything more than life's necessities...{w} you don't want any excessive pleasures."
    mc_s "For Nullum's sake, you live in a sewer!{w} That really goes to show you aren't searching for any luxuries."
    mc_s "So why do this when you could easily retire?{w} Maybe start investing in banking or form a cult?"
    mc_s "With your money...{w} I bet you could even start the process of becoming a Great Terror."
    hide deu onlayer front
    show deu_down onlayer front
    d "Enough."
    mc_s "Don't take compliments well?{w} That's fine-{nw}"
    hide deu_down onlayer front
    show deu_frown onlayer front
    d "I don't like being accused of falsehoods."
    mc_s "HAHAha what? Man, I haven't accused you of anything?"
    mc_s "I'm drawing conclusions-"
    hide deu_frown onlayer front
    show deu_side onlayer front
    d "Coming to {i}illogical{/i} conclusions."
    mc_s "And guess where the sign is pointing me to?"
    d "...{w} where?"
    mc_s "It points to me that you're seeking INFORMATION for something you don't know."
    hide deu_side onlayer front
    show deu_frown onlayer front
    d "There's {b}nothing{/b} I don't know."
    mc_s "..."
    "You pause for a moment, considering what you're going to say next could cost you a lot."
    "But you can't stand to remain ignorant forever."
    "After all, if Deulithoteq went out of its way to get {b}you{/b} of all people here."
    "Then that must mean its search for INFORMATION..."
    mc_s "...{w} I'm guessing it's got something to do with me.{w} Doesn't it?"
    hide deu_frown onlayer front
    show deu_down onlayer front
    d "No I-{nw}"
    mc_s "Enough with the condescending,{w} so can you tell me {b}why{/b} you brought me here?"
    hide deu_down onlayer front
    show deu_smile onlayer front
    d "Ahahaha..."
    mc "Deulithoteq slams its tendrils on the ground as its tail surrounds me like a wreath."
    d "What else if not for the fact that you spoke to TWO great terrors and survived?"
    d "That's something pretty incredible isn't it?"
    mc_s "Thousands of monsters do it everyday."
    hide deu_smile onlayer front
    show deu onlayer front
    d "Really?{w} I mean maybe if they {b}work{/b} for them or are one of their worshippers."
    d "You fall into none of those categories."
    mc "It looks like Deulithoteq doesn't intend on giving away any of its intentions so easily."
    stop music fadeout 2.0
    mc "Guess I'll have to take a peak inside and look!"
    ##### INSIGHT SECTION HERE
    hide deu onlayer front with dissolve
    play sound "audio/sfx/hand.wav"
    show banner_back onlayer back with dissolve
    show banner_front onlayer front with dissolve
    $renpy.pause(0.2, hard=True)
    show hand_zoom onlayer inyourface
    $renpy.pause(1.0, hard=True)
    play music "audio/music/Dirt.wav"
    if insight_timer:
        show screen text_timer(duration=620.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d3" )
    hide hand_zoom onlayer inyourface
    hide banner_front onlayer front
    hide banner_back onlayer back
    jump phase6_d3_S3

label d3_Qmutant:
    mc_s "You said that you were a MUTANT of some kind... what was that about?"
    hide deu onlayer front
    show deu_side onlayer front
    d "It simply means that, like you, I was born in a different shape than expected."
    show screen cue_text("Deulithoteq's voice goes hoarse.\n   Dejected body language.") with dissolve
    hide deu_side onlayer front
    show deu_down onlayer front
    d "And it doesn't mean anything."
    hide screen cue_text with dissolve
    mc_s "I think it does effect you."
    mc_s "Even if you treat yourself the same, that doesn't stop from everyone else-"
    d "Who said that you could get all personal all of a sudden?"
    hide deu_down onlayer front
    show deu onlayer front
    d "You think this DRIVES me? That..."
    if perception > 2:
        show screen testing_text("Test: Perception -> Success", True)
        d "That it's my {a=jump:d3_p2}GOAL{/a}?"
    else:
        show screen testing_text("Test: perception -> Failed", False)
        d "That it's my goal?"
    d "That couldn't be further form the truth..."
    $deuQmutant=True
    jump phase4_d3



#############################
##################### POINTERS FROM DIALOGUE 3
############################


label d3_p1:
    mc_s "You ALMOST know,{w} tell me, what's the thing you're missing?"
    mc_s "Or perhaps you're embellishing... overcompensating for something."
    $ deulithoteq_door -= 1
    d "...{w} well you listen here..."
    return

label d3_p2:
    mc_s "Well... is it?"
    d "Is it what?"
    if "goal" not in keywords:
        show screen unlock_text("New keyword: GOAL")
        $ keywords.append("goal")
        $ deu_keywords.append("goal")
    mc_s "Your GOAL?"
    d "No... I don't think so."
    mc "I wanted to say more... but I couldn't keep pushing it."
    mc "I guess I could leave it off there."
    $deuQmutant=True
    jump phase4_d3

label d3_p3:
    if "contract" not in keywords:
        show screen unlock_text("New keyword: CONTRACT")
        $ keywords.append("contract")
        $ deu_keywords.append("contract")
    mc_s "A CONTRACT you say?{w} Well how are those made?"
    d "They're woven by custom silk I produce myself."
    d "Also tied together with a little bit of arcane magic."
    d "So that if anyone breaks one... there will be consequences to suffer."
    mc "Yikes."
    return

label d3_p4:
    hide screen cue_text with dissolve
    mc_s "Are you really sure you're... the SAME as everyone else?"
    show screen cue_text("Deulithoteq's skin is melting.\n   It's lying.") with dissolve
    d "I know that I do look a little different, but I'm just a regular earwurm like all the other little ones."
    hide screen cue_text with dissolve
    if "mutant" not in keywords:
        show screen unlock_text("New keyword: MUTANT")
        $ keywords.append("mutant")
        $ deu_keywords.append("mutant")
    mc_s "I know you're lying Deulithoteq.{w} Trust me, as a MUTANT myself, I know when someone sticks out from their species."
    mc_s "Not that there's anything wrong with it though, they happen occasionally."
    mc_s "And if anything, your mutations have made you stronger-"
    d "I'd ...hardly say that."
    mc_s "There's no need to lie about something like that."
    d "I couldn't know, most monsters see mutants as a bad omen or something to be avoided at all costs."
    d "Luckily, I wasn't cast out for being one, but I know that many people who are \"mishappen\" don't associate with the rest of their kin."
    mc "Yeah... I would know."
    $deuQwurm = True
    jump phase4_d3

label d3_p5:
    mc_s "Oh you have your own goals do you?"
    if "goal" not in keywords:
        show screen unlock_text("New keyword: GOAL")
        $ keywords.append("goal")
        $ deu_keywords.append("goal")
    d "Obviously I don't just live solely for my business."
    d "I have a life outside of work."
    mc_s "Weird, I never took you for someone who as a social life."
    mc_s "Say have you been to any good cult parties-"
    d "Ughh...{w} let's just drop this."
    $deuQinformation = True
    jump phase4_d3
