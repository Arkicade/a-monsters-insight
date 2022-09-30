label splashscreen:
    play sound "audio/sfx/whisper.mp3"
    $ quick_menu = False
    $save_name = "-- the beginning --"
    show on_moon_particle onlayer inyourface with dissolve
    show on_moon_particle onlayer inyourface with dissolve
    if persistent.doneritual:
        mc_narr "..."
        mc_narr "I'm not going to look."
    elif persistent.seenopening:
        $ randomnum = renpy.random.randint(1,7)
        if randomnum == 1:
            show mater onlayer back with dissolve
            mo "For everything to stay the same, everything needs to change."
            mo "We can CONTROL this change."
            mo "...{w} and to do so..."
            hide mater onlayer back with dissolve
            mo "We're getting rid of you."
        elif randomnum == 2:
            show mater onlayer back with dissolve
            mo "Have you no shame?"
            mo "Look at yourself,{w} it's so... filthy."
            mo "People who see you will be so disgusted..."
            hide mater onlayer back with dissolve
            mo "... because it would bring them so much pain."
        elif randomnum == 3:
            show mater onlayer back with dissolve
            mo "..."
            hide mater onlayer back with dissolve
            mo "Why did you look?"
        elif randomnum == 4:
            show mater onlayer back with dissolve
            mo "When was the last time we've made something... acceptable?"
            mo "Something up to our \"standards\"?"
            mo "Something beautiful."
            hide mater onlayer back with dissolve
            mo "Because clearly it isn't you."
        elif randomnum == 5:
            show mater onlayer back with dissolve
            mo "Usually when there's a fault within our system, it can be amended easily."
            mo "..."
            mo "But a THING like yourself..."
            hide mater onlayer back with dissolve
            mo "No.{w} It can never be fixed."
            mo "Even if we had all the time in the world."
        elif randomnum == 6:
            show mater onlayer back with dissolve
            mo "Every day we grow weaker."
            mo "It becomes so painful, so many resources spent just to produce another siphon..."
            mo "And what a shame to know..."
            hide mater onlayer back with dissolve
            mo "... that you're the culmination of all our efforts."
        else:
            show mater onlayer back with dissolve
            mo "..."
            mo "Nothing."
            mo "You are nothing, are worth nothing and have nothing."
            hide mater onlayer back with dissolve
            mo "You shouldn't have looked."


        #hide on_moon_particle onlayer inyourface with dissolve

    else:
        show mater onlayer back with dissolve
        mo "What sort of misshapen madness have we made?"
        mo "Look at the wretched thing! Have you no shame?"
        mo "What damaged laugh it bellows.{w} What filthy tears it cries."
        mo "It smiles... with that disfigured silver tongue...{w} it smiles."
        mo "..."
        mo "Get out.{w} We know you’re here."
        mo "We speak of you...{w} you,{w} one with a silver tongue..."
        mo "...corroded skin, broken horn."
        mo "Listening to our thoughts I see?{w} With that weak power of INSIGHT?"
        mo "Haha..."
        mo "GET OUT!"
        mo "You have no place here you wretch!"
        mo "You WORTHLESS piece of BILE!"
        mo "Seize the one with the silver tongue and DISPOSE OF IT!!"
        mo "Us conspicio have no use for the weak and malformed."
        mo "Hm...{w} you hear us silver tongued?"
        mo "In your dying moments: learn this."
        mo "You are a plague on this planet, a disgrace to our kind."
        mo "You are NOTHING."
        hide mater onlayer back with dissolve
        #hide on_moon_particle onlayer inyourface with dissolve
        ##--------
        window hide
        $renpy.pause(1.5, hard=True)
        mc "I suppose the Conspicio Mater was right regarding something."
        mc "I may be born and am worth nothing."
        mc "But that's something I want to change."
        mc "No more will I be looked down upon as a wretch."
        mc "... as a failure."
        mc "I will THRIVE in this realm and claim it as my own!"
        mc "And I'll do so with the only thing I have..."
        mc "My words..."
        mc "... and the power of INSIGHT."
        $ persistent.seenopening = True

    stop sound fadeout 1.0
    play sound "audio/sfx/title.mp3"
    show mock_zoom
    $renpy.pause(4, hard=True)
    hide mock_zoom with dissolve
    return

label the_start:
    window hide
    $save_name = "-- setup --"
    $ quick_menu = False
    play music "audio/sfx/basement.mp3"
    #show screen setup_text("Setup phase")
    ending "Now you will choose a mode to play in."
    ending "Adjustments here are not permanent."
    ending "Changes can be made in the preferences menu later on."
    ending "If you want to access more accessibility features..."
    ending "(i.e. dyslexic font, self voicing...)"
    ending "Press the \"X\" key on your keyboard."
    jump mode_change

label mode_change:
    window hide
    ending "Select a template mode."

    call screen mode() with dissolve
    if mode == "assist":
        $emotion_hints = True
        $test_text = True
        $insight_timer = False
        $interlocutor_state = True
        show screen setup_text("Assist Mode")
    elif mode == "default":
        $emotion_hints = False
        $test_text = True
        $insight_timer = True
        $interlocutor_state = False
        show screen setup_text("Default Mode")
    elif mode == "challenge":
        $emotion_hints = False
        $test_text = False
        $insight_timer = True
        $interlocutor_state = False
        show screen setup_text("Challenge Mode")

    ending "You've selected the [mode] mode."
    if mode == "challenge":
        ending "In this mode, you'll get less points when you raise your stats."
    elif mode == "default":
        ending "In this mode, you won't be able to see interlocutor states."
        ending "But you'll get test labels."
    else:
        ending "In this mode, you'll get everything except the TIMER."
    menu:
        ending "Do you want to play in [mode] mode?"
        "Play in [mode] mode ()":
            ending "Excellent,{w} let's begin..."
        "I'd like to change my choice ()":
            jump mode_change

    #show mock_title
    stop music fadeout 2.0
    play sound "audio/sfx/title.mp3"

    ##----- TITLE CREDITS (or go to main menu and this whole sequence was a splash screen)
    show chapter1 with dissolve
    $renpy.pause(5, hard=True)
    hide chapter1 with dissolve

    show chasm onlayer back with dissolve:
        alpha 0.0
        linear 30.5 alpha 0.6

    show on_moon_particle onlayer inyourface with dissolve
    play sound "audio/sfx/cave.mp3"

    $save_name = "-- prologue --"

    "For a moment, you don’t remember where you are."
    "Or how you got here."
    "You feel lost... unsure of where you’re going and almost..."
    "Unsure of who you are."
    "...{w} You’d like to think that you’re past your weaknesses."
    "Your defects."
    "...{w}Your...{w} insecurities."
    "In a daze of confusion, sometimes being lost can make one’s soul..."
    "Feel as if it lost itself."
    "..."
    stop sound fadeout 2.0
    "Then you see it."
    play sound "audio/sfx/zoom.mp3"
    hide chasm onlayer back with dissolve
    hide on_moon_particle onlayer inyourface with dissolve
    show white with dissolve
    "A moment of clarity washes over you."
    "And you found yourself in..."
    show screen unlock_text("New keyword: CHASM")
    $ met_fer = True
    $ keywords.append("chasm")
    $ fer_keywords.append("chasm")
    "...THE CHASM."
    hide white with dissolve



    ##--- OBTAINED KEYWORD CHASM


    show river onlayer back with dissolve
    $ quick_menu = True
    play music "audio/sfx/river.mp3"
    play sound "audio/sfx/beast.mp3"
    mc "Across the endless Melduvian river,{w} a gargantuan beast can be seen engaging in a battle."
    show blue_p onlayer inyourface with dissolve
    show shargoth onlayer front with dissolve
    play nature "audio/sfx/shargoth.mp3"
    mc "His opponent appears to be a hooked-back Shargoth."
    mc "The more hooked the back and braces, the stronger they come as they say."
    hide shargoth onlayer front with dissolve
    mc "As for the beast, he had no discernible features other than it spewing a toxic pink substance when it roared."
    stop nature fadeout 2.0
    mc "Fairly standard large ears, a trunk face, lilac claws and a fur made of plasma."
    mc "I can guess it's a beast of the burning star."
    menu:
        mc "I know this..."
        "...from reading on the subject of monsters":
            $ knowledge += 1
        "...from observation and using logic":
            $ points += 1
    mc "..."
    show bloody_shargoth onlayer front with dissolve
    play nature "audio/sfx/shargoth.mp3"
    play sound "audio/sfx/flesh.mp3"
    mc "In a matter of moments, the winner was decided."
    mc "With a mission, the Shargoth carries the plasma on the second hooked back, and flies away."
    stop nature fadeout 2.0
    hide bloody_shargoth onlayer front with dissolve
    mc "Leaving the meat of the beast behind."
    mc "...{w} I wonder if it’s safe to eat?"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    hide blue_p onlayer inyourface with dissolve
    hide river onlayer back with dissolve

    show homeb onlayer farback
    show homef onlayer back

    #show keychee_hands onlayer front with dissolve
    #show keychee_h_eyes onlayer front with dissolve
    play ambient "audio/sfx/basement.mp3"
    play sound "audio/sfx/door.wav"
    mc "Just as I take my first step into the door,{w} I hear a shriek across the room..."
    show keychee up upsquint blinkup onlayer front with dissolve
    ###--- transition
    k "Silver-tongued, you have kept me waiting long enough!"
    mc_s "Greetings Keychee-"
    hide keychee up upsquint blinkup onlayer front
    show keychee hands handssquint blinkhands onlayer front with vpunch
    play sound "audio/sfx/break.mp3"
    k "I've been waiting for hooouuurrrsss"
    stop sound fadeout 2.0
    mc_s "How was your day-"
    k "Don’t use your semantics on me-"
    mc_s "Oh thank you Keychee! my day has been spectacular."
    mc_s "I had to withstand walking to-and-fro, watching ‘cat-fights’ and pick up after the leftovers."
    mc_s "Because that’s going to be our only source of nourishment."
    k "..."
    hide keychee hands handssquint blinkhands onlayer front
    show keychee down nosquint blinkdown down_smirk onlayer front
    play sound "audio/sfx/window.mp3"
    k "...I could help"
    k "If you let me out-"
    hide keychee down nosquint blinkdown down_smirk onlayer front
    show keychee down downsquint blinkdown nomouth onlayer front
    stop sound fadeout 2.0
    mc_s "Not a chance."
    play music "audio/music/Tutorial.wav" fadein 2.0
    mc "This is Keychee, a parasite that once attached itself to me."
    mc "Since I have INSIGHT, it was fairly easy to find it and dispose of it from my mind."
    mc "But then Keychee started panicking and begged for its life."
    mc "It promised it won’t reattach to me unless I find it food and let it live here."
    mc "I said I would agree to those terms."
    menu:
        mc "It believed me because I seemed to be..."
        "... charming and agreeable":
            $ charisma += 1
        "... trustworthy and true to my word":
            $ reputable += 1
        "... powerful and could be of use to them":
            $ supreme +=1
    hide keychee down downsquint blinkdown nomouth onlayer front
    show keychee down nosquint blinkdown nomouth onlayer front
    k "...what is that?"
    mc_s "Unsure, looked like a beast of the burning star."
    mc_s "But it would egest this... pink liquid."
    hide keychee down nosquint blinkdown nomouth onlayer front
    show keychee down nosquint blinkdown down_open onlayer front
    k "Perhaps they’re evolving as a species."
    mc_s "Perhaps."
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down nosquint blinkdown nomouth onlayer front
    mc "I grab my tools and start hammering on the flesh."
    mc "With no physical strength, I couldn’t carry all of the meat back to home."
    mc "Most of these \"meat sections\" were covered in plated armour, since the Shargoth skinned the plasma fur off the beast."
    hide keychee down nosquint blinkdown nomouth onlayer front
    show keychee down downsquint blinkdown down_smirk onlayer front
    k "Speaking of evolving...{w} let’s talk about your siphon career."
    mc_s "I have a good source of clients if that’s what you’re asking."
    hide keychee down downsquint blinkdown down_smirk onlayer front
    show keychee up nosquint blinkup nomouth onlayer front
    k "But are you content with where you are?"
    mc_s "I already have plans to go bigger."
    hide keychee up nosquint blinkup nomouth onlayer front
    show keychee hands handssquint blinkhands nomouth onlayer front
    k "... what do you mean?"
    mc_s "My sights are set on a first milestone: a Great Terror."
    hide keychee hands handssquint blinkhands nomouth onlayer front
    show keychee up nosquint blinkup nomouth onlayer front
    k "What?"
    mc_s "Don’t think I’m capable?"
    "I let out a soft laugh and stick out my silver tongue."
    mc_s "Well, today, I wasn’t just getting us food..."
    mc_s "I found a KEYWORD before I found the delectable beast we’re going to eat."
    mc_s "It was... the CHASM!"
    hide keychee up nosquint blinkup nomouth onlayer front
    show keychee hands handssquint blinkhands nomouth onlayer front
    ##--- KEYWORD CHASM
    k "Don’t tell me...{w} this is...{w} you’re-"
    k "You’re going to siphon off of Fernweh?"
    mc_s "Who other than the one of the Lost?"
    hide keychee hands handssquint blinkhands nomouth onlayer front with dissolve
    show food_prep onlayer inyourface with dissolve
    play nature "audio/sfx/sizzle.mp3"
    mc "Smiling, I start sizzling the meat on the hearth whilst beating it with my hammer."
    mc "The odour smells delicious, like rusted wood and Bromine."
    play sound "audio/sfx/ching.mp3"
    mc "I hear a light spark sound, meaning the fire has melted the last chink in the armour."
    stop sound fadeout 1.0
    stop nature fadeout 1.0
    hide food_prep onlayer inyourface with dissolve
    mc "After letting all the oozing metal collapse and clear off any remaining silicon left on the meat..."
    mc "I pull back the hammer and start weaving the meat and carving out the trunks."
    play sound "audio/sfx/plate.wav"
    show food_ready onlayer inyourface with dissolve
    mc "And now, the dish was finally ready."
    play sound "audio/sfx/pour.mp3"
    mc "Then, I squish Keychee’s jar and let the meat (and its juices) flow inside for it to consume."
    stop sound fadeout 1.0
    mc "It nibbles on some pieces before turning to face me."
    hide food_ready onlayer inyourface with dissolve
    show keychee down nosquint blinkdown down_open onlayer front with dissolve
    k "Alright, if you’re going to do this then you might as well get some help!"
    k "It’s always better to do some prep before you meet with any interlocutors."
    ##--- tutorial part actually begins

    menu:
        k "Do you want to do a little bit of a refresher?"
        "A reminder is always nice(choose if it's your first time playing)":
            jump k_tutorial
        "I think I'll be just fine(you've played this before)":
            jump k_skip

label k_skip:
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down nosquint blinkdown down_smirk onlayer front
    k "Feeling confident?{w} That's good..."
    k "Let's keep it that way."
    jump before_d1

label k_tutorial:
    $save_name = "-- tutorial --"
    stop music fadeout 2.0
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down nosquint blinkdown down_smirk onlayer front
    k "Alright, let's begin!"
    show keychee down nosquint blinkdown down_open onlayer front
    play music "audio/sfx/basement.mp3"
    k "The goal of the {b}Dialogue{/b} you have with each interlocutor is simple..."
    k "You want to convince the interlocutor, into choosing you as their...{w}siphon."
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee down downsquint blinkdown down_open onlayer front
    k "Whatever that means."
    hide keychee down downsquint blinkdown down_open onlayer front
    show keychee down nosquint blinkdown nomouth onlayer front
    mc_s "A siphon is a being that needs to feed off the mental energy of others to survive."
    mc "But it's not just about \"surviving\" for me.{w} It's about {b}thriving{/b} in this plane."
    mc_s "The more mental power I accumulate,{w} the greater my power of INSIGHT will become."
    mc_s "And the longer I will live."
    mc_s "Greater terrors,{w} like Fernweh of the Lost,{w} will grant me greater mental power."
    hide keychee down nosquint blinkdown nomouth onlayer front
    show keychee up blinkup onlayer front
    k "Why do you need your power of INSIGHT anyways?"
    mc_s "Funny you should ask Keychee..."
    mc_s "The power of INSIGHT is what allows me to get a glimpse of the minds of others."
    k "So you can see what's in their minds?{w} And I thought this was going to be difficult."
    hide keychee up blinkup onlayer front
    show keychee up blinkup up_closed onlayer front
    mc_s "Seeing their minds isn't so {i}simple{/i} as \"knowing their current thoughts\" Keychee."
    mc_s "It's like...{w} jumping into a pool of all their ideas, memories, experiences and feelings."
    mc_s "It's easy to get lost in their head if you don't know where to go{w} or what to look for."
    mc_s "The power of INSIGHT acts as the access point and,{w} if strong enough,{w} can be my guide when inside the mind."
    mc_s "Let's...{w} start with you as an example. Hm?"
    hide keychee up blinkup up_closed onlayer front
    show keychee hands handssquint blinkhands onlayer front with vpunch
    k "Wait WHAT?{w} I did not ASK FOR THIS SILVER-TONGUE-"
    mc "I laugh."
    stop music
    hide keychee hands handssquint blinkhands onlayer front
    mc "Too late."
    play sound "audio/sfx/hand.wav"
    show banner_back onlayer back with dissolve
    show banner_front onlayer front with dissolve
    $renpy.pause(0.2, hard=True)
    show hand_zoom onlayer inyourface
    $renpy.pause(1.0, hard=True)
    play music "audio/music/Insight.wav"
    #### section where you dive into the mind
    hide hand_zoom onlayer inyourface
    hide banner_front onlayer front
    hide banner_back onlayer back
    jump k_tutorial_insight

label k_tutorial_insight:
    window hide
    $ quick_menu = False

    call screen keychee_mind with fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    if _return == "eye" or _return == "EYE" or _return == "Eye":
        window show
        "Congratulations! You found the answer!"
        "This is what you'll need to do for most dialogues,{w} solve puzzles and input words."
        "Sometimes, you'll need to input more than one word in order to win."

    elif _return == "backspace":
        window show
        "You decided to use your emergency BACKSPACE to exit Keychee's mind."

    else:
        "Unfortunately, that was the wrong answer."
        "The correct input was \"EYE\"."

    jump k_tutorial_2


label k_tutorial_2:
    stop music fadeout 2.0
    hide keychee hands handssquint blinkhands onlayer front
    show keychee down downsquint blinkdown onlayer front
    k "...{w} I...{w} did you just enter my mind now?"
    mc_s "Let me guess,{w} your head is a bit light and dizzy.{w} You feel as if you \"blanked out\" for a second."
    hide keychee down downsquint blinkdown onlayer front
    show keychee down nosquint blinkdown down_open onlayer front
    k "Correct."
    k "Wait, so that means you intend to use the power of INSIGHT {b}during{/b} the Dialogue?"
    mc_s "When else is a better time?"
    k "You didn't need to do this for your clients in the past."
    mc_s "Well my \"clients\" are easy to convince.{w} Now we're going up a proper, worshiped terror."
    mc_s "All tricks and tactics should be laid on the table."
    k "Hmm... yes I suppose so."
    hide keychee down nosquint blinkdown down_open onlayer front
    show keychee hands blinkhands nomouth onlayer front
    mc "Keychee fidgets and moves around in its jar."
    k "But your power of INSIGHT alone isn't enough to convince someone."
    mc_s "You don't say?{w} I thought I could just go up to someone and say-"
    mc_s "{i}Greetings fellow associate.{w} Could you be my source of power from which I will leech on indefinitely?{/i}"
    mc_s "But no.{w} You need to spin it in a way that can be mutually beneficial."
    k "That is true I suppose."
    hide keychee hands blinkhands nomouth onlayer front
    show keychee hands blinkhands hands_smile onlayer front
    play music "audio/music/dirt_demo.mp3" fadein 2.0
    k "But no,{w} what you need are the 3 Ps to assist you!"
    mc_s "The 3 Ps?"
    window hide
    $ quick_menu = False
    show newspaper_bg onlayer inyourface with dissolve
    k_narr "There are 3 things you put into a conversation."
    k_narr "Or as I like to call them...{w} {b}the three Ps{/b}."
    show tut1 onlayer inyourface with dissolve
    k_narr "{b}P{/b}resence. {w}{b}P{/b}rescience.{w} and...{b}P{/b}erception!"
    k_narr "Each one is valuable in their own way and can be a key to your success in winning the Dialogue"
    k_narr "It's also known as \"winning their favour\"."
    hide tut1 onlayer inyourface with dissolve
    show tut2 onlayer inyourface with dissolve
    k_narr "Your {b}P{/b}resence is how you control your demeanour in the conversation."
    k_narr "It's your ability to manipulate how you \"come across\" or present yourself."
    k_narr "There are 3 {b}traits{/b} that {b}P{/b}resence encompasses."
    show tut3 onlayer inyourface with dissolve
    hide tut2 onlayer inyourface
    k_narr "1) Charisma."
    k_narr "How {i}\"agreeable\"{/i}, {i}\"charming\"{/i} or {i}\"likeable\"{/i} you are."
    show tut4 onlayer inyourface with dissolve
    hide tut3 onlayer inyourface
    k_narr "2) Reputable."
    k_narr "How {i}'trustworthy'{/i}, {i}\"honest\"{/i}, and {i}\"respectable\"{/i} you are."
    show tut5 onlayer inyourface with dissolve
    hide tut4 onlayer inyourface
    k_narr "3) Supreme."
    k_narr "How {i}'powerful'{/i} and {i}\"strong\"{/i} you are."
    k_narr "This controls if you're the {i}\"dominant speaker\"{/i}."
    k_narr "Or the one who leads the conversation."
    k_narr "Note the words {b}\"appear to be\"{/b} and how things are in {i}\"airquotes\".{/i}"
    k_narr "Because, frankly speaking,{w} you are neither likeable, trustworthy nor powerful."
    mc "I grab Keychee's jar and tighten my grip."
    mc_narr "I'm sorry?{w} Did you say something?"
    k_narr "Hahahaha!{w} Not at all!"
    mc "I lay down the jar."
    k_narr "Ahem.{w} What I meant to say was this:"
    k_narr "It doesn't matter {b}who{/b} you are.{w} It's {b}who{/b} you pretend to be."
    k_narr "It's the ability to hide your true nature."
    k_narr "And present yourself as someone more convincing."
    hide tut5 onlayer inyourface with dissolve
    show tut6 onlayer inyourface with dissolve
    k_narr "Next on the list is {b}P{/b}rescience."
    k_narr "It's your ability to recall facts and use your reason."
    k_narr "There are 2 {b}traits{/b} that compose your {b}P{/b}rescience."
    show tut7 onlayer inyourface with dissolve
    hide tut6 onlayer inyourface
    k_narr "1) Knowledge."
    k_narr "It's how much you KNOW things or how \"cultured\" you are."
    k_narr "If you go scouting or... \"digging up some dirt\" on an interlocutor."
    k_narr "You gain more knowledge."
    show tut8 onlayer inyourface with dissolve
    hide tut7 onlayer inyourface
    k_narr "2) Intellect."
    k_narr "Your ability to make sound judgements and use logic."
    k_narr "These can be used if you were to..."
    mc_narr "Dig up some old dirt on them?"
    k_narr "W-Well!{w} You can't introduce it straight away."
    k_narr "{i}\"Hey I'm here to blackmail you\"{/i} {w}isn't all that convincing."
    mc_narr "Why not?{w} Wouldn't they feel threatened?"
    k_narr "They can beat you to a pulp.{w} With your malformed body and lack of strength..."
    k_narr "It would be too easy."
    mc "As much as I detest that idea,{w} Keychee is right."
    mc "I'm not one to use my brute force as a weapon."
    mc "That's why I take it to a playing field where I stand a better chance."
    mc "One involving less punches and more words."
    hide tut8 onlayer inyourface with dissolve
    show tut9 onlayer inyourface with dissolve
    k_narr "Finally there's your {b}P{/b}erception which has one, singular {b}trait{/b}."
    mc_narr "...{w} you mean perception?"
    k_narr "That's it!"
    k_narr "{b}P{/b}erception has the trait of perception!"
    mc_narr "This is a ridiculous naming system."
    k_narr "That's how I'm going to fit in the 3 Ps!"
    k_narr "Anyways,{w} your {b}P{/b}erception/perception is a crucial ability."
    k_narr "This determines whether you can pick up on important words or body language."
    k_narr "Important words translate into {b}POINTERS{/b}."
    k_narr "And body language translates into {b}CUES{/b}."
    mc_narr "You don't say?"
    hide tut9 onlayer inyourface with dissolve
    hide newspaper_bg onlayer inyourface with dissolve
    hide keychee hands blinkhands hands_smile onlayer front
    show keychee down blinkdown down_open onlayer front
    $ quick_menu = True
    k "Indulge me for a second.{w} First I will explain POINTERS."
    k "For the sake of argument:{w} let it be that I said the following sentence."
    k "{i}After walking past the shop, I arrived at home.{/i}"
    k "Fairly innocuous statement right?"
    k "Let's say you had greater {b}P{/b}erception.{w} Maybe you'd be able to notice a word..."
    jump pointer_example

label pointer_example:
    k "{i}After walking past {a=jump:shop_example}THE SHOP{/a}, I arrived at home.{/i}"
    "Click on the word that's {b}bolded{/b} (THE SHOP). The word (THE SHOP) is the POINTER."
    jump pointer_example

label ex_2:
    mc_s "At what time did you arrive to your house?"
    k "Roughly five moons after the blood sun."
    return

label ex_1:
    mc_s "And where is \"HOME\" for you?"
    k "Near the Melduvian river, across the banks of Bahoog."
    return

label shop_example:
    hide keychee down blinkdown down_open onlayer front
    show keychee down blinkdown nomouth onlayer front
    mc_s "What shop did you walk past?"
    hide keychee down blinkdown nomouth onlayer front
    show keychee hands blinkhands hands_smile onlayer front
    k "The Uldinoor store of supplies and syringes."
    hide keychee hands blinkhands hands_smile onlayer front
    show keychee hands blinkhands nomouth onlayer front
    k "What you just clicked on was a POINTER."
    k "Essentially,{w} you interrupted me to press/question me about the POINTER word."
    k "In this case, it was \"THE SHOP\"."
    k "So you asked me what \"shop\" I was walking past."
    "You may return to the original text{w} (aka what Keychee would've said if you didn't interrupt)."
    "But sometimes, an interruption can lead to a separate train of thought."
    k "Sometimes there may be multiple pointers in a sentence, and you may be forced to pick one."
    k "So you may have to decide what should be questioned or not."
    hide keychee hands blinkhands nomouth onlayer front
    show keychee up blinkup onlayer front
    k "{i}After walking past the shop, I {a=call:ex_2}ARRIVED{/a} at {a=call:ex_1}HOME{/a}.{/i}"
    hide keychee up blinkup onlayer front
    show keychee up blinkup up_smile onlayer front
    k "Sometimes, the better option may be to let the interlocutor keep talking."
    k "If you keep pressing them about words or keep interrupting them,{w} they may get annoyed."
    hide keychee up blinkup up_smile onlayer front
    show keychee up blinkup nomouth onlayer front
    k "This will {b}close{/b} them up,{w} and they'll reveal less information to you."
    "You can see the state of the interlocutor by enabling \"Interlocutor State\" in the menu."
    "This \"state\" will show a bar that's half full half empty."
    "If the bar goes empty (or if the interlocutor is CLOSED){w} it's game over."
    "You've pestered them too much and they'll stop the dialogue."
    "You can unlock KEYWORDS by \"opening\" up the interlocutor."
    "This is done using your Presence traits."
    hide keychee up blinkup nomouth onlayer front
    show keychee up blinkup up_smile onlayer front
    k "So that's POINTERS done!"
    k "Next are cues..."
    hide keychee up blinkup up_smile onlayer front
    show keychee hands blinkhands nomouth onlayer front
    k "CUES are hints of body language."
    k "Words alone don't tell the whole story,{w} mannerisms of a person can change everything."
    k "Let it be that I said..."
    show screen cue_text("Keychee bears extended claws.\n   Reserved body language") with dissolve
    k "{i}I saw Uralda yesterday.{/i}"
    "See the eye mark next to Keychee?{w} Hover over it and text will appear."
    "You see that the body language Keychee is giving is one that is {i}reserved.{/i}"
    "Meaning that it is trying to hide something."
    "It could be that Keychee is flat out lying,{w} or Keychee is hiding some information regarding the encounter."
    hide screen cue_text with dissolve
    k "Let's say I used a different body language instead."
    hide keychee hands blinkhands nomouth onlayer front
    show keychee hands handssquint blinkhands onlayer front
    show screen cue_text("Keychee's skin is shining.\n   Repressed anger.") with dissolve
    k "{i}I saw Uralda yesterday.{/i}"
    "Hover over the new eye mark again, and different text will appear."
    "Now, Keychee's body language is {i}repressed anger{/i}."
    "You can deduce that there is a strain/tension in the relationship between Keychee and Uralda."
    "Clearly,{w} Keychee did not want to see them that day."
    hide screen cue_text with dissolve
    hide keychee hands handssquint blinkhands onlayer front
    show keychee down blinkdown down_open onlayer front
    k "I think you get the rough idea on how CUES work."
    k "So to summarise."
    $ quick_menu = False
    show newspaper_bg onlayer inyourface with dissolve
    show tut10 onlayer inyourface with dissolve
    k_narr "There's {b}P{/b}resence, {w}{b}P{/b}rescience,{w} and {b}P{/b}erception."
    k_narr "{b}P{/b}resence has the Charisma, Reputable and Supreme {b}traits{/b}."
    k_narr "{b}P{/b}rescience has the Knowledge and Intellect {b}traits{/b}."
    k_narr "And {b}P{/b}erception has the perception {b}trait{/b}."
    k_narr "Perception can be used to notice POINTERS (important words) and CUES (body language)."
    mc "For every single interlocutor,{w} I know there are multiple strategies to pursue."
    mc "They use a unique combination of Keychee's 3 Ps."
    mc "Sometimes you can make yourself appear as a sycophant to lower their guard{w} (negative Supreme)(positive Charisma)."
    mc "Perhaps you can find some blackmail and bribe them{w} (positive Knowledge)."
    mc "Occasionally, I'll refute their ideas and convince them why they need me as their siphon{w} (positive Intellect)(positive Reputable)."
    mc "But most of the time,{w} I just go with what feels right and adjust myself to the situation."
    menu:
        k_narr "So... are we clear?"
        "I think we're good to go (finished with the explanation)":
            k_narr "Excellent!"
            hide tut10 onlayer inyourface with dissolve
            hide newspaper_bg onlayer inyourface with dissolve
            jump before_d1
        "Can I hear that one more time? (repeat the explanation)":
            k_narr "Certainly."
            jump summary

label summary:
    k_narr "You will enter the Dialogue (conversation){w} with a single interlocutor (the person you're talking to)."
    k_narr "You want to convince the interlocutor, into choosing you as their siphon."
    k_narr "Which means you can gain their mental power{w} so that you can grow stronger and continue surviving."
    k_narr "But you need to be able to use your words to convince them that this is a good idea."
    k_narr "There's your power of INSIGHT, which lets you access their minds."
    k_narr "So you can get information or understand who they are better.{w} And convince them more effectively."
    k_narr "But there's also the 3 Ps I've devised to help with this too."
    k_narr "There's {b}P{/b}resence, {w}{b}P{/b}rescience,{w} and {b}P{/b}erception."
    k_narr "{b}P{/b}resence has the Charisma, Reputable and Supreme {b}traits{/b}."
    k_narr "{b}P{/b}rescience has the Knowledge and Intellect {b}traits{/b}."
    k_narr "And {b}P{/b}erception has the perception {b}trait{/b}."
    k_narr "Perception can be used to notice POINTERS (important words) and CUES (body language)."
    k_narr "A combination of Ps (and using your INSIGHT) can be the key into \"winning\" the Dialogue."
    k_narr "\"Winning\" the Dialogue means convincing your interlocutor that they should let you be their siphon."
    k_narr "This can also be known as \"winning their favour\"."
    menu:
        k_narr "Did you get all of that?"
        "Yes, I think I understand now (move on)":
            k "Good."
            hide tut10 onlayer inyourface with dissolve
            hide newspaper_bg onlayer inyourface with dissolve
            jump before_d1
        "Sorry I don't think so. (repeat the exposition)":
            mc_s "One more time?"
            k "...{w} fine."
            jump summary

    return


label before_d1:
    stop music fadeout 2.0
    $ quick_menu = True
    hide keychee down nosquint blinkdown down_smirk onlayer front
    show keychee up nosquint blinkup onlayer front
    $save_name = "-- prep for dialogue 1 --"
    k "So...{w} when are you meeting Fernweh?"
    hide keychee up nosquint blinkup onlayer front
    show keychee up nosquint blinkup up_closed onlayer front
    play music "audio/sfx/basement.mp3"
    mc_s "When I hear their call."
    hide keychee up nosquint blinkup up_closed onlayer front
    show keychee up nosquint blinkup up_smile onlayer front
    k "...{w} do they have some telecommunication network?"
    mc_s "If only,{w} but no."
    hide keychee up nosquint blinkup up_smile onlayer front
    show keychee up nosquint blinkup up_closed onlayer front
    mc_s "Their home is the CHASM and {i}usually{/i} nobody can get in."
    mc_s "But since I've been there before, I think I can go there again."
    hide keychee up nosquint blinkup up_closed onlayer front with dissolve
    mc "I tried getting in the CHASM this moonrise and it worked."
    mc "Although I'll have to be careful not to lose myself in it."
    mc "Should be easy enough,{w} I'm used to navigating peoples' minds anyways."
    stop music fadeout 2.0
    mc "...{w} I wonder what Fernweh's mind looks like."
    show screen setup_text("Unlocked Journal and Papers")
    play sound "audio/sfx/collect.wav"
    $ extra_menu = True
    "You grab out your journal and some papers you have lying around."
    play music "audio/music/Menu.wav" fadein 2.0
    "Your {b}journal{/b} keeps track of all of the KEYWORDS you have."
    "And your {b}papers{/b} have your STATS written on them {w}(e.g. presence, prescience and perception)."
    "During the dialogues, you'll gain temporary presence stats which indicate how you present yourself in the conversation."
    "Once the conversation is over, all your stats earned DURING the conversation will be reset to \"normal\"."
    "After all, presence indicates how your INTERLOCUTOR perceives you.{w} Once you're done seeing them, these stats play no role."
    "However, you can boost your \"normal\" presence stats before the conversation."
    "Which is what you're going to do now."
    "You have [points] points to spend across your presence, prescience and perception."
    menu:
        "Do you want to discuss strategy?"
        "Yes, I want strategy tips":
            jump stra_tip
        "No, I want to go straight in!":
            jump skip_tip

label stra_tip:
    show screen setup_text("Strategy tips")
    ending "Every stat is important in their own way and has a use."
    ending "But it depends on the interlocutor..."
    ending "And the strategy you choose"
    ending "If you're unsure of what to do..."
    ending "It's best to {u}equally distribute the stats{/u}."
    ending "Usually you want to \"pair up\" two/three traits together."
    ending "And it's usually 2 presence stats and 1 prescience stat..."
    ending "But this can vary."
    ending "Perception is {b}really{/b} useful for getting {b}important{/b} keywords."
    ending "But if your other stats aren't good, then perception is useless."
    ending "In terms of focus, you could do 2 presence and 1 perception."
    ending "2 prescience and 1 perception."
    ending "Or ignore perception and do a bit of presence and prescience."
    ending "Investing all of your points in one single stat is a mistake."
    ending "Any strategies involving blackmail or uncovering \"dirty\" secrets will usually need..."
    ending "Supreme, Knowledge{w} (and ocassionally intellect and negative reputable)."
    jump skip_tip

label skip_tip:
    "Keep in mind once you ask about a KEYWORD and you go inside their mind..."
    "Then you're locked down that \"strategy\" or route."
    "With this in mind, distirbute your [points] points!"
    show stut_1 onlayer credit with dissolve
    $renpy.pause(2, hard=True)
    ending "Click on the \"+\" (PLUS) sign to add 1 to a stat."
    hide stut_1 onlayer credit with dissolve
    show stut_2 onlayer credit with dissolve
    $renpy.pause(4, hard=True)
    ending "Click on the WORD of the stat to reset that stat to zero."
    ending "The stat points will be transferred to your overall points."
    ending "... which can be spent elsewhere."
    hide stut_2 onlayer credit with dissolve
    $ quick_menu = False
    $ extra_menu = False
    window hide
    show newspaper_bg onlayer inyourface with dissolve
    call screen stat_screen with dissolve
    hide newspaper_bg onlayer inyourface with dissolve
    $ quick_menu = True
    $ extra_menu = True
    "You read the papers,{w} there are headlines of Jack Rabbit and the missing minds of Lusinscape."
    "Good, now you'll have a choice to make."
    "Either you can go digging for some \"information\" regarding Fernweh... or you can gain more points to boost your stats."
    menu:
        "On this evening, you decide to..."
        "Read and raise stats (gain +3 points to use and re-assign)":
            if mode == "challenge":
                $ points += 2
            else:
                $ points += 3
            mc "I decided to take a famous void cult zine from the early days of Yarshaggoth's reckoning."
            mc "As much as I hate to admit it, they were one of my earliest influences for the work I do now..."
            "You gained 2 points to spend."
            $ quick_menu = False
            $ extra_menu = False
            window hide
            show newspaper_bg onlayer inyourface with dissolve
            call screen stat_screen with dissolve
            hide newspaper_bg onlayer inyourface with dissolve
            $ quick_menu = True
            $ extra_menu = True
            "You practiced your ability to hide your true nature."
            "More headlines go on about the OUTERWORLD's upcoming black hole trinity."
            hide homef onlayer back
            hide homeb onlayer farback with fade
            jump start_d1
        "Scout for information (collect keywords and gain +1 knowledge)":
            $ knowledge += 1
            jump info_d1

    return

label info_d1:
    mc "As prep for the Dialogue,{w} I usually search for information regarding the interlocutor."
    mc "Who in this case will be Fernweh."
    mc "It's always better to stay one step ahead of your opponent."
    mc "And that means knowing {i}more{/i} about them than they know about {b}you.{/b}"
    mc "..."
    mc "There isn't much time until the Dialogue starts."
    mc "So I should choose carefully where I go get my information."
    mc "There's Globin near the Melduvian river who's obsessed with studying great terrors."
    mc "Or there is a G'narg Keychee knows that runs a bar{w} and I'm guessing he hears a bunch of things from different folk."
    mc "Hmmm..."
    window hide
    menu:
        "Go to the Melduvian river with Globin (she's an academic studying terrors)":
            mc "Better to trust the {i}experts{/i} with this one."
            ### transition
            stop ambient fadeout 2.0
            hide homef onlayer back
            hide homeb onlayer farback with fade
            show river onlayer back with dissolve
            show blue_p onlayer inyourface with dissolve
            mc "A trek later,{w} I'm at the Melduvian river."
            mc "Normally it's a dangerous place where predators tear apart their prey."
            mc "But because of the time, there's not much of a need to be cautious...{w} I think."
            mc "I meet up with Globin,{w} we've done an exchange like this before."
            mc "But not enough times where she's supposed to expect me."
            mc "Under the guise of {i}wanting to study great terrors{/i},{w} she reveals to me a few things of Fernweh."
            ### KEYWORD: LOST
            show screen unlock_text("New keyword: LOST")
            $ keywords.append("lost")
            $ fer_keywords.append("lost")
            mc "I learnt that the CHASM is for those who have \"lost their way\"."
            mc "The Chasm itself is home to something{w} (Hobin-globin doesn't know){w} that reduces you to nothing."
            ### KEYWORD: SOUL
            show screen unlock_text("New keyword: SOUL")
            $ keywords.append("soul")
            $ fer_keywords.append("soul")
            mc "Once your SOUL has been extracted by the CHASM,{w} Fernweh uses this to nurture the CHASM and let it grow."
            mc "Any remaining debris looks like fractured, glass-like shapes floating astray."
            ##### KEYWORDS added to Journal
            ##### New information added to Journal
            hide blue_p onlayer inyourface with dissolve
            mc_s "Good talk!"
            #### transition
            hide river onlayer back with dissolve

        "Go to the G'narg at the bar downtown (he's a friend keychee knows)":
            mc_s "Hey Keychee."
            show keychee down blinkdown down_open onlayer front with dissolve
            k "What is it?"
            mc_s "You said that you know a guy who runs a bar."
            k "The G'narg?{w} Yeah."
            k "He runs a bar called Zilker near Moowrongo.{w} Be quick because it closes right about now."
            hide keychee down blinkdown down_open onlayer front with dissolve
            mc_s "Right, right.{w} On it!"
            hide homef onlayer back
            hide homeb onlayer farback with fade
            ### transition
            show silkerf onlayer back with fade
            show silker onlayer farback with dissolve
            stop ambient fadeout 2.0
            mc "It took a while to get to Zilker.{w} Moowrongo isn't a simple walk away."
            mc "Just as the G'narg was closing up,{w} I asked if I could borrow some of his time."
            mc "Annoyed,{w} he let me in for {i}one{/i} drink."
            mc "I only had the time to ask one question."
            mc "The G'narg didn't have much to say on Fernweh...{w} but one of his clients did."
            ### KEYWORD: MAP
            show screen unlock_text("New keyword: MAP")
            $ keywords.append("map")
            $ fer_keywords.append("map")
            $ event_track.append("compass")
            mc "Apparently there's a secret MAP that allows one to navigate the CHASM."
            mc "The client said something about \"finding\" another device and that the MAP isn't the only way to navigate it."
            mc "Something vague like that.{w} But it's interesting how this was deemed to be important information."
            mc "I thanked the G'narg for his time and the good drink,{w} before leaving the Zilker bar."
            #### transition
            hide silkerf onlayer back with dissolve
            hide silker onlayer farback with fade

    jump start_d1

########################################################################################
#############################################################################################
########################################################################################################
################ A C T U A L    D I A L O G U E    S T A R T S     H E R E #############################
########################################################################################
#############################################################################################
########################################################################################################

label start_d1:
    stop ambient fadeout 2.0
    $save_name = "-- start of dialogue 1 --"
    stop music fadeout 2.0
    ### transition home
    "Your preparation time for the Dialogue is up."
    "Now,{w} the silver-tongued will attempt to {b}win{/b} the favour of the interlocutor:{w} Fernweh of the Lost."
    #### transition
    #### BIG TITLE TRANSITION SCREEN:
    #### Fernweh of the Lost
    window hide
    play sound "audio/sfx/quake.mp3"
    play nature "audio/sfx/destroy.wav"
    show falling_test with dissolve
    $renpy.pause(1.5, hard=True)
    mc "Almost instantaneously,{w} I feel my body collapse into the floor..."
    mc "And soon after, I was dragged to the centre or the core of this plane."
    mc "In that moment, I wasn't falling down but instead, I was flying down."
    mc "As the seconds pass, my home seemed more of a memory...{w} and then a stranger."
    mc "Everything was spinning, in motion, yet I felt strangely unphased."
    mc "I knew what to expect from great cosmic terrors."
    mc "The fall felt never-ending, the impact was going to be severe..."
    hide falling_test
    stop sound fadeout 2.0
    mc "But I never really hit the ground."
    mc "..."
    stop nature fadeout 2.0
    "A few minutes pass as you try to recuperate from the fall."
    show chasm onlayer farback with fade
    show fog_test2 onlayer back with dissolve
    show fog_test onlayer inyourface with dissolve
    play ambient "audio/sfx/cave.mp3"
    mc "It takes me a few seconds before I could fully comprehend what had just happened."
    mc "The humidity is almost suffocating,{w} and if you look long enough, the glass shards and walls look back at you."
    mc "The air, frigid and moist, should give a clear sensation."
    mc "Yet my body feels weak and light,{w} almost as if I don't exist."
    #### show Fernweh
    show fernweh normal onlayer front with dissolve
    play music "audio/music/Fernweh.wav" fadein 3.0
    mc "I see Fernweh form itself around me.{w} It wasn't like a figure coming closer from the distance."
    mc "It's more as if they were already here,{w} waiting for me,{w} and chose to reveal themself now."
    #hide fernweh normal onlayer front with dissolve
    show fernweh_f_eyes onlayer inyourface with dissolve
    mc "Their figure staggers above mine, yet their ethereal form and lifeless eyeballs make them seem less threatening."
    f "Greetings, silver-tongued.{w} I was told that you have come into my Chasm."
    mc_s "My greetings..."
    #### THE FIRST IMPRESSION
    ### this will be unseen if interlocutor state is disabled
    show screen fer_door() with dissolve
    hide fernweh_f_eyes onlayer inyourface with dissolve
    "At this phase of the Dialogue,{w} this is where you make your first impression."
    "And where you dictate the tone of the conversation."
    window hide
    menu:
        "Who told you I was coming? (+ supreme)":
            $ temp_supreme += 1
            #strategy no.3: supreme
            f "I suppose...hmm..."
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "It must've been myself."
            mc_s "Yourself?"
            f "It couldn't have been you or anyone else?"
            mc_s "Was that a question?"
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            f "Do you want an answer?"
            mc "They just keep giving me questions,{w} almost as if they're retaliating."
            mc "I could push forward or take a step back..."
        "Are you Fernweh? (- supreme  + charisma)":
            #strategy no.1+4: confused
            $ temp_supreme -= 1
            $ temp_charisma += 1
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "Are you the silver-tongued?"
            mc_s "..."
            mc "They give a warm chuckle."
            hide fernweh turn onlayer front
            show fernweh front onlayer front
            f "You can never be sure of anything in this world little one."
            f "Are you supposed to go into the walls with the others?"
            mc_s "N-No!{w} That I'm certain of."
            mc "I'm not going anywhere near those creepy looking walls."
            mc_s "I think I'll be fine...{w} haha..."
            hide fernweh front onlayer front
            show fernweh normal onlayer front
            mc "They begin to stroke the top of my horn."
            f "There there...{w} there there.... therethere"
            mc "Are they patronizing me?"
            mc "Maybe they look down upon me or cherish me?{w} I could exploit this..."
            mc "Or re-assert the tone I want."

        "So...you say this Chasm is \"yours\"? (no effect)":
            #strategy no.4: lead to blackmail
            f "Well it is not mine as much as it is the SOULs that live here..."
            ### KEYWORD: SOUL
            if "soul" not in keywords:
                show screen unlock_text("New keyword: SOUL")
                $ keywords.append("soul")
                $ fer_keywords.append("soul")
            mc_s "There are SOULs that live here?"
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "Why, there once were SOULs that could call this home."
            f "But they disappear within an instant."
            show screen cue_text("An eerie, reverberating voice.\n   Threatening body language.") with dissolve
            f "I doubt that they're even here at all."
            hide screen cue_text with dissolve
            hide fernweh turn onlayer front
            show fernweh normal smile onlayer front with dissolve
            mc "Its mouth gapes open into a smile,{w} both sinister and inviting."
            hide fernweh normal smile onlayer front with dissolve
            show fernweh normal noblink nomouth onlayer front with dissolve
            mc "Something is definitely odd..."

        "How did you know I was the silver-tongued? (+ reputable)":
            #strategy no.2: reputable
            $ temp_reputable += 1
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "Good to see you asking questions!{w} But there's no point to it all..."
            mc_s "Well it would be to my benefit."
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            f "Why is that?"
            mc_s "Um..."
            mc "I don't have a comeback...yet."
            mc "Best I drop the subject and move on."

    menu:
        f "Anyways,{w} I wanted to ask what brought you here?"
        "Do you know what a siphon is? (+ knowledge)":
            # strategy no4: automatic blackmail
            $ temp_knowledge += 1
            hide fernweh normal onlayer front
            show fernweh front onlayer front
            f "No, please explain..."
            mc_s "It's a being that..."
            mc "Is there any way I can put this nicely?"
            mc_s "Needs the {i}help{/i} of others to survive."
            hide fernweh front onlayer front
            show fernweh turn onlayer front
            f "Haha...{w} is that another way to say 'parasite'?"
            mc "Keychee would be fuming if it was here."
            mc_s "No,{w} the siphon is not attached to the host."
            mc_s "It just needs, (a deal){w} yes a deal to progress."
            hide fernweh turn onlayer front
            show fernweh front onlayer front
            f "What...deal do you speak of?"
            mc_s "One that is mutually beneficial for both parties."
            f "Hmmm..."
            hide fernweh front onlayer front with dissolve
            mc "They turn their back against me and start to float."
            show fernweh turn onlayer front with dissolve
            f "What's the point?"
            show fernweh_s_eyes onlayer inyourface with dissolve
            mc_s "Well, you could gain something out of it."
            f "I'm not talking about stupid siphons.{w} I mean the point of it all."
            mc_s "..."
            mc "I shouldn't try to say anything now.{w} The best I can do is let them talk."
            hide fernweh_s_eyes onlayer inyourface with dissolve
        "I was hoping you could tell me that... (- supreme)":
            # strategy no.1+4: confused
            $ temp_supreme -= 1
            hide fernweh normal onlayer front
            show fernweh front onlayer front
            f "And why should I be able to know?"
            mc_s "I..."
            mc "Wasn't so sure where I was going with this one."
            mc "Thought I could buy me some more time before I have to 'lay it down'."
            ### KEYWORD: LOST
            if (supreme + temp_supreme) < 0:
                show screen testing_text("Test: Negative Supreme -> Success", True)
                f "Oh you poor thing..."
                if "lost" not in keywords:
                    show screen unlock_text("New keyword: LOST")
                    $ keywords.append("lost")
                    $ fer_keywords.append("lost")
                hide fernweh front onlayer front
                show fernweh tilt onlayer front
                f "...you may be already LOST."
                f "But perhaps you're a lot like me in this way."
                mc "LOST? What's this?"
                mc_s "Are you LOST?"
            else:
                show screen testing_text("Test: Negative Supreme -> Failed", False)
                f "It seems like you can handle this on your own."
                hide fernweh front onlayer front
                show fernweh tilt onlayer front
                f "I don't have to tell you everything..."
            f "...haha, oh you are just-"
            hide fernweh tilt onlayer front
            show fernweh turn onlayer front
            f "..."
            f "I was going to say pathetic, but you're helplessness is endearing."
            mc_s "My what?"
            mc "Helplessness?{w} Wait this isn't so bad."
            mc "I can turn this around,{w} or I can keep using this."
        "I thought that I could ask the questions first. (+ supreme)":
            # strategy no.3: supreme
            $ temp_supreme += 1
            $ fernweh_door -= 1
            hide fernweh normal onlayer front
            show fernweh front onlayer front
            show oneblink onlayer inyourface with dissolve
            f "I'm sorry?{w} Do you know who I am?"
            mc_s "Do you know who you even are?"
            f "I-"
            hide oneblink onlayer inyourface with dissolve
            mc "They pause."
            mc_s "I'd rather hear it from you yourself rather than me making assumptions."
            mc_s "This needless back and forth is superfluous at best.{w} And time wasting at worst."
            mc "Managed to sneak in a question there.{w} Is this good?"
            hide fernweh front onlayer front
            show fernweh tilt onlayer front
            f "You shouldn't make a statement like that."
            mc_s "I-"
            hide fernweh tilt
            show fernweh turn onlayer front
            f "Why are you saying something like that?{w} I wouldn't make you say something like that."
            mc "Since when did they made me?"
            mc "Fernweh is delusional about something but I can't figure out what."
        "Well does that even matter? (- reputable)":
            # strategy no.2 reputable
            $ temp_reputable -= 1
            hide fernweh normal onlayer front
            show fernweh front onlayer front
            f "It doesn't?"
            mc_s "Well no,{w} what matters is that..."
            window hide
            menu:
                "I'm here talking to you (+ supreme)":
                    f "Hmm... I see."
                    $ temp_supreme += 1
                    # strategy no.3 dominant
                "You're talking to me (+ reputable)":
                    $ temp_reputable += 1
                    f "Hmm... I see."
                    #strategy no.2 reputable

            if (charisma + temp_charisma) > 0:
                show screen testing_text("Test: Charisma -> Success", True)
                f "It's what we have in the current moment."
                if "lost" not in keywords:
                    show screen unlock_text("New keyword: LOST")
                    $ keywords.append("lost")
                    $ fer_keywords.append("lost")
                hide fernweh front onlayer front
                show fernweh tilt onlayer front
                f "Sometimes I feel as if I'm so LOST that I don't know what's happening now."
            else:
                show screen testing_text("Test: Charisma -> Failed", False)
                hide fernweh front onlayer front
                show fernweh tilt onlayer front
                f "Well I highly doubt that."
                f "You appear as fictitious enough to me."
            mc_s "Well you can hear my voice."
            f "I {i}appear{/i} to hear your voice."
            hide fernweh tilt onlayer front
            show fernweh front onlayer front
            f "Oh hahaha..."
            mc "Fernweh's laugh is a lot deeper than their normal voice.{w} It's a quiet boom that washes over you."
            show fernweh turn onlayer front
            f "Aren't you a strange thing?{w} This little thing that has come down here."
            ##### CUE
            f "Fallen from the heavens?"
            mc "What is this guy talking about?{w} I'm not some kind of fallen angel."
            mc_s "...{w} I..."
            mc "I don't think we should have this debate now."
            f "..."
    f "..."
    show screen setup_text("Strategy update")
    mc "Based on their general ambivalence and disinterest in me."
    mc "It doesn't look like charisma is going to help a lot..."
    hide fernweh turn onlayer front
    show fernweh tilt onlayer front
    f "You know I've been thinking of a lot of things."
    f "Yes..."
    f "I've been thinking a lot..."
    menu:
        f "...about what there is and what there isn't."
        "Define: \"what there is\" and \"what there isn't\" (+ intellect  + reputable)":
            # strategy 2: reputable
            $ temp_intellect += 1
            $ temp_reputable += 1
            hide fernweh tilt onlayer front
            show fernweh front onlayer front
            show fernweh_f_eyes onlayer inyourface with dissolve
            f "What I mean to say is that in this moment,{w} my epistemological status is being questioned."
            f "As well as my metaphysical one."
            mc "What load of nonsense was that?"
            mc "I need to be on the same wavelength as them, so I can get through."
            mc_s "Questioning... can be good?"
            hide fernweh front onlayer front
            show fernweh turn onlayer front
            f "Haha...{w} you wouldn't get it."
            mc_s "You don't know who I am,{w} so you can't make assumptions about what I will or will not 'get'."
            hide fernweh_f_eyes onlayer inyourface with dissolve
            f "I suppose that is true."
            hide fernweh turn onlayer front
            show fernweh tilt onlayer front
            f "But sometimes I doubt you're even here."
            f "Sometimes I think conversations are useless."
            hide fernweh tilt onlayer front
            show fernweh normal onlayer front
            f "But sometimes I think they're concrete and undeniable."
            mc "I may not be their therapist,{w} but them opening up can only mean good things for me."
        "Oh have you {i}really{/i} now? (+ supreme)":
            # strategy 3: supreme
            $ temp_supreme += 1
            $ fernweh_door -= 1
            hide fernweh tilt onlayer front
            show fernweh front onlayer front
            show fernweh_f_eyes onlayer inyourface with dissolve
            f "Are you implying that I don't think about things."
            mc_s "I reckon that you're way too deep into your mind."
            mc "Or their head is way too far up their backside."
            mc "That it all just becomes a meaningless mess that you don't know what to do with."
            hide fernweh_f_eyes onlayer inyourface with dissolve
            f "I-{w} I'm... I don't know what to say to that."
            hide fernweh front onlayer front
            show fernweh normal onlayer front
            f "You have a bit of spunk in you..."
            mc "They seem undecided whether or not they like that."
            mc "I'll let them make up their mind."
        "I can't understand you (- charisma)":
            # strategy 1: ignorance
            $ temp_charisma -= 1
            $ fernweh_door += 1
            hide fernweh tilt onlayer front
            show fernweh front onlayer front
            f "Oh ahaha...{w} it's funny because..."
            show fernweh_f_eyes onlayer inyourface with dissolve
            f "Because sometimes I don't always understand myself."
            mc_s "I like to think that nobody really does."
            mc "This,{w} of course,{w} is a load of rubbish."
            mc "But it's never about who you are,{w} but who you pretend to be."
            hide fernweh_f_eyes onlayer inyourface with dissolve
            hide fernweh front onlayer front
            show fernweh turn onlayer front
            f "Those that come here are always LOST,{w} whether they become disillusioned with reality..."
            f "...or simply don't know the path that they should take in life."
            f "It could even be for those who doubt their own existence."
            f "I...{w} ..."
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            if (supreme + temp_supreme) < 0:
                show screen testing_text("Test: Negative Supreme -> Success", True)
                f "When I would get lost in the CHASM..."
                ### KEYWORD: MAP
                if "map" not in keywords:
                    show screen unlock_text("New keyword: MAP")
                    $ keywords.append("map")
                    $ fer_keywords.append("map")
                f "... over the years I created a MAP."
                f "And it would chart everything within the CHASM so I would never get lost again."
                mc "A map you say?"
            else:
                show screen testing_text("Test: Negative Supreme -> Failed", False)
                f "Nevermind..."
            mc "Hmm..."
        "... (let them continue talking:  no effect)":
            hide fernweh tilt onlayer front
            show fernweh front onlayer front
            f "And at first I started to doubt how we can justify anything."
            f "Based on our understanding, everything seems to feeble and it can all collapse in an instance."
            f "You ask to justify something, and it keeps on going on...{w} leading to a never-ending chain of reasoning."
            f "Until you admit defeat."
            f "But then there's also one other thing..."
            hide fernweh front onlayer front
            show fernweh turn onlayer front
            f "..."
            mc "Perhaps they felt they said too much?"
            mc "Interesting."
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            if (knowledge + temp_knowledge) > 0:
                show screen testing_text("Test: Knowledge -> Success", True)
                mc "If I remember correctly,{w} this feels similar to Agrippan skepticism."
                #### KEYWORD: SKEPTIC
                if "skeptic" not in keywords:
                    show screen unlock_text("New keyword: SKEPTIC")
                    $ keywords.append("skeptic")
                    $ fer_keywords.append("skeptic")
                mc "Ah yes! The classic SKEPTIC.{w} It seems so obvious now."
            else:
                show screen testing_text("Test: Knowledge -> Failed", False)
                mc "Let them run their mouth if they want to."
    ################# PHASE 1 FINISHED
    ################# PHASE 2 BEGINS

    jump phase2_d1

label phase2_d1:
    $save_name = "-- dialogue 1 --"
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "But this is all irrelevant talk."
    f "I don't think it's appropriate for me to discuss these things with you."
    show fernweh_f_eyes onlayer inyourface with dissolve
    f "What I need is an answer relating to why you're {i}here{/i}."
    mc_s "Well I told you that-"
    f "Not how you got {i}here{/i} or what you want to speak with me about."
    f "As in, {i}why{/i} are you here?"
    mc_s "I'm sorry?"
    hide fernweh front onlayer front
    show fernweh tilt onlayer front
    hide fernweh_f_eyes onlayer inyourface
    show fernweh_t_eyes onlayer inyourface
    f "Only those who have fallen astray land in the CHASM."
    f "I know that you tried to {i}enter{/i} against the wishes of this place."
    f "Which seems incredibly bizarre because I haven't seen such an entry in a while."
    hide fernweh_t_eyes onlayer inyourface
    show fernweh_f_eyes onlayer inyourface
    hide fernweh tilt onlayer front
    show fernweh normal onlayer front
    f "You're either here because you deserve to be,{w} or you have breached an access point which should be illegal."
    mc "I need to think fast and know what they're talking about."
    ######### IF KEYWORD: LOST
    ### do this
    if "lost" in keywords:
        mc "People come to the CHASM if they're LOST."
        mc "So that means I was probably called here because I was {i}LOST{/i} too."
        mc "Think..."
        window hide
        menu:
            "I've LOST my sense of purpose (- reputable)":
                $ temp_reputable -= 1
                mc_s "At first I thought I knew what I was meant to do,{w} but now I don't know who I am."
                ## MINUS reputable
                ## open up Fernweh
            "I've LOST touch with reality itself (+ reputable)":
                $ fernweh_door += 1
                $ temp_reputable += 1
                ## PLUS reputable
                mc_s "I sometimes doubt that even if I'm living or exist."
            "I've LOST any reason to care (+ supreme)":
                $ temp_supreme += 1
                ## PLUS supreme
                mc_s "Because I won't be able to truly understand anything."


        if perception > 0:
            show screen testing_text("Test: Perception -> Success", True)
            f "Ah, so you're LOST too,{w} just like the {a=call:d1_p1}REST OF US{/a}."
        else:
            show screen testing_text("Test: Perception -> Failed", False)
            f "Ah, so you're LOST too,{w} just like the rest of us."
            f "That's quite alright."

        hide fernweh normal onlayer front
        show fernweh turn onlayer front
        f "In fact, I think this could be quite a good sign!"
        f "No one has lasted as long as you,{w} I thought you would be gone by now."
        f "How quaint!"
        hide fernweh turn onlayer front
        show fernweh normal onlayer front
        show screen cue_text("A sincerity in their smile.\n   They've been craving for company\n         for some time.") with dissolve
        mc "They make several soft giggling noises."
        mc "It's a bit eerie and unsettling..."
        hide screen cue_text with dissolve

    elif "soul" in keywords:
        ######## IF KEYWORD: SOUL
        ### do this
        mc_s "I'm just another SOUL living here...{w} like everyone else."
        hide fernweh normal onlayer front
        show fernweh turn onlayer front
        f "Ahaha... then you won't be here for long..."
        mc "This isn't a good sign."
        if perception > 0:
            show screen testing_text("Test: Perception -> Success", True)
            f "You should've {a=call:d1_p2}DISAPPEARED{/a} by now, I'm surprised you haven't."
        else:
            show screen testing_text("Test: Perception -> Failed", False)
            f "You should've disappeared by now, I'm surprised you haven't."
            f "Perhaps you are blessed!"
        hide fernweh turn onlayer front
        show fernweh normal onlayer front
        f "But anyways, this is a good sign you aren't gone!"
        mc "They seem to think that I'm an exception, or something that defies the rules of the CHASM."
        mc "So that's why I haven't left yet."
    #### ELSE
    else:
        mc "...{w} my mind is pulling a blank on me."
        mc "This is ok, I'll run with the latter option."
        mc_s "Sure, I 'breached' an access point.{w} But I'm figuring this."
        mc_s "If it was such a great deal you'd probably have done something to be right now."
        f "I-"
        mc_s "But you're choosing to keep me here alive because this is an anomaly you haven't seen before hm?"
        mc_s "Wise choice,{w} I have a lot to give."
        hide fernweh normal onlayer front
        show fernweh turn onlayer front
        if perception > 0:
            show screen cue_text("Fernweh bears brighter skin.\n   They seem genuinely interested") with dissolve
        f "Ahaha... what sort of thing could you possibly offer me?"
        mc_s "Oh I don't know...{w} some INSIGHT?"
        if perception > 0:
            hide screen cue_text with dissolve
        hide fernweh turn onlayer front
        show fernweh normal onlayer front
        f "What did you say?"
        mc "Whoops! Maybe I'll keep the tongue-in-cheek references to myself."
        mc_s "I said some greater understanding.{w} I can tell you've been lonely for a while."
        mc "Their appalling social skills, weird conversation and lack of coherent thoughts..."
        mc "Are great indicators that they haven't had a conversation in probably years."
        f "I won't be swayed by this.{w} After this you'll have to go."
        mc "Are they going to kill me?"
        mc "No, they would've done so by now.{w} This is just a bluff, I'm sure of it."

    f "But in your last,{w} final moments,{w} I will tell you this."
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "That everything you will say will be irrelevant."
    f "You will disassemble and lose yourself to the CHASM like everyone else."
    f "No matter how hard you try,{w} little silver-tongued,{w} you will be in the place where you're meant to be."
    mc "Tch.{w} I was told that I was 'meant to die' far too many times to take this talk seriously."
    mc "Even though this discussion has me at the centre,{w} I need to refocus back to Fernweh."
    mc "I can either let myself continue to be the centre and, through this,{w} reveal what Fernweh has to offer."
    mc "Or I can completely shift the focus of the conversation away from me."
    mc_s "And where is that?"
    mc "Fernweh begins to turn inward."
    hide fernweh_f_eyes onlayer inyourface with dissolve
    hide fernweh front onlayer front
    show fernweh front noblink nomouth up onlayer front
    f "Within the CHASM.{w} Forever."
    window hide
    menu:
        "And who decided that? (+ supreme)":
            $ temp_supreme += 1
            ## strategy: supreme, blackmail, number 4
            hide fernweh front noblink nomouth up onlayer front
            show fernweh normal onlayer front
            if perception > 0:
                show screen testing_text("Test: Perception -> Success", True)
                f "{a=call:d1_p3}SOMEONE{/a} long before me..."
            else:
                show screen testing_text("Test: Perception -> Failed", False)
                f "Some being from eons ago."
                mc_s "Does this mean you're not the 'de-facto' ruler of the place?"
                show screen cue_text("Their body is turning inwards.\n   Threatened body language and \n      nervous.") with dissolve
                f "Hmm... perhaps."
                f "But no one can fully tame the CHASM."
                hide screen cue_text with dissolve
                "They pause."
                f "It's a beauty and force of its own."

            hide fernweh normal onlayer front
            show fernweh tilt onlayer front
            f "But there is no need to control what is essentially nature itself."
            f "It's...{w} it's the only thing that feels real."
            f "But makes everything else,{w} including myself, feel so insignificant."
            mc_s "Does that mean you think of me as...{w} fake?"
            hide fernweh tilt onlayer front
            show fernweh normal smile onlayer front
            "Fernweh forms a grin and mist escapes through the gaping hole."
            f "Haha...."
            hide fernweh normal smile onlayer front
            show fernweh normal onlayer front

        "And what if that didn't happen? (+ intellect)":
            $ temp_intellect += 1
            hide fernweh front noblink nomouth up onlayer front
            show fernweh tilt onlayer front
            ## strategy: supreme, number 3
            if perception > 0:
                show screen cue_text("They have burrowed bush legs.\n   Irritated and angry body language.") with dissolve
            f "There's no need to discuss that because it won't never happen."
            if perception > 0:
                hide screen cue_text with dissolve
            if perception > 0:
                f "There's an {a=call:d1_p4}ORDER{/a} to things."
            else:
                f "There's an order to things."

            mc_s "Ah yes, of course."
            hide fernweh tilt onlayer front
            show fernweh turn onlayer front
            f "I'd like to think it's the only thing that I haven't made up."
            mc_s "Haha!{w} Does that mean you think I'm made up too?"
            f "Well, what else could you be?"
            f "Your mere existence breaks the rules of the CHASM,{w} that everyone will disappear."
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            f "So that means you cannot exist."

        "Is this where everyone is meant to go? (- knowledge)":
            hide fernweh front noblink nomouth up onlayer front
            show fernweh tilt onlayer front
            $ temp_knowledge -= 1
            ### strategy: number 1, playing ignorant
            if perception > 0:
                show screen cue_text("Their void heart is glowing.\n   Nurturing body language.\n   They think you're naive and weak.") with dissolve
            f "Not everyone, only for special people like you and me."
            if perception > 0:
                hide screen cue_text with dissolve
            mc "So does this mean they're going to 'pass on' as well?"
            mc_s "Are you just as {i}weak{/i} and helpless as me then?"
            hide fernweh tilt onlayer front
            show fernweh normal onlayer front
            f "I'd like to think I can outlast you."
            f "After all... you're just something in my mind."

        "And why do you believe that? (+ reputable)":
            $ temp_reputable += 1
            hide fernweh front noblink nomouth up onlayer front
            show fernweh normal onlayer front
            ### strategy number 2: reputable
            f "It doesn't matter what I believe,{w} it is only the way things are."
            mc_s "Your idea on 'the way things are' is not infallible."
            f "...{w} If you're a figment of my imagination, I couldn't possibly understand why you'd contradict me."

    mc_s "I'm sorry?"
    mc "What?"
    mc "Something that cannot exist, a figment of their imagination, something in their mind?"
    mc "Are you kidding me?"
    mc "How on earth am I supposed to win Fernweh's favour if they think I'm fake?"
    mc "That I don't exist?"
    show screen setup_text("Strategy update")
    ending "You can try to convince Fernweh you exist."
    ending "But you'll need a strong case and you need them to trust you."
    ending "Or you can break down their walls...{w} find a weakness."
    ending "But you'll need a strong conviction."
    mc_s "So... how come I'm talking to you?"
    f "Why it's simple, there's either two possibilities."
    show screen cue_text("Fernweh's eyes are shaded.\n   They're teling the truth.") with dissolve
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "One:{w} My monad is being supplied with nutrients inside a machine meant to simulate reality."
    f "Which includes you to be a part of the reality."
    mc_s "But I'm nothing more than just a bunch of nuts and bolts meant to resemble a person."
    "Fernweh nods their head."
    f "Or Two:{w} There is some malevolent demon who attempts to deceive me in believing in a nonexistent world."
    hide screen cue_text with dissolve
    f "He conjures up locations, people and such with his incomprehensible powers, solely for deceit."
    mc "Wow, talk about being self centred,{w} or being a solipsist."
    mc "Must take an awful lot of brain power to be this self-deluded."
    mc_s "So I'm either working for a Devil or I'm an artificial simulation."
    hide fernweh front onlayer front
    show fernweh turn onlayer front
    f "...{w} I wish I could say {i}\"Oh I didn't mean to insult you!,{w} of course I don't think that.\"{/i}"
    f "But..."
    hide fernweh turn onlayer front
    show fernweh tilt onlayer front
    f "I honestly don't care."
    mc "Hmm... interesting.{w} Guess I have to find some way to convince them 'to care' about the siphon."
    mc "Or maybe I could use this to my advantage."
    mc "But first, if this is the place 'I'm meant to be in',{w} then I should get to {i}know{/i} it."
    mc_s "Fernweh, could I ask you as to how the CHASM works?"
    hide fernweh tilt onlayer front
    show fernweh turn onlayer front
    show fernweh_f_eyes onlayer inyourface with dissolve
    f "Hmmm... it isn't complicated."
    ##### IF KEYWORD LOST
    if "lost" in keywords or "soul" in keywords:
        if "lost" not in keywords:
            show screen unlock_text("New keyword: LOST")
            $ keywords.append("lost")
            $ fer_keywords.append("lost")
        f "You already know that LOST SOULs come to this place."
        if "soul" not in keywords:
            show screen unlock_text("New keyword: SOUL")
            $ keywords.append("soul")
            $ fer_keywords.append("soul")
        hide fernweh turn onlayer front
        show fernweh front onlayer front
        f "Often when they doubt their reality,{w} doubt their purpose{w} or doubt even existing."
        f "That's when I take over."
        if perception > 0:
            show screen testing_text("Test: Perception -> Success", True)
            f "The CHASM does the work itself of {a=call:d1_p5}CONVERTING{/a} the LOST SOULs into energy."
        else:
            show screen testing_text("Test: Perception -> Failed", False)
            f "The CHASM does the work itself of converting the LOST SOULs into energy."

        f "And it lets the CHASM continue to thrive off of the nutrients of LOST SOULs."
        mc_s "So,{w} if nobody were LOST, would the CHASM cease to exist?"
        f "Foolish bile.{w} Nobody is free from me or free from the CHASM."
        f "Everyone will come here,{w} because there isn't a single being that's sure of themself."
        mc_s "Well,{w} I'd like to think that I'm holding myself pretty well together."
        hide fernweh front onlayer front
        show fernweh normal onlayer front
        f "You'd be surprised as to how weak and fallible you are, once staring into the gaping maw."
        mc_s "And... the maw is?"
        f "The opening pores where the CHASM breathes and consumes."
        mc "This place is starting to sound more like an actual person versus a static location."
        ### MIST pointer here
    else:
        f "I see...{w} I never told you as to what I do here, have I?"
        if perception > 0:
            show screen testing_text("Test: Perception -> Success", True)
            f "I, as a terror, lure {a=call:d1_p6}ANYONE{/a} that are LOST into the CHASM."
            if "lost" not in keywords:
                show screen unlock_text("New keyword: LOST")
                $ keywords.append("lost")
                $ fer_keywords.append("lost")
        else:
            show screen testing_text("Test: Perception -> Failed", False)
            f "I, as a terror, lure anyone that are LOST into the CHASM."
        hide fernweh turn onlayer front
        show fernweh normal onlayer front
        f "Then, the CHASM itself corrodes your very being, reducing you to less than nothing."
        f "Any remaining debris looks like fractured, glass-like shapes floating astray."
        f "Through this we can feed the CHASM to continue thriving,{w} and feed me so I can live."

    mc_s "But, if you aren't here, then what would happen?"
    f "People would still come to the CHASM,{w} they would just have to find the way themselves."
    f "Almost everyone goes through me first before I see them here."
    hide fernweh_f_eyes onlayer inyourface with dissolve
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "...{w} except for you.{w} I didn't anticipate that you would be here."
    f "Which is quite strange."
    f "But you'd be taken care of in a much more interesting way."
    mc "I don't like the sound of that."
    f "Because if you aren't LOST and somehow got in,{w} that means that the CHASM called you."
    f "Not me."
    mc_s "And why-"
    hide fernweh front onlayer front
    show fernweh tilt onlayer front
    f "Why, the lower you go down the CHASM (and closer into the earth) the more LOST you are."
    f "There are different layers to this place."
    hide fernweh tilt onlayer front
    show fernweh turn onlayer front
    f "First is for those with simple doubts:{w} they may not even disappear and simply wander back."
    if perception > 0 and (intellect + temp_intellect) > 0:
        show screen testing_text("Test: Perception + Intellect -> Success", True)
        f "The second are those who fully acknowledge that they can't {a=call:d1_p7}KNOW{/a} anything."
    else:
        show screen testing_text("Test: Perception + Intellect -> Failed", False)
        f "The second are those who fully acknowledge that they can't know anything."
    f "And the third, are those who undergo a classic {i}'existential nihilism'{/i}."
    f "The fourth are for those who are truly invisible,{w} no purpose, direction."
    f "The fifth are for those who think that reality itself is a complete farce."
    f "And sixth...{w} are for those who doubt that {b}they{/b} even exist themselves..."
    hide fernweh turn onlayer front
    show fernweh normal noblink smile onlayer front
    f "Incredible no?"
    mc_s "That...{w}sure is something."
    hide fernweh normal noblink smile onlayer front
    show fernweh normal onlayer front
    f "You seem to be an inquisitive creature."
    mc "That seems to amuse them."
    "The Questioning will now begin."
    "Use the KEYWORDs you have so far to ask Fernweh about them."
    "To do this, simply type in the KEYWORD you want to ask about."
    "Or perhaps you can ask about non-KEYWORDs too?"
    "Be warned because ONCE you've asked a question about a KEYWORD, that's it."
    "You cannot go back to it."

    ### this is the last menu choice

    ### POINTERS and CUES here and there

    ### then jump STRAIGHT to phase 4
    ### make phase 5 easy/simple
    ### write phase 6: this will comprise
        ### make Fernweh ramble on regarding how the CHASM as a structure works
        ### make Fernweh talk about how NOTHING exists (if you go strategy 2 or 3)
        ### make FernWeh talk about the past (if you go strategy 1 or 4)
        ### make a gameover for the player/end stat if you failed
    ### conclude


    jump phase4_d1


########################################
############################# need to implement the feature of
########## when you ask Fernweh about 'MAP', the conversation will then CLOSE
############# you CANNOT ask about the map again!!
label phase4_d1:
    f "Do you have anything else left to ask?"
    call screen questioning_input("phase7_d1")

    $ question = _return
    $ question = question.lower()

    if question =="lost":
        if "lost" in keywords and ferQlost == False:
            jump d1_Qlost
        elif ferQlost:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "soul":
        if "soul" in keywords and ferQsoul == False:
            jump d1_Qsoul
        elif ferQsoul:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "map":
        if "map" in keywords and ferQmap == False:
            jump d1_Qmap
        elif ferQmap:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "skeptic":
        if "skeptic" in keywords and ferQskeptic == False:
            jump d1_Qskeptic
        elif ferQskeptic:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "mist":
        if "mist" in keywords and ferQmist == False:
            jump d1_Qmist
        elif ferQmist:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "chasm":
        if "chasm" in keywords and ferQchasm == False:
            jump d1_Qchasm
        elif ferQchasm:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "faces":
        if "faces" in keywords and ferQfaces == False:
            jump d1_Qfaces
        elif ferQfaces:
            "You already asked this question."
        else:
            "You don't have this KEYWORD."
    elif question == "fernweh":
        jump d1_Qfernweh
    else:
        f "I'm sorry I don't understand."
    #f "You just typed in [question]."
    jump phase4_d1


### for all the phase 5/6 checks, I'm JUST writing WINNING states (aka where you win)
### you need to do checks on the stats (charisma, supreme, reputable)
## and if they FAIL the checks, they go into the FAIL states instead
## so there'll be an alternate... we'll call it "phase 8" states to go when they fail
### some will grant gameovers, others will let you continue with the "LOSE" condition
### depending on how badly you did

### need to finish strategy 2 and the PHASE 7 part
### also remember to add in stat checks THROUGHOUT the conversation for wins/fails
### if they LOSE just take them to phase7


################################
################# LEERE
#########################
label phase5_d1_Leere:
    window hide
    $ showtext = False
    $ showtext2 = False
    $ showinput = False
    $ quick_menu = False

    call screen fernweeh_leere_1(d1_leere()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase5_d1_Leere_door2

    else:
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."

    jump phase7_d1

label phase5_d1_Leere_door2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen fernweeh_leere_2() with quick_fade

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase5_d1_Leere

    elif search == "leere":
        window show
        jump phase6_d1_Leere

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase5_d1_Leere_door2

    jump phase7_d1

label phase6_d1_Leere:
    stop music fadeout 2.0
    hide screen text_timer
    show screen fer_door() with dissolve
    mc_s "Before I go 'disappear' forever, I was wondering about something."
    f "And that is?"
    mc_s "Did you ever have someone you knew very personally?"
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "Why would you ask such a thing?"
    mc_s "Haha... I don't know, it seems like you don't go out much."
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "I don't go out {i}at all{/i}.{w} The CHASM is my home and there's nowhere else to be."
    mc_s "Fernweh.{w} I'm not asking for hypotheticals here."
    f "I... don't understand what you're talking about."
    mc_s "Fernweh, I don't think you heard my question."
    mc_s "I'm asking if you {i}knew{/i} anybody. {w}If you were ever close with anyone."
    mc_s "If somebody {i}raised{/i} you Fernweh."
    mc_s "I'd consider that a close connection."
    mc_s "So I'd like you to repeat your answer, {i}truthfully{/i}, this time."
    hide fernweh front onlayer front
    show fernweh front oneblink onlayer front
    f "I don't know what you're doing and why you think I should answer you."
    mc_s "Because one of two things is going to happen."
    mc_s "You'll {i}\"disappear\"{/i} just like LEERE did or you'll be ruined."
    hide fernweh front oneblink onlayer front
    show fernweh tilt onlayer front
    f "What...{w} what did you say...{w} again?"
    mc_s "Oh so bells are ringing now? Excellent!"
    mc_s "I'm talking about LEERE.{w} LEERE."
    mc_s "Last time I checked you had ears-{nw}"
    stop music
    hide fernweh tilt onlayer front
    show fernweh front oneblink up onlayer front with vpunch
    f "SILENCE!"
    play nature "audio/sfx/destroy.wav"
    play sound "audio/sfx/quake.mp3"
    "The ground shakes and the mist closes in."
    play music "audio/music/Tension.wav"
    "There's a ringing in your ear and a beating in your head and a rip in your skin."
    "Fernweh's legs start rattling as they moves towards you."
    hide fernweh front oneblink up onlayer front
    show fernweh front oneblink point onlayer front with vpunch
    stop sound fadeout 2.0
    stop nature fadeout 2.0
    f "You.{w} You will NEVER{w} NEVER NEVER NEVER {nw}"
    f "SAY THAT NAME AGAIN!"
    f "UNDERSTOOD?"
    mc_s "I'm going to pretend I didn't hear the garbage that spewed from your mouth."
    mc_s "Now's not the time to get emotionally invested in someone you betrayed now is it?"
    hide fernweh front oneblink point onlayer front
    show fernweh front oneblink noarm onlayer front
    mc_s "No no no."
    mc_s "NOW is the time to start thinking about what happens next...{w} if you don't do as I say."
    hide fernweh front oneblink noarm onlayer front
    show fernweh front noblink onlayer front
    stop music fadeout 1.0
    f "Why."
    mc "Fernweh's form begins to dissipate across the room."
    if (supreme + temp_supreme) > 0 and (knowledge + temp_knowledge) > 1:
        play music "audio/music/Gaining.wav" fadein 1.0
    else:
        play music "audio/music/Losing.wav" fadein 1.0

    mc "Resembling a white ink, it starts to snatch everything and choke the life out of what little flora is on the ground."
    if (supreme + temp_supreme) > 0:
        show screen testing_text("Test: Supreme -> Success", True)
        f "WHY are you DOING THIS?"
    else:
        show screen testing_text("Test: Supreme -> Failed", False)
        $ fernweh_door -= 4
        f "What makes you think YOU CAN DO THIS?"
    mc_s "...{w} It isn't hard to explain."
    mc_s "You see,{w} just like the CHASM needs the LOST SOULs to fulfil its needs."
    mc_s "I have some things that fulfil mine."
    mc_s "Like the CHASM, without this, I will surely die.{w} It's a necessity for me, I need to survive."
    mc "Of course,{w} this is false."
    mc "But if they start suspecting that I just want to ladder climb,{w} word may go around of my...tactics..."
    mc_s "For me, I don't need any of your LOST SOULs.{w} What I need is a part of yours."
    hide fernweh front noblink onlayer front
    show fernweh normal noblink onlayer front
    show fernweh_f_eyes onlayer inyourface with dissolve
    if (knowledge + temp_knowledge) > 1:
        show screen testing_text("Test: Knowledge -> Success", True)
        f "Take it from SOMEONE ELSE!{w} LET ME GRIEVE!"
    else:
        show screen testing_text("Test: Knowledge -> Failed", False)
        $ fernweh_door -= 4
        f "WHY DON'T YOU TAKE IT FROM SOMEONE ELSE?"
    mc "And this is coming from someone who murdered their parent in the cold midwinter mist."
    mc "People would think such a thing is shameful,{w} but as much as I don't want to admit it."
    mc "In another world,{w} I would've done the same."
    mc "Not in Fernweh's and LEERE's position...{w} but in mine."
    mc "But this isn't about me, it's about the mistake Fernweh made."
    mc "How to usurp the Ruler of the CHASM, they had to kill them."
    mc "LEERE of the Lost,{w} the rightful guardian of the CHASM,{w} is dead, thanks to them."
    mc_s "No,{w} it has to be you."
    mc_s "This is why the CHASM called for me after all.{w} It was for LEERE."
    hide fernweh normal noblink onlayer front
    show fernweh turn onlayer front
    f "..."
    hide fernweh_f_eyes onlayer inyourface with dissolve
    mc "Suddenly, their whole demeanour changes."
    mc "Instead of wrath to foolish ire,{w} Fernweh is consumed by a lugubrious blue."
    hide fog_test2 onlayer back with dissolve
    hide fog_test onlayer inyourface with dissolve
    mc "The mist slows to a sombre stop.{w} And their forlorn face looks away."
    mc "A gaping maw in their face cracks across the rest of the body."
    mc "Did I cut too deep?{w} No.{w} This is what I need to do to convince them."
    mc "Even though I hardly believed I was here to make Fernweh atone for LEERE's death..."
    mc "The more I look at them,{w} the more convincing this story I fabricated becomes."
    mc "There's this conflict, a duality in their expression."
    mc "Their body coming to a standstill, yet they comprise a spinning, empty face."
    mc "Them believing this to be true,{w} yet a healthy dose of skepticism is there too."
    mc_s "And now,{w} you're going to make me your siphon."
    stop music fadeout 2.0
    mc_s "Or I won't be the only one seeking retribution."
    if (intellect + temp_intellect) > 1:
        show screen testing_text("Test: Intellect -> Success", True)
        f "..."
    else:
        show screen testing_text("Test: Intellect -> Failed", False)
        $ fernweh_door -= 4
        f "..."

    if fernweh_door < 2:
        hide fernweh turn onlayer front
        show fernweh front oneblink up onlayer front
        show fog_test2 onlayer back with dissolve
        show fog_test onlayer inyourface with dissolve
        jump phase8_d1
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "Fine...{w}done."
    hide fernweh front onlayer front
    show fernweh normal onlayer front
    f "It's...done."
    f "I will let you be my siphon."
    mc "That was...unexpectedly quick."
    mc "So, it actually worked."
    mc_s "Great-{nw}"
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "I don't want to see you ever again.{w} Just take my soul and leave..."
    f "Please..."
    show fog_test2 onlayer back with dissolve
    show fog_test onlayer inyourface with dissolve
    mc_s "As much as I'd love to,{w} it doesn't quite work like that."
    mc_s "I just need to make a quick imprint to \"seal\" the deal."
    mc_s "Because otherwise you could go back on your word."
    mc "I start pacing around the room, picking up glass shards on the CHASM floor."
    mc_s "And try to screw me over."
    mc_s "I'd like to think of you as an honest, decent person Fernweh."
    mc_s "But with your track record,{w} I'm going to have some precautions taken."
    mc_s "Now, if you'll let me do the honours..."
    hide fernweh turn onlayer front
    show fernweh normal onlayer front
    show fernweh_s_eyes onlayer inyourface with dissolve
    $ fernweh_str = "blackmail"
    "Fernweh doesn't say anything, but their swirling eyes act as a tacit agreement."
    "You're good to go."
    "Using your power of INSIGHT, enter the mind of Fernweh."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    hide fernweh_s_eyes onlayer inyourface with dissolve
    jump d1_win

################################
################# COMPASS
#########################
label phase5_d1_Compass:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen fernweeh_leere_1(d1_compass()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase5_d1_Compass_door2

    else:
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."

    jump phase7_d1

label phase5_d1_Compass_door2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen fernweeh_leere_2() with quick_fade

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase5_d1_Compass

    elif search == "compass":
        window show
        jump phase6_d1_Compass

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase5_d1_Compass_door2

    jump phase7_d1

label phase6_d1_Compass:
    stop music fadeout 2.0
    hide screen text_timer
    show screen fer_door() with dissolve
    mc_s "Before I go 'disappear' forever, I was wondering about something."
    f "And that is?"
    mc_s "Could I see...ONE last time{w} the Melduvian River?"
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "You don't get to make any last 'final' {i}requests{/i}."
    mc_s "Oh I don't do I?"
    mc "I open my mouth and grin widely.{w} Their eyes are hollow but I can see right through them."
    mc_s "Guess that means I get to make {b}demands{/b}."
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "I'm not taking you outside of this place."
    mc_s "I'm not asking you to."
    mc_s "I'm {b}demanding{/b} you to tell me everything you know about the COMPASS."
    hide fernweh front onlayer front
    show fernweh tilt onlayer front
    f "I don't know what you're talking about."
    mc_s "Oh of course you do!{w} Remember when you said something about your MAP?"
    mc_s "How...there was {b}only one copy{/b} of it?"
    mc_s "And how that was the {b}only way to navigate the CHASM{/b}?"
    mc_s "Now let's say,{w} hypothetically,{w} near the Melduvian River..."
    mc_s "There was a LOST SOUL who successfully escape the CHASM."
    mc_s "And stole the CHASM's heart, or its greatest artifact:{w} the WindFire COMPASS?"
    mc_s "Meaning that the original (and intended) form of navigation...{w}was swept right under your nose due to your incompetence?"
    mc_s "You would call this a serious blunder yes?"
    ## CUE
    hide fernweh tilt onlayer front
    show fernweh front oneblink onlayer front
    stop music
    f "I don't know what you're talking about."
    f "You don't exist."
    mc_s "But I surely must do!{w} Because you couldn't have possibly been aware of this."
    mc_s "Figments of your imagination {b}must{/b} ONLY retain information that you already know."
    mc "It was hard to find because I didn't expect their memory to be so fractured."
    mc "But that doesn't matter,{w} I got Fernweh right where I want them."
    mc_s "You've been suffering from memory loss for quite a while."
    mc_s "I'm not surprised that you aren't able to recall what the WindFire COMPASS is and what happened to it."
    mc_s "But let's get back to me 'not existing' and all."
    mc_s "If you 'created' me,{w} it means one of two things:"
    mc_s "I'm either some deep, {b}DEEP{/b} repressed representation of your psyche and your mistakes."
    mc_s "Or I'm an actual person with the power to ruin you."
    mc_s "Either way, I don't see things looking good for you."
    if (supreme + temp_supreme) > 0 and (knowledge + temp_knowledge) > 1:
        play music "audio/music/Gaining.wav" fadein 1.0
    else:
        play music "audio/music/Losing.wav" fadein 1.0

    hide fernweh front oneblink onlayer front
    show fernweh front oneblink point onlayer front with vpunch
    if (supreme + temp_supreme) > 0:
        show screen testing_text("Test: Supreme -> Success", True)
        f "OH WHY IS THAT?"
        f "Because I... no YOU will be dead before anyone hears a word of what you're saying..."
    else:
        show screen testing_text("Test: Supreme -> Failed", False)
        $ fernweh_door -= 4
        f "I'll TELL you THIS SILVEErr-tongueedd."
        f "You will be dead before ANYONE HEARS WORD OF THISs.s.."
    mc_s "Hahahaha!{w} Seriously? Come ON Fernweh we've been through this."
    mc_s "I would've been dead by now if I were LOST."
    mc_s "I know that you know that I'm not going anywhere."
    mc_s "And I know that you can't do a thing to me unless the CHASM says so."
    mc_s "Hellooo? CHASM?{w} What's your take on the puny, little silver-tongued detective here?"
    "Silence."
    mc_s "That's what I thought."
    hide fernweh front oneblink point onlayer front
    show fernweh front onlayer front with dissolve
    f "...{w} why are you DOING this?"
    f "What could you possibly WANT FROM ME?"
    hide fernweh front onlayer front
    show fernweh front oneblink up onlayer front
    f "I have NOTHING."
    mc_s "So,{w} I have a few more {b}demands{/b}."
    hide fernweh front oneblink up onlayer front
    show fernweh normal onlayer front
    f "Go to Hölle."
    mc_s "First, do you know what a siphon is?"
    f "..."
    mc_s "Well you see,{w} just like this great, glorious CHASM needs the LOST SOULs to fulfil its needs."
    mc_s "I have some things that fulfil mine."
    mc_s "Like the CHASM, without this, I will surely die.{w} It's a necessity for me, I need to survive."
    mc "Of course,{w} this is false."
    mc "But if they start suspecting that I just want to ladder climb,{w} word may go around of my...tactics..."
    mc_s "For me, I don't need any of your LOST SOULs.{w} What I need..."
    "You move in closer."
    mc_s "Is a teeny weeny part of YOURS."
    hide fernweh normal onlayer front
    if (knowledge + temp_knowledge) > 1:
        show fernweh front onlayer front
        show screen testing_text("Test: Knowledge -> Success", True)
        f "...{w}never."
        hide fernweh front onlayer front
    else:
        show screen testing_text("Test: Knowledge -> Failed", False)
        $ fernweh_door -= 4
        show fernweh front smile onlayer front with vpunch
        f "HAHAHAHA... NEVER!"
        hide fernweh front smile onlayer front
    show fernweh normal onlayer front
    mc_s "You don't have a choice."
    mc_s "It's either ruined OR, this won't be of any consequence because I..."
    mc_s "What was the word again?"
    mc_s "{i}\"Don't exist\"?{/i}"
    mc "In the moment, I think I must've let the power trip get to me."
    mc "In all honesty,{w} I wouldn't have the resources to spread around a \"rumour\" of the COMPASS."
    mc "Maybe with the G'narg's help, but it would be too much of an effort for one person."
    mc "But it doesn't matter who I really am.{w} It's who I {i}pretend{/i} to be."
    mc "And I'll just have to see if Fernweh buys it."
    mc_s "I'll let you take your time."
    stop music fadeout 2.0
    "A few minutes...{w} maybe hours pass."
    "During which, you notice how the CHASM is unchanging."
    "Almost as if it's indifferent to the suffering its guardian faces."
    "That's the thing with nature,{w} being a servant grants you no setbacks,{w} but it grants you no reward."
    "Because nature sees no nuance, ideologies or moral compass.{w} It just acts as it should."
    mc "Fernweh's eyes gape wide open.{w} Their masks falling at the seams."
    mc "Even though there lies nothing in their face,{w} I can see it becoming more distorted...hopeless."
    mc "Can they keep it together?"
    "Fernweh takes a step towards you."
    if (intellect + temp_intellect) > 1:
        show screen testing_text("Test: Intellect -> Success", True)
        f "..."
    else:
        show screen testing_text("Test: Intellect -> Failed", False)
        $ fernweh_door -= 4
        f "..."
    if fernweh_door < 2:
        hide fernweh normal onlayer front
        show fernweh front oneblink up onlayer front
        jump phase8_d1
    f "...{w}done."
    mc_s "I'm sorry?"
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "It's...{w} it's done.{w} You have my word."
    f "I will let you be my siphon."
    mc "Holy Hölle, it actually worked!"
    mc_s "Great to see the enthusiasm."
    mc_s "Now,{w} I just need to make a quick imprint to \"seal\" the deal."
    hide fernweh front onlayer front
    show fernweh normal onlayer front
    $ fernweh_str = "blackmail"
    "Using your power of INSIGHT, enter the mind of Fernweh."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    jump d1_win

################################
################# NOTHING
#########################
label phase6_d1_S2:
    stop music fadeout 2.0
    mc "Fernweh keeps denying my own existence...{w} which is aggravating to say the least."
    mc "But I can't convince them that I need to be their siphon, if I'm not anything."
    mc_s "On what grounds do you think I don't exist?"
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "You're here in the CHASM,{w} so even if you're real now, you're going to disappear soon."
    mc_s "I... *MAY* see your point here.{w} But I hardly think I'm going to be gone since it's been a while."
    mc_s "I know that you know that I'm not going anywhere."
    mc_s "And I know that you can't do a thing to me unless the CHASM says so."
    mc_s "So, the only option we have left here... is one where I'm a figment of your imagination."
    mc_s "Which is why I'm not going away."
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "I suppose... yes."
    if "skeptic" in keywords:
        mc "If they're just a SKEPTIC in disguise,{w} I merely have to refuse SKEPTIC talking points."
        mc "This should be...enlightening."
    else:
        mc "Maybe I don't need to prove that I'm real, as much as I have to prove that {b}their{/b} ideas are false."
        mc "If I can prove that you cannot believe the world doesn't exist,{w} then I disprove me being fake."
        mc "This is going to be...interesting."
    mc_s "Would you say that me {i}not{/i} existing is a biproduct of your metaphysical beliefs?"
    hide fernweh front onlayer front
    show fernweh tilt onlayer front
    f "What do you mean?"
    mc_s "You not believing in me is not anything against me in particular."
    mc_s "It's just because you don't believe in reality itself."
    f "..."
    mc_s "..."
    mc "Making them trust me,{w} means I have to trust in this silence."
    "Fernweh's misty form begins to shift.{w} One of their tendril-like legs pulls up a mask."
    "They stare at it for a couple of moments."
    "You wonder how such a great terror,{w} could be seen so weak like this."
    "How they could not be shameful or be ashamed of their vulnerability."
    mc "I certainly wouldn't be able to do that."
    f "..."
    hide fernweh tilt onlayer front
    show fernweh turn onlayer front
    play music "audio/music/Confused.wav"
    f "But how could you?"
    mc_s "How could I...what?"
    f "How can you truly, sincerely believe in anything?"
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "What if this is all an illusion?{w} How can you be certain of anything?"
    hide fernweh front onlayer front
    show fernweh front oneblink onlayer front
    f "Knowledge is fallible.{w} Bonds of lovers will break.{w} And time will melt away."
    f "The only certainty lies in the uncertain."
    mc "They form a hideous smile."
    hide fernweh front oneblink onlayer front
    show fernweh front frontblink smile onlayer front
    f "And in the CHASM."
    mc_s "Well, you see, I think you WOULD have a point."
    mc_s "Under the model of standard analysis for knowledge,{w} there's no way to escape this paradox."
    mc_s "You could never truly justify anything!"
    mc_s "Some foundationalists like to claim there are basic beliefs that the whole world boils down to."
    mc_s "Like axioms of knowledge."
    mc_s "Other coherence theorists like to say knowledge is an interconnections between beliefs."
    mc_s "And how beliefs are only credible upon the supposition of others."
    hide fernweh front frontblink smile onlayer front
    show fernweh tilt noblink nomouth onlayer front
    f "Which is how knowledge works?"
    mc_s "But we don't know the credibility of others,{w} or whether or not they're real."
    mc_s "It doesn't matter if one of them is false,{w} if they can all support each other in false ways it works."
    mc_s "So that's out of the question too."
    hide fernweh tilt noblink nomouth onlayer front
    show fernweh turn onlayer front
    f "If it isn't something that's intrinsic to the universe,{w} nor is it based on a web of beliefs..."
    if (intellect + temp_intellect) > 1:
        show screen testing_text("Test: Intellect -> Success", True)
        f "Then what is it?"
        mc_s "You can't get to that right away."
    else:
        show screen testing_text("Test: Intellect -> Failed", False)
        $ fernweh_door -= 5
        f "Then you make NO SENSE."
        mc_s "I mean... um{w}... well...{w}..."
        mc "Hang on a moment, I got this."
        mc_s "Well first off. I mean..."
    hide fernweh turn onlayer front
    show fernweh normal onlayer front
    mc_s "First, if you reframe what you think knowledge is.{w} Then...not believing in anything becomes pointless."
    mc_s "If we looked at knowledge under a contextualist model{w} or a Default and Challenge model."
    mc_s "Then things start to make sense."
    mc_s "Because knowledge isn't infallible,{w} but that's the whole point."
    mc_s "Knowledge should be made, countered, and remade again."
    mc_s "It doesn't possess any divine qualities,{w} its inherent usefulness is in relation to us."
    mc_s "So it doesn't matter if the malevolent demon tricks you,{w} or if this whole world is a simulation."
    mc_s "Because we can still WORK within this system."
    mc "I turn to them."
    show fernweh_s_eyes onlayer inyourface with dissolve
    mc_s "Your claim presupposes foundationalism (which we know to be false){w} and your conception of experience incorporates the Myth of the Given."
    mc_s "This myth is the assimilation of sapience to sentience, of thought to mere sensation."
    mc_s "Or in other words:{w} knowledge of what we perceive can be independent of the conceptual processes which result in perception."
    mc_s "It is because of this myth you're able to live in your delusions of a non-existent world."
    mc_s "What I'm saying Fernweh, is that with this in mind there should be no reason to doubt my existence."
    stop music fadeout 2.0
    mc_s "What matters is that you can hear and see me {b}in this moment{/b}.{w} Right?"
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    if (reputable + temp_reputable) > 1:
        play music "audio/music/Gaining.wav" fadein 1.0
    else:
        play music "audio/music/Losing.wav" fadein 1.0
    f "...{w} you are saying things I've never heard of."
    f "So you couldn't be made from some part of my imagination."
    f "You must be here,{w} in the present."
    f "And your reasoning couldn't come from my consciousness."
    f "Hmm..."
    if (reputable + temp_reputable) > 1:
        show screen testing_text("Test: Reputable -> Success", True)
        f "..."
    else:
        show screen testing_text("Test: Reputable -> Failed", False)
        $ fernweh_door -= 5
        f "..."
    if fernweh_door < 2:
        hide fernweh_s_eyes onlayer inyourface with dissolve
        hide fernweh turn onlayer front
        show fernweh front onlayer front
        f "You know what...{w} I don't believe you."
        mc_s "I'm sorry...{w} what did you just-{nw}"
        f "You're an extension of Cartes' Daemon, here to RUIN my LIFE!"
        mc_s "What?{w} That's not what I'm-"
        hide fernweh front onlayer front
        show fernweh front oneblink up onlayer front
        f "Listen HERE! YOU THINK YOU CAN CONVINCE ME TO BE COMPLACENT WITH MY LIFE?"
        f "I DON'T THINK SOoooo..."
        jump phase8_d1
    "Fernweh's eyes have a black shine wipe across them.{w} Their face is alight and dark."
    hide fernweh turn onlayer front
    show fernweh normal onlayer front
    f "Silver-tongued,{w} I don't know if this explanation is enough. I may need to think on it."
    f "But if you could give me some time."
    mc_s "Well,{w} if I'll be happy to give you my time...{w} for a price."
    hide fernweh_s_eyes onlayer inyourface with dissolve
    show fernweh_f_eyes  onlayer inyourface with dissolve
    f "Why for a price?"
    mc_s "My time is a valuable resource,{w} and one that is limited."
    mc_s "I am only able to survive off of the {i}gracious{/i} help of others."
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "And how...how do they help?"
    mc_s "Well it doesn't cost much.{w} Hardly anything at all.{w} It's just..."
    mc_s "A piece of your soul."
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "...{w} what?"
    mc_s "I'm a siphon, Fernweh."
    mc_s "Just as it's the CHASM's nature to make LOST souls disappear."
    mc_s "It is within mine to sustain myself through mental energy."
    hide fernweh_f_eyes  onlayer inyourface with dissolve
    f "And what... happens if you don't get mine."
    mc_s "If I don't,{w} I'll surely disappear.{w} And you'll never be able to find any more truths again."
    mc "This is all based on the assumption that Fernweh will {i}hopefully{/i} want to keep hearing from me."
    mc "If they still want to believe that everything is fake,{w} then there's nothing I can do."
    stop music fadeout 2.0
    f "..."
    hide fernweh front onlayer front
    show fernweh normal onlayer front
    f "Consider it done."
    f "Thank you for listening to my woes,{w} and for once in years..."
    f "Giving me something to actually {b}think{/b} about."
    mc_s "Great,{w} so I'll sign off the deal!"
    "Using your power of INSIGHT, enter the mind of Fernweh."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    jump d1_win

################################
################# BROKEN
#########################
label phase6_d1_S3:
    stop music fadeout 2.0
    show screen fer_door() with dissolve
    hide fernweh normal onlayer front
    show fernweh front oneblink up onlayer front with vpunch
    f "SILENCE!"
    f "I will hear no more of your NONSENSE!"
    mc_s "If you're going to have an ideology, it needs to be consistent."
    f "STOP!"
    mc_s "Look at me."
    hide fernweh front oneblink up onlayer front
    show fernweh front oneblink noarm onlayer front
    f "You should have disappeared by now..."
    mc_s "Fernweh, Look. At. Me."
    play music "audio/music/Confused.wav" fadein 1.0
    f "WHY... oh on Hölle's plane WHY aren't you going away?"
    mc_s "Fernweh please you're being hysterical."
    hide fernweh front oneblink noarm onlayer front
    show fernweh front noblink onlayer front
    f "..."
    mc "What little blood they have in them must've evaporated because it is boiling."
    mc "It raises one of its sharp, spider-like legs around my neck."
    hide fernweh front noblink onlayer front
    show fernweh front oneblink point onlayer front with vpunch
    f "Hysterical?{w} HYSTERICAL?"
    f "Well this HYSTERICAL can SNAP your neck off."
    mc_s "No use in killing me if I don't exist!"
    f "No use in keeping you alive either."
    mc_s "As long as I'm in your mind, I'll always be born again."
    mc "Of course I certainly WON'T.{w} I'm just going on the assumption that Fernweh will believe this."
    mc "Frankly speaking,{w} I'm shivering and almost terrified for my life."
    mc "Fernweh isn't a \"fighting\" terror per say.{w} But with my fragile malformed body,{w} they could easily break me."
    f "..."
    hide fernweh front oneblink point onlayer front
    show fernweh normal onlayer front
    f "Don't...don't insult me again."
    f "Please."
    mc_s "Fernweh I'm not here to insult you.{w} I'm here to deliver the honest truth, and it's this."
    mc "...{w} which is...{w} think..."
    mc "Hmmm..."
    hide screen fer_door with dissolve
    stop music fadeout 2.0
    mc "I guess I have to take a look inside their mind to see what's going on..."
    ### do an INSIGHT section here
    #### find the KEYWORD broken
    play sound "audio/sfx/hand.wav"
    show banner_back onlayer back with dissolve
    show banner_front onlayer front with dissolve
    $renpy.pause(0.2, hard=True)
    show hand_zoom onlayer inyourface
    $renpy.pause(1.0, hard=True)
    play music "audio/music/Insight.wav"
    if insight_timer:
        show screen text_timer(duration=120.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d1" )
    hide hand_zoom onlayer inyourface
    hide banner_front onlayer front
    hide banner_back onlayer back
    jump d1_broken_insight

label d1_broken_insight:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen fernweeh_leere_1(d1_broken()) with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    #$ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump phase5_d1_broken_door2

    else:
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."

    jump phase7_d1

label phase5_d1_broken_door2:
    window hide
    $ quick_menu = False
    $ showtext = False
    $ showtext2 = False
    $ showinput = False

    call screen fernweeh_leere_2() with quick_fade

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump d1_broken_insight

    elif search == "broken":
        window show
        jump phase7_d1_S3

    elif search == "EXIT":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump phase5_d1_broken_door2

    jump phase7_d1

label phase7_d1_S3:
    stop music fadeout 1.0
    hide screen text_timer
    mc_s "Are you okay?"
    f "I'm...{w} I'm fine."
    mc_s "You're breaking at the seams.{w} You're tearing yourself apart."
    if "mist" in keywords:
        mc_s "If I'm not mistaken,{w} the mist has slowly been corroding your being with time."
    else:
        mc_s "I know what the CHASM does.{w} And so do you."
    mc_s "This place holds no double standards for you.{w} It will treat you just like it does with anyone else."
    hide fernweh normal onlayer front
    show fernweh front oneblink onlayer front with vpunch
    f "But I'm NOT...{w} in danger.{w} This is only the first floor of the CHASM."
    mc_s "But the fact that you're suffering this much on a {i}safe{/i} floor can only be a bad sign."
    mc_s "There's no need to deny it anymore, it's fine to say that things are not okay."
    mc_s "That you need help,{w} and that things don't have to be this way."
    hide fernweh front oneblink onlayer front
    show fernweh turn onlayer front
    f "What... doesn't have to be this way?"
    mc_s "Life.{w} Let's face it, you don't really think much of anything do you?"
    mc_s "Everything's an illusion.{w} I'm a simulation, the outside world doesn't exist..."
    mc_s "People outside are created by an \"evil demon\" of sorts. Nothing is to be trusted."
    mc_s "You've become so disillusioned with life that you're practically not living one at all."
    hide fernweh turn onlayer front
    show fernweh tilt onlayer front
    f "Is that a problem?"
    f "The only thing I need to do is govern the CHASM that's all."
    stop music
    mc_s "You're lying to yourself."
    f "What?"
    mc_s "You and I know perfectly well that the CHASM would work just the same without you."
    mc_s "And do you know why?"
    f "...{w} why?"
    if (supreme + temp_supreme) > 1 and (knowledge + temp_knowledge) > 1:
        play music "audio/music/Gaining.wav" fadein 1.0
    else:
        play music "audio/music/Losing.wav" fadein 1.0
    mc_s "Because it doesn't exist."
    hide fernweh tilt onlayer front
    show fernweh front oneblink point onlayer front with vpunch
    if (supreme + temp_supreme) > 1:
        show screen testing_text("Test: Supreme -> Success", True)
        f "What you're saying is LUDICROUS!{w} What I've devoted myself to this entire time doesn't EXIST?"
    else:
        show screen testing_text("Test: Supreme -> Failed", False)
        $ fernweh_door -= 5
        f "Oh how DARE YOU!{w} THE AUDACITY YOU HAVE TO SAY THAT TO MY FACE..."
    mc_s "The CHASM makes anything that goes inside disappear."
    hide fernweh front oneblink point onlayer front
    show fernweh tilt onlayer front
    f "...yes."
    mc_s "How do you know that it hasn't consumed itself?"
    hide fernweh tilt onlayer front
    show fernweh normal onlayer front
    f "No.{w} Such a thing would be impossible...unthinkable."
    mc "Hmm. Maybe not the right angle to go for."
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "The CHASM takes other beings that are here and makes THEM disappear."
    f "It's how the cycle works,{w} how it maintains itself."
    mc "So, if the CHASM makes everything inside disappear...then that must mean."
    mc_s "Remember when you said how it's impossible that what you've \"devoted yourself\" to doesn't exist?"
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "That was...only a few seconds ago."
    mc_s "You know what WOULD make this feasible?"
    f "There's no point in debating that."
    mc_s "Is if {b}you{/b} don't exist."
    hide fernweh front onlayer front
    show fernweh normal onlayer front
    f "...{w} what?"
    mc "Fernweh said earlier about how the CHASM is divided into floors."
    mc "The deeper you go, the stronger the force of the CHASM."
    mc "So there's one thing I need to do, which is bring Fernweh down."
    mc "Or in other words,{w} I need to make Fernweh descend the CHASM.{w} Now it is I who has to call them under."
    mc_s "Isn't everything so obvious now?"
    mc_s "I don't exist.{w} The CHASM doesn't exist.{w} And neither do you!"
    hide fernweh normal onlayer front
    show fernweh tilt onlayer front
    f "What?"
    f "But there's a contradiction,{w} it's precisely BECAUSE I'm able to conjure you means I MUST THINK."
    f "Cogito Ergo Sum. I can't NOT exist if I can think."
    f "Therefore I must exist."
    mc "Fair point fair point...{w} but I think I can do better."
    mc_s "How do you know this isn't an \"illusion\" of thought?"
    mc_s "You \"creating\" me and thinking is based on a preconceived notion that YOU were created."
    mc_s "But what if this is just nothing?{w} You're nothing."
    mc_s "And all of this, is the last days of your SOUL trying to reconcile your nonexistence."
    mc_s "The empty space of objects do exist.{w} The hole in the cup, the space between words. The silence."
    mc_s "They, in theory, are there and do interact with the world.{w} But in isolation... what are they but nothing?"
    stop music fadeout 2.0
    mc_s "They are the presence of non-existence:{w} just like you Fernweh."
    hide fernweh tilt onlayer front
    show fernweh normal onlayer front
    f "I..."
    if (knowledge + temp_knowledge) > 1:
        show screen testing_text("Test: Knowledge -> Success", True)
        f "..."
    else:
        show screen testing_text("Test: Knowledge -> Failed", False)
        $ fernweh_door -= 5
        f "..."
    if fernweh_door < 2:
        hide fernweh normal onlayer front
        show fernweh front oneblink up onlayer front with vpunch
        f "I... can't BELIVE you said that to ME!"
        mc_s "Wait... I'm just stating-"
        hide fernweh front oneblink up onlayer front
        show fernweh front oneblink point onlayer front with vpunch
        f "I know EXACTLY WHAT YOU'RE UP TO..."
        f "Thought you could LURE ME INTO THE CHASM could you?"
        f "You PATHETIC LITTLE WELP!{w} GET OUT OF MY SIGHT-"
        hide fernweh front oneblink point onlayer front
        show fernweh front oneblink up onlayer front
        mc_s "Wait Fernweh I-{nw}"
        jump phase8_d1
    mc "They seem genuinely stunned,{w} unable to say anything."
    mc_s "Take a walk with me down."
    mc "I \"simulate\" walking down the CHASM floors so that they'll go deeper."
    mc "Soon, I notice I'm only talking to their head."
    mc "As I was talking, I notice that Fernweh is slowly beginning to collapse."
    mc "Wait...{w} are they starting to GENUINELY believe they don't exist?"
    mc "And because of that, they're ACTUALLY ceasing to exist."
    mc_s "To be true, the CHASM has consumed you a long time ago."
    mc_s "You're nothing but the debris that's left you see?"
    mc_s "You're..."
    hide fernweh normal onlayer front with dissolve
    mc "Their voice is completely gone,{w} I can barely see their form now."
    mc "I saw in real time how the CHASM consumes someone."
    mc "In the midst of the fall, I catch a glimpse of a lavender light."
    mc "That...must be their mind."
    mc "Even if they're gone, I can still \"feed\" off their energy."
    mc "All I need to do, is sign their leftover spirit."
    $ fernweh_str = "death"
    "Using your power of INSIGHT, enter whatever remains of Fernweh's mind."
    "You will leave your \"mark\" on their mind: which can say anything you want."
    "A signature?{w} A KEYWORD?{w} Or perhaps it's a word that's meaningful to you."
    ### do an INSIGHT section here
    jump d1_win


label insight_time_up_d1:
    stop music fadeout 2.0
    mc "ARRghhh-{w} I can't...{nw}"
    "Spending too much time in the mind of another person can cause strain on your mental energy."
    "Unfortunately, it looks like your time is up in navigating Fernweh's mind."
    mc "Wait! If I only had more time-{nw}"
    mc "..."
    mc "After I was booted out of Fernweh's mind, they turned and gave me a soft smile."
    mc "Good.{w} They don't seem to have taken on any side effects from my INSIGHT."
    mc "Meaning they probably won't suspect a thing."
    jump phase7_d1

label phase7_d1:
    stop music fadeout 2.0
    hide screen fer_door
    $save_name = "-- end of dialogue 1 --"
    hide screen fer_door with dissolve
    f "I see you have no more questions for me.{w} Well, I appreciate your time here."
    f "Thank you, it's not often I get to experience the company of others."
    play music "audio/music/Tension.wav"
    mc_s "Wait!{w} I have one last thing to ask of you."
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "Which is...?"
    mc_s "Would you be interested in... an exchange?"
    mc_s "Mutually beneficial of course,{w} but it's something that could change your life."
    f "Hahaha...{w} silver-tongued. Why would I ever want to make a deal with someone who doesn't exist?"
    mc "Oh Goden, they still think I'm fake."
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "The CHASM now beckons for you to go..."
    mc_s "Wait!{w} I just need ONE thing from you-"
    f "This first floor will close,{w} I suggest you leave."
    mc_s "Your soul!{w} YOUR SOUUULLL{nw}"
    stop nature fadeout 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    hide fernweh front onlayer front with dissolve
    hide fog_test2 onlayer back with dissolve
    hide fog_test onlayer inyourface with dissolve
    hide chasm onlayer farback with dissolve
    #show black onlayer farback with dissolve
    mc "And with that, they were gone."
    mc "So I left the CHASM empty-handed..."
    "Unfortunately, you failed to win Fernweh's favour.{w} And have \"LOST\" the first dialogue."
    "But sometimes,{w} you have to live with these failures and push on forward."
    "The story will still progress with this outcome."
    jump chapter2

label phase8_d1:
    stop music
    hide screen fer_door
    play music "audio/music/Tension.wav"
    hide fernweh front oneblink up onlayer front
    show fernweh front oneblink point onlayer front with vpunch
    f "You have DISTURBED this place for LONG ENOUGH!"
    f "I want to hear NO MORE WORD OUT OF YOU!"
    mc_s "But I thought I didn't exist... remember?"
    hide fernweh front oneblink point onlayer front with vpunch
    show fernweh front oneblink scream point onlayer front with vpunch
    f "SHUT UP!{w} I don't care about WHAT you are..."
    f "I JUST WANT YOU DEAD!"
    play nature "audio/sfx/destroy.wav"
    play sound "audio/sfx/quake.mp3"
    f "WITNESS MY WRATH, PUNY INSECT!!"
    mc "Oh god,{w} I have to get out of here now!"
    stop nature fadeout 2.0
    stop ambient fadeout 2.0
    stop music fadeout 2.0
    hide fernweh front oneblink scream point onlayer front
    hide fog_test2 onlayer back with dissolve
    hide fog_test onlayer inyourface with dissolve
    hide chasm onlayer farback with dissolve
    #show black onlayer farback with dissolve
    stop sound
    f "GET BACK HEREEEeeeeeeee{nw}"
    mc "I could still hear their voice, echoing and reverberating across the CHASM."
    mc "A voice so dense and filled with ire, that I could feel the air push itself around me."
    stop nature fadeout 2.0
    "Unfortunately, you failed to win Fernweh's favour.{w} And have \"LOST\" the first dialogue."
    "But sometimes,{w} you have to live with these failures and push on forward."
    "The story will still progress with this outcome."
    jump chapter2

#########################
########################## QUESTIONING PHASE 4
#############################

label d1_Qlost:
    mc_s "You say that there's always a time for everyone to come to the CHASM."
    f "Yes I did say that..."
    mc_s "But..."
    window hide
    menu:
        "Are you LOST? (+ charisma)":
            $ temp_charisma += 1
            f "I...{w} no."
            mc_s "But you said earlier how you think that I'm a figment of your imagination.{w} Someone that doesn't exist."
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "Correct."
            mc_s "So, that must mean that you've...LOST touch with reality?"
            mc_s "Or you're starting to doubt reality itself?"
            mc_s "What layer would you be put on?{w} The fourth? Or maybe it was the fifth-"
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            f "Silence!{w} Enough with your questioning!"
            mc "This isn't going anywhere, they're just too deep into denial."

            #if insight_timer:
                #show screen text_timer(duration=120.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d1" )
            jump phase6_d1_S3

        "Am I LOST? (- supreme)":
            $ temp_supreme -= 1
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "Why... of course you are."
            f "Even if you breached an illegal access point, or the CHASM called you."
            f "In the end you're here."
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            f "As everything was meant to be."

    $ferQlost = True

    jump phase4_d1

label d1_Qsoul:
    mc_s "Why do you need the energy of SOULs?{w} Surely you can sustain yourself."
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "I could, but this CHASM should have it.{w} It's a natural cycle."
    f "It's almost as if I were to ask a parasite not to leech on a host."
    f "It's in their very nature to do so."
    mc_s "I've come across parasites before,{w} and convinced them that they don't need a host."
    hide fernweh front onlayer front
    show fernweh turn onlayer front
    f "You think you can outsmart nature?"
    mc_s "I think nature doesn't need to be outsmarted,{w} but it needs to be worked with."
    mc_s "And it changes just like everything else, and you need to be willing to make changes too."
    ### CUE super untrustworthy
    hide fernweh turn onlayer front
    show fernweh normal onlayer front
    if perception > 0:
        show screen cue_text("Fernweh's eyes are getting brighter.\n   They're deceiving you.") with dissolve
    f "...Sure thing..."
    if perception > 0:
        hide screen cue_text
    $ferQsoul = True

    jump phase4_d1

label d1_Qmap:
    $ fernweh_door -=1
    mc_s "You said that you were in possession of a MAP of the CHASM."
    menu:
        f "It's not \"in possession\" as much as I was the one who created it."
        "How did you create the MAP? (no effect)":
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "If you spend a long enough time here then you start to notice all the little details."
            f "The crevices in the walls,{w} pores in the floor,{w} eyes looking back."
            f "Any remaining glass debris isn't going anywhere.{w} So they can act as pinpoints."
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            f "And with the twisting and turning,{w} you can keep track of the orientation based on the NILL cycles."
            mc_s "Ah, I see..."
        "But did you really make it? (!! confrontation)":
            ### LEERE blackmail
            ### CUE HERE
            f "I...{w} wait."
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            $ fernweh_door -=1
            if perception > 0:
                show screen cue_text("Fernweh's eyes are glowing.\n   They're deceiving you.") with dissolve
            f "Are you accusing me of lying?"
            if perception > 0:
                hide screen cue_text
            mc_s "Wasn't there...{w} maybe some ancient scriptures from before?"
            mc_s "Or the CHASM could've laid out the paths for you... making it easier to navigate?"
            if (intellect + temp_intellect) > 0:
                mc_s "Because you said that, and I quote, you \"govern\" the CHASM."
                mc_s "Meaning that {b}YOU{/b} own it and control it."
                mc_s "If that's the case,{w} the use of a MAP, for you, would be superfluous."
                mc_s "Why would you need a MAP if you control the CHASM?"
                mc_s "Unless,{w} because the CHASM works for you,{w} it showed you the MAP."
                mc_s "I'm not being accusatory,{w} I'm just asking for an explanation."
                hide fernweh turn onlayer front
                show fernweh front nomouth point onlayer front
                f "I. Don't NEED to justify myself to you!{w} You, you aren't even real."
                mc "They're getting agitated."
                mc_s "Hey, hey listen.{w} It's fine. I'll drop it."
                mc_s "You won't have to say a thing."
                hide fernweh front nomouth point onlayer front
                show fernweh front oneblink noarm onlayer front
                f "...{w} that was very unbecoming of you."
                mc_s "I know, I apologise."
                hide fernweh front oneblink noarm onlayer front
                show fernweh turn onlayer front
                f "So...{w} what now?"
                mc_s "Now I'm going to take a swim."
                hide fernweh turn onlayer front
                show fernweh normal onlayer front
                f "A what?"
                stop music fadeout 2.0
                "Use your INSIGHT to enter Fernweh's mind."
                hide screen fer_door with dissolve
                play sound "audio/sfx/hand.wav"
                show banner_back onlayer back with dissolve
                show banner_front onlayer front with dissolve
                $renpy.pause(0.2, hard=True)
                show hand_zoom onlayer inyourface
                $renpy.pause(1.0, hard=True)
                play music "audio/music/Insight.wav"
                if insight_timer:
                    show screen text_timer(duration=120.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d1" )
                hide hand_zoom onlayer inyourface
                hide banner_front onlayer front
                hide banner_back onlayer back
                jump phase5_d1_Leere
            else:
                f "There could've been, but those only acted as an assistance to me."
                hide fernweh turn onlayer front
                show fernweh normal onlayer front
                f "But I now, I know the way well enough that sometimes I can manage without it."
                mc_s "Did you...discard it?"
                f "No,{w} I simply hid it from sight!"

        "Is there only one copy of the MAP? (!! confrontation)":
            $ fernweh_door -=1
            f "Of course!{w} I was the one who created it, so there could only be one copy."
            #### CUE HERE
            if perception > 0:
                show screen cue_text("Fernweh's eyes are glowing.\n   They're deceiving you.") with dissolve
            hide fernweh normal onlayer front
            show fernweh turn onlayer front
            f "No one else governs the CHASM here, it is only I."
            f "Not a single being who enters here would be able to find a way out."
            f "Because the inscriptions on the MAP is in a language that only I can read."
            if perception > 0:
                hide screen cue_text with dissolve
            if "compass" in event_track:
                mc "Wait... I swear the G'narg spoke of someone who found another way."
                mc_s "It's funny...{w} because I don't think you should be so sure of that."
                hide fernweh turn onlayer front
                show fernweh normal onlayer front
                f "How can I possibly be unsure of this?"
                f "It's one of the most certain things in my life.{w} I can only-"
                mc_s "Like a classic solipsist you frame the conversation around yourself."
                mc_s "Let me enlighten you, and show you this thing called 'other people'."
                mc_s "And how other people, do indeed, exist too."
                stop music fadeout 2.0
                mc "In order to show them this,{w} I guess I have to take a look inside their mind..."
                hide screen fer_door with dissolve
                play sound "audio/sfx/hand.wav"
                show banner_back onlayer back with dissolve
                show banner_front onlayer front with dissolve
                $renpy.pause(0.2, hard=True)
                show hand_zoom onlayer inyourface
                $renpy.pause(1.0, hard=True)
                play music "audio/music/Insight.wav"
                if insight_timer:
                    show screen text_timer(duration=120.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d1" )
                hide hand_zoom onlayer inyourface
                hide banner_front onlayer front
                hide banner_back onlayer back
                jump phase5_d1_Compass
            else:
                hide fernweh turn onlayer front
                show fernweh normal onlayer front
                mc "I guess they have a point.{w} Who else could've possibly known of it?"
                mc "I only figured out about the MAP because they told me so."
                mc "Oh well..."
            ### COMPASS blackmail

    $ferQmap = True

    jump phase4_d1

label d1_Qskeptic:
    $ fernweh_door -=1
    mc_s "You seem to be a clear-cut SKEPTIC to me."
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "I don't go by insignificant labels."
    mc_s "But your general inability to accept me being here, is fascinating."
    mc_s "What I think, is that we'll take your beliefs and align them with the axioms of skepticism."
    mc_s "Then we can see the differences and break it down."
    hide fernweh turn onlayer front
    show fernweh front onlayer front
    f "Why would you want to do such a moronic task?"
    mc_s "I'm competent enough that I can do it, and I want to do it."
    hide fernweh front onlayer front
    show fernweh normal onlayer front
    f "You're going to tear down everything I say.{w} Here to mock me and-"
    mc_s "Relax Fernweh, you can {b}trust{/b} me.{w} No harm will be done to you."
    ### reputable strategy
    #jump phase4_d1
    $ferQskeptic = True
    jump phase6_d1_S2

label d1_Qmist:
    ### this locks in the dominant strategy
    mc_s "I just wanted to ask..."
    mc_s "Does the mist break down {i}anyone{/i} who enters?"
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "Yes, that is true."
    $ fernweh_door -=1
    mc_s "How come you haven't broken down in that case?"
    menu:
        f "I manage to keep myself together."
        "Do you? (!! confrontation)":
            $ fernweh_door -=1
            f "What?"
            mc_s "Are you really keeping yourself together?"
            hide fernweh front onlayer front
            show fernweh turn onlayer front
            f "The{w}...THE. AUDACITY-{nw}"
            mc_s "I see you coming down at the seems.{w} Not only physically with your fading body."
            mc_s "But mentally too."
            mc_s "You can barely hold two thoughts together.{w} You're wandering from one thing to the next."
            mc_s "I don't see how you could even-{nw}"
            hide fernweh turn onlayer front
            show fernweh front oneblink onlayer front
            f "Silence."
            mc "Okay, clearly this is going nowhere."
            hide fernweh front oneblink onlayer front
            hide screen fer_door with dissolve
            #if insight_timer:
                #show screen text_timer(duration=120.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d1" )
            jump phase6_d1_S3
        "I see. (+ charisma)":
            hide fernweh front onlayer front
            show fernweh turn onlayer front
            f "Sometimes the CHASM undoes me,{w} but that's alright, it's in their nature to do so."
            if "faces" not in keywords:
                show screen unlock_text("New keyword: FACES")
                $ keywords.append("faces")
                $ fer_keywords.append("faces")
            f "Because of this I have to keep remaking new FACES for myself."
            f "You can see them hanging at the sides."
            hide fernweh turn onlayer front
            show fernweh normal onlayer front
            f "Sometimes I wear them as masks,{w} but now I've given up trying to appease people."
            f "So I just let them see my empty face,{w} so they know the same fate that will arrive to them."

    $ferQmist = True
    jump phase4_d1

label d1_Qfaces:
    if "facetalk" not in event_track:
        $event_track.append("facetalk")
    ### this locks in the dominant strategy
    mc_s "How do you make the FACES?"
    hide fernweh normal onlayer front
    show fernweh turn onlayer front
    f "From the glass shards lying around or from the CHASM itself."
    mc_s "Were you born with a FACE?"
    f "I probably was,{w} but it's been so long I forgot now."
    f "It's funny{w} Leeee-{nw}"
    ##CUE
    if perception > 0:
        show screen cue_text("Fernweh's legs are churning.\n   They're trying to hide something.") with dissolve
    f "Leaving the new masks around."
    if perception > 0:
        hide screen cue_text with dissolve
    mc_s "What was that?"
    hide fernweh turn onlayer front
    show fernweh normal onlayer front
    f "It's...funny leaving the masks around on the CHASM."
    mc "I fail to see why this is humorous."
    $ferQfaces = True
    jump phase4_d1

label d1_Qchasm:
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "The CHASM has been my home for as long as I can remember."
    f "And it is my subject, my source of energy and my greatest work."
    f "I couldn't be more proud."
    mc_s "What came first?{w} The CHASM or you?"
    #### CUE
    if perception > 0:
        show screen cue_text("Fernweh's eyes are glowing.\n   They're deceiving you.") with dissolve
    f "I couldn't know.{w} We were both born together,{w} intrinsically tied with one another."
    if perception > 0:
        hide screen cue_text with dissolve
    window hide
    menu:
        "But what if there was someone before? (!! confrontation)":
            $ fernweh_door -= 2
            ### blackmail
            hide fernweh front onlayer front
            show fernweh normal onlayer front
            f "What? How...{w}what are you saying?"
            mc_s "You couldn't have possibly known what had come before."
            mc_s "You said that you were both \"born together\" but is there any concrete proof of that?"
            mc_s "How could you have possibly known that it wasn't here before you?"
            mc_s "The only was you could've known...{w} was to have been there BEFORE you were born."
            mc_s "Which presents a contradiction."
            hide fernweh normal onlayer front
            show fernweh front oneblink noarm onlayer front
            f "Are you seriously questioning what I'm saying?"
            mc_s "And you have the audacity to question my existence.{w} I'd say we're fair."
            hide fernweh front oneblink noarm onlayer front
            show fernweh normal onlayer front
            f "Hmm...{w} you're funny. And remind me of someone I once held dear."
            f "But they don't matter now..."
            mc "Oh they don't?{w} I'll be the judge of that."
            stop music fadeout 2.0
            mc "Let me take a peak inside."
            hide screen fer_door with dissolve
            play sound "audio/sfx/hand.wav"
            show banner_back onlayer back with dissolve
            show banner_front onlayer front with dissolve
            $renpy.pause(0.2, hard=True)
            show hand_zoom onlayer inyourface
            $renpy.pause(1.0, hard=True)
            play music "audio/music/Insight.wav"
            if insight_timer:
                show screen text_timer(duration=120.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="insight_time_up_d1" )
            hide hand_zoom onlayer inyourface
            hide banner_front onlayer front
            hide banner_back onlayer back
            jump phase5_d1_Leere
        "Well isn't that just wonderful (+ charisma)":
            f "Haha...{w} it certainly is!"
        "So you do acknowledge that this place exists (+ intellect)":
            hide fernweh front onlayer front
            show fernweh normal onlayer front
            f "Yes...{w} I suppose I do."
            mc_s "But you refuse to acknowledge my existence.{w} You claim for me to be a part of your imagination."
            mc_s "But that simply doesn't make any sense if you claim the CHASM is real."
            mc_s "You can't 'pick and choose' what's real.{w} Either nothing is real or all of it."
            jump phase6_d1_S2
    $ferQchasm = True
    jump phase4_d1

label d1_Qfernweh:
    $ fernweh_door +=1
    hide fernweh normal onlayer front
    show fernweh front onlayer front
    f "I am Fernweh of the Lost,{w} ruler of the CHASM which is home to those that are lost."
    f "I beckon them with my call,{w} and they come."
    f "They disappear.{w} And I do it again."
    mc_s "Could you survive without the CHASM?"
    hide fernweh front onlayer front
    show fernweh normal onlayer front
    f "It's not about whether I {i}could{/i} or {i}could not{/i}."
    f "I simply don't want to live a life that isn't here."
    $ferQfernweh = True
    jump phase4_d1

#############################
##################### POINTERS FROM DIALOGUE 1
############################

label d1_p1:
    mc_s "Who is \"the rest of us\"?"
    ### KEYWORD: SOUL
    if "soul" not in keywords:
        show screen unlock_text("New keyword: SOUL")
        $ keywords.append("soul")
        $ fer_keywords.append("soul")
    f "Why, the other SOULs of course."
    f "I call them to this sacred place so they can be forgotten."
    mc_s "But why would anyone want to be forgotten?"
    f "It's not that they {i}don't{/i} want to be forgotten."
    f "Simply put, they don't {i}want{/i} anything."
    mc_s "Do you?"
    f "..."
    return

label d1_p2:
    mc_s "Why would a SOUL like me disappear?"
    f "Oh!{w} Don't you know?"
    if "lost" not in keywords:
        show screen unlock_text("New keyword: LOST")
        $ keywords.append("lost")
        $ fer_keywords.append("lost")
    #### KEYWORD: LOST
    f "You're a LOST SOUL here."
    f "The CHASM beckons all who are LOST to come."
    f "All those who don't need or don't want to exist."
    f "All those who cannot exist as they are."
    mc_s "Will they be reborn again?"
    f "Haha...{w} I'm not one to say."
    return

label d1_p3:
    $ fernweh_door -=1
    mc_s "Pray tell, who is this enigma?"
    f "Well of course it was-"
    f "..."
    hide fernweh normal onlayer front with dissolve
    mc "They dissolve into the air and then reappear again."
    ## CUE HERE
    if perception > 0:
        show screen cue_text("Fernweh's eyes are glowing.\n   They're deceiving you.") with dissolve
    show fernweh front onlayer front with dissolve
    f "Someone long before your time..."
    mc_s "I could guess that."
    mc_s "But *who* specifically?"
    ## CUE HERE
    hide fernweh front onlayer front
    show fernweh normal onlayer front
    f "Does it matter?"
    if perception > 0:
        hide screen cue_text with dissolve
    return

label d1_p4:
    $ fernweh_door -=1
    mc_s "What sort of order is placed in the CHASM."
    f "At the bottom are lowlives like you.{w} Those who are meant to disappear."
    f "Then there's me, who acts as an Empyrean Ambassador for the great CHASM itself."
    mc "I always thought that the CHASM is a home for Fernweh.{w} Or a vessel for their work."
    mc "Perhaps it is not the CHASM that serves Fernweh's purposes."
    mc "But it is Fernweh who serves the CHASM."
    return

label d1_p5:
    mc_s "What exactly allows for this process of conversion?"
    mc_s "How do the lost souls here turn into nothing?{w} Or the broken glass shards?"
    "Fernweh's eyes grow darker and their legs start spinning."
    f "OoooOh!{w} It's all because of the great MIST!"
    if "mist" not in keywords:
        show screen unlock_text("New keyword: MIST")
        $ keywords.append("mist")
        $ fer_keywords.append("mist")
    f "The CHASM is home to the MIST that corrodes every being who enters."
    f "It's funny because you should be shattering,{w} dissolving,{w} fading..."
    f "Guess you're not as LOST as I thought you were!{w} Haha..."
    mc "This feels...uncomfortable..."
    f "Once the MIST has done its job,{w} I feed onto the energy left to sustain myself."
    mc "So it isn't in Fernweh's control of who gets to disappear and when!"
    mc "That's up to the system of the CHASM.{w} Interesting."
    return

label d1_p6:
    $ fernweh_door -=1
    mc_s "What constitutes \"being lost\"?"
    f "Someone who is \"lost\" needed to have believed in something, only for it to have been taken away."
    f "You can't be \"lost\" if you never had anything."
    mc "So it isn't about what you don't have, but about how \"great\" the fall was."
    mc "What a tragedy."
    f "These lost beings may have doubted their reality,{w} doubted their purpose{w} or doubted even existing."
    f "If it is to the point where it's debilitating, or if they decide to follow my call before it worsens..."
    f "Then they'll find themselves here, with everyone else."
    f "First they hear my call,{w} and soon they'll follow to be here."
    return

label d1_p7:
    $ fernweh_door -=1
    mc_s "Do you mean that they can't know if anything else exists?"
    f "No, simply put:{w} it's that they don't believe they can ever be sure of their own knowledge."
    f "Because of the Agrippan dilemma you get modes of infinity, assumption and circularity."
    f "When people keep asking you to justify your beliefs or they ask {i}\"how do you know this?\"{/i}"
    f "You have limited responses."
    f "The mode of infinity is the useless endeavour to continuously justify yourself."
    f "The mode of assumption is you refusing to answer."
    f "The mode of circularity is when you repeat what you said and end up back where you started."
    mc "Oh I get it now..."
    mc "This is..."
    if "skeptic" not in keywords:
        show screen unlock_text("New keyword: SKEPTIC")
        $ keywords.append("skeptic")
        $ fer_keywords.append("skeptic")
    f "A classical SKEPTICal paradox."

    return
