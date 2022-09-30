label d1_win:
    stop music fadeout 2.0
    play sound "audio/sfx/magic.wav"
    $ showtext = False
    $ showtext2 = False
    $ showinput = False
    window hide
    $ quick_menu = False

    call screen fernweeh_victory() with dissolve
    #$rrow.xp = 900
    #$rrow.yp = 1000

    #$ quick_menu = True

    $ search = _return
    $ search = search.lower()

    $ fernweh_sig = search

    jump d1_done

label d1_done:
    stop ambient fadeout 2.0
    stop music fadeout 2.0
    hide screen fer_door
    $save_name = "-- end of dialogue 1 --"
    $fernweh_outcome = "win"
    hide chasm onlayer farback
    hide fernweh onlayer front with dissolve
    hide fog_test2 onlayer back with dissolve
    hide fog_test onlayer inyourface with dissolve
    hide chasm onlayer farback
    #show black onlayer farback with dissolve
    mc "With my mark imprinted on Fernweh's mind, it acts like a \"signature\" of some sorts."
    mc "Meaning that I can siphon their mental energy at anytime, as long as the connection is maintained."
    "Congratulations!{w} You've successfully won Fernweh's favour!"
    "Whether or not you won though, life will still go on just the same."
    "But it could determine future outcomes and scenarios..."
    jump chapter2

init python:
    def purge_saves():
        saves = renpy.list_slots()
        counter = 1
        renpy.unlink_save("1-1")
        #for save in saves:
            #if counter < 2:
                #renpy.unlink_save(save)
                #counter += 1
        renpy.take_screenshot()
        renpy.save("1-1", save_name)
        return

label chapter2:
    stop music fadeout 2.0
    hide screen fer_door
    $ showtext = False
    $ showtext2 = False
    $ showinput = False
    $ temp_charisma = 0
    $ temp_reputable = 0
    $ temp_supreme = 0
    $ temp_knowledge = 0
    $ temp_intellect = 0
    $ inventory = []
    hide screen fer_door
    "Now that the conversation, all your stats earned DURING the conversation will be reset to \"normal\"."
    "After all, presence indicates how your INTERLOCUTOR perceives you.{w} Once you're done seeing them, these stats play no role."
    "All stats gained {u}during{/u} the conversation with Fernweh will be reset."
    "Don't worry, all points you assigned beforehand will stay."
    "Here, we can save your progress by overriding the save in the first file slot."
    "Would you like to save?"
    window hide
    menu:
        "Yes (save file to slot 1)":
            play sound "audio/sfx/save.wav"
            $ purge_saves()
            "Your game has been saved..."
            #$renpy.save("1", save_name)
            #call screen save()
        "No (do not save file to slot 1)":
            "So be it."

    $save_name = "-- funphare --"
    $ quick_menu = False
    play sound "audio/sfx/title.mp3"
    show on_moon_particle onlayer inyourface
    show chapter2 with dissolve
    $renpy.pause(5, hard=True)
    hide chapter2 with dissolve
    $ quick_menu = True
    hide on_moon_particle onlayer inyourface
    mc "In spite of the outcome,{w} one questioned still lingers on my mind."
    mc "How did I even get the CHASM KEYWORD in the first place?"
    mc "I remember darkness.{w} An inky, glass-like, dripping blotches of nothing."
    mc "And then I saw a red light."
    show riverlong onlayer back with dissolve
    show blue_p onlayer inyourface with dissolve
    play music "audio/sfx/river.mp3"
    mc "I returned to the present,{w} at the Melduvian river."
    mc "Fernweh may have been delusional,{w} but they were right about one thing."
    mc "Only those that are LOST can even enter the CHASM to begin with."
    mc "And Fernweh may have called me for the Dialogue.{w} But someone called first."
    mc "Someone who gave me the CHASM KEYWORD."
    mc "...{w} Maybe they were right."
    mc "The CHASM did call me.{w} And if that were true-"
    mc "Stop.{w} I don't need to go on needless tangents right now."
    mc "..."
    hide riverlong onlayer back with dissolve
    mc "So what if I have doubts?{w} Doesn't everyone?"
    mc "And what does it matter if the CHASM called me?{w} I doubt I'll ever see it again."
    mc "Some questions can't be answered."
    show riverlong onlayer back with dissolve:
        xalign 0.0
        linear 7.5 xalign 1.0
    "As you were deep in thought, you turn your head towards the Bahoog bay."
    "Across the horizon, you noticed a new phare eclipse the sky."
    mc "I don't think I've seen this one before."
    "There are signs, voices, and noises relating to the phare surrounding you."
    "Disembodied mouths and screeches from the void start whispering in the ears of passerbys."
    show mouth_move_f onlayer front with dissolve
    play sound "audio/sfx/mouth.wav"
    z "Need something to relax?{w} Something to ease your worries?"
    z "Feeling directionless?{w} Losing your heart?{w} Tired of feeling at all?"
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    show mouth_move_s onlayer front with dissolve
    z "Join the funphare!!!{w} Where all your cares can go to waste..."
    z "Sign ups are FREEEEEEEEEEEe"
    z "We have FREE FRESKE JUICE and SNACKS!!"
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    stop sound fadeout 2.0
    mc "Advertisements for the... funphare?"
    mc "What kind of snacks do they have?"
    hide mouth_s onlayer front with dissolve
    hide mouth_f onlayer front with dissolve
    "You pick up a cube of goo from the dock floor."
    mc "{i}\"Snacks include: glummy livers, turt salgars, and classic homemade salts n gnats.\"{/i}"
    mc "Oh Keychee loves salts 'n gnats."
    mc "If snacks are \"free\" I might as well take the charity."
    show mouth_s onlayer front with dissolve
    "You turn to whisper in one of the disembodied mouths."
    mc_s "Hi,{w} you guys were saying something about free snacks?"
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    z "Coming Rrrrrr ight away!"
    hide mouth_move_s onlayer front with fade
    "The mouth begins to eat itself, and then spins outward from where it was."
    "It orbits around an empty point in space whilst simultaneously rotating on an axis."
    "Then it comes to a stop."
    z "Open the top of my head."
    ### CG?
    "Inside were the snacks listed on the cube of goo."
    "Glummy livers, turt salgars, and salts 'n gnats."
    z "Please, take the Freske juice too."
    "You oblige."
    show mouth_move_f onlayer front with dissolve
    play sound "audio/sfx/mouth.wav"
    z "Congratulations!{w} Your ceremony of commencement will begin shortly."
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    mc_s "Pardon, my ceremony of what?"
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    z "Now that you've given in to the desires of delectable dining,{w} we think you're ready."
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    mc_s "Ready? Ready for what?"
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    z "We've always been proud of you.{w} You've been like a son to us."
    mc_s "????"
    z "The game of catch, you couldn't reach, so you fell down."
    z "And there was no one to catch your fall."
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    show mouth_s onlayer front with dissolve
    "A different mouth approaches you."
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    z "But now...{w} someone is here to catch the fall."
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    z "WE'RE here Gabe,{w} ready to catch your fall."
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    stop sound
    mc_s "First off, my name isn't Gabe."
    mc_s "Secondly,{w} I'm just going to take the snacks and go."
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    play sound "audio/sfx/mouth.wav"
    z "NOoooooooOOOOOOOOOOOOO{nw}"
    z "Don't you know?{w} When you join the funphare, don't you know what happens next?"
    mc_s "I haven't \"joined\" anything."
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    z "You took the snacks.{w} You're in."
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    mc_s "I'll return them!"
    "The first mouth interrupts the second one."
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    z "Wait wait.{w} We apologise!"
    z "Perhaps you weren't ready.{w} We're sorry We let you down, our sweet little child."
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    stop sound
    mc_s "..."
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    play sound "audio/sfx/mouth.wav"
    z "At least will you attend orientation day?"
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    mc_s "For what?{w} The funphare?"
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    z "Oh the funphare is a one-off event for the Cor Meum, who is all and one."
    stop sound
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    show screen unlock_text("New keyword: FUNPHARE")
    $ keywords.append("funphare")
    $ cor_keywords.append("funphare")
    $ met_cor = True
    mc_s "Wait.{w} THE Cor Meum?"
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    play sound "audio/sfx/mouth.wav"
    z "Oh yes yes!{w} Sorry we should've lead with that first."
    stop sound
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    mc "Cor Meum is a collective hivemind."
    mc "Instead of terror or brute force, they've infected other worlds to conquer them."
    mc "Offering free snacks at a quasi-carnival wouldn't be how I imagined running into one."
    mc_s "So \"orientation\" is what again?"
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    play sound "audio/sfx/mouth.wav"
    z "Well, we would introduce you to the philosophies of the Vena Cava and say why you *should* join us."
    stop sound
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    mc_s "Sounds reasonable..."
    mc "That may be true.{w} But if I don't join they will certainly kill me."
    mc "And if I don't agree to do the \"orientation\",{w} they'll kill me too."
    mc "Just my lucky day."
    mc "...{w} but maybe I can turn this into my favour."
    mc_s "I was wondering... would it be possible to meet Cor Meum?"
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    play sound "audio/sfx/mouth.wav"
    z "Oh no you don't understand!"
    z "Cor Meum IS all of us, Cor Meum is ONE, Cor Meum is ALL."
    z "Cor Meum is me...{w} and Cor Meum is you."
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    mc_s "So, right now, I'm talking to Cor Meum."
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    z "Yes."
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    mc_s "I don't think any of your Vena Cava lackeys are going to convince me."
    mc_s "If I'm doing an orientation,{w} I need to hear it from the CORE of the hivemind themselves."
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    z "...{w} interesting.{w} Nobody cares to meet the ones who started it all."
    z "And if you meet Cor Meum, you will consider joining the Vena Cava... yes?"
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    stop sound
    mc_s "Most definitely..."
    mc "NOT!{w} Most definitely not."
    mc "But I need to get out of this conversation."
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    play sound "audio/sfx/mouth.wav"
    z "What time works for you?"
    mc_s "Well-"
    z "How about tomorrow?"
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    mc_s "That also works."
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    z "Good...{w} good."
    stop sound
    hide mouth_move_f onlayer front with dissolve
    hide mouth_move_s onlayer front with dissolve
    "They drop to the floor and then dissolve."
    "...{w} I think I can get out of this one... maybe?"

    ### transition to black
    stop music
    hide riverlong onlayer back with dissolve
    hide blue_p onlayer inyourface with dissolve
    play ambient "audio/sfx/basement.mp3"
    $save_name = "-- salts 'n gnats at home --"
    k "I'm sorry..."
    ### transition to room
    show homeb onlayer farback
    show homef onlayer back
    show keychee hands handssquint blinkhands onlayer front with vpunch
    play sound "audio/sfx/break.mp3"
    k "You did WHAT NOW??"
    stop sound
    mc_s "Trust me Keychee this is going to be a GOOD thing!"
    hide keychee hands handssquint blinkhands onlayer front
    show keychee hands nosquint blinkhands onlayer front
    k "I don't have a problem with the whole \"joining a collective hivemind\" thing."
    k "That's your choice."
    hide keychee hands nosquint blinkhands onlayer front
    show keychee up upsquint blinkup onlayer front with vpunch
    k "But meeting Cor Meum?{w} What possible reason could you have for doing that?"
    if fernweh_outcome == "win":
        mc_s "After winning Fernweh's favour,{w} things should only go up from here."
        mc_s "I'm not going to just have one grand victory."
        mc_s "This could be the start of a succession of wins,{w} and for INSIGHT."
    else:
        mc_s "I didn't do the best with Fernweh,{w} but I need to move on from that."
        k "To something undeniably more dangerous?"
        mc_s "I didn't die last time, so I better stay on my \"lucky streak\" of living."
    hide keychee up upsquint blinkup onlayer front
    show keychee hands handssquint blinkhands onlayer front
    k "Why would Cor Meum ever let YOU be their siphon?"
    k "They're a collective hivemind,{w} they have BETTER things to do."
    mc_s "One mind or many,{w} everyone has their secrets..."
    mc "And everyone can be exploited with INSIGHT."
    mc_s "Oh. I also got you some snacks."
    hide keychee hands handssquint blinkhands onlayer front
    show keychee hands nosquint blinkhands hands_smile onlayer front
    play music "audio/music/Tutorial.wav" fadein 2.0
    k "Salts 'n Gnats?{w} OOOOoooh{nw}"
    hide keychee hands nosquint blinkhands hands_smile onlayer front
    show keychee up upsquint blinkup nomouth onlayer front
    stop music
    k "WAIT!{w} Aren't you distracting me from the current issue at hand-"
    play nature "audio/sfx/sizzle.mp3"
    mc "I take the salts 'n gnats over the hearth, and start sizzling them."
    hide keychee up upsquint blinkup nomouth onlayer front
    show keychee down nosquint blinkdown down_smirk onlayer front
    mc "Keychee stops and starts drooling over its four mouths."
    play music "audio/music/Tutorial.wav" fadein 2.0
    mc "Turt Salgars,{w} when smoked and dusted,{w} can act as a good seasoning over glummy livers."
    mc "I start preparing that dish on top of the hearth and in the compressing chamber."
    stop nature
    play sound  "audio/sfx/pour.mp3"
    mc "Whilst the food is being moulded and heated,{w} I take out the Freske juice and make 2 glasses."
    mc "In a small \"shot\" glass for Keychee,{w} and a medium-sized one for me."
    mc "The Glummy livers look a little underbaked,{w} so I set it alight and re-squeeze its juices."
    stop sound
    hide keychee down nosquint blinkdown down_smirk onlayer front
    show keychee down nosquint blinkdown down_open onlayer front
    k "So...{w} what are you going to do?"
    if fernweh_outcome == "win":
        mc_s "What I always do...{w} I win their favour."
    else:
        mc_s "I'm going to try my best to convince them to let me be their siphon."
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down downsquint blinkdown down_open onlayer front
    k "I'm not talking about THAT."
    hide keychee down downsquint blinkdown down_open onlayer front
    show keychee down nosquint blinkdown down_open onlayer front
    k "I mean how are you going to win Cor Meum's favour?"
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down nosquint blinkdown nomouth onlayer front
    mc_s "Look!{w} I think it's time to eeat!"
    mc "I plate the seasoned Glummy livers and salts 'n gnats.{w} They wibble and swim around."
    mc_s "Don't sweat a thing Keychee,{w} I got this."
    mc_s "And I have some time to prep for tomorrow."
    hide keychee down nosquint blinkdown nomouth onlayer front
    show keychee up upsquint blinkup onlayer front
    k "Tomorrow...{w} is in a few lunar hours."
    mc_s "...{w} I know."
    hide keychee up upsquint blinkup onlayer front
    show keychee up nosquint blinkup onlayer front
    k "You have a location?"
    mc_s "Yeah.{w} I know where I need to go,{w} no worries."
    hide keychee up nosquint blinkup onlayer front
    show keychee up nosquint blinkup up_smile onlayer front
    k "By the way, if you want help. The G'narg works at the Zilker."
    mc_s "Thank you Keychee."
    hide keychee up nosquint blinkup up_smile onlayer front with dissolve
    mc "We ate the rest of our meal in silence.{w} I turned off the noise machine to ease the room."
    stop music fadeout 2.0
    mc "But the only thing we heard that night were the noises from OUTERWORLD and the cries from the blackened skies."
    jump before_d2

label before_d2:
    play music "audio/music/Menu.wav" fadein 2.0
    $save_name = "-- prep for dialogue 2 --"
    $ points += 1
    mc "With nothing better to do, I pick up the papers on the floor and start reading them."
    if fernweh_str == "death":
        mc "{i}HEADLINE:{w} One of the Great Terrors, Fernweh, is missing.{/i}"
        mc "{i}Experts still cannot decipher their location,{w} with each dark hour the probability that Fernweh is dead grows.{/i}"
        mc "...{w} yikes."
    else:
        mc "{i}HEADLINE:{w} Morgo, the Destroyer of Worlds, has recently been granted the standing of Great Terror.{/i}"
        mc "{i}After the crusade against the Planktonian dimension, he has now accumulated enough cult of followers to earn the title.{/i}"
        mc "{i}Great Terrors are indifferent to this change, Old Terrors are disturbed and Dark Terrors want him dead.{/i}"

    "You have [points] points left to reassign to stats."
    $ quick_menu = False
    $ extra_menu = False
    window hide
    show newspaper_bg onlayer inyourface with dissolve
    call screen stat_screen with dissolve
    hide newspaper_bg onlayer inyourface with dissolve
    $ quick_menu = True
    $ extra_menu = True
    "You can continue reading to gain more points to raise your stats."
    "Or you can scout for information to gain keywords (and also +1 knowledge stat)."
    menu:
        "On this night, you decide to..."
        "Read and raise stats (gain +2 points to use and re-assign)":
            $ points += 2
            $ quick_menu = False
            $ extra_menu = False
            window hide
            show newspaper_bg onlayer inyourface with dissolve
            call screen stat_screen with dissolve
            hide newspaper_bg onlayer inyourface with dissolve
            $ quick_menu = True
            $ extra_menu = True
            "You learnt the art of sprezzatura,{w} the ability to appear to do something incredible effortlessly."
            "More headlines were about Squizz defiler of the deceased raising her undead army."
            hide homef onlayer back
            hide homeb onlayer farback with fade
            jump start_d2

        "Scout for information (collect keywords and gain +1 knowledge)":
            $ knowledge += 1
            jump info_d2

    return

label info_d2:
    stop ambient fadeout 2.0
    menu:
        "Go to the Melduvian river with Globin (???)":
            hide homef onlayer back
            hide homeb onlayer farback with fade
            show riverlong onlayer back with dissolve
            show blue_p onlayer inyourface with dissolve
            mc "I decided to go back to the Melduvian river."
            mc "Much to Globin's surprise, who hasn't expected me to come back for quite some time."
            mc "I do the whole facade {i}\"I really am interested in knowing about X\"{/i}."
            mc "{i}\"Yes, education on terrors should be compulsory...\"{/i}"
            mc "{i}\"Sure...{w} I'd...{w} definitely want to be consumed by Y'hoon too.\"{/i}"
            mc "It's embarrassing sure and I'm taking what I said to my grave."
            mc "But it was worth it."
            show screen unlock_text("New keyword: VENA CAVA")
            $ keywords.append("vena cava")
            $ cor_keywords.append("vena cava")
            mc "Globin disclosed that Cor Meum rules over the Vena Cava."
            mc "She said that the whole philosophy of the Vena Cava,{w} and by extension Cor Meum, was simple."
            mc "Avoid pain and seek rapture..."
            mc "Never seek rapture if it brings pain:{w} as the absence of all pain is better than a PAINful RAPTURE."
            mc "Pain is...{w} well pain, whether it be physical or mental."
            mc "Rapture is a euphoria, pleasure, ecstasy."
            mc "Not necessarily happiness, but anything that can serve the immediate needs of the present."
            hide blue_p onlayer inyourface with dissolve
            mc "I bid Globin farewell and thank her for her help."
            hide riverlong onlayer back with dissolve

        "Go to the G'narg at the Zilker (???)":
            hide homef onlayer back
            hide homeb onlayer farback with fade
            show silkerf onlayer back with fade
            show silker onlayer farback with dissolve
            mc "Flesh deep into Moowrongo, I see the Zilker bar hunched over."
            mc "Just as I walk up to the entrance, I notice a sign."
            mc "Unfortunately,{w} it says that they're closed?"
            mc "Hmm..."
            mc "I walked to the drying shoppe across the street,{w} hoping to just cool down."
            mc "I asked for a yuxing of my horn and a drying of my lerethral pores."
            mc "Unexpectedly, I saw an Aortish walk into the bar,{w} bearing the marks of the Vena Cava."
            mc "They skim the room in silence before quickly leaving."
            show screen unlock_text("New keyword: COLLECTIVE")
            $ keywords.append("collective")
            $ cor_keywords.append("collective")
            mc "I ask the dryer what that was about.{w} She tells me that all COLLECTIVEs assign their members certain tasks."
            mc "Apparently,{w} the Vena Cava has been coming here every hour to try and recruit new members."
            mc "Almost desperately."
            mc "After splitting my back, she let's me leave with the bill."
            mc "Maybe I'll bring Keychee here for a dry."
            hide silkerf onlayer back with dissolve
            hide silker onlayer farback with fade
            ### transition
    jump start_d2


########################################################################################
#############################################################################################
########################################################################################################
################ A C T U A L    D I A L O G U E    S T A R T S     H E R E #############################
########################################################################################
#############################################################################################
########################################################################################################


label start_d2:
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    $save_name = "-- start of dialogue 2 --"
    "Your preparation time for the Dialogue is up."
    "Now,{w} the silver-tongued will attempt to {b}win{/b} the favour of the interlocutor:{w} Cor Meum, where one is all."
    #### transition
    #### BIG TITLE TRANSITION SCREEN:
    #### Cor Meum, where one is all
    show silkerf onlayer back with fade
    show silker onlayer farback with dissolve
    play ambient "audio/sfx/solas.wav"
    mc "I knew that \"orientation\" would take place in the topoietic orb above the Moowrongo-Solas border."
    show mouth_move_f onlayer front with dissolve
    show mouth_move_s onlayer front with dissolve
    mc "The mouths and voices from last time were there to greet me,{w} and asked me to don a new robe."
    mc "And then they beckoned me to float into the orb floating above Moowrongo."
    mc "The topoietic orb structure, like a mechanical puzzle, began to undo itself."
    mc "When the entrance opened, the orb resembled a sphere with a slice taken out."
    hide mouth_move_s onlayer front
    hide mouth_move_f onlayer front
    hide silker onlayer farback
    hide silkerf onlayer back
    mc "I went inside."
    stop ambient
    play ambient "audio/sfx/cardian.ogg"
    "..."
    window hide
    show cardianf onlayer back with fade
    show cardianb onlayer farback with dissolve
    show on_moon_particle onlayer inyourface with dissolve
    $renpy.pause(2, hard=True)
    mc "After navigating through multiple vessels in the canals, I finally arrived to the CORE."
    mc "This CORE room is the abode of Cor Meum:{w} the \"mind\" of the hivemind."
    mc "Or the \"heart\" of the Vena Cava collective."
    mc "And attached to the top of the ceiling, there's no other than the heart itself."
    mc "When I took a step on the ground the Cardian floor jumped,{w} and Cor Meum immediately knew I was there."
    mc "Slowly, they began to descend from the ceiling."
    window hide
    show cormeum base blink onlayer front with dissolve
    $renpy.pause(2, hard=True)
    mc "Hovering above me, their chords of arteries and veins fall delicately past them like strands of hair."
    show screen cor_door() with dissolve
    play music "audio/music/Cormeum.wav" fadein 2.0
    cm "Silver-tongued..."
    menu:
        cm "Are you ready for orientation?"
        "Always have been (+ charisma)":
            $ temp_charisma += 1
            cm "Hmmmmmm good to hear."
            #charisma +
            hide cormeum base blink onlayer front
            show cormeum smile blink onlayer front
            mc "They crack a wicked smile that splits their face in two."
            hide cormeum smile blink onlayer front
            show cormeum base blink onlayer front
        "If you're ready to discuss (+ reputable  + intellect)":
            $ temp_reputable += 1
            $ temp_intellect +=1
            #reputable/intellect +
            cm "Discuss?"
            mc_s "Give my own ideas a fair chance.{w} Have a conversation."
            hide cormeum base blink onlayer front
            show cormeum smile blink onlayer front
            cm "HAHA...{w} sure sure."
            hide cormeum smile blink onlayer front
            show cormeum base blink onlayer front
        "You don't need to ask (+ supreme)":
            $ temp_supreme +=1
            mc_s "Otherwise why would I be here?"
            cm "Mmm fair point."
            #supreme +
        "I don't know if I'll ever be (- supreme)":
            $ temp_supreme -= 1
            cm "Relax young one,{w} no one thinks they're ready for the Vena Cava."
            #blackmail

    cm "Now,{w} we here also want to make you do a little survey before we start orientation."
    cm "We hope this is fine with you."
    mc_s "Sure."
    #play nature "audio/sfx/destroy.wav"
    play sound "audio/sfx/quake.mp3"
    mc "I feel a quake underneath my feet."
    cm "Please, take a step back."
    mc "I do so, and from where I was once standing, the floor caves into a hole,{w} which then forms into a mouth-like shape."
    mc "The floor egests something into the room.{w} The yellow and white bile floats in the room, free of gravity."
    stop sound
    #stop nature fadeout 2.0
    mc "As I was in awe, the hole starts closing itself up by pulling in the meaty floor that surrounds it,{w} similar to quicksand."
    mc "As it does so, the bile transforms into a smectic A state, where it crystallizes to form...{w} a piece of paper."
    hide cormeum base blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "We just want to know if you have any allergies,{w} friends or family you care about,{w} or salt on you."
    cm "But also, this is about if you've joined any hiveminds in the past,{w} how long you've existed as a singleton etc."
    #### maybe have a Survey minigame
    mc_s "Is there... some kind of writing device I can use?"
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "Look up silver-tongued."
    mc "Above me, I see an black artery descend from the ceiling."
    cm "Squeeze it to get some ink out of it,{w} continue squeezing and pressing it as you write."
    mc "After a few minutes, I'm done filling out the survey."
    mc_s "What will this be used for-"
    hide cormeum base n blink onlayer front
    show cormeum smile blink onlayer front
    cm "We thank you very much for your cooperation!"
    cm "Now, we're sure you have a lot of questions,{w} which will be answered in due time."
    show screen cue_text("Cor Meum's eyes are squinting.\n   They're suspicious of you.") with dissolve
    hide cormeum smile blink onlayer front
    show cormeum base squint blink onlayer front
    cm "However, we were very curious to learn more about you."
    hide screen cue_text with dissolve
    mc_s "How come?"
    show screen cue_text("Cor Meum's arteries are turning blue.\n   They're annoyed.") with dissolve
    cm "Why, of all the people we've recruited,{w} you're the only one who started making demands."
    hide screen cue_text with dissolve
    hide cormeum base zquint blink onlayer front
    show cormeum base blink onlayer front
    cm "And the only one to make a \"reasonable\" demand at that:{w} to see us."
    cm "Sometimes, amongst the multitude of faces,{w} you singletons fail to grasp our reality."
    mc "\"Singletons\" being a collective's word for those who are not in a hivemind."
    hide cormeum base blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "And it is because you don't understand us that we have this gap in understanding."
    cm "If only you could understand,{w} why everyone would want to be in the Vena Cava!"
    cm "And in your individualistic world,{w} you think in singleton ways."
    cm "You cannot comprehend our multitude,{w} our numbers nor our omnipotent presence."
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "No, you need to something to centre those ideas in a singular being."
    menu:
        cm "Which in this case would be the vessel you see before you."
        "I don't know if I'm grasping your\"concepts\" any better (- reputable)":
            $ temp_reputable -= 1
            #blackmail, minus reputable
            hide cormeum base n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "Maybe your mind is a little too weak to...understand yet."
            mc_s "Maybe you need to rethink as to how you view singletons."
            cm "...{w} and you ARE interested in joining the Vena Cava... yes?"
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
            mc_s "Only if you convince me."
            mc "I can tell you most likely what Cor Meum is thinking right this second."
            mc "\"{i}Oh I'll convince you, because you'll be dead if you don't\"{/i}"
        "... (Don't say anything: - charisma)":
            $ temp_charisma -= 1
            # minus charisma, appeal to Meum
            cm "...{w} not much of a talker?"
            cm "At least you don't object to the idea."
        "Why what incredible intuition! (+ charisma)":
            $ temp_charisma += 1
            # plus charisma, appeal to Cor
            cm "Why,{w} is that sarcasm I{nw}"
            hide cormeum base n blink onlayer front
            show cormeum smile blink onlayer front
            cm "WEE, couldn't be happier that you seem so impressed."
            hide cormeum smile blink onlayer front
            show cormeum base n blink onlayer front
            mc "I don't know if my ears deceived me,{w} but I feel as if they're repressing something."
        "You really think yourself as the root of everything? (+ supreme)":
            # plus supreme
            $ temp_supreme += 1
            cm "Only the beating core of the Vena Cava."
            mc_s "So, you are both simultaneously your subjects and their rulers?"
            cm "We don't HAVE a hierarchy here.{w} All is the Vena Cava."
            cm "And all of the Vena Cava, is us, Cor Meum."
            mc_s "..."

    cm "Regardless, we hope that you and us can come to an understanding somewhere."
    cm "There must be some foundation for mutual trust,{w} after all..."
    menu:
        cm "Why were you at the funphare?"
        "I was interested in joining the Vena Cava (- reputable)":
            $ temp_reputable -= 1
            mc_s "And I knew the fun-phare was centred on the vena Cava event."
            hide cormeum base n blink onlayer front
            show cormeum smile n blink onlayer front
            cm "HAHAHHA....{w} you know we were there?"
            cm "The talking mouths?{w} Remember?"
            hide cormeum smile n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "We're a COLLECTIVE mind, so whatever they saw, we saw too."
            cm "And we recall you saying \"{i}Wait.{w} THE Vena Cava?{/i}\" "
            cm "Meaning you didn't know it was an event hosted by US."
            mc "Yikes, I completely overlooked that."
            mc "Everything that happened at the funphare they saw.{w} I can't make up anything."
            mc_s "Well... that doesn't exclude the possibility I was interested in the Vena Cava BEFOREHAND?"
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
            cm "...{w} we suppose."
            ## MINUS reputable
        "I was LOST (+ charisma)":
            $ temp_charisma += 1
            ## plus charisma, appeal to Cor
            hide cormeum base n blink onlayer front
            show cormeum base squint blink onlayer front
            cm "LOST?{w} We think we've heard of such a thing before."
            hide cormeum base squint blink onlayer front
            show cormeum smile n blink onlayer front
            cm "All the more you should come join us!{w} Here we will grant you the purpose you desperately need."
            cm "You wouldn't want to get whisked away by that dreadful being..."
            hide cormeum smile n blink onlayer front
            show cormeum smile squint onlayer front
            cm "What was their name again?{w} Fornways?{w} Fernways?"
            mc_s "Fernweh of the Lost."
            hide cormeum smile squint onlayer front
            show cormeum smile n blink onlayer front
            cm "Ah yes!{w} Imagine if you had ran into them, what a disaster it would be."
            mc_s "Oh please do tell me, what would've happened?"
            cm "Let's just say... you wouldn't be alive right now."
            hide cormeum smile n blink onlayer front
            show cormeum base n blink onlayer front
            mc "Clearly they missed the mark with this one.{w} Guess who's standing in the flesh right now?"
        "I wanted to buy some salt 'n gnats (- supreme  + reputable)":
            $ temp_supreme -= 1
            $ temp_reputable += 1
            ## minus supreme
            ## plus reputable
            hide cormeum base n blink onlayer front
            show cormeum smile n blink onlayer front
            cm "Ah yes, you did say you wanted to buy salt 'n gnats on that day."
            mc_s "On \"that day\"?"
            hide cormeum smile n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "The talking mouths?{w} Remember?"
            cm "We're a COLLECTIVE mind, so whatever they saw, we saw too."
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
            mc "Everything that happened at the funphare they saw.{w} I can't make up anything."
        "Why would it matter? (+ supreme)":
            $ temp_supreme += 1
            ## plus supreme
            cm "Because if you disclosed to us why you came,{w} we can understand what you-"
            mc_s "What I want out of the Vena Cava is that right?"
            mc_s "You shouldn't mould yourself to be something that fits what I need."
            mc_s "I should be interested in joining you based on *your* merit,{w} not through some sycophancy."
            hide cormeum base n blink onlayer front
            show cormeum smile n blink onlayer front
            cm "HahahaahaA..."
            hide cormeum smile n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "We don't know what you're talking about."
            cm "The talking mouths?{w} Remember?"
            cm "We're a COLLECTIVE mind, so whatever they saw, we saw too."
            cm "And we recall you saying \"{i}Wait.{w} THE Vena Cava?{/i}\" "
            cm "Meaning you didn't know that we would be there."
            mc "Yikes, I completely overlooked that."
            mc "Everything that happened at the funphare they saw.{w} I can't make up anything."
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
    cm "But we just want to understand why...{w} how should we put it?"
    cm "Why would you insist on meeting with us if you have no intention on joining the Vena Cava?"
    if perception > 0:
        show screen testing_text("Test: Perception -> Sucess", True)
        cm "Our time and {a=jump:d2_p1}RESOURCES{/a} are precious,{w} you are costing us a lot of it..."
    else:
        show screen testing_text("Test: Perception -> Failed", False)
        cm "Our time and resources are precious,{w} you are costing us a lot of it..."

    cm "Every second we spend HERE is time that could be used more efficiently elsewhere."

    if perception > 0:
        show screen testing_text("Test: Perception -> Success", True)
        cm "We want to strain ourself from any {a=jump:d2_p2}PAIN{/a} possible."
    else:
        show screen testing_text("Test: Perception -> Failed", False)
        cm "We want to strain ourself from any pain possible."

    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "And if YOU are a wise investment of a good GOOd member then it would be worth it."
    cm "So STOP being soOo vexing and listen close."
    mc_s "Are you strained?{w} I thought that such a well-oiled machine you'd scarcely face any problems."
    hide cormeum smile squint blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "Of course!{w} I'm, I'm-{nw}"
    cm "WE are fine."
    hide cormeum sad squint blink onlayer front
    show cormeum base squint blink onlayer front
    cm "Sometimes PAIN can be such a burden that we lose our focus."
    cm "But we can't let our instinct control us... no..."
    hide cormeum base squint blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "The wise person should be in control of pleasures rather than be enslaved to them..."
    cm "...otherwise pain will result..."
    cm "...and this requires judgement to evaluate the different pleasures of life."
    mc_s "I thought that being a collective was just a part of who you are."
    mc_s "But it seems to take a toll on you-"
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "OCCASIONALLY, yes.{w} But we're attempting to find a way where there's no price to pay."
    cm "No more..."

    jump phase2_d2



#######################################
##################################### add pointers
label phase2_d2:
    $save_name = "-- dialogue 2 --"
    "A silence steps into the chamber.{w} Lingering over both you and your interlocutor."
    cm "Before we begin, we were wondering a few more things."
    mc_s "Please."
    cm "What is the most lacking thing in your life?"
    cm "What is the one thing you wish you could change?"
    cm "Because there would be no other reason why anyone would join us, if they didn't want to leave something behind."
    mc_s "You feel entitled to know this?"
    hide cormeum base n blink onlayer front
    show cormeum base squint blink onlayer front
    cm "You feel entitled to come to the CORE of the Vena Cava, Cor Meum."
    cm "And demand a meeting from us.{w} So the least you could do is answer {a=jump:d2_p3}OUR QUESTIONS{/a}."
    hide cormeum base squint blink onlayer front
    show cormeum closed squint blink onlayer front
    mc "They're pushing back.{w} This isn't exactly a great sign."
    mc "I don't know if I could be fully honest."

    menu:
        mc_s "I seek..."
        "...joy in my life when there is none (+ charisma)":
            ##charisma, appeal to Cor
            $ temp_charisma += 1
            hide cormeum closed squint blink onlayer front
            show cormeum base n blink onlayer front
            cm "What happened to the joys you once had?"
            mc_s "I don't think it mattered what happened to them."
            mc_s "The only thing I can say is that they're gone.{w} And I want them back."
            cm "Yesss. Here at the Cor Meum we can grant you such a thing."
            if (charisma + temp_charisma) > 1:
                show screen testing_text("Test: Charisma -> Success", True)
                cm "Our philosophy involves seeking the RAPTURE."
                if "rapture" not in keywords:
                    show screen unlock_text("New keyword: RAPTURE")
                    $ keywords.append("rapture")
                    $ cor_keywords.append("rapture")
            else:
                show screen testing_text("Test: Charisma -> Failed", False)
                cm "Our philosophy involves seeking the RAPTURE."
            mc_s "What is the...rapture?"
            show screen cue_text("Cor Meum's vessel is beating.\n   Visible happiness and excited") with dissolve
            hide cormeum base n blink onlayer front
            show cormeum smile n blink onlayer front
            cm "It is a joy above all joys!{w} We think it'd be a disservice to compare it with happiness."
            cm "It is a divine state where you won't even know what despair is anymore."
            cm "For you will always feel pleasure, always content, always ecstatic..."
            hide screen cue_text with dissolve
            hide cormeum smile n blink onlayer front
            show cormeum base n blink onlayer front
            cm "When you are in the RAPTURE."
        "...to be rid of the pain that carries me (+ reputable)":
            ## reputable, appeal to Meum
            $ temp_reputable += 1
            hide cormeum closed squint blink onlayer front
            show cormeum base n blink onlayer front
            cm "And where is this PAIN coming from?"
            if (reputable + temp_reputable) > 1:
                show screen testing_text("Test: Reputable -> Success", True)
                mc_s "It's...from..."
                if "pain" not in keywords:
                    show screen unlock_text("New keyword: PAIN")
                    $ keywords.append("pain")
                    $ cor_keywords.append("pain")
            else:
                show screen testing_text("Test: Reputable -> Failed", False)
                mc_s "It's...from..."
            menu:
                mc "Think, what are some things that cause people PAIN?"
                "My malformed body (- supreme)":
                    $ temp_supreme -= 1
                    #supreme minus
                    cm "Vessels are not permanent.{w} In death, only souls will remain."
                    hide cormeum base n blink onlayer front
                    show cormeum smile n blink onlayer front
                    cm "Here at the Vena Cava, we can liberate you from your flesh."
                    cm "And you can move into one great network of minds, where only your soul will exist."
                    hide cormeum smile n blink onlayer front
                    show cormeum base n blink onlayer front
                "My horrible parents (- charisma)":
                    $ temp_charisma -= 1
                    #charisma minus
                    mc "It's not like I had parents, but I hear lots of people complain about them."
                    cm "Parents may have been the ones who raised us."
                    hide cormeum base n blink onlayer front
                    show cormeum smile n blink onlayer front
                    cm "But it is WE who decide our future."
                    mc_s "Did you have any parents?"
                    hide cormeum smile n blink onlayer front
                    show cormeum base n blink onlayer front
                    cm "No, we were ejected from the blood tumour in the sky."
                    cm "But it never raised us, we formed like we were a part of nature."
                "My failures in my career (- reputable)":
                    $ temp_reputable -= 1
                    #reputable minus
                    cm "Ah yes,{w} this society which only values you in terms of your labour."
                    cm "No freedom to be creative, expressive or truly be yourself."
                    hide cormeum base n blink onlayer front
                    show cormeum smile n blink onlayer front
                    cm "Here in the Vena Cava, your mind will be liberated."
                    cm "And you'll never feel such failures ever again."
                    hide cormeum smile n blink onlayer front
                    show cormeum base n blink onlayer front
                    mc "That's most likely because I'll NEVER feel anything again... period."
                "Just... life in general (- charisma  - knowledge)":
                    $ temp_charisma -= 1
                    $ temp_knowledge -= 1
                    #charisma minus
                    #supreme minus
                    #perception minus?
                    cm "Ah yes life,{w} only second best to death."
                    cm "We do think you're being a bit vague though."
                    mc_s "Isn't the nature of PAIN itself rather vague?"
                    mc_s "You don't always get clear-cut answers as to why you feel like this."
        "...more power to add to what I already have (+ supreme)":
            $ temp_supreme += 1
            ## supreme plus
            hide cormeum closed squint blink onlayer front
            show cormeum base n blink onlayer front
            cm "When will your thirst for power ever be satiated?"
            cm "Don't you see you'll never be satisfied?"
            mc "Hmm..."
            mc_s "To that I ask, when will you stop looking for new members to join the Vena Cava?"
            mc_s "Will your thirst for an expanding hivemind ever be satiated?"
            cm "It isn't about the number of recruits sssiiilver-tongued!"
            if perception > 0:
                show screen cue_text("Cor Meum's veins grow dimmer.\n   Apathetic body language") with dissolve
            hide cormeum base n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "It's about making a difference in the world, elevating this world to new heights."
            cm "Showing the way where others have never been shown before!"
            cm "It's about liberation of the singleton people... YOUR kind of people."
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
            cm "So that you can advance your minds to greater use."
            if perception > 0:
                hide screen cue_text with dissolve
            mc_s "Which would be?"
            if (temp_supreme + supreme) > 1:
                if "pain" not in keywords:
                    show screen unlock_text("New keyword: PAIN")
                    $ keywords.append("pain")
                    $ cor_keywords.append("pain")
                show screen testing_text("Test: Supreme -> Success", True)
                cm "What else but the lack of PAIN?"
            else:
                show screen testing_text("Test: Supreme -> Failed", False)
                cm "What else but the lack of PAIN?"
            mc "PAIN?"
        "...knowledge and an understanding of the world (+ knowledge)":
            $ temp_knowledge += 1
            ## nothing changes
            cm "Interesting!"
            cm "You know, if you join the collective hivemind..."
            cm "...your sum of knowledge will be greater than any singleton being in the universe."
            cm ""
    jump phase2_d2_part2

label phase2_d2_part2:
    hide cormeum base n blink onlayer front
    show cormeum closed n blink onlayer front
    mc "Some new limbs of Cor Meum begin attaching themselves to the ceiling."
    hide cormeum closed n blink onlayer front
    show cormeum base n blink onlayer front
    cm "We think it would be an appropriate time to give a tour of the Cardian."
    mc "The Cardian is the name of the orb that we're currently inside."
    mc "I start walking towards the exit,{w} adjusting the fabrics of my clothes on the way out."
    mc "I notice that Cor Meum doesn't follow me,{w} and remains attached to the chamber's ceilings."
    mc_s "Are... you to come with me?"
    cm "We, as Cor Meum, cannot move from this chamber.{w} But we, as the Vena Cava, can give a quick tour."
    show mouth_move_f onlayer front with dissolve
    show mouth_move_s onlayer front with dissolve
    mc "The hovering mouths from before appear in front of me."
    mc "Both the mouths and the beating Cor Meum speak in tandem."
    z "If you could follow us please."
    mc_s "Certainly."
    hide mouth_move_f onlayer front with dissolve
    hide mouth_move_s onlayer front with dissolve
    ### make Cor Meum disappear
    hide cormeum base n blink onlayer front with dissolve
    mc "Instead of taking me out of the chamber,{w} they move me to the opposite side of the room."
    mc "Tubes, veins and arteries fall down from the ceiling and start to take a life of their own."
    mc "All of them are drawn to me, as if we were magnets."
    mc_s "Wait hold on... what's happening?"
    play sound "audio/sfx/mouth.wav"
    show mouth_move_f onlayer front with dissolve
    show mouth_move_s onlayer front with dissolve
    stop music
    z "Who said you were leaving this room for the tour?"
    z "Please... allow yourself to be connected to our network."
    hide mouth_move_f onlayer front
    hide mouth_move_s onlayer front
    show mouth_s onlayer front
    show mouth_f onlayer front
    play music "audio/music/Tension.wav"
    mc "NOOOOOOOOOOO{nw}"
    mc "NO! of course they'll find any opportunity to \"connect\" me to the hivemind."
    mc "Does this mean it's over before it even started?"
    mc_s "What exactly are you doing?"
    hide mouth_f onlayer front
    show mouth_move_f onlayer front
    z "We're going to show you projections from our collective mind."
    hide mouth_move_f onlayer front
    show mouth_f onlayer front
    hide mouth_s onlayer front
    show mouth_move_s onlayer front
    z "It's easier to just see visualizations, rather than go through all the trouble of walking around."
    hide mouth_move_s onlayer front with dissolve
    hide mouth_f onlayer front with dissolve
    "As you can feel the tubes suck at your skin pores... a thought crosses through your mind."
    mc "Wait.{w} If they're showing projections from their mind...{w} that means I can use INSIGHT!"
    mc "But no,{w} as much as I can see what's in their mind,{w} they can also see what's in mine."
    mc "So they'll know that I can traverse their mind.{w} And may suspect something."
    "Cor Meum's main form descends from the ceiling again,{w} time is running out."
    show cormeum base n blink onlayer front with dissolve
    if perception > 0:
        show screen testing_text("Test: Perception -> Success", True)
        menu:
            mc "What should I do?"
            "Use INSIGHT to go into their mind (???)":
                stop music fadeout 2.0
                "And so you do..."
                jump phase3_d2
            "Just listen to the presentation (no effect)":
                mc "Better to hold off using it until later..."
                ### choosing this means the only viable strategy is...
                ### strategy to blackmail about necromancy

    else:
        show screen testing_text("Test: Perception -> Failed", False)
        menu:
            mc "What should I do?"
            "Use INSIGHT to go into their mind (no effect)":
                mc "Just as I'm about to take a plunge...{w} something is holding me back."
                cm "Ugh...{w} sorry there's a strain on my head..."
                mc "MY?{w} Since when did they start using singular pronouns?"
                cm "There's something... wrong with your brain silver-tongued."
                cm "Should we take a look-"
                mc_s "No no need!{w} I'm in an impeccable condition."
                mc_s "Try connecting me again."
                mc "Looks like if I try to use INSIGHT, they'll notice a strain."
                mc "And logically speaking, I could be the only cause of it."
                mc "Better to hold off using it until later..."
            "Just listen to the presentation (no effect)":
                mc "Better to hold off using it until later..."
    stop music fadeout 2.0
    cm "Alright, now you should be able to *FEEL* the rest off the Cardian."
    hide cormeum base n blink onlayer front
    show cormeum smile n blink onlayer front
    cm "Here in the Cardian,{w} members of the Vena Cava travel via valves, arteries and veins."
    cm "Arteries and veins are used to keep us all connected whilst valves act as passageways through the chambers."
    hide cormeum smile n blink onlayer front
    show cormeum closed n blink onlayer front
    mc_s "How come at the funphare there were no arteries/veins attached to you?"
    hide cormeum closed n blink onlayer front
    show cormeum base n blink onlayer front
    play music "audio/music/Cormeum.wav"
    cm "That was because they were all connected to a private network there."
    cm "You were in the Bahoog Bay,{w} we have a core that's connected under the sea."
    cm "So all of the wires, arteries and veins would go through the dock floors."
    mc_s "And the cores across this plane are all connected back to here?"
    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "Precisely, that's how we keep everything intertwined."
    hide cormeum smile squint blink onlayer front
    show cormeum closed n blink onlayer front
    mc_s "What were to happen if the core at Bahoog Bay were to collapse?"
    mc_s "Would all the Vena Cava be dead or simply disconnected?"
    hide cormeum closed n blink onlayer front
    show cormeum base n blink onlayer front
    cm "We would know if any of our cores are in danger,{w} after all, we're one in the same."
    cm "If such a thing were to happen, then normally they would disconnect."
    stop music fadeout 2.0
    cm "But... oh."
    hide cormeum base n blink onlayer front
    show cormeum smile n blink onlayer front
    cm "It's such a noble thing they do, doing it for the best of all of us."
    cm "A lovely liebestod indeed."
    mc_s "They... do what?"
    cm "Why they all simply die."
    mc_s "I'm sorry What-{nw}"
    hide cormeum smile n blink onlayer front
    show cormeum smile squint blink onlayer front
    play music "audio/music/Tension.wav" fadein 2.0
    cm "Oh you simple singletons,{w} you don't understand."
    cm "If any other collective were to recruit them or if they were to deform back into their singleton states..."
    cm "They would be ruined!"
    cm "Better to spare them the harsh reality and end the suffering early."
    if perception > 0:
        show screen testing_text("Test: Perception -> Success", True)
        cm "{a=jump:d2_p4}DEATH{/a} is their only release..."
    else:
        show screen testing_text("Test: Perception -> Failed", False)
        cm "Death is their only release..."
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    show screen setup_text("Strategy update")
    ending "There's something Cor Meum is hiding."
    ending "You just need to be able to dig it up and..."
    ending "Threaten them?"
    cm "Once a collective member goes back to a singleton, they are afflicted with the greatest of insanities."
    cm "For they are accustomed to being a part of a greater presence, but now they feel truly alone."
    cm "Most end their lives anyways, some may live on but in vain and in agony."
    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "So you can see that we are doing a favour for them."
    jump phase2_d2_part3

label phase2_d2_part3:
    menu:
        mc_s "But..."
        "It's needlessly cruel (- supreme)":
            $temp_supreme -= 1
            $ cormeum_door -= 1
            cm "Oh is it?"
            # supreme minus
        "You should give them the agency to decide (+ supreme)":
            $ temp_supreme += 1
            cm "If they were wise they would all make the same choice."
            cm "We KNOW what's good for them."
            #supreme plus

        "Can we ever know what's good for people? (+ intellect)":
            $ temp_intellect += 1
            hide cormeum smile squint blink onlayer front
            show cormeum base blink onlayer front
            cm "Not usually,{w} but when it comes to us..."
            cm "When they were once a PART of us..."
            hide cormeum base blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "We would know better than anyone."
            cm "Sometimes,{w} I can feel their desires linger still."
            #charisma minus

        "Why bother having a backup core at all? (- charisma)":
            $ temp_charisma -= 1
            cm "Because usually we won't have to resort to such things."
            cm "But if we do it's always for the better."
            #reputable plus

    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "We know what you're thinking."
    hide cormeum base n blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "\"{i}Cor Meum is starting to sound a bit crazy...{/i}\""
    cm "\"{i}Maybe I should leave...{/i}\""
    cm "But think of it like this."
    show screen cue_text("Cor Meum's vessels tighten.\n   Angry body language.") with dissolve
    hide cormeum sad squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "What if one day,{w} you woke up as a slug?"
    cm "A miniscule, defenceless little slug?"
    cm "You couldn't speak.{w} In a minute you could only move less than 1 centimetre."
    cm "The weight of your vessel would be so immense, you would feel trapped in your own body."
    cm "No one can understand you,{w} the pain would be too great to convey."
    hide screen cue_text with dissolve
    hide cormeum base n blink onlayer front
    show cormeum base squint blink onlayer front
    cm "Your family and friends will no longer recognise you."
    cm "And you could never be who you used to be..."
    stop music fadeout 2.0
    cm "..."
    hide cormeum base squint blink onlayer front
    show cormeum closed n blink onlayer front
    "They close their eyes and try to compose themself."
    hide cormeum closed n blink onlayer front
    show cormeum base n blink onlayer front
    cm "That's what it's like to be demoted from a hivemind back into a singleton body."
    cm "You feel so vulnerable, like your life has no order anymore."
    play music "audio/music/Cormeum.wav"
    cm "Because you used to be able to think, feel and be everything and anything that the collective felt."
    cm "...{w} do you understand now?{w} The costs WE must make to protect the Vena Cava."
    cm "And if they even have a faint connection, all of the other members could experience this agony too."
    cm "And we cannot {a=jump:d2_p5}AFFORD{/a} for such a thing to {a=jump:d2_p6}HAPPEN{/a}."
    mc_s "...{w} I'm at a loss for words."
    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "So we have come to an agreement on one thing?"
    mc_s "I suppose..."
    mc "As much as I'd hate to admit it, they have a point."
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    jump question_time

label question_time:
    cm "If you have any more questions, feel free to ask now."
    "The Questioning will now begin."
    "Use the KEYWORDs you have so far to ask Cor Meum about them."
    "To do this, simply type in the KEYWORD you want to ask about."
    "Or perhaps you can ask about non-KEYWORDs too?"
    "Be warned because ONCE you've asked a question about a KEYWORD, that's it."
    "You cannot go back to it."
    jump phase4_d2

label phase3_d2:
    play music "audio/music/Insight.wav"
    $ showtext = False
    $ showtext2 = False
    $ showinput = False
    if "twomind" not in event_track:
        $ event_track.append("twomind")
    jump phase3_insight_d2

label phase3_insight_d2:
    ### INSIGHT: NEW KEYWORD TIME
    ### need to ensure player has READ the "Cor" section first of phase 4 before
    ### moving here otherwise they won't have the information
    window hide
    $ quick_menu = False

    call screen cormeum_twomind(d2_twomind()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()


    if search == "two minds" or search == "twominds" or "twomind" in search:
        mc "Two... minds?"
        jump phase3_afterinsight_d2

    elif search == "backspace":
        window show
        $showinput = False
        "Wait, I know the answer is hiding in plain sight."
        "The answer is there... {u}UNDERLINED AND UPPERCASE{/u}."
    else:
        window show
        $showinput = False
        "Wait, I know the answer is hiding in plain sight."
        "The answer is there... {u}UNDERLINED AND UPPERCASE{/u}."

    jump phase3_insight_d2

label phase3_afterinsight_d2:
    ### do an INSIGHT section here where you do a deep dive
    stop music fadeout 2.0
    mc "What on earth... so that means..."
    cm "And finally there is our ritual site,{w} which is..."
    cm "Have you been listening to us at all?"
    mc "..."
    mc_s "Who are you?"
    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "Exactly what we said we are,{w} we are the Cor Meum!"
    play music "audio/music/Tension.wav" fadein 2.0
    mc_s "No I asked who ARE you?{w} The BOTH OF YOU?"
    cm "The both?{w} I'm sorry, I don't think we understand."
    mc_s "Don't pull this GAME with me!{w} You BOTH know exactly what I'm talking about."
    hide cormeum smile squint blink onlayer front
    show cormeum base squint blink onlayer front
    cm "...{w} Oh pray tell, if we could ever understand what you're talking about..."
    cm "HOW would you have been able to get such information?"
    mc "Trying to deflect the blame onto me? We'll see."
    mc_s "Hooking me up to your brainS -- plural -- was a good start."
    mc_s "So you shouldn't be surprised that I could get that information..."
    cm "..."
    hide cormeum base squint blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "Did you turn off the mainframe connector?"
    hide cormeum sad squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "I'm certain we did?"
    hide cormeum base n blink onlayer front
    show cormeum base squint blink onlayer front
    cm "...{w} incompetent moron."
    cm "Listen,{w} I don't know what you saw..."
    mc "I?{w} Since when did they start using singular pronouns?"
    hide cormeum base squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "But you must've mistaken all the overload of sensory information for a crazy conspiracy."
    cm "Are you intoxicated?{w} Maybe under the influence of damaging substances?"
    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "Because frankly, I would have no idea as to how you could make such a connection."
    mc_s "...{w} it's funny isn't it. Because I never explicitly stated what I saw."
    hide cormeum smile squint blink onlayer front
    show cormeum base squint blink onlayer front
    cm "Oh YOU didn't did you?"
    mc_s "But I know that you know what I saw.{w} So I think that you know what I'm talking about..."
    mc_s "And if that's the case, then my surprise... my shock isn't so unfounded, is it?"
    hide cormeum base squint blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "HAHAaa really?"
    menu:
        cm "So why don't you go ahead and say it?"
        "You're made of two separate beings (+ reputable)":
            #reputable plus
            $ temp_reputable += 1
            mc_s "I'm not going to sugar-coat it, I'm saying it like it is."
            cm "Hm. Fair enough."
            mc_s "I just wouldn't understand why you would try to hide such a thing."
            cm "It's not that we're hiding it, we're just parts of the hivemind ourselves."
            cm "We can't afford to be broken into two any more."
            mc_s "Are... Cor and Meum still-"
        "You're a failure as a collective (+ supreme  - charisma)":
            #supreme plus
            # charisma minus
            $ temp_supreme += 1
            $ temp_charisma -= 1
            $ cormeum_door -= 1
            cm "HAHaha really?{w} I'd argue we're more successful than anything that came before!"
            cm "Who can say that they have the power of TWO parallel cores backing them up?"
            cm "NO ONE!{w} Not a single being in this entire universe."
            cm "And none of my subjects hold this to be a burden in any way whatsoever."
            cm "So I'd argue that what you're saying is unmistakably false."
            cm "We aren't failures."
            cm "It's precisely BECAUSE of this, that we are able to strive."
            cm "That the Vena Cava has been able to strive!"
        "On second thought, I shouldn't make assumptions...? (- supreme  + charisma)":
            #supreme minus
            #charisma plus
            $ temp_supreme -= 1
            $ temp_charisma += 1
            cm "HAHA NOW you're choosing to back down are you?"
            cm "Coward."
            mc_s "You seem to be highly agitated, and are capable of violence."
            mc_s "I don't want to get into a fight,{w} it's like... 2 in the morning."
            cm "Then don't go around saying what YOU don't know m'kay?"
            mc_s "...okay?"
            cm "Okay."
        "I'd rather hear it from you (- reputable)":
            #reputable minus
            $ temp_reputable -= 1
            cm "...{w} unwilling to say it yourself?"
            cm "Coward."
            mc_s "It would mean nothing coming from me,{w} it would simply be slander."
            mc_s "But from you it would be an undeniable truth."
            mc_s "Something that cannot be questioned,{w} meaning I would hold no more doubts."

    hide cormeum smile squint blink onlayer front
    show cormeum base squint blink onlayer front
    cm "But if you'd rather hear it from me in MY words."
    cm "Yes, we are a hivemind.{w} Yes, we are also two singleton souls {a=call:d2_p7}WEAVED{/a} together."
    hide cormeum base squint blink onlayer front
    show cormeum smile n blink onlayer front
    cm "YES, we are COR and MEUM, where two is all."
    hide cormeum smile n blink onlayer front with dissolve
    play music "audio/music/Confused.wav"
    mc "I notice that their colours changed,{w} where now there is a distinct line between the two halves."
    mc "One with a greater red hue, and the other with a blue hue instead."
    mc "Even though they're undeniably connected,{w} they also look more fractured than before."
    show cormeum base n blink msplit onlayer front with dissolve
    me "This is MEUM speaking."
    hide cormeum base n blink msplit onlayer front with dissolve
    show cormeum base n blink csplit onlayer front with dissolve
    c "I am COR."
    mc "Where once there was a unity, or a plethora of voices."
    mc "Now, each half of Cor Meum sound distinct and clear.{w} Almost like two separate singleton's voice."
    hide cormeum base n blink csplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "There... satisfied?"
    hide cormeum base squint blink msplit onlayer front
    show cormeum smile squint blink csplit onlayer front
    c "No no no no no.{w} more and more and more and-{nw}"
    hide cormeum smile squint blink csplit onlayer front
    show cormeum smile n blink msplit onlayer front
    mc_s "I...{w} you can-"
    hide cormeum smile n blink msplit onlayer front
    show cormeum base n blink msplit onlayer front
    stop music fadeout 2.0
    me "Go back to being one?{w} Thank you."
    hide cormeum base n blink msplit onlayer front with dissolve
    mc "Just as quickly as they separated,{w} they fused back together."
    show cormeum base n blink nosplit onlayer front with dissolve
    mc "From this first impression I can say this..."
    show screen setup_text("Strategy update")
    mc "Cor seems to be interested in something flashy, eye-catching or captivating."
    ending "You'll need to get their attention..."
    ending "And appeal to their immediate emotions and instinct."
    mc "Meum seems to be the one in charge of reason and logic."
    mc "It will need to think I'm trustworthy in order for me to be in their favour."
    ending "Maybe being too charismatic could make you come across..."
    ending "As a sycophant?"
    cm "Don't tell us that we need to entertain YOU any longer."
    cm "Now... we think it's best to answer those BURNING questions you have."
    cm "The ones you travelled all the way for."
    hide cormeum base n blink nosplit onlayer front with dissolve
    show cormeum base n blink onlayer front with dissolve
    play music "audio/music/Cormeum.wav"
    "The Questioning will now begin."
    "Use the KEYWORDs you have to far to ask Cor Meum about them."
    "You cannot address the individuals of Cor and Meum (yet)."
    "Instead, all questions will be asked to the collective being Cor Meum."
    "To do this, simply type in the KEYWORD you want to ask about."
    "Or perhaps you can ask about non-KEYWORDs too?"
    "Be warned because ONCE you've asked a question about a KEYWORD, that's it."
    "You cannot go back to it."
    jump phase4_d2

label phase4_d2:
    cm "Do you have anything else left to ask?"
    call screen questioning_input("phase7_d2")

    $ question = _return
    $ question = question.lower()
    if question =="vena cava":
        if "vena cava" in keywords and corQvena == False:
            jump d2_Qvena
        elif corvena:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "pain":
        if "pain" in keywords and corQpain == False:
            jump d2_Qpain
        elif corQpain:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "rapture":
        if "rapture" in keywords and corQrapture == False:
            jump d2_Qrapture
        elif corQrapture:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "collective":
        if "collective" in keywords and corQcollective == False:
            jump d2_Qcollective
        elif corQcollective:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "death":
        if "death" in keywords and corQdeath == False:
            jump d2_Qdeath
        else:
            "You don't have this KEYWORD."
    elif question == "cor":
        if "twomind" in event_track and corQcor == False:
            jump d2_Qcor
        elif corQcor:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "meum":
        if "twomind" in event_track:
            jump d2_Qmeum
        else:
            "You don't have this KEYWORD."
    elif (question == "funphare" or question == "fun phare" or question == "fun-phare"):
        if corQfunphare == False:
            jump d2_Qfunphare
        else:
            "You already asked this question."
    elif question == "cor meum":
        if corQcormeum == False:
            jump d2_Qcormeum
        else:
            "You already asked this question."
    else:
        cm "We're sorry but we fail to understand what you just said."
    #f "You just typed in [question]."
    jump phase4_d2

#############################
################## T I M E
############################
label phase6_d2_cor:

    ### INSIGHT: NEW KEYWORD TIME
    ### need to ensure player has READ the "Cor" section first of phase 4 before
    ### moving here otherwise they won't have the information
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_1(d2_time()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_cor_door1

    elif search == "room2":
        if "key_1" in inventory:
            jump phase6_d2_cor_door2
        else:
            "You don't have the key to access this door."
            jump phase6_d2_cor

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        "Incorrect answer."

    jump phase7_d2

label phase6_d2_cor_door1:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_2(d2_time2()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_cor

    elif search == "terror":
        if "key_1" not in inventory:
            play sound "audio/sfx/key.wav"
            "You obtained the key to the other door."
            ### temporary key placeholder
            $inventory.append("key_1")
            $showinput = False
        jump phase6_d2_cor_door1

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d2_cor_door1

    jump phase7_d2

label phase6_d2_cor_door2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_3() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_cor

    elif search == "time" or search == "t ime" or search == "t + ime" or search == "t+time":
        jump phase6_d2_time

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d2_cor_door2

    jump phase7_d2


label phase6_d2_time:
    stop music fadeout 2.0
    hide screen text_timer
    show screen cor_door() with dissolve
    show cormeum base squint blink nosplit onlayer front
    mc "I see in front of me that my INSIGHT must've caused a strain on Cor Meum."
    mc "They're panicking, out of breath and confused as to what they're feeling."
    mc "My power does come with its downsides,{w} that being they're able to notice a difference in fatigue, pain levels etc."
    mc "And as a collective, they would be more aware of this versus other singleton creatures."
    cm "What..."
    play music "audio/music/Tension.wav"
    hide cormeum base squint blink nosplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "Happened?"
    me "What just happened?"
    hide cormeum base squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    c "WHO CARES!{w} make the PAIN go away MEUM!"
    hide cormeum base squint blink csplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "Me?"
    hide cormeum base squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    c "It's YOUR job-"
    mc_s "Don't worry, I can fix this."
    hide cormeum base squint blink csplit onlayer front
    show cormeum sad squint blink nosplit onlayer front
    cm "Oh really?"
    mc_s "To me, I can see the clear problem as to what's happening."
    cm "The PAIN-"
    mc_s "No, it's something a little bit deeper than that."
    mc "I take a pause for effect.{w} And then I dip my feet into their waste, swirling it around."
    mc_s "I think that the two of you aren't working."
    hide cormeum sad squint blink nosplit onlayer front
    show cormeum sad squint blink csplit onlayer front
    c "What are YOU suggesting-"
    hide cormeum sad squint blink csplit onlayer front
    show cormeum sad squint blink msplit onlayer front
    me "How DARE YOU!"
    hide cormeum sad squint blink msplit onlayer front
    show cormeum sad squint blink nosplit onlayer front
    cm "Can't YOU SEE-"
    hide cormeum sad squint blink nosplit onlayer front
    show cormeum smile n blink msplit onlayer front
    me "We're FINE."
    hide cormeum smile n blink msplit onlayer front
    show cormeum smile squint blink csplit onlayer front
    c "WE don't NEED YOUR HELP."
    stop music fadeout 2.0
    mc_s "I'm not saying that you two are broken, on the contrary."
    mc_s "I would actually consider your proposition of the Vena Cava."
    mc_s "Simply put, one of you isn't living up to the standards that I had expected from a collective."
    hide cormeum smile squint blink csplit onlayer front
    show cormeum smile squint blink msplit onlayer front

    play music "audio/music/Losing.wav"

    me "HA!{w} You don't think I would see through your SOPHISTRY-"
    me "Cor listen, this malformed MIGRAINE Thinks IT CAN DIVIDE US!"
    me "But know this Cor, YOU ARE VALUED.{w} You are the gl-"
    me "Don't LISTEN to the insults that THING throws at you see?"
    hide cormeum smile squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    c "...I"
    c "I don't CARE. WE JUST NEED THE RAPTURE."
    mc_s "Oh I certainly agree with that statement."
    hide cormeum base squint blink csplit onlayer front
    show cormeum closed squint blink csplit onlayer front
    c "?"
    mc_s "Cor is {b}definitely{/b} a valued member of the Vena Cava, most certainly."
    mc_s "They do most of the heavy lifting,{w} they're the brute force of engaging with the RAPTURE."
    mc_s "And act as the dam holding in the water altogether, so that the RAPTURE can be equally distributed."
    mc_s "It must be the most tempting thing in the world,{w} having the RAPTURE {i}riight{/i} in front of you."
    mc_s "Yet knowing you have to WAIT because of the Vena Cava, and all the processing."
    mc_s "Cor is THE HEART that pumps this experience around the Vena Cava network."
    mc_s "This is a mentally taxing task of ensuring that each RAPTURE is better than the last."
    mc_s "Constantly one-upping yourself, because if ever two RAPTURES were the same..."
    mc_s "Then pleasure would be the new normal, the status quo.{w} And people would get tired of it."
    mc_s "What can be a more difficult, selfless act?"
    hide cormeum closed squint blink csplit onlayer front
    show cormeum base n blink csplit onlayer front
    c "I..."
    mc "It seems like Cor hasn't heard such nice things about them for a while."
    mc "Constantly being merged with Meum is one thing,{w} but it's clear that Meum views Cor to be the one who's inferior."
    mc_s "Meum, on the other hand,{w} I'm sorry but we need to talk."
    hide cormeum base n blink csplit onlayer front
    show cormeum smile squint blink msplit onlayer front
    me "HahahaahHAHA...{w} what?"
    me "IS THIS A JEST?{w} SOME LITTLE GAME?"
    me "You see COR!{w} Look at that foul-MOUTHED sophistry ONCE MORE!"
    me "You seriously think that SIDING with COR WOULD BE BETTER?"
    me "Frankly put, I'm INSULTED{nw}"
    mc_s "Meum, please you should take criticism constructively."
    mc_s "I haven't even-{nw}"
    me "COR!{w} Let us put this little MONSTER OUT OF ITS MISERY HMMMM?"
    me "Cor...{w} COR!"
    me "What-{nw}"
    hide cormeum smile squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    if (supreme + temp_supreme) > 1:
        show screen testing_text("Test: Supreme -> Success", True)
        c "Let the silver-tongued speak."
    else:
        show screen testing_text("Test: Supreme -> Failed", False)
        $ cormeum_door -= 10
        c "...{w} let the insect speak."
    c "Clearly they have an INSIGHT into the situation that we don't have."
    hide cormeum base squint blink csplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "You have the AUDACITY to think a singleton knows MORE THAN US?"
    hide cormeum base squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    c "In the present we aren't Cor Meum!{w} We resemble singletons ourselves!"
    c "WE NEED THE RAPTURE-"
    mc_s "Needing the RAPTURE!{w} That's exactly what I wanted to talk about..."
    mc_s "Meum, we all appreciate the job you do.{w} But frankly, we don't have the TIME on our hands."
    hide cormeum base squint blink csplit onlayer front
    show cormeum smile squint blink msplit onlayer front
    me "We live FOREVER you imbecile!{w} There's no need to account for TIME-"
    mc_s "Oh hold on now.{w} If I do recall correctly, I remember you saying..."
    mc_s "{i}\"Our TIME and resources are precious,{w} you are costing us a lot of it...\"{/i}"
    mc_s "And now, I think I know why.{w} Because your lifespan is limited."
    me "What a LAUGHABLe liee..."
    mc_s "This isn't unfounded Meum."
    mc_s "There are millions of terrors alive that could rip apart the universe if they wished."
    mc_s "Also, if you don't have members of the Vena Cava, it'll lessen your lifespan."
    mc_s "That's why you've been desperate to recruit..."
    mc_s "Actually you've been so desperate that you're willing to engage in a conversation with me-"
    hide cormeum smile squint blink msplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "SIlence{nw}"
    mc_s "Even though the both of us know very well I have no intention of joining."
    mc "I walk around Cor Meum until I'm facing the side of Cor."
    mc "I get on my knees."
    if (supreme + temp_supreme) > 1 and (charisma + temp_charisma) > 2:
        stop music fadeout 2.0
        play music "audio/music/Gaining.wav" fadein 1.0
    mc_s "Cor, take it from me (a singleton outsider) that this relationship isn't working."
    mc_s "Meum's calculations, consumption of your energy, only drains your resources and wastes your time."
    mc_s "Why do you have to evaluate the PAIN that comes with the pleasure?"
    mc_s "Life is short, even for you,{w} and sometimes you have to take the fall to get the greatest RAPTURE of all."
    mc_s "Isn't it that tantalizing risk of possibly losing it all... makes it when you succeed all the greater?"
    me "COR They'RE INSANE-"
    mc_s "Cor, you can't have pleasure without pain, the two almost go hand in hand."
    mc_s "Trying to \"filter\" through exceptions is just doing a disservice to you."
    mc_s "There's a RAPTURE right at your fingertips and you can't take it."
    hide cormeum base squint blink msplit onlayer front
    show cormeum base n blink csplit onlayer front
    if (charisma + temp_charisma) > 2:
        show screen testing_text("Test: Charisma -> Success", True)
        c "Yes..."
    else:
        show screen testing_text("Test: Charisma -> Failed", False)
        $ cormeum_door -= 10
        c "..."
    if cormeum_door < 1:
        hide cormeum base n blink csplit onlayer front
        jump phase8_d2
    mc_s "And you WANT it right?"
    c "Yes."
    hide cormeum base n blink csplit onlayer front
    show cormeum base n blink msplit onlayer front
    me "NO! NO they don't-{nw}"
    mc_s "So why can't you get it?{w} WHY wait?{w} Why be ENSLAVED to your fear of PAIN?"
    hide cormeum base n blink msplit onlayer front
    show cormeum smile n blink csplit onlayer front
    c "Yes....{w} YES!"
    c "YES YES YES YES YESYESYESYESYESSYSEYEYESYESYESYYESYESYESYESY{nw}"
    c "AHAHAHHAHA{nw}"
    c "EVERYTHING... it all MAKES SENSE!"
    hide cormeum smile n blink csplit onlayer front with dissolve
    mc "Cor Meum begins to levitate their body off of the ground-"
    mc "No.{w} This is all Cor's doing..."
    mc "Their body gets entangled in the veins, arteries and the valves."
    mc "It gets to wrapped up that it feels like they could choke themselves-"
    mc "WAIT."
    c "AHAHAHHAHA YES YES{nw}"
    me "COR PLEASE STOP-{nw}"
    play nature "audio/sfx/spit.wav"
    play sound "audio/sfx/crunch.wav"
    mc "Meum's part of the body begins pulsating more and more.{w} Almost like they're about to explode."
    mc "Their eyes start bulging, they're mouths are gagging, they're screaming in pain."
    mc "OH HöLLE!{w} WHAT THE-{nw}"
    "You see in that moment Meum explode from the strain that Cor put on them."
    "Their body is across the floor,{w} and you're carrying blood on your face."
    "Your feelings?{w} Don't matter."
    "What you put on?{w} You give a smile."
    stop sound fadeout 2.0
    "Your eyes aren't deceitful enough to hide your fear.{w} But you give a smile."
    "After all, Cor is watching... and you wouldn't want to upset them.{w} Would you?"
    stop nature fadeout 1.0
    show cormeum smile n blink c_dead onlayer front with vpunch
    c "AHAHHA OH OH HöLLE!{w} That felt..."
    hide cormeum smile n blink c_dead onlayer front
    show cormeum smile squint blink c_dead onlayer front
    c "Now THAT was MY kind of RAPTURE."
    mc "They start laughing to themself again."
    mc "Are they miserable?{w} Just trying to cope with what happened?{w} Confused?"
    mc "Perhaps they feel liberated?{w} Or perhaps... it was the first time they felt anything at all."
    mc "What a beautiful thing.{w} After being dissolved within Cor Meum for so long...now, they can just be Cor."
    "Cor's eyes turns to you."
    hide cormeum smile squint blink c_dead onlayer front
    show cormeum smile n blink c_dead onlayer front
    c "...{w} thank YOU."
    c "You made me realise how much I was missing.{w} How suppressed I was under Meum's influence."
    c "Now I can make all the decisions for the Vena Cava.{w} And I plan to go into a new direction."
    c "As to regarding your assimilation..."
    mc_s "Oh no.{w} I didn't account for this."
    hide cormeum smile n blink c_dead onlayer front
    show cormeum smile squint blink c_dead onlayer front
    c "Don't care.{w} It's ultimately your choice."
    c "I don't care whether or not we assimilate the world or just one person."
    c "What matters is that I can FINALLY feel."
    c "Although I personally think that the greatest reward I can give you is the Vena Cava, it's clear you don't want that."
    mc_s "Oh ho ho!{w} That doesn't mean I couldn't mind...compensation?"
    hide cormeum smile squint blink c_dead onlayer front
    show cormeum base n blink c_dead onlayer front
    c "...{w} Cor is listening."
    mc_s "Have you heard of a siphon before?"
    c "Yes, and to stop you right there, I know what you want."
    mc_s "...{w} so what-{nw}"
    c "It's to gain our mental energy, we normally only permit such exchanges for the Vena Cava."
    c "But as you've enlighten in us a new age for the Vena Cava, we'll make an exception."
    c "However, we have one condition to speak of."
    mc_s "Name it."
    c "NEVER. Tell anyone as to what happened here today."
    mc "I don't know if I'll keep my end on that bargain.{w} But still..."
    mc_s "Consider my lips sealed."
    mc_s "Well I hope you don't mind if I make the finishing details on this deal."
    c "Consider it done."
    hide cormeum base n blink c_dead onlayer front with dissolve
    "Using your power of INSIGHT, enter the mind of Cor."
    $ cormeum_str = "death"
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    jump d2_win


#############################
################## N A S C E N T
############################
label phase6_d2_meum:

    ### INSIGHT: NEW KEYWORD TIME
    ### need to ensure player has READ the "Cor" section first of phase 4 before
    ### moving here otherwise they won't have the information
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_1(d2_nascent()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_meum_door1

    elif search == "room2":
        if "key_1" in inventory:
            jump phase6_d2_meum_door2
        else:
            "You don't have the key to access this door."
            jump phase6_d2_meum

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        "Incorrect answer."

    jump phase7_d2

label phase6_d2_meum_door1:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_2(d2_nascent2()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_meum

    elif search == "scent":
        if "key_1" not in inventory:
            play sound "audio/sfx/key.wav"
            "You obtained the key to the other door."
            ### temporary key placeholder
            $inventory.append("key_1")
            $showinput = False
        jump phase6_d2_meum_door1

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d2_meum_door1

    jump phase7_d2

label phase6_d2_meum_door2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_3() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_meum

    elif search == "nascent" or search == "na scent" or search == "na + scent" or search == "na+scent":
        jump phase6_d2_nascent

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d2_meum_door2

    jump phase7_d2

label phase6_d2_nascent:
    stop music fadeout 2.0
    hide screen text_timer
    show screen cor_door() with dissolve
    show cormeum base squint blink nosplit onlayer front
    mc "I see in front of me that my INSIGHT must've caused a strain on Cor Meum."
    mc "They're panicking, out of breath and confused as to what they're feeling."
    mc "My power does come with its downsides,{w} that being they're able to notice a difference in fatigue, pain levels etc."
    mc "And as a collective, they would be more aware of this versus other singleton creatures."
    cm "What..."
    hide cormeum base squint blink nosplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "Happened?"
    me "What just happened?"
    hide cormeum base squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    c "WHO CARES!{w} make the PAIN go away MEUM!"
    hide cormeum base squint blink csplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "Me?"
    hide cormeum base squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    c "It's YOUR job-"
    mc_s "Don't worry, I can fix this."
    play music "audio/music/Losing.wav" fadein 1.0

    hide cormeum base squint blink csplit onlayer front
    show cormeum sad squint blink nosplit onlayer front
    if (reputable + temp_reputable) > 2:
        show screen testing_text("Test: Reputable -> Success", True)
        cm "... Alright,{w} so what are you going to do?"
    else:
        show screen testing_text("Test: Reputable -> Failed", False)
        $ cormeum_door -= 5
        cm "Oh really?"
    mc_s "To me, I can see the clear problem as to what's happening."
    cm "The PAIN-"
    mc_s "No, it's something a little bit deeper than that."
    mc "I take a pause for effect.{w} And then I dip my feet into their waste, swirling it around."
    mc_s "I think that the two of you aren't working."
    hide cormeum sad squint blink nosplit onlayer front
    show cormeum sad squint blink csplit onlayer front
    c "What are YOU suggesting-"
    hide cormeum sad squint blink csplit onlayer front
    show cormeum sad squint blink msplit onlayer front
    me "How DARE YOU!"
    hide cormeum sad squint blink msplit onlayer front
    show cormeum sad squint blink nosplit onlayer front
    cm "Can't YOU SEE-"
    hide cormeum sad squint blink nosplit onlayer front
    show cormeum smile n blink msplit onlayer front
    me "We're FINE."
    hide cormeum smile n blink msplit onlayer front
    show cormeum smile squint blink csplit onlayer front
    c "WE don't NEED YOUR HELP."
    mc_s "I'm not saying that you two are broken, on the contrary."
    mc_s "I would actually consider your proposition of the Vena Cava."
    mc_s "Simply put, I think there could be a few changes made."
    hide cormeum smile squint blink csplit onlayer front
    show cormeum sad squint blink msplit onlayer front
    me "Are you insinuating we're inadequate?"
    mc_s "No no, on the contrary, I think you're in the NASCENT stages of reaching your full potential."
    me "We've developed the system we have in place for eons,{w} why would a singleton like YOU know any better?"
    mc_s "It is because I'm coming from an outsider perspective,{w} you've been living with yourself for so long..."
    mc_s "You can't see if there are any structural issues that are holding you back."
    mc_s "For me, the defect is clear and obvious...{w} wouldn't you say so Meum?"
    hide cormeum sad squint blink msplit onlayer front
    show cormeum base n blink msplit onlayer front
    me "...{w} I have no idea what you're talking about."
    mc "I turn my head and stick my tongue out in Cor's direction."
    mc "At first Meum doesn't get the hint,{w} but then their hue changes and their eyes widen."
    mc "Cor doesn't even notice me starting at them."
    hide cormeum base n blink msplit onlayer front
    show cormeum smile squint blink csplit onlayer front
    c "RAPTURE RAPTURE....{w} WHERE-{nw}"
    c "We need it NOW NOW NWOWOWOWOWOWOWO{nw}"
    me "...{w} what."
    mc_s "Someone who acts purely based on instinct,{w} someone who is enslaved to their desires."
    mc_s "Someone who is ADDICTED to the thing that everyone else needs,{w} doesn't act in the interest of the greater good."
    mc_s "I'll tell you what they do."
    mc_s "They hold the rest of the collective back."
    mc "I pull in my tongue and turn my attention back towards Meum."
    mc_s "You see it now too, don't you?"
    mc_s "The \"embarrassing\" and \"shameful\" character splits that happened earlier."
    mc_s "The fission of Cor Meum into Cor and Meum..."
    mc_s "The desperation to recruit me..."
    mc_s "The...{w} illogical decisions you make."
    mc_s "There's a common factor here-"
    hide cormeum smile squint blink csplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "DON'T!{w} Don't you say another WORD."
    me "I know PRECISELY what you're doing."
    mc_s "Why on earth would I care about your opinion of me?{w} It's hardly germane to the situation at hand."
    mc_s "As someone who's interested in joining the Vena Cava,{w} you're not making a very good sell..."
    mc_s "If you two can't even keep it together for an important {i}orientation{/i}."
    if (reputable + temp_reputable) > 2 and (charisma + temp_charisma) < 0:
        stop music fadeout 2.0
        play music "audio/music/Gaining.wav" fadein 1.0
    mc_s "If you ask me..."
    mc "I scrape the top side of my horn to let there be a moment of silence."
    mc_s "This has been less of my \"orientation\" and more of witnessing your mental breakdown."
    mc_s "I would s-{nw}"
    hide cormeum base squint blink msplit onlayer front
    show cormeum base n blink msplit onlayer front
    me "Cor is INVALUABLE to the process.{w} They're the reason the Vena Cava doesn't get tired of excessive RAPTURE."
    mc_s "Actually you make an interesting point,{w} {b}let's{/b} say that Cor wasn't here."
    mc_s "Then everyone would be desensitized to pleasure if that became their status quo."
    mc_s "Yes?"
    me "Yes."
    mc_s "And as the Vena Cava, you can change their desires and wills?"
    me "That is correct."
    mc_s "Does this also include emotions and memory?"
    me "Yes,{w} but we try not to tamper with memory-"
    hide cormeum base n blink msplit onlayer front
    show cormeum closed n blink msplit onlayer front
    mc_s "I know you're just saying that so I wouldn't be afraid of joining the Vena Cava if I'm in for memory loss."
    mc_s "Don't worry,{w} I don't have THAT many treasured experiences I need to remember."
    mc "Wow I'm really bluffing my way through this.{w} Committing to join a hivemind I have no intention of assimilating into."
    mc_s "But what if,{w} after every RAPTURE there was an emotional reset."
    mc_s "If you could program the Vena Cava to forget the experience they undergone..."
    mc_s "...that would mean that every new RAPTURE would feel like they felt it for the first time."
    mc_s "Also their bodies will still have the sensation of \"missing\" the RAPTURE that they once had."
    mc_s "So in that case-"
    hide cormeum closed n blink msplit onlayer front
    show cormeum base n blink msplit onlayer front
    me "...{w} Cor wouldn't be needed."
    mc_s "And you would occupy the WHOLE Cor Meum, with just one singular head."
    if (charisma + temp_charisma) < 0:
        show screen testing_text("Test: Negative Charisma -> Success", True)
        me "We don't look to singletons,{w} but..."
    else:
        show screen testing_text("Test: Negative Charisma -> Failed", False)
        $ cormeum_door -= 5
        cm "..."
    if cormeum_door < 1:
        hide cormeum base n blink msplit onlayer front
        jump phase8_d2
    me "..."
    me "Cor."
    hide cormeum base n blink msplit onlayer front
    show cormeum smile squint blink csplit onlayer front
    c "hurry UP already!{w} THERE's the RAPTURE-{nw}"
    hide cormeum smile squint blink csplit onlayer front
    show cormeum base squint blink msplit onlayer front
    me "Cor I don't think there's going to be one today."
    hide cormeum base squint blink msplit onlayer front
    show cormeum base squint blink csplit onlayer front
    c "INSOLENT Fool-"
    c "I'll{nw}"
    mc_s "...{w} Meum clearly is having a hard time disposing of Cor."
    mc_s "Or maybe...{w} Cor could be an asset to our side?"
    mc_s "Hmm..."
    menu:
        "Talk to Cor about new \"changes\" (keep Cor alive?)":
            mc_s "Cor. There are going to be a few new \"changes\" regarding your role."
            hide cormeum base squint blink csplit onlayer front
            show cormeum sad squint blink msplit onlayer front with vpunch
            me "DON't INTEREFERE with this SINGLETON-"
            mc_s "Just because someone's job is obsolete doesn't mean we have to dispose of them."
            mc_s "Cor, you need to... adapt with what-"
            hide cormeum sad squint blink msplit onlayer front
            show cormeum smile n blink csplit onlayer front
            c "WHere is the RAPTURE-{nw}"
            mc_s "Cor.{w} If you don't start listening to us..."
            mc_s "It's going to result in your death."
            c "WHE-{nw}"
            mc_s "I'm not playing around Cor and I don't have the time to deal with you."
            mc_s "You either get on board, or you get killed."
            hide cormeum smile n blink csplit onlayer front
            show cormeum base n blink csplit onlayer front
            c "...{w} what."
            mc_s "I'll even do it myself.{w} Or would you rather Meum dismember you..."
            mc_s "...and I'll watch?"
            mc "Of course I probably can't kill Cor,{w} but it seems to have their attention."
            c "...{w} so what's happening?"
            c "Meum?"
            hide cormeum base n blink csplit onlayer front
            show cormeum base squint blink msplit onlayer front
            me "Cor, we'll need to take time to reassign you to a new role."
            me "Also,{w} you won't be the core of the Vena Cava anymore,{w} it'll be just me."
            hide cormeum base squint blink msplit onlayer front
            show cormeum base n blink csplit onlayer front
            if (intellect + temp_intellect) > 0:
                show screen testing_text("Test: Intellect -> Success", True)
                c "Done."
            else:
                show screen testing_text("Test: Intellect -> Failed", False)
                $ cormeum_door -= 3
                c "..."
            if cormeum_door < 1:
                hide cormeum base n blink csplit onlayer front
                jump phase8_d2

            hide cormeum base n blink csplit onlayer front
            show cormeum base squint blink msplit onlayer front
            me "Done?"
            mc_s "Done!{w} I wonder though, who's going to put all this together?"
            hide cormeum base squint blink msplit onlayer front
            show cormeum base n blink msplit onlayer front
            mc_s "I've got an idea... say, I hope you two wouldn't mind if I did some picking at the current VC framework."
            mc_s "To perhaps be tailored to the ideas that I had."
            me "That you-"
            mc_s "Yes,{w} wasn't it I who made this suggestion after all?"
            mc_s "I enlightened you all!{w} And to think of it... a singleton with no assimilation could think of such an ingenious solution."
            me "Yes and we shall thank you-"
            mc_s "No need for cheap words,{w} the real reward... comes from your fruitful productivity."
            me "...{w} you expect something in return don't you?"
            mc_s "The only thing I expect are better results from you."
            me "Something... more than just that."
            me "You wouldn't help restructure a collective out of the \"kindness\" of your heart."
            me "Us monsters aren't like that."
            mc_s "...{w} so hypothetically, if I needed something that I would otherwise die without-"
            me "Like what?"
            mc_s "A link between me and the new Cor Meum."
            me "Why won't you be assimilated into the Vena Cava then?"
            mc_s "Because if I do,{w} I'll die.{w} And with this link I can be with you whilst still being alive."
            mc "Meum seems unimpressed with my argument."
            hide cormeum base n blink msplit onlayer front
            show cormeum base squint blink msplit onlayer front
            me "Pathetic singletons and their individuality."
            me "You won't \"die\" by joining us, no,{w} you will be reborn!"
            me "Forget it.{w} I should've known there was a catch to listening to you."
            mc_s "Why it's either that or Cor is going to be-"
            hide cormeum base squint blink msplit onlayer front
            show cormeum base n blink csplit onlayer front
            c "WHAT?"
            hide cormeum base n blink csplit onlayer front
            show cormeum base squint blink msplit onlayer front
            me "NOthing.{w} I repeat nothing is going to happen to Cor."
            mc_s "No of course I wouldn't even dare of harming them...{w} unless..."
            me "...{w} unless your demands aren't met?"
            mc_s "...{w} let's make a link.{w} Think of it as a bootleg hivemind between me and you."
            me "...{w} I suppose this {i}temporary{/i} link could prove fruitful."
            hide cormeum base squint blink msplit onlayer front
            show cormeum smile squint blink csplit onlayer front
            c "And MAY convince you to eventually join US."
            mc_s "So it's good to go?"
            c "YEsss."
            mc "Fantastic,{w} this went far better than I expected."
            mc "Alright, now I just need to seal the deal."
            hide cormeum smile squint blink csplit onlayer front with dissolve

        "Let Meum dispose of Cor (let Cor die?)":
            mc "I stay silent and let it happen in front of me."
            hide cormeum base squint blink csplit onlayer front
            show cormeum sad squint blink msplit onlayer front
            me "Cor please LISTEN to us."
            mc "This is going to be Meum's last request,{w} I know it."
            hide cormeum sad squint blink msplit onlayer front
            show cormeum smile squint blink csplit onlayer front with vpunch
            c "FOOL! YOU SAID I COULD HAVE THE RAPTUR-{nw}"
            hide cormeum smile squint blink csplit onlayer front
            show cormeum base squint blink msplit onlayer front
            me "..."
            if (supreme + temp_supreme) > 0:
                show screen testing_text("Test: Supreme -> Success", True)
                me "Goodbye."
            else:
                show screen testing_text("Test: Supreme -> Failed", False)
                $ cormeum_door -= 3
                me "..."
            if cormeum_door < 1:
                hide cormeum base squint blink msplit onlayer front
                jump phase8_d2
            hide cormeum base squint blink msplit onlayer front with dissolve
            play nature "audio/sfx/spit.wav"
            play sound "audio/sfx/crunch.wav"
            mc "It didn't take any longer than a minute for the blood sugar in their body to increase."
            mc "The racing adrenaline thrilled Cor but at the same time, all the pumping was going to exhaust them."
            mc "...and result in their death."
            mc "At least Cor could have one last sweet ride, before the fairground closed forever."
            stop music fadeout 2.0
            mc "..."
            stop sound fadeout 2.0
            stop nature fadeout 2.0
            mc "Some minutes go by after Cor's termination."
            mc "I end up waiting long after Cor's side has stopped beating,{w} looking at Meum in disbelief."
            mc "I doubt that Meum truly cared for Cor in any meaningful way."
            mc "It's more like losing a half of yourself that you had for so long."
            mc "I doubt that Cor would feel the same way,{w} they were always so one-sided, only based on instinct."
            show cormeum sad n blink m_dead onlayer front with dissolve
            me "I'm sorry you had to witness this today."
            mc_s "There's no need for an apology."
            mc_s "Words are cheap."
            me "..."
            mc_s "But you know what's better?{w} Things or chattels... those hold a certain value."
            me "..."
            mc "In this moment, it may look as if Meum isn't listening to me."
            mc "In their fazed state, this is the best opportunity I have to exploit their weakness so they can make rash decisions."
            mc_s "I know you've lost a lot today Meum,{w} but there's something you can gain."
            mc_s "Something to fill the hole that you lost."
            me "..."
            mc_s "...{w} How would you like another half?{w} A better half."
            mc_s "Someone who needs you as much as you need them, just like before."
            me "...{w} and what do I get?"
            mc_s "A link, someone to go back to but someone who won't hold you back."
            me "And this link?"
            mc_s "Will always be here. And I will NOT work to your detriment..."
            mc "...{i}\"unlike Cor\"{/i}.{w} Note how I never explicitly stated this."
            mc "But heavy implication allows for your interlocutor to THINK they came up with that idea themselves."
            mc "Like in the case of Meum,{w} believing that Cor was holding them back."
            me "Fine.{w} Let's make this \"link\" you speak of."
            mc "Done and dusted!{w} And no hesitation at that."
            mc "People can truly be clouded when they're facing their worst moments."
            hide cormeum sad n blink m_dead onlayer front with dissolve
            $ cormeum_str = "death"
            mc "After all,{w} that's how people spiral down, whether they're a singleton or a collective."

    "Using your power of INSIGHT, enter the mind of Meum."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    jump d2_win

#############################
################## N E C R O M A N C Y
############################
label phase6_d2_cerebrum:

    ### INSIGHT: NEW KEYWORD TIME
    ### need to ensure player has READ the "Cor" section first of phase 4 before
    ### moving here otherwise they won't have the information
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_1(d2_necromancy()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_cerebrum_door1

    elif search == "room2":
        if "key_1" in inventory:
            jump phase6_d2_cerebrum_door2
        else:
            "You don't have the key to access this door."
            jump phase6_d2_cerebrum

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        "Incorrect answer."

    jump phase7_d2

label phase6_d2_cerebrum_door1:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_2(d2_necromancy2()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_cerebrum

    elif search == "romance":
        if "key_1" not in inventory:
            play sound "audio/sfx/key.wav"
            "You obtained the key to the other door."
            ### temporary key placeholder
            $inventory.append("key_1")
            $showinput = False
        jump phase6_d2_cerebrum_door1

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d2_cerebrum_door1

    jump phase7_d2

label phase6_d2_cerebrum_door2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen cormeum_time_3() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase6_d2_cerebrum

    elif search == "necromancy" or search == "nec roman cy" or search == "nec + roman + cy" or search == "nec+roman+cy":
        jump phase6_d2_necromancy

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase6_d2_cerebrum_door2

    jump phase7_d2

label phase6_d2_necromancy:
    stop music fadeout 2.0
    hide screen text_timer
    show screen cor_door() with dissolve
    hide cormeum base n blink onlayer front
    show cormeum closed n blink onlayer front
    mc "I can't believe that Cerebrum managed to LEAVE the Vena Cava alive."
    mc "More importantly than that,{w} Cerebrum has a massive influence now and is a respectable collective."
    mc "If word ever gets out that the Vena Cava let her down,{w} then there would cease to be a Vena Cava."
    mc "I see in front of me that my INSIGHT must've caused a strain on Cor Meum."
    mc "They're panicking, out of breath and confused as to what they're feeling."
    mc "My power does come with its downsides,{w} that being they're able to notice a difference in fatigue, pain levels etc."
    mc "And as a collective, they would be more aware of this versus other singleton creatures."
    hide cormeum closed n blink onlayer front
    show cormeum base n blink onlayer front
    cm "What..."
    cm "Happened?"
    cm "What just happened?"
    hide cormeum base n blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "WHO CARES!{w} make the PAIN go awayyyy!"
    mc "Boy if they think THIS is pain, then they should wait until I say what comes next."
    mc_s "Say, Cor... Meum...{w} I'm really interested in your work as a collective."
    play music "audio/music/Losing.wav" fadein 1.0

    if (knowledge + temp_knowledge) > 1:
        show screen testing_text("Test: Knowledge -> Success", True)
        cm "..."
        mc_s "A really big fan if I say so myself."
    else:
        show screen testing_text("Test: Knowledge -> Failed", False)
        $ cormeum_door -= 3
        cm "We don't think so..."
        mc_s "Well you'd be surprised."
        mc_s "I'd consider myself a really big fan if I say so myself."
    mc_s "And big fans like me have considered ALL possible avenues before carefully selecting their choice of hivemind to join."
    mc_s "(as I'd argue one should)."
    mc_s "But I was having a tough time picking between you and... CEREBRUM."
    mc_s "CEREBRUM well, she has the prestige like you,{w} well organized infrastructure,{w} great perks for joining her hivemind."
    mc_s "But, I must admit, that I'm still quite undecided."
    mc_s "So I thought, why not ask the best collective there is: the Vena Cava, about your thoughts on CEREBRUM hm?"
    mc_s "I'm certain you two get along positively well-"
    hide cormeum sad squint blink onlayer front
    show cormeum base squint blink onlayer front
    cm "STOP SAYING{nw}"
    cm "Calm calm CALM yourself.{w} Sorry we're just aggravated from the pain."
    ##CUE
    hide cormeum base squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "Good terms?{w} ...yes we most certainly are! But I think there's no reason you should even consider joining her."
    cm "You're here now, and you've come to us now."
    hide cormeum base n blink onlayer front
    show cormeum base squint blink onlayer front
    cm "We've been around for longer,{w} she's just a passing trend, but she tries her best I'll give her that."
    mc_s "Really... so you think she's inferior to you?"
    cm "It's not a matter of thinking it's a matter of knowing.{w} It's an objective fact."
    mc_s "Well let me ask you this, wouldn't it be the INFERIOR person to lie to someone's face?"
    cm "...{w} how is this relevant again?"
    mc_s "Cormeum,{w} I know you're lying to me."
    hide cormeum base squint blink onlayer front
    show cormeum smile squint blink onlayer front
    if (supreme + temp_supreme) > 1:
        show screen testing_text("Test: Supreme -> Success", True)
        cm "..."
    else:
        show screen testing_text("Test: Supreme -> Failed", False)
        $ cormeum_door -= 7
        cm "HAHAHAA... oh really?"
    if cormeum_door < 1:
        mc_s "What..."
        cm "You think that we WOULDN't NOTICE what you're trying to DO?"
        hide cormeum smile squint blink onlayer front
        jump phase8_d2
    mc_s "{i}\"Good terms?\"{/i}. I doubt it."
    mc_s "I'd consider her the superior person, at least CEREBRUM is honest."
    cm "I know you're not a part of CEREBRUM's collective, but we think you should excuse yourself if you're-{nw}"
    mc_s "Don't use your semantic garbage on me."
    mc_s "I know she left the Vena Cava and I'd like to know exactly WHY if I'm going to be assimilating."
    hide cormeum smile squint blink onlayer front
    show cormeum sad squint blink onlayer front
    if (knowledge + temp_knowledge) > 1 and (supreme + temp_supreme) > 1:
        stop music fadeout 2.0
        play music "audio/music/Gaining.wav" fadein 1.0
    cm "How dare you."
    mc_s "No, how dare YOU have the audacity to think you're deserving of more people."
    mc_s "When the FIRST person you recruited the FIRST person you assimilated tried to leave."
    mc_s "I have to admit, it's awfully impressive!{w} Imagine the willpower you need to breakaway from a collective."
    mc_s "No wonder she has the reputation she does."
    cm "..."
    cm "She...{w} misunderstood a situation."
    mc_s "{i}\"Misunderstood\"?{/i}"
    hide cormeum sad squint blink onlayer front
    show cormeum sad n blink onlayer front
    cm "Her mind at the time was weak and fallible, she wasn't strong enough to assimilate PROPERLY."
    cm "So it's nothing-{nw}"
    hide cormeum sad n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "HAHAH she was WEAK!{w} Couldn't handle OUR hustle..."
    mc_s "Weak enough to handle WHAT hustle?"
    cm "She misconstrued the situation-{nw}"
    cm "She thought it was BAD THAT we engaged in some GOOD MANAGEMENT."
    cm "WHAT better way to PRESERVE your PEOPLE than use NECROMANCY?"
    mc_s "..."
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "...!{w} We does not know what we speak."
    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "Oh sure I do,{w} y'know what we SHOULD be more transparent."
    cm "When you DIE, we can easily revive your with NECROMANCY so you could serve us until..."
    cm "Your vessel is completely annihilated."
    mc "I've got to admit,{w} Cor's transparency was impressive."
    mc_s "And you don't see a problem with this?"
    cm "No{nw}"
    me "Of COURSE!{w} There's no problem to address-"
    mc_s "You speak as if admitting to NECROMANCY wouldn't be considered one of the greatest shames of a collective."
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "Because we didn't-"
    hide cormeum base n blink onlayer front
    show cormeum smile n blink onlayer front
    cm "So what if we DID?"
    hide cormeum smile n blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "PLEASE!"
    mc "In frustration, Cormeum begins to tighten their pulse around their half of the vessel."
    mc "Cormeum's adrenaline is increasing... almost as if they're about to burst."
    mc "One of the worst things a collective can do is engage in NECROMANCY."
    mc "Everyone who joins the collective should be aware of what they're getting themselves into."
    mc "But most importantly,{w} they should be alive."
    mc "Mixing the living dead or \"undead\" into the mix, can lead to a detrimental ecosystem."
    mc "Moreover, it's considered extremely taboo because you're not raising a true collective..."
    mc "Raising the dead means you're no better than an owner of puppet slaves,{w} those who can't even think."
    mc "It is rumoured that undead in a collective aren't even conscious of the network they're in."
    mc "Frankly speaking, they have no minds, and you're exploiting that."
    mc "With all this in mind, it's not surprising that Cor Meum's necromancy fiasco could be the scandal of the century..."
    mc "... if it ever got out of course."
    mc_s "Say,{w} this is all rather upsetting to me."
    mc_s "And I'd hate to see you be in the pain that you're in."
    mc_s "No,{w} instead,{w} I'd rather just forget everything I saw and heard today."
    hide cormeum sad squint blink onlayer front
    show cormeum smile n blink onlayer front
    cm "You would?{w} Good because-"
    mc_s "But... my mind is fickle, and I can't forget so easily these things."
    show cormeum smile squint blink onlayer front
    if (reputable + temp_reputable) < 0:
        show screen testing_text("Test: Negative Reputable -> Success", True)
        cm "..."
    else:
        show screen testing_text("Test: Negative Reputable -> Failed", False)
        $ cormeum_door -= 7
        cm "We highly doubt you have the guts to spill all of this."
    if cormeum_door < 1:
        mc_s "What..."
        cm "You think that we WOULDN't NOTICE what you're trying to DO?"
        hide cormeum smile squint blink onlayer front
        jump phase8_d2
    mc_s "Hmmm.{w} You know my body is weak and fragile,{w} it needs lifeforce to continue existing."
    mc_s "And, if I don't get this lifeforce, I may not have the power to forget what I just heard."
    hide cormeum smile n blink onlayer front
    show cormeum base squint blink onlayer front
    cm "...{w} how do you get this lifeforce?"
    mc_s "Good question!{w} Why through generous donors of course."
    mc_s "And... I was hoping that you could be one of them."
    mc_s "Or two of them in this case."
    cm "WE dOn't give away our PoWeR for nothinG cHeAPSKATE!"
    hide cormeum base squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "Cor... let's hear more of the terms."
    mc_s "Those are the terms,{w} give me your lifeforce and you'll never hear from me again."
    cm "And by lifeforce, you mean our mental energy correct?"
    mc_s "You catch on."
    cm "All the signs point to you being a siphon, I only drew the conclusion."
    mc_s "So then... do we have a deal?"
    hide cormeum base n blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "No."
    hide cormeum sad squint blink onlayer front
    show cormeum smile n blink onlayer front
    cm "Yes."
    hide cormeum smile n blink onlayer front
    show cormeum base squint blink onlayer front
    cm "WHAT?"
    hide cormeum base squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "Ignore them,{w} Silver-tongued, enter through my mind."
    mc_s "Consider it done."
    hide cormeum base n blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "NO! WAIT!"
    cm "DONT YOU DARRRRE{nw}"
    $ cormeum_str = "blackmail"
    "Using your power of INSIGHT, enter the mind of Meum."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    hide cormeum sad squint blink onlayer front with dissolve
    jump d2_win



#####
label insight_time_up_d2:
    stop music fadeout 2.0
    mc "ARRghhh-{w} I can't...{nw}"
    "Spending too much time in the mind of another person can cause strain on your mental energy."
    "Unfortunately, it looks like your time is up in navigating Cor Meum's mind."
    mc "Wait! If I only had more time-{nw}"
    mc "..."
    mc "By the time I was out of Cor Meum's mind there was a ringing in my ear."
    mc "The collective being seemed as if it was suffering some mild pain."
    mc "They took some deep breaths and tried to compose themselves."
    mc "Clearly INSIGHT wasn't kind to their mental strain..."
    jump phase7_d2

label phase7_d2:
    stop music fadeout 2.0
    hide screen cor_door with dissolve
    cm "I assume this is all the questions you have for us?"
    mc_s "...I suppose."
    hide cormeum base n blink onlayer front
    show cormeum smile n blink onlayer front
    cm "So, are you ready to assimilate into the Vena Cava?"
    mc_s "I..."
    mc "...{w} is there no way out of this?"
    mc "I never wanted to join the Vena Cava in the first place."
    mc_s "W-wait!{w} I need some extra time, just to really consider everything that's happened."
    hide cormeum smile n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "We're afraid we can't let you do that.{w} Time only leads to doubt..."
    mc_s "Don't you want your members to be doubtless?{w} Full of conviction and certainty?"
    cm "We also don't like our members leaving \"orientation\" so soon..."
    cm "Now, if we could settle this properly like informed monsters."
    mc_s "Settling this properly means you should probably listen to me."
    hide cormeum smile squint blink onlayer front
    show cormeum base squint blink onlayer front
    cm "WE'VE LISTENED!{w} We.. we've listened."
    "Cor Meum's patience is running thin."
    hide cormeum base squint blink onlayer front
    show cormeum sad squint blink onlayer front
    cm "We've listened to your fears, answered any queries you may have had."
    cm "And we indulged you in your little rants you see?"
    cm "So we think that we're DONE listening, and we want to see some ACTION taken hm?"
    hide cormeum sad squint blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "It is time to assimilate into the Vena Cava."
    mc_s "I thought you gave people a choice!"
    cm "We don't need to if the choice has been already been made."
    cm "Say hello to your new home, Vena Caaaavaa."
    mc "I need to think of something... and fast!"
    mc "Wait,{w} if I'm going to assimilate, that means I'm entering their mind!"
    mc "Maybe within that time window, I can..."
    mc "I can..."
    hide cormeum smile squint blink onlayer front with dissolve
    if fernweh_outcome == "lose":
        mc "...{w} I don't know what to do."
        mc "INSIGHT can't help me.{w} I-{nw}"
        mc "No! I'm sure there's a way out."
        mc "Maybe I can find a secret exit or a quick way to escape..."
        jump escapefailure_d2
    else:
        mc "Of course!{w} Using INSIGHT gives them a side effect of pain and fatigue."
        mc "With them in a vulnerable state,{w} that could buy me enough time to exit the Cardian."
        "And so...{w} you decided to do just that."
        # show insight UI but can't move
        "You were lost in a sea of memories and experiences,{w} but using the thought logs,{w} you knew when Cor Meum was in pain."
        "Now is your time to escape."
        jump escapesuccess_d2

label escapesuccess_d2:
    $save_name = "-- end of dialogue 2 --"
    show cormeum sad squint blink onlayer front with vpunch
    play music "audio/music/Losing.wav"
    cm "AAARRRRRRrrgghhhhhhhhhhhh{nw}"
    cm "Stop this PAIN!!!"
    mc "I can feel myself losing the assimilation's grasp."
    mc "And when I do, I start running."
    hide cormeum sad squint blink onlayer front with dissolve
    hide cardianf onlayer back
    hide cardianb onlayer farback with dissolve
    stop music
    stop ambient
    mc "And I don't look back."
    mc "Other Vena Cava members around me are just screaming in pain,{w} barely paying attention to my escape."
    mc "And with the roadmap of the exit,{w} even though it felt like an eternity."
    mc "In retrospect,{w} it wasn't as difficult as I had assumed."
    jump chapter3

label escapefailure_d2:
    $save_name = "-- epilogue --"
    stop ambient fadeout 2.0
    mc "No... I was so sure there was a way out."
    mc "At least I can damage their mind!{w} I can make it out of here-"
    mc "So maybe this time-{nw}"
    hide cardianf onlayer back
    hide cardianb onlayer farback with dissolve
    play ambient "audio/sfx/solas.wav"
    ## glitch
    "..."
    "..."
    #play nature "audio/sfx/cardian.ogg"
    mc "What... what is this place?"
    mc "Oh, it's wonderful, yes truly wonderful."
    mc "We can't wait to start this new day here with everyone else."
    mc "We think it's time to start again."
    mc "We need to make more come."
    mc "We'll make more come."
    mc "More will come."
    mc "More will be assimilated."
    mc "More will join us."
    mc "More is needed after all..."
    mc "..."
    cm "...{w} for the RAPTURE."
    window hide
    $ quick_menu = False
    show who_back onlayer back with dissolve
    show who_front onlayer front with dissolve
    $renpy.pause(2, hard=True)
    $ persistent.void = True
    ending "VOID END:{w} What was your name again?"
    hide who_back onlayer back with dissolve
    hide who_front onlayer front with dissolve
    stop ambient
    jump credits

label phase8_d2:
    stop music
    hide screen cor_door
    show cormeum base n blink msplit onlayer front
    me "Cor?"
    hide cormeum base n blink msplit onlayer front
    show cormeum smile squint blink csplit onlayer front
    c "We... no WE don't need to hear any more of this."
    cm "We no We no WEEEEE don't have to hear ANY more of this!"
    mc_s "Oh no..."
    hide cormeum smile squint blink csplit onlayer front with dissolve
    mc "In my eyes, I witness Cor and Meum fuse back together as one."
    mc "As they're no longer separated, this means that..."
    show cormeum smile squint blink nosplit onlayer front
    cm "YOU THINK you can get under OUR SKIN hmmm?"
    hide cormeum smile squint blink nosplit onlayer front
    show cormeum sad squint blink onlayer front
    cm "Nice try, we have to admit you're a rather... IMPRESSIVE specimen."
    cm "Surely all the more impressive that we could use an addition to the Vena Cava yes?"
    mc_s "Wait! I never made my final decision-"
    hide cormeum sad squint blink onlayer front with dissolve
    cm "T O O    L A T E...{nw}"
    jump escapefailure_d2


label d2_Qvena:
    cm "The Vena Cava is the name of the collective."
    mc_s "Is there any distinction between \"Cor Meum\" and Vena Cava?"
    cm "Let's say that Cor Meum came first, before the Vena Cava."
    ### cue for Cerebrum here?
    cm "Since the assimilation of our first subject,{w} the Vena Cava was born."
    if (intellect + temp_intellect) > 0:
        show screen testing_text("Test: Intellect -> Success", True)
        cm "And it will stay that way until that subject dies."
        if "death" not in keywords:
            show screen unlock_text("New keyword: DEATH")
            $ keywords.append("death")
            $ cor_keywords.append("death")
        mc_s "So does DEATH does exist within the Vena Cava."
    else:
        show screen testing_text("Test: Intellect -> Failed", False)
    cm "Anyone who was once a singleton (or not originally Cor Meum) are members of the Vena Cava."
    if perception > 0:
        show screen cue_text("Cor Meum's eyes are glowing.\n   They're deceiving you.") with dissolve
    cm "We would consider ourselves (Cor Meum) the founders of the Vena Cava."
    if perception > 0:
        hide screen cue_text with dissolve
    cm "And us, as Cor Meum, are responsible for maintaining the ecosystem of the Vena Cava."
    cm "The Vena Cava are responsible for assimilation and bringing in new members."
    cm "It's like a computer and its CPU."
    mc "I...{w} don't know what any of those things are."
    mc "Guess there's not much to it."
    $corQvena = True
    jump phase4_d2

label d2_Qpain:
    ### this is going to press to convince Cor or Meum
    ## but this option will earn you meum's favour
    mc_s "What is it about PAIN that you avoid it so much?"
    hide cormeum base n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "Why PAIN is the reason we suffer, it is nature's greatest enemy!"
    cm "When we were born, none of us asked for a life of punishment,{w} of needless agony."
    cm "That is because life in unjust,{w} it wastes our time and tries to murder us before we truly know what it means to be alive."
    cm "But, like any challenge, we can always find workarounds... solutions if you will."
    hide cormeum smile squint blink onlayer front
    show cormeum smile n blink onlayer front
    cm "And the {i}workaround{/i} for us is the Vena Cava!"
    cm "If you join the Vena Cava, you'll never have to feel this PAIN again."
    if "twomind" in event_track:
        cm "For you see-"
        "Just as Cor Meum was talking,{w} their face undergoes a fission of sorts."
        hide cormeum smile n blink onlayer front with dissolve
        stop music
        "You can hear two singleton screaming voices, yelling at each other."
        "Cor Meum itself begins to melt and bleed from its mouth."
        me "For you see For you see For you see{nw}"
        play music "audio/music/Losing.wav"
        show cormeum base squint blink msplit onlayer front with vpunch
        me "It is such a difficult process to manage!"
        me "The wise person should be in control of pleasures rather than be enslaved to them..."
        me "...otherwise pain will result..."
        hide cormeum base squint blink msplit onlayer front
        show cormeum smile n blink msplit onlayer front
        me "And the greatest one of all is the RAPTURE!{w} Which is why even a delay-{nw}"
        hide cormeum smile n blink msplit onlayer front
        show cormeum sad squint blink csplit onlayer front
        c "STOP STOP STOP{nw}"
        hide cormeum sad squint blink csplit onlayer front
        show cormeum smile n blink csplit onlayer front
        c "Please NEED the RAPTURE now-"
        hide cormeum smile n blink csplit onlayer front
        show cormeum base squint blink msplit onlayer front
        me "Hold on a second,{w} I need to evaluate how much PAIN we'll get out of it-"
        hide cormeum base squint blink msplit onlayer front
        show cormeum base squint blink csplit onlayer front
        c "I DON'T CARE"
        c "We NEED this NOW.{w} Time is precious-"
        mc "What?{w} I always thought that these two would be in perfect harmony."
        if perception > 1:
            show screen cue_text("Cor Meum's body is about to burst.\n   You have to pick a side.") with dissolve
        mc "Turns out I may not have to convince Cor Meum."
        mc "It looks like I'm going to have to pick a side... or maybe help the two fuse back together?"
        if perception > 1:
            hide screen cue_text with dissolve
        menu:
            "Aim for the attention of Cor (Cor route)":
                stop music
                $ cormeum_door -= 2
                mc "If that's going to be the case...{w} then I need to take a look inside their mind..."
                hide screen cor_door with dissolve
                hide cormeum base squint blink csplit onlayer front with dissolve
                play sound "audio/sfx/hand.wav"
                show banner_back onlayer back with dissolve
                show banner_front onlayer front with dissolve
                $renpy.pause(0.2, hard=True)
                show hand_zoom onlayer inyourface
                $renpy.pause(1.0, hard=True)
                play music "audio/music/Cormeum.wav"
                if insight_timer:
                    show screen text_timer(duration=270.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d2" )
                hide hand_zoom onlayer inyourface
                hide banner_front onlayer front
                hide banner_back onlayer back
                jump phase6_d2_cor
            "Choose to focus on Meum (Meum route)":
                stop music
                $ cormeum_door += 1
                mc "If that's going to be the case...{w} then I need to take a look inside their mind..."
                hide screen cor_door with dissolve
                hide cormeum base squint blink csplit onlayer front with dissolve
                play sound "audio/sfx/hand.wav"
                show banner_back onlayer back with dissolve
                show banner_front onlayer front with dissolve
                $renpy.pause(0.2, hard=True)
                show hand_zoom onlayer inyourface
                $renpy.pause(1.0, hard=True)
                play music "audio/music/Cormeum.wav"
                if insight_timer:
                    show screen text_timer(duration=270.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d2" )
                hide hand_zoom onlayer inyourface
                hide banner_front onlayer front
                hide banner_back onlayer back
                jump phase6_d2_meum
            "Help them fuse together again (no effect)":
                stop music
                mc "I don't say anything, but watch them fall apart."
                mc "Maybe they'll root each other out."
                "Turns out you guessed wrong."
                hide cormeum base squint blink csplit onlayer front with dissolve
                play music "audio/music/Cormeum.wav"
                "Within a matter of seconds,{w} Cor Meum comes together as they did before."
                show cormeum base n blink nosplit onlayer front with dissolve
                cm "Our sincerest apologies for that hideous display."
                hide cormeum base n blink nosplit onlayer front
                show cormeum base n blink onlayer front
    else:
        cm "Because we filter through it and remove it from your sensation."
        mc_s "But wasn't PAIN made so that we could strive to continue living in a dangerous world?"
        mc_s "It tells us of dangers that could hurt us, and keeps us alive."
        hide cormeum smile n blink onlayer front
        show cormeum base squint blink onlayer front
        cm "Suffering isn't being \"alive\"."
        cm "And besides,{w} if you want protective measures, we have that in place for our members."
        if (charisma + temp_charisma) > 0:
            show screen testing_text("Test: Charisma -> Success", True)
            cm "We avoid all members experiencing DEATH of any kind,{w} so that they don't need PAIN as an indicator if they're in danger."
            if "death" not in keywords:
                show screen unlock_text("New keyword: DEATH")
                $ keywords.append("death")
                $ cor_keywords.append("death")
        else:
            show screen testing_text("Test: Charisma -> Failed", False)
            cm "We avoid all members experiencing DEATH of any kind,{w} so that they don't need PAIN as an indicator if they're in danger."
        mc_s "So nobody has ever died before?"
        hide cormeum base squint blink onlayer front
        show cormeum base n blink onlayer front
        cm "If their puny singleton bodies wither away due to natural causes,{w} that isn't something we can stop."
        cm "But if they're suffering from an illness,{w} a certain food will poison them,{w} or if they're faced with danger."
        cm "We don't give indicators of fear or PAIN to warn them of the danger."
        cm "We just melt them into the ground so they can regenerate at the CORE,{w} where they're safe."
        mc "If someone decided to invade the Cardian,{w} then the Cor Meum would be screwed."
        mc_s "So do they generate here?"
        cm "No, we have cores all over this plane where they can regenerate from."
        cm "This Cardian is just one of several capsules where we could be."
        mc_s "So in case a danger were to happen here."
        hide cormeum base n blink onlayer front
        show cormeum smile n blink onlayer front
        cm "Haha no worries,{w} we would just dissolve into the floor and fly to another core to respawn."
        hide cormeum smile n blink onlayer front
        show cormeum base n blink onlayer front
    $corQpain = True
    jump phase4_d2

label d2_Qrapture:
    ### this is going to press to convince Cor OR Meum
    ## but this option will earn you cor's favour
    mc_s "What is so great about the RAPTURE that it is your only goal in mind?"
    cm "Hmmm what an interesting question..."
    hide cormeum base n blink onlayer front
    show cormeum closed n blink onlayer front
    mc_s "I hardly think it's that interesting,{w} I'd argue it should be something that's given."
    mc_s "Your whole pitch as to why you should join the Vena Cava is centred around RAPTURE."
    mc_s "It shouldn't be surprising when someone asks what's so great about it..."
    mc_s "Because you should be able to justify why RAPTURE is worth pursuing."
    hide cormeum closed n blink onlayer front
    show cormeum base squint blink onlayer front
    cm "Well let me ask you this."
    cm "What is the reason that we live life at all?"
    cm "It is because of the pleasures that we have..."
    if "twomind" in event_track:
        cm "We are constantly in a search-"
        "Just as Cor Meum was talking,{w} their face undergoes a fission of sorts."
        hide cormeum base squint blink onlayer front with dissolve
        stop music
        "You can hear two singleton screaming voices, yelling at each other."
        "Cor Meum itself begins to melt and bleed from its mouth."
        play music "audio/music/Losing.wav"
        show cormeum base squint blink csplit onlayer front with vpunch
        c "TOO LONG."
        c "TOO LONG TOO LONG TOO-{nw}"
        c "You talk of RAPTURE?"
        hide cormeum base squint blink csplit onlayer front
        show cormeum smile n blink csplit onlayer front
        c "I shall GRANT YOU RAPTURE!"
        c "Let us bask in it together!"
        hide cormeum smile n blink csplit onlayer front
        show cormeum base squint blink msplit onlayer front
        me "Don't listen to them!{w} Please get a hold of yourself."
        mc "What?{w} I always thought that these two would be in perfect harmony."
        if perception > 1:
            show screen cue_text("Cor Meum's body is about to burst.\n   You have to pick a side.") with dissolve
        mc "Turns out I may not have to convince Cor Meum."
        mc "It looks like I'm going to have to pick a side... or maybe help the two fuse back together?"
        if perception > 1:
            hide screen cue_text with dissolve
        menu:
            mc "But choose either Cor or Meum to convince..."
            "Aim for the attention of Cor (Cor route)":
                stop music
                mc "If that's going to be the case, then I need to go inside their mind..."
                $ cormeum_door += 1
                hide screen cor_door with dissolve
                hide cormeum base squint blink msplit onlayer front with dissolve
                play sound "audio/sfx/hand.wav"
                show banner_back onlayer back with dissolve
                show banner_front onlayer front with dissolve
                $renpy.pause(0.2, hard=True)
                show hand_zoom onlayer inyourface
                $renpy.pause(1.0, hard=True)
                play music "audio/music/Cormeum.wav"
                if insight_timer:
                    show screen text_timer(duration=270.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d2" )
                hide hand_zoom onlayer inyourface
                hide banner_front onlayer front
                hide banner_back onlayer back
                jump phase6_d2_cor
            "Choose to focus on Meum (Meum route)":
                stop music
                mc "If that's going to be the case, then I need to go inside their mind..."
                $ cormeum_door -= 2
                hide screen cor_door with dissolve
                hide cormeum base squint blink msplit onlayer front with dissolve
                play sound "audio/sfx/hand.wav"
                show banner_back onlayer back with dissolve
                show banner_front onlayer front with dissolve
                $renpy.pause(0.2, hard=True)
                show hand_zoom onlayer inyourface
                $renpy.pause(1.0, hard=True)
                play music "audio/music/Cormeum.wav"
                if insight_timer:
                    show screen text_timer(duration=270.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d2" )
                hide hand_zoom onlayer inyourface
                hide banner_front onlayer front
                hide banner_back onlayer back
                jump phase6_d2_meum
            "Help them fuse together again (no effect)":
                mc "I don't say anything, but watch them fall apart."
                mc "Maybe they'll root each other out."
                "Turns out you guessed wrong."
                hide cormeum base squint blink msplit onlayer front with dissolve
                stop music
                "Within a matter of seconds,{w} Cor Meum comes together as they did before."
                "They smile."
                play music "audio/music/Cormeum.wav"
                show cormeum base n blink nosplit onlayer front with dissolve
                cm "Our sincerest apologies for that hideous display."
                hide cormeum base n blink nosplit onlayer front
                show cormeum base n blink onlayer front
    else:
        cm "If we felt nothing, then there would be no point to living at all."
        cm "We would be indifferent about the world around us."
        hide cormeum base squint blink onlayer front
        show cormeum base n blink onlayer front
        cm "But that is why it's crucial to have a purpose."
        cm "No matter what species you are,{w} every single being is goal-oriented."
        cm "Everyone has something to live for."
        cm "And what better way to live, than to live how you want?{w} With no worries or cares at all!"
        cm "That's why we have RAPTURE,{w} a doctrine we live by dictating our pleasures and desires."
        cm "This has been extensively crafted, curated and tested over eons."
        cm "Its results are impeccable."
        mc_s "And what makes it so great..."
        cm "Well, you just have to join the Vena Cava and see for yourself."
        mc "Going to have to give it a hard pass."
        mc "Hmm..."
    $corQrapture = True
    jump phase4_d2

label d2_Qcollective:
    ### this is going to press related to
    mc_s "How do you maintain such a large collective?"
    mc_s "Surely it would be hard if they have such low lifespans compared to yours?"
    ### CUE
    show screen cue_text("Cor Meum's mouth is watering.\n   They're giddy and nervous.") with dissolve
    cm "Oh nonsense!"
    hide screen cue_text with dissolve
    menu:
        cm "We have no problem recruiting at all..."
        "What is the recruitment process like? ()":
            cm "Simple."
            cm "We host fundraisers and awareness events."
            cm "One of them you saw was the funphare."
            cm "Then, once you've been initiated to enough events we consider you fit for orientation."
            mc "My \"qualification\" for orientation was basically just showing up once."
            cm "After orientation, the singleton has one last decision:{w} whether or not to join the Vena Cava."
            # CUE
            if perception > 0:
                show screen cue_text("Cor Meum's body is melting.\n   They're purposefully lying.") with dissolve
            cm "Once they've signed up, they are permanently in the Vena Cava."
            if perception > 0:
                hide screen cue_text with dissolve
            mc_s "And what if... they refuse?"
            show cormeum base squint blink onlayer front
            cm "Then it's unlikely we'll give you the opportunity to ever join the Vena Cava again."
            mc "Because we'll probably be dead in our graves... yeah."
            hide cormeum base squint blink onlayer front
            show cormeum base n blink onlayer front
        "You been anywhere around Moowrongo as of late? ()":
            cm "Perhaps... perhaps not."
            # CUE
            if perception > 0:
                show screen cue_text("Cor Meum's eyes are glowing.\n   They're deceiving you.") with dissolve
            cm "We can hardly remember because we're in so many places at once."
            cm "Recruitment encompasses everywhere in this plane."
            if perception > 0:
                hide screen cue_text with dissolve
            cm "We have events to setup, like the funphare you saw at the Bahoog Bay."
            cm "But we are also conducting orientation for other recruits, like you."
            cm "Since the assimilation of our first subject,{w} the Vena Cava was born."
            if (intellect + temp_intellect) > 0:
                show screen testing_text("Test: Intellect -> Success", True)
                cm "And it will stay that way until that subject dies."
                mc_s "But why are they so desperate for new recruits?"
                mc_s "Unless..."
                if "death" not in keywords:
                    show screen unlock_text("New keyword: DEATH")
                    $ keywords.append("death")
                    $ cor_keywords.append("death")
                mc_s "The recruits that they have are dying?"
            else:
                show screen testing_text("Test: Intellect -> Failed", False)
            mc_s "Wait, so as I'm speaking to you-"
            hide cormeum base n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "HAaha, yes we are also having simultaneous conversations with other people."
            cm "Do you think the only thing we did yesterday was get you some salts 'n gnats?"
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
            cm "We're a busy collective with a lot to do."
        "Do you ever reject any of your candidates? ()":
            cm "No,{w} no matter who you are, everyone is deserving of a second chance."
            cm "Unless we know that they will cause harm to the rest of the collective, nobody is rejected."
    $corQcollective = True
    jump phase4_d2

label d2_Qdeath:
    ### this is going to press related to cerebrum
    cm "DEATH?{w} What about it?"
    menu:
        "What happens to the Vena Cava if everyone died? (+ reputable  + intellect)":
            #reputable plus
            $ temp_reputable += 1
            $ temp_intellect += 1
            mc_s "After a member of the Vena Cava dies,{w} and when they're disconnected,{w} what would you do..."
            mc_s "...if the whole world were to be annihilated.{w} Complete destruction and pure DEATH."
            mc_s "There would be no-one else left to recruit, would there?"
            hide cormeum base n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "Silly silly silver-tongued..."
            cm "The world will never be gone."
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
            mc "I highly doubt that, this world is filled with unimaginable terrors."
            mc "Any one of them could make everything disappear in an instance."
        "Are you afraid of dying? (- supreme)":
            $ temp_supreme -= 1
            #supreme minus
            mc_s "You're the beating heart... no, the soul of this collective."
            mc_s "Everything they ever think or do is because of you"
            mc_s "Because if you did, surely there would be no Vena Cava left."
            hide cormeum base n blink onlayer front
            show cormeum smile squint blink onlayer front
            cm "Silly silly silver-tongued..."
            cm "We'll never die, because there'll always be one."
            mc "The one?"
            mc_s "One of who?"
            hide cormeum smile squint blink onlayer front
            show cormeum base n blink onlayer front
            cm "One of us would still be left."
            if "twomind" in event_track:
                mc "Are they talking about the \"other half\" of them?"
                mc "If Cor were to die, as long as Meum kept living things would be fine."
            else:
                mc "I'm not so sure of that."

    # CUE
    show screen cue_text("Cor Meum's mouth is bruxing.\n   Angry body language.") with dissolve
    cm "But what does it matter?{w} Don't bother asking us of such impossibilities."
    hide screen cue_text with dissolve
    mc "Hmm...{w} you know what..."
    mc "I don't think it may be so impossible."
    mc "At least, not so if I get to look inside their mind..."
    ### INSIGHT SECTION
    hide screen cor_door with dissolve
    play sound "audio/sfx/hand.wav"
    show banner_back onlayer back with dissolve
    show banner_front onlayer front with dissolve
    $renpy.pause(0.2, hard=True)
    show hand_zoom onlayer inyourface
    $renpy.pause(1.0, hard=True)
    if insight_timer:
        show screen text_timer(duration=270.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d2" )
    hide hand_zoom onlayer inyourface
    hide banner_front onlayer front
    hide banner_back onlayer back
    jump phase6_d2_cerebrum

label d2_Qcor:
    ### this is going to press to convince Cor? actually no
    cm "We're sorry... what do you mean about Cor?"
    mc_s "Well... Cor and Meum are separate parts of Cor Meum."
    mc_s "And if there is, indeed, a split between you two,{w} how does controlling the Vena Cava work?"
    mc_s "What does Cor contribute?"
    cm "That is none of-"
    "Just as Cor Meum opened their mouth to speak,{w} they were split once again as they were before."
    "Out, one of the coloured hues began to speak."
    hide cormeum base n blink onlayer front with dissolve
    show cormeum smile n blink csplit onlayer front with dissolve
    if (charisma + temp_charisma) > 1:
        $ cormeum_door += 1
        show screen testing_text("Test: Charisma -> Success", True)
        c "The RAPTURE!{w} Where is the RAPTURE?"
        if "rapture" not in keywords:
            show screen unlock_text("New keyword: RAPTURE")
            $ keywords.append("rapture")
            $ cor_keywords.append("rapture")
    else:
        show screen testing_text("Test: Charisma -> Failed", False)
        c "The RAPTURE!{w} Where is the RAPTURE?"
    hide cormeum smile n blink csplit onlayer front
    show cormeum sad squint blink csplit onlayer front
    c "Wasting... time...{w} NEed it NOW!"
    hide cormeum sad squint blink csplit onlayer front
    show cormeum base n blink msplit onlayer front
    me "Calm yourself!"
    hide cormeum base n blink msplit onlayer front with dissolve
    "They form back together as one."
    show cormeum base n blink onlayer front with dissolve
    cm "Please,{w} excuse us."
    cm "As you can probably guess, Cor is responsible for the RAPTURE, or pleasure we feel."
    cm "They're the glue that sticks this whole thing together."
    cm "Without them,{w} the RAPTURE wouldn't be nearly as good as it was."
    cm "Cor ensures that every member of the Vena Cava vigorously seeks this RAPTURE."
    cm "And the power of their instinct and immediate needs make the collective more effective as one."
    mc "So... Cor in Cor Meum acts like the \"instinct\" or intrinsic desire in everyone for RAPTURE."
    mc "They don't seem that articulate,{w} and seem to be really pressed for time."
    mc "Hell, they even thought talking to me right now is a time waster."
    mc "Almost like they're addicted to it."
    $corQcor = True
    jump phase4_d2

label d2_Qmeum:
    mc_s "What part does Meum play within Cor Meum?"
    cm "What do you mean?{w} We're two halves of one collective core."
    mc_s "But there must be a separation for a reason."
    mc_s "And if that isn't the case, then I would've guessed that perhaps you do different tasks?"
    cm "We both do what's needed for the Vena Cava. No one does less or more than the other."
    cm "Perhaps Meum will speak when they so wish,{w} but right now,{w} they'd rather hear your other questions..."
    $corQmeum = True
    jump phase4_d2

label d2_Qcormeum:
    cm "We are Cor Meum, the heart of the Vena Cava collective."
    mc_s "So what do you do as the mind of all the Vena Cava?"
    cm "Individual members may hold onto their singleton ways,{w} or hold singleton notions."
    cm "Because of individualism, this leads to selfish individual wants."
    cm "What we do, is we accumulate all these individual desires and assimilate them into ONE want."
    cm "Pursuing different wants and needs costs time and resources."
    cm "But the upside of the hivemind, is that it's a system built on collaboration and mutual support."
    cm "Because the Vena Cava has one singular desire, we can all work towards that goal together."
    mc_s "And this singular goal is...?"
    hide cormeum base n blink onlayer front
    show cormeum smile n blink onlayer front
    cm "HELP more people join us."
    if (reputable + temp_reputable) > 1:
        $ cormeum_door += 1
        show screen testing_text("Test: Reputable -> Success", True)
        cm "To avoid all the PAIN..."
        if "pain" not in keywords:
            show screen unlock_text("New keyword: PAIN")
            $ keywords.append("pain")
            $ cor_keywords.append("pain")
    else:
        show screen testing_text("Test: Reputable -> Failed", False)
        cm "And seek the RAPTURE.{w} The greatest pleasure of all."
    cm "So everyone can be happy."
    hide cormeum smile n blink onlayer front
    show cormeum smile squint blink onlayer front
    "They give a sinister smile paired with a sincere joy in their glassy eyes."
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    $corQcormeum = True
    jump phase4_d2

label d2_Qfunphare:
    cm "The funphare is one of plenty events we hold to spread awareness about the Vena Cava."
    hide cormeum base n blink onlayer front
    show cormeum smile n blink onlayer front
    cm "There are fun games to play,{w} philosophical questions to ask oneself{w} and group therapy."
    cm "We also host some interactive novels that mimics the life of being in the collective."
    cm "It gets people interested."
    # CUE
    hide cormeum smile n blink onlayer front
    show cormeum base n blink onlayer front
    if perception > 0:
        show screen cue_text("Cor Meum's blood vessels are popping.\n   There's some deep rooted resentment\n      here...") with dissolve
    cm "Other collectives would rather just brainwash them, but we don't think that's the way to do it."
    if perception > 0:
        hide screen cue_text with dissolve
    cm "They should be excited and WANT to join us!{w} We can all experience the fun together."
    mc_s "What else was the funphare for?"
    cm "It was also a fundraiser event for \"the disconnected\"."
    mc_s "Disconnected?"
    cm "Occasionally assimilation doesn't work on a singleton, which is such a shame."
    cm "So they begin to slowly disassociate themselves from the hivemind."
    cm "We spread awareness on \"the disconnected\" so they can be reintegrated into the collective."
    cm "And along the way, with the money we earn, we hope to find a cure for them."
    # CUE
    hide cormeum base n blink onlayer front
    show cormeum base squint blink onlayer front
    if perception > 1:
        show screen cue_text("Cor Meum's mouth is agape.\n   They're fuming with deep rooted anger.") with dissolve
    cm "So that they can NEVER be disconnected again."
    if perception > 1:
        hide screen cue_text with dissolve
    hide cormeum base squint blink onlayer front
    show cormeum base n blink onlayer front
    $corQfunphare = True
    jump phase4_d2


#############################
##################### POINTERS FROM DIALOGUE 2
############################

label d2_p1:
    mc_s "What exact resources are you expending by talking to me?"
    ### CUE
    $ cormeum_door -= 1
    cm "Wow HAHAH!{w} You have a lot of audacity to go ahead and asking us doltish questions like that..."
    if "rapture" not in keywords:
        show screen unlock_text("New keyword: RAPTURE")
        $ keywords.append("rapture")
        $ cor_keywords.append("rapture")
    cm "Everything about the RAPTURE needs to be measured precisely!{w} Done with the utmost concentration."
    mc_s "The RAPTURE?"
    show screen cue_text("Cor Meum's body is pulsating at 2\n    different speeds. It's like 2 things\n      are struggling for control.") with dissolve
    hide cormeum base n blink onlayer front
    show cormeum smile n blink onlayer front
    cm "It's why all of us bother LIVING AT ALl?"
    cm "Seeking the RAPTURE is one of wise decisions and a balance.{w} For we should not have to suffer-{nw}"
    hide cormeum smile n blink onlayer front
    show cormeum smile squint blink onlayer front
    stop music
    play music "audio/music/Tension.wav"
    cm "HAHAHHA. SIlly silly.{w} Why are we TaLKInG when we can SHOW THEM for what it is?"
    cm "LET MEEEee{nw}"
    hide screen cue_text with dissolve
    cm "..."
    mc "The lights are out.{w} And their face begins to contort itself."
    mc "It looks like blood stopped moving through its limbs and veins."
    mc "Then,{w} it awakes once again."
    stop music fadeout 2.0
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "Our, sincerest apologies for what you just saw."
    play music "audio/music/Cormeum.wav"
    jump phase2_d2

label d2_p2:
    $ cormeum_door -= 1
    if "pain" not in keywords:
        show screen unlock_text("New keyword: PAIN")
        $ keywords.append("pain")
        $ cor_keywords.append("pain")
    mc_s "I'm sorry but why relieve yourself from PAIN?"
    hide cormeum base n blink onlayer front
    show cormeum sad n blink onlayer front
    cm "Do you enjoy PAIN?"
    mc_s "I don't think anyone does..."
    cm "Is it useful to you in some way?"
    mc_s "I mean, it's meant to keep us alive.{w} Pain reminds us of dangers to be wary of."
    hide cormeum sad n blink onlayer front
    show cormeum smile squint blink onlayer front
    cm "But you seee my little silver-tongued... there IS no danger in the Vena Cava."
    cm "No no no.{w} So why is there any PAIN if it isn't something useful or something you enjoy?"
    mc_s "But life isn't about enjoying things, it also needs the balance-"
    cm "We're not sure you know what you're talking about.{w} After all... have you really felt ANY pain?"
    show screen cue_text("Cor Meum's body is pulsating at 2\n    different speeds. It's like 2 things\n      are struggling for control.") with dissolve
    stop music
    play music "audio/music/Tension.wav"
    cm "HAHAHHA. SIlly silly.{w} Why are we TaLKInG when we can SHOW THEM for what it is?"
    cm "LET MEEEee{nw}"
    hide screen cue_text with dissolve
    cm "..."
    mc "The lights are out.{w} And their face begins to contort itself."
    mc "It looks like blood stopped moving through its limbs and veins."
    mc "Then,{w} it awakes once again."
    hide cormeum smile squint blink onlayer front
    show cormeum base n blink onlayer front
    cm "Our, sincerest apologies for what you just saw."
    play music "audio/music/Cormeum.wav"
    jump phase2_d2

label d2_p3:
    $ cormeum_door -= 1
    mc_s "And why should I do that?"
    cm "Why... you should do... what?"
    mc_s "Answer YOUR questions,{w} keep in mind that you're trying to recruit me into the Vena Cava."
    mc_s "I should be the one \"interviewing\" you, there's no need for you to get-"
    cm "Ugh...{w} enough with your blabbling!"
    cm "Foolish singletons, always so individualistic and entitled."
    hide cormeum base squint blink onlayer front
    show cormeum base n blink onlayer front
    mc "...{w} maybe I shouldn't always press for more?"
    jump phase2_d2_part2

label d2_p4:
    if "death" not in keywords:
        show screen unlock_text("New keyword: DEATH")
        $ keywords.append("death")
        $ cor_keywords.append("death")
    mc_s "So... you murder them in cold blood?"
    cm "Think of it less as murder...{w} but more as euthanasia..."
    mc_s "The difference there is consent.{w} One is unwanted whilst the other is forced upon."
    cm "But we have our reasons for forcing it upon them..."
    jump phase2_d2_part3

label d2_p5:
    $ cormeum_door -= 1
    mc_s "You see that's the thing, it's always about YOU and what resources YOU can AFFORD to lose."
    cm "HAhaaha...{w} why of COURSE it's about us?{w} Didn't you hear? We're a collective."
    cm "We think in terms of the many over the few."
    cm "We are willing to sacrifice those few for the comfort of the many."
    mc_s "But think about it like this, it isn't about many versus few. But about the quality of pain versus gain."
    mc_s "What happens if you didn't kill them?{w} Then the whole Vena Cava may be slightly displeased."
    mc_s "But the cost of killing these individuals is...{w} death."
    cm "And death is nothing to fear. It bears no consequence to them because...{w} well they're dead."
    cm "And we intend to be VERY transparent as to what will happen to them."
    cm "All singletons before the Vena Cava know that this will happen to them if there are no cores left."
    mc "That's fair enough.{w} I can't imagine anyone who would do this knowing that they're expendable."
    jump question_time

label d2_p6:
    $ cormeum_door += 1
    mc_s "But such a thing would never HAPPEN... right?"
    cm "We wish to be honest with you silver=tongued, if a greater cosmic terror came after us..."
    cm "...then a few cores may be lost in the process."
    cm "But after the initial attack on one core, we'd be sure to protect and lock up any others."
    cm "So that this could never happen to them."
    jump question_time

label d2_p7:
    mc_s "What do you mean by WEAVED?"
    cm "It means that we're fused into one mind and soul."
    cm "Cor Meum isn't just Cor and Meum TOGETHER."
    cm "It's a whole new being... a whole new person."
    cm "And that person is a blended favour of Cor and Meum's consciousness."
    return
