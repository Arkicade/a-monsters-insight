screen flowers():
    zorder 99
    #add "images/bg/flowers.png"
    #add "lily_p"
    #add "lily_p2"
    add SnowBlossom("test/particle.png", count= 100, yspeed=(-40,40))
    #add "images/bg/flower_monster_in_front.png"
    #add "lily_p"
    #add "lily_p2"


screen unlock_text(message):
    zorder 99
    on "show" action Play("sound", "audio/sfx/ctc.wav") ##add a cute sound!

    frame:
        ysize 30 yalign .5
        background Solid("#F74747") #change line color here
        at lineappear
    hbox:
        align (.5,.5)
        add Text(message, slow=True, slow_cps=30, size=60, font="fonts/Coves Bold.otf",color="#FBE593", outlines=[(6,"#fff",0,0),(3, "#F74747",0,0)])
        # change text properties here^

    # hide screen after a second
    timer 1.5 action Hide("unlock_text", transition=Dissolve(1.0))


screen setup_text(message):
    zorder 99
    #on "show" action Play("sound", "audio/sfx/collect.wav") ##add a cute sound!

    frame:
        ysize 30 yalign .5
        background Solid("#E72222") #change line color here
        at lineappear
    hbox:
        align (.5,.5)
        add Text(message, slow=True, slow_cps=30, size=85, font="fonts/Coves Bold.otf",color="#fff", outlines=[(6,"#fff",0,0),(3, "#000",0,0)])
        # change text properties here^

    # hide screen after a second
    timer 1.5 action Hide("setup_text", transition=Dissolve(0.8))


transform lineappear:
    yzoom 0
    easein .25 yzoom 1.4
    easeout .15 yzoom 1.0
    pause 1.4
    easeout .3 yzoom 0


screen gui_tooltip(my_text):
    #add my_picture xpos my_tt_xpos ypos my_tt_ypos
    text my_text xpos 1100 ypos 200 font "fonts/Coves Bold.otf"


transform floatingtext:
    xalign 0.5
    yalign 1.0, alpha 1.0
    linear 4.5 yalign 0.0, alpha 0.0


transform slowlyshow:
    alpha 0.0
    linear 1.5 alpha 1.0

screen testing_text(message, success):
    #zorder 99
    if test_text:
        if success:
            add "gui/button/tool_bg.png" at floatingtext
        else:
            add "gui/button/choice_hover_background.png" at floatingtext
        add Text(message, size=50, font="fonts/Coves Bold.otf") at floatingtext

    timer 3.0 action Hide("testing_text", transition=Dissolve(1))
#show screen testing_text("Test: Reputable -> Failed", False)

screen gui_cue(my_text):
    #add my_picture xpos my_tt_xpos ypos my_tt_ypos
    add "gui/stat/bubble.png" xpos 1110 ypos 200 #at slowlyshow
    text my_text xpos 1150 ypos 250 font "fonts/Coves Bold.otf" #at slowlyshow

screen cue_text(message):

    #hbox:
        #xalign 0.2
        #yalign 0.5
    imagebutton auto "gui/stat/cue_%s.png" action NullAction() hovered [Show("gui_cue", my_text=message, transition=Dissolve(0.5))] unhovered Hide("gui_cue", transition=Dissolve(0.5)) xpos 1400 ypos 450

###### testing_text takes two parameters
##### the string to say and whether or not it's a success
#### put FALSE if it's a failed test
#### put TRUE if it's a successful test
#show screen testing_text("Test: Reputable -> Failed", False)

init python:
    mode = "default"

screen mode():
    imagebutton auto "gui/stat/assist_%s.png" action [SetVariable("mode", "assist"), Play("sound", "audio/sfx/collect_low.wav"), Return()] hovered Play("sound", "audio/sfx/hover_1.wav") xalign 0.0 yalign 0.15
    imagebutton auto "gui/stat/default_%s.png" action [SetVariable("mode", "default"), Play("sound", "audio/sfx/collect.wav"), Return()] hovered Play("sound", "audio/sfx/hover_1.wav") xalign 0.48 yalign 0.15
    imagebutton auto "gui/stat/challenge_%s.png" action [SetVariable("mode", "challenge"), Play("sound", "audio/sfx/collect_high.wav"), Return()] hovered Play("sound", "audio/sfx/hover_1.wav") xalign 0.99 yalign 0.15
############################
##################### S T A T    S C R E E N
############################

screen stat_screen():
    #zorder 89
    tag menu
    add "newspaper_bg"
    add "gui/stat/stat_base.png"

    vbox:
        xalign 0.3
        yalign 0.1
        #text "STAT RAISING"
        add "gui/stat/stat_header.png"

    vbox:
        xalign 0.57
        yalign 0.5
        imagebutton auto "gui/stat/done_%s.png" action [Hide("stat_screen"),Return(), Play("sound", "audio/sfx/page.mp3")] hovered Play("sound", "audio/sfx/tap_high.wav")

    vbox:
        xalign 0.9
        yalign 0.2
        add "gui/stat/bubble.png"

    hbox:
        xalign 0.11
        yalign 0.9
        add "gui/stat/points.png"
        text "[points]" size 75 style "text_timer_ok"


    #frame:
        #xalign 0.3
        #yalign 0.4
        #vbox:
            #### hovered [ Play ("test_one", "sfx/click.wav"),   don't forget sfx
            #textbutton "Presence" action [Hide("stat_screen"), Show("stat_presence")] hovered [Show("gui_tooltip", my_text="How well I can present myself in conversations")] unhovered Hide("gui_tooltip")
            #imagebutton auto "gui/stat/presence_%s.png" action [Hide("stat_screen"), Show("stat_presence")] hovered [Show("gui_tooltip", my_text="How well I can present myself in conversations")] unhovered Hide("gui_tooltip")
            #textbutton "Prescience" action [Hide("stat_screen"), Show("stat_prescience")] hovered [Show("gui_tooltip", my_text="My ability to recall facts and use my reason")] unhovered Hide("gui_tooltip")
            #imagebutton auto "gui/stat/prescience_%s.png" action [Hide("stat_screen"), Show("stat_prescience")] hovered [Show("gui_tooltip", my_text="My ability to recall facts and use my reason")] unhovered Hide("gui_tooltip")
            #textbutton "Perception" action [Hide("stat_screen"), Show("stat_perception")] hovered [Show("gui_tooltip", my_text="Helps me pick up cues and pointers in speech")] unhovered Hide("gui_tooltip")
            #imagebutton auto "gui/stat/perception_%s.png" action [Hide("stat_screen"), Show("stat_perception")] hovered [Show("gui_tooltip", my_text="Helps me pick up cues and pointers in speech")] unhovered Hide("gui_tooltip")

    vbox:
        xalign 0.1
        yalign 0.4
        imagebutton auto "gui/stat/presence_%s.png" action [Hide("stat_screen"), Show("stat_presence"), Play("sound", "audio/sfx/flip.mp3")] hovered [Show("gui_tooltip", my_text="How well I can present\n   myself in conversations."), Play("sound", "audio/sfx/select_2.wav")] unhovered Hide("gui_tooltip")
    vbox:
        xalign 0.2
        yalign 0.55
        imagebutton auto "gui/stat/prescience_%s.png" action [Hide("stat_screen"), Show("stat_prescience"), Play("sound", "audio/sfx/flip.mp3")] hovered [Show("gui_tooltip", my_text="My ability to recall facts\n   and use my reason."), Play("sound", "audio/sfx/select_2.wav")] unhovered Hide("gui_tooltip")
    vbox:
        xalign 0.3
        yalign 0.7
        imagebutton auto "gui/stat/perception_%s.png" action [Hide("stat_screen"), Show("stat_perception"), Play("sound", "audio/sfx/flip.mp3")] hovered [Show("gui_tooltip", my_text="Helps me pick up cues and\n   pointers during the dialogue."), Play("sound", "audio/sfx/select_2.wav")] unhovered Hide("gui_tooltip")

default addon = 1
screen stat_presence():
    add "newspaper_bg"
    add "gui/stat/stat_base.png"
    $ points_to = abs(charisma) + abs(reputable) + abs(supreme) + points
    $ char_to = abs(charisma) + points
    $ rept_to = abs(reputable) + points
    $ supr_to = abs(supreme) + points

    vbox:
        xalign 0.9
        yalign 0.2
        add "gui/stat/bubble.png"


    vbox:
        xalign 0.3
        yalign 0.1
        #text "PRESENCE"
        add "gui/stat/presence_title.png"

    hbox:
        xalign 0.11
        yalign 0.9
        add "gui/stat/points.png"
        text "[points]" size 75 style "text_timer_ok"


    python:
        if addon == 1:
            textsign = "+"
            toolsign = "+1"
        else:
            textsign = "-"
            toolsign = "-1"



    hbox:
        xalign 0.12
        yalign 0.4
        # action NullAction()
        textbutton "[textsign]" action [If(points > 0,  [SetVariable("points", points-1), SetVariable("charisma", charisma+addon)],  SetVariable("points", points)), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="My ability to be \"likeable\",\n charming and agreeable.\n     {i}+1/-1 to charisma {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#fc5abb" text_size 120
        textbutton "Charisma" action [SetVariable("points", char_to), SetVariable("charisma", 0), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="My ability to be \"likeable\",\n charming and agreeable.\n     {i}reset charisma to zero. {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#fc5abb"
        text ": [charisma]" style "nonhover_stat"
    hbox:
        xalign 0.22
        yalign 0.55
        textbutton "[textsign]" action [ If(points > 0, [SetVariable("points", points-1), SetVariable("reputable", reputable+addon)],  SetVariable("points", points)), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="Appearing as trustworthy,\n respectable and thoughtful.\n     {i}+1/-1 to reputable {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#f7a942" text_size 120
        textbutton "Reputable" action [SetVariable("points", rept_to), SetVariable("reputable", 0), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="Appearing as trustworthy,\n respectable and thoughtful.\n     {i}reset reputable to zero. {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#f7a942"
        text ": [reputable]" style "nonhover_stat"
    hbox:
        xalign 0.32
        yalign 0.7
        textbutton "[textsign]" action [If(points > 0,[SetVariable("points", points-1), SetVariable("supreme", supreme+addon)], SetVariable("points", points)), Play("sound", "audio/sfx/select_2.wav") ] hovered [Show("gui_tooltip", my_text="How to appear as \"powerful\",\n strong and the dominant speaker.\n     {i}+1/-1 to supreme {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#ff353a" text_size 120
        textbutton "Supreme" action [SetVariable("points", supr_to), SetVariable("supreme", 0), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="How to appear as \"powerful\",\n strong and the dominant speaker.\n     {i}reset supreme to zero {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#ff353a"
        text ": [supreme]" style "nonhover_stat"

    #hbox:
        #xalign 0.15
        #yalign 0.2
        #textbutton "Reset all points" action [SetVariable("points", points_to), SetVariable("charisma", 0), SetVariable("reputable", 0), SetVariable("supreme", 0)] text_style "text_stat"

    hbox:
        xalign 0.55
        yalign 0.9
        if textsign == "+":
            textbutton "switch to -1" action [If(addon == 1, SetVariable("addon",-1), SetVariable("addon",1))] text_style "text_stat2"
        else:
            textbutton "switch to +1" action [If(addon == 1, SetVariable("addon",-1), SetVariable("addon",1))] text_style "text_stat2"



    vbox:
        xalign 0.57
        yalign 0.5
        imagebutton auto "gui/stat/done_%s.png" action [Hide("stat_presence"), Show("stat_screen"), Play("sound", "audio/sfx/book_close.wav")] hovered Play("sound", "audio/sfx/tap.wav")

screen stat_prescience():
    add "newspaper_bg"
    add "gui/stat/stat_base.png"
    $ points_to = abs(knowledge) + abs(intellect) + points
    $ know_to = abs(knowledge) + points
    $ inte_to = abs(intellect) + points

    python:
        if addon == 1:
            textsign = "+"
            toolsign = "+1"
        else:
            textsign = "-"
            toolsign = "-1"

    vbox:
        xalign 0.9
        yalign 0.2
        add "gui/stat/bubble.png"


    vbox:
        xalign 0.3
        yalign 0.1
        #text "PRESENCE"
        add "gui/stat/prescience_title.png"

    hbox:
        xalign 0.11
        yalign 0.9
        add "gui/stat/points.png"
        text "[points]" size 75 style "text_timer_ok"


    hbox:
        xalign 0.12
        yalign 0.4
        # action NullAction()
        textbutton "[textsign]" action [If(points > 0,[SetVariable("points", points-1), SetVariable("knowledge", knowledge+addon)], SetVariable("points", points)), Play("sound", "audio/sfx/select_2.wav") ] hovered [Show("gui_tooltip", my_text="My capacity to retain and\n   remember information.\n     {i}+1/-1 to knowledge. {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#4893fd" text_size 120
        textbutton "Knowledge" action [SetVariable("points", know_to), SetVariable("knowledge", 0), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="My capacity to retain and\n   remember information.\n     {i}reset knowledge to zero. {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#4893fd"
        text ": [knowledge]" style "nonhover_stat"
    hbox:
        xalign 0.22
        yalign 0.55
        textbutton "[textsign]" action [If(points > 0,[SetVariable("points", points-1), SetVariable("intellect", intellect+addon)], SetVariable("points", points)), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="How I make sound judgements\n and use logic.\n     {i}+1/-1 to intellect. {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#73f440" text_size 120
        textbutton "Intellect" action [SetVariable("points", inte_to), SetVariable("intellect", 0), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="How I make sound judgements\n and use logic.\n     {i}reset intellect to zero. {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_color "#fff" text_hover_color "#73f440"
        text ": [intellect]" style "nonhover_stat"


    hbox:
        xalign 0.55
        yalign 0.9
        if textsign == "+":
            textbutton "switch to -1" action [If(addon == 1, SetVariable("addon",-1), SetVariable("addon",1))] text_style "text_stat2"
        else:
            textbutton "switch to +1" action [If(addon == 1, SetVariable("addon",-1), SetVariable("addon",1))] text_style "text_stat2"


    vbox:
        xalign 0.57
        yalign 0.5
        imagebutton auto "gui/stat/done_%s.png" action [Hide("stat_prescience"), Show("stat_screen"), Play("sound", "audio/sfx/book_close.wav")] hovered Play("sound", "audio/sfx/tap.wav")




    #frame:
        #xalign 0.6
        #yalign 0.1
        #vbox:
            #textbutton "R E S E T" action [SetVariable("points", points_to), SetVariable("knowledge", 0), SetVariable("intellect", 0)]
            #textbutton "Change to +1/-1" action [If(addon == 1, SetVariable("addon",-1), SetVariable("addon",1))]


    #frame:
        #xalign 0.3
        #yalign 0.4
        #vbox:
            #textbutton "Knowledge" action [If(points > 0,[SetVariable("points", points-1), SetVariable("knowledge", knowledge+addon)], SetVariable("points", points)) ] hovered [Show("gui_tooltip", my_text="My capacity to retain and remember information")] unhovered Hide("gui_tooltip")
            #textbutton "Intellect" action [If(points > 0,[SetVariable("points", points-1), SetVariable("intellect", intellect+addon)], SetVariable("points", points))] hovered [Show("gui_tooltip", my_text="How I make sound judgements and use logic")] unhovered Hide("gui_tooltip")


    #frame:
        #xalign 0.8
        #yalign 0.8
        #textbutton "GO BACK" action [Hide("stat_prescience"), Show("stat_screen")]


screen stat_perception():
    add "newspaper_bg"
    add "gui/stat/stat_base.png"
    $ points_to = perception + points

    vbox:
        xalign 0.3
        yalign 0.1
        #text "PRESENCE"
        add "gui/stat/perception_title.png"

    vbox:
        xalign 0.9
        yalign 0.2
        add "gui/stat/bubble.png"

    hbox:
        xalign 0.11
        yalign 0.9
        add "gui/stat/points.png"
        text "[points]" size 75 style "text_timer_ok"


    hbox:
        xalign 0.22
        yalign 0.55
        # action NullAction()
        textbutton "+" action [If(points > 0,[SetVariable("points", points-1), SetVariable("perception", perception+1)], SetVariable("points", points)), Play("sound", "audio/sfx/select_2.wav") ] hovered [Show("gui_tooltip", my_text="My ability notice CUES and\n POINTERS."), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat" text_size 120
        textbutton "Perception" action [SetVariable("points", points_to), SetVariable("perception", 0), Play("sound", "audio/sfx/select_2.wav")] hovered [Show("gui_tooltip", my_text="My ability notice CUES and\n POINTERS.\n     {i}reset perception to zero. {/i}"), Play("sound", "audio/sfx/hover_2.wav")] unhovered Hide("gui_tooltip") text_style "text_stat"
        text ": [perception]" style "nonhover_stat"


    vbox:
        xalign 0.57
        yalign 0.5
        imagebutton auto "gui/stat/done_%s.png" action [Hide("stat_perception"), Show("stat_screen"), Play("sound", "audio/sfx/book_close.wav")] hovered [Play("sound", "audio/sfx/tap.wav")]


    #frame:
        #xalign 0.3
        #yalign 0.4
        #vbox:
            #textbutton "Perception" action [If(points > 1,[SetVariable("points", points-2), SetVariable("perception", perception+1)], SetVariable("points", points)) ] hovered [Show("gui_tooltip", my_text="My ability notice CUES and POINTERS")] unhovered Hide("gui_tooltip")

    #frame:
        #xalign 0.7
        #yalign 0.4
        #vbox:
            #text "Points is [points]"
            #text "Every Perception costs 2 points instead of 1"
            #text "##############"
            #text "Perception is [perception]"


screen questioning_input(exitlabel):
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 0.07
        ypadding 0.07

        vbox:
            #xpadding 100
            #ypadding 100
            text "Start typing in a KEYWORD below (or non keyword)\n"
            input default "" length 12
            text "\nWhen you've typed in the KEYWORD, press ENTER."

    frame:
        xalign 0.9
        yalign 0.9
        vbox:

            textbutton "NO MORE QUESTIONS" action Jump(exitlabel)


screen stat_inv():
    zorder 89
    tag menu
    add "newspaper_bg"
    add "gui/stat/stat_base.png"
    python:
        personality = ""
        know_type = ""
        inte_type = ""
        personality_list = [abs(charisma + temp_charisma), abs(reputable + temp_reputable), abs(supreme + temp_supreme)]
        person_char = abs(charisma + temp_charisma) ##a
        person_rept = abs(reputable + temp_reputable) ##b
        person_supr = abs(supreme + temp_supreme) ##c
        char_total = charisma + temp_charisma
        rept_total = reputable + temp_reputable
        supr_total = supreme + temp_supreme
        know_total = knowledge + temp_knowledge
        inte_total = intellect + temp_intellect
        twomix = []

        if person_char >= person_supr and person_rept >= person_supr:
            if (charisma+temp_charisma) < 0:
                twomix.append("N charisma")
            else:
                twomix.append("charisma")
            if (reputable + temp_reputable) < 0:
                twomix.append("N reputable")
            else:
                twomix.append("reputable")
        elif person_char <= person_rept and person_char <= person_supr:
            if (supreme + temp_supreme) < 0:
                twomix.append("N supreme")
            else:
                twomix.append("supreme")
            if (reputable + temp_reputable) < 0:
                twomix.append("N reputable")
            else:
                twomix.append("reputable")
        elif person_char >= person_rept and person_rept <= person_supr:
            if (charisma+temp_charisma) < 0:
                twomix.append("N charisma")
            else:
                twomix.append("charisma")
            if (supreme + temp_supreme) < 0:
                twomix.append("N supreme")
            else:
                twomix.append("supreme")

        if know_total < 0:
            know_type = "ignorant"
        elif know_total == 0:
            know_type = "relatively informed"
        else:
            know_type = "knowledgeable"

        if inte_total < 0:
            inte_type = "foolish"
        elif inte_total == 0:
            inte_type = "cautious"
        else:
            inte_type = "an intellectual"

        if person_char == 0 and person_rept == 0 and person_supr == 0:
            personality = "not clearly defined"
        elif "N charisma" in twomix and "reputable" in twomix:
            personality = "apathetic"
        elif "N charisma" in twomix and "supreme" in twomix:
            personality = "domineering"
        elif "N reputable" in twomix and "charisma" in twomix:
            personality = "a sciolist"
        elif "N reputable" in twomix and "supreme" in twomix:
            personality = "corrupt"
        elif "N supreme" in twomix and "charisma" in twomix:
            personality = "a sycophant"
        elif "N supreme" in twomix and "reputable" in twomix:
            personality = "yielding"
        elif "charisma" in twomix and "reputable" in twomix:
            personality = "noble"
        elif "charisma" in twomix and "supreme" in twomix:
            personality = "captivating"
        elif "reputable" in twomix and "supreme" in twomix:
            personality = "competent"
        else:
            personality = "not clearly defined"




    vbox:
        xalign 0.3
        yalign 0.1
        #text "STAT RAISING"
        add "gui/stat/stat_header.png"

    vbox:
        xalign 0.57
        yalign 0.5
        imagebutton auto "gui/stat/done_%s.png" action [Hide("stat_inv"),Return(), Play("sound", "audio/sfx/page.mp3")]

    vbox:
        xalign 0.9
        yalign 0.2
        add "gui/stat/bubble.png"

    hbox:
        xalign 0.12
        yalign 0.36
        # action NullAction()
        add "gui/stat/char_icon.png"
        text "Charisma" style "text_stat" color "#fc5abb"
        text ": [char_total]" style "nonhover_stat" color "#fc5abb"
    hbox:
        xalign 0.18
        yalign 0.45
        add "gui/stat/repu_icon.png"
        text "Reputable" style "text_stat" color "#f7a942"
        text ": [rept_total]" style "nonhover_stat" color "#f7a942"
    hbox:
        xalign 0.24
        yalign 0.55
        add "gui/stat/supr_icon.png"
        text "Supreme" style "text_stat" color "#ff353a"
        text ": [supr_total]" style "nonhover_stat" color "#ff353a"

    hbox:
        xalign 0.3
        yalign 0.65
        add "gui/stat/know_icon.png"
        text "Knowledge" style "text_stat" color "#4893fd"
        text ": [know_total]" style "nonhover_stat" color "#4893fd"

    hbox:
        xalign 0.42
        yalign 0.75
        add "gui/stat/inte_icon.png"
        text "Intellect" style "text_stat" color "#73f440"
        text ": [inte_total]" style "nonhover_stat" color "#73f440"

    hbox:
        xalign 0.12
        yalign 0.89
        add "gui/stat/perc_icon.png"
        text "Perception" style "text_stat"
        text ": [perception]" style "nonhover_stat"

    text "I am [personality]."xpos 1100 ypos 200 font "fonts/Coves Bold.otf"
    text "I am [know_type]."xpos 1150 ypos 260 font "fonts/Coves Bold.otf"
    text "And I am [inte_type]."xpos 1200 ypos 320 font "fonts/Coves Bold.otf"






############################
##################### K E Y W O R D    U I
############################
screen vpgrid_test():

    vpgrid:

        cols 1
        spacing 5
        draggable True
        mousewheel True

        scrollbars "vertical"

        area (100, 300, 800, 700)

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        for i in range(1, 100):

            textbutton "Button [i]":
                xysize (200, 50)
                action Return(i)



####call screen keyword_inv


screen keyword_inv():
    tag menu
    zorder 89
    add "gui/stat/inv_bg.png"

    imagebutton auto "gui/stat/exit_%s.png" action [Hide("keyword_inv"), Return(), Play("sound", "audio/sfx/book_close.wav")] xalign 0.005 yalign 0.96

    if met_fer:
        imagebutton auto "gui/stat/fer_%s.png" action [Hide("keyword_inv"), Show("fern_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.33 yalign 0.05 #xalign 0.01 yalign 0.05

    if met_cor:
        imagebutton auto "gui/stat/cor_%s.png" action [Hide("keyword_inv"), Show("cor_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.66 yalign 0.05 #xalign 0.33 yalign 0.05

    if met_deu:
        imagebutton auto "gui/stat/deu_%s.png" action [Hide("keyword_inv"), Show("deu_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.99 yalign 0.05 #xalign 0.66 yalign 0.05


    imagebutton auto "gui/stat/misc_%s.png" action NullAction() xalign 0.01 yalign 0.05 #xalign 0.99 yalign 0.05

    add "gui/stat/keyword_inv_bg.png" xpos 50 ypos 200

    text "This is where I've been\njournaling and storing\nall of the KEYWORDS\nI've found." xalign 0.87 yalign 0.21 size 70 style "text_keyinv"
    text "There are labels above\nto filter through the\ndifferent types of\nKEYWORDS." xalign 0.87 yalign 0.75 size 70 style "text_keyinv"

    vpgrid:

        cols 1
        spacing 5
        draggable True
        mousewheel True

        scrollbars "vertical"

        area (100, 200, 800, 700)

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        for word in keywords:

            textbutton "[word]":
                xysize (500, 120)
                text_style "text_keyinv"
                action NullAction()



#### put the signature here if you're done
screen fern_inv():
    tag menu
    zorder 89
    add "gui/stat/inv_bg.png"

    imagebutton auto "gui/stat/exit_%s.png" action [Hide("fern_inv"), Return(), Play("sound", "audio/sfx/book_close.wav")] xalign 0.005 yalign 0.96

    if met_fer:
        imagebutton auto "gui/stat/fer_%s.png" action NullAction() xalign 0.33 yalign 0.05

    if met_cor:
        imagebutton auto "gui/stat/cor_%s.png" action [Hide("fern_inv"), Show("cor_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.66 yalign 0.05

    if met_deu:
        imagebutton auto "gui/stat/deu_%s.png" action [Hide("fern_inv"), Show("deu_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.99 yalign 0.05



    imagebutton auto "gui/stat/misc_%s.png" action [Hide("fern_inv"), Show("keyword_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.01 yalign 0.05
    add "gui/stat/keyword_inv_bg.png" xpos 50 ypos 200

    add "gui/stat/fern_icon.png" xalign 0.95 yalign 0.86

    if fernweh_sig != "":
        text "code: [fernweh_sig]" xalign 0.82 yalign 0.75 size 88 style "text_keyinv"


    vpgrid:

        cols 1
        spacing 5
        draggable True
        mousewheel True

        scrollbars "vertical"

        area (100, 200, 800, 700)

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        for word in fer_keywords:

            textbutton "[word]":
                xysize (500, 120)
                text_style "text_keyinv"
                action NullAction()

screen cor_inv():
    tag menu
    zorder 89
    add "gui/stat/inv_bg.png"

    imagebutton auto "gui/stat/exit_%s.png" action [Hide("cor_inv"), Return(), Play("sound", "audio/sfx/book_close.wav")] xalign 0.005 yalign 0.96

    if met_fer:
        imagebutton auto "gui/stat/fer_%s.png" action [Hide("cor_inv"), Show("fern_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.33 yalign 0.05

    if met_cor:
        imagebutton auto "gui/stat/cor_%s.png" action NullAction() xalign 0.66 yalign 0.05

    if met_deu:
        imagebutton auto "gui/stat/deu_%s.png" action [Hide("cor_inv"), Show("deu_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.99 yalign 0.05



    imagebutton auto "gui/stat/misc_%s.png" action [Hide("cor_inv"), Show("keyword_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.01 yalign 0.05
    add "gui/stat/keyword_inv_bg.png" xpos 50 ypos 200

    add "gui/stat/cor_icon.png" xalign 0.95 yalign 0.86

    if cormeum_sig != "":
        text "code: [cormeum_sig]" xalign 0.82 yalign 0.75 size 88 style "text_keyinv"




    vpgrid:

        cols 1
        spacing 5
        draggable True
        mousewheel True

        scrollbars "vertical"

        area (100, 200, 800, 700)

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        for word in cor_keywords:

            textbutton "[word]":
                xysize (500, 120)
                text_style "text_keyinv"
                action NullAction()

screen deu_inv():
    tag menu
    zorder 89
    add "gui/stat/inv_bg.png"

    imagebutton auto "gui/stat/exit_%s.png" action [Hide("deu_inv"), Return(), Play("sound", "audio/sfx/book_close.wav")] xalign 0.005 yalign 0.96

    if met_fer:
        imagebutton auto "gui/stat/fer_%s.png" action [Hide("deu_inv"), Show("fern_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.33 yalign 0.05

    if met_cor:
        imagebutton auto "gui/stat/cor_%s.png" action [Hide("deu_inv"), Show("cor_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.66 yalign 0.05

    if met_deu:
        imagebutton auto "gui/stat/deu_%s.png" action NullAction() xalign 0.99 yalign 0.05



    imagebutton auto "gui/stat/misc_%s.png" action [Hide("deu_inv"), Show("keyword_inv"), Play("sound", "audio/sfx/page.mp3")] xalign 0.01 yalign 0.05
    add "gui/stat/keyword_inv_bg.png" xpos 50 ypos 200

    add "gui/stat/deu_icon.png" xalign 0.95 yalign 0.86

    if deulithoteq_sig != "":
        text "code: [deulithoteq_sig]" xalign 0.82 yalign 0.75 size 88 style "text_keyinv"


    vpgrid:

        cols 1
        spacing 5
        draggable True
        mousewheel True

        scrollbars "vertical"

        area (100, 200, 800, 700)

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        for word in deu_keywords:

            textbutton "[word]":
                xysize (500, 120)
                text_style "text_keyinv"
                action NullAction()


############################
##################### D O O R   U I
############################

screen fer_door():
    if interlocutor_state:
        python:
            f_state = ""
            if 4 <= fernweh_door <= 6:
                f_state = "neutral"
            elif fernweh_door > 8:
                f_state = "open"
            elif fernweh_door > 6:
                f_state = "comfortable"
            elif fernweh_door < 2:
                f_state = "closed"
            elif fernweh_door < 4:
                f_state = "suspicious"

        text "Fernweh's state: [f_state]" style "text_insight":
            xalign 0.12
            yalign 0.5
        bar:
            xalign 0.1
            yalign 0.6
            value AnimatedValue(value=fernweh_door, range=10, delay=1.3)
            #range 10
            xysize (500,65)


screen cor_door():
    if interlocutor_state:
        python:
            f_state = ""
            if 4 <= cormeum_door <= 6:
                f_state = "neutral"
            elif cormeum_door > 8:
                f_state = "open"
            elif cormeum_door > 6:
                f_state = "comfortable"
            elif cormeum_door < 2:
                f_state = "closed"
            elif cormeum_door < 4:
                f_state = "suspicious"

        text "Cor Meum's state: [f_state]" style "text_insight":
            xalign 0.08
            yalign 0.5
        bar:
            xalign 0.08
            yalign 0.6
            #value cormeum_door
            value AnimatedValue(value=cormeum_door, range=10, delay=1.3)
            #range 10
            xysize (500,65)


screen deu_door():
    if interlocutor_state:
        python:
            f_state = ""
            if 4 <= deulithoteq_door <= 6:
                f_state = "neutral"
            elif deulithoteq_door > 8:
                f_state = "open"
            elif deulithoteq_door > 6:
                f_state = "comfortable"
            elif deulithoteq_door < 2:
                f_state = "closed"
            elif deulithoteq_door < 4:
                f_state = "suspicious"

        text "Deulithoteq's state: [f_state]" style "text_insight":
            xalign 0.05
            yalign 0.55
        bar:
            xalign 0.05
            yalign 0.65
            #value deulithoteq_door
            value AnimatedValue(value=deulithoteq_door, range=10, delay=1.3)
            #range 10
            xysize (500,65)
