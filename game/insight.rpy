###############################################################################
################################## I N    G A M E    I N S I G H T ###########
#################################################################################

############### MENU UI is HERE
init python:
    style.trigger = Style(style.button)
    style.trigger.size = 40
    style.trigger.color = "#ffffff"
    style.trigger.hover_color = "#9EF58A"
    style.trigger.font = "fonts/Coves Bold.otf"

############### TIMER IS HERE

style text_timer_ok:
    size 72
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

#fonts/Coves Bold.otf

style text_stat:
    size 72
    color "#FFF"
    hover_color "#F74747"
    outlines [(2, "#000", 0, 0)]

style text_keyinv:
    size 72
    color "#FFF"
    font "fonts/Coves Bold.otf"
    hover_color "#F74747"
    outlines [(2, "#000", 0, 0)]

style text_insight:
    size 51
    color "#FFF"
    font "fonts/Coves Bold.otf"
    #hover_color "#F74747"
    outlines [(2, "#000", 0, 0)]

style text_stat2:
    size 60
    color "#FBE593"
    hover_color "#F55482"
    outlines [(2, "#000", 0, 0)]

style nonhover_stat:
    size 72
    color "#FFF"
    outlines [(2, "#000", 0, 0)]



style text_timer_near:
    size 72
    color "#F22"
    outlines [(2, "#000", 0, 0)]


init python:

    def text_countdown( st, at,
                        duration = 10.0,
                        fail_label = 'fail_label',
                        screen = 'text_timer',
                        ok_style = 'text_timer_ok',
                        near_style = 'text_timer_near',
                        style_swap = 20.0,
                        text_format = "{minutes:02d}:{seconds:02d}:{micro_seconds[0]}" ):

        remaining = duration - st

        parts_dict = {
            'minutes' : int( remaining // 60 ),
            'seconds' : int( remaining % 60 ),
            'micro_seconds' : str(int( (remaining % 1) * 10000 )), # we use str() so we can define precision
        }

        if remaining <= 0.0:
            renpy.hide_screen(screen)
            renpy.call(fail_label)

        return Text( text_format.format(**parts_dict),
                     style = ok_style if remaining > style_swap else near_style), .1


########### POINTERS UI is HERE
init python:
    #### make insight_timer enabled by default
    #### make it emotion hints disabled by default
    #### still undecided on test_text but leaning on enabled by default
    #### make interlocutor state DISABLED by default


    style.lexikon = Style(style.say_dialogue)    # base style to work with
    style.lexikon.bold = True
    style.lexikon.color = "#F93247"
    style.lexikon.hover_color = "#9EF58A"
    style.lexikon.font = "fonts/Coves Bold.otf"
    #style.lexikon.underline = True
    style.lexikon.hover_underline = True

    #style.hyperlink_text = Style(style.say_dialogue)
    #style.hyperlink_text.bold = True
    #style.hyperlink_text.color = "#ffffff"
    #style.hyperlink_text.hover_color = "#000000"

    #style.hyperlink_text = style.lexikon


    def hyperlink_styler(target):
        return style.lexikon

    def hyperlink_callback(target):
        # handle click.
        return

    #style.default.hyperlink_functions = (hyperlink_styler, hyperlink_callback, None)
    #style.default.hyperlink_functions[0] = hyperlink_styler

    style.default.hyperlink_functions = (hyperlink_styler, style.default.hyperlink_functions[1], None)


######### ok so FIRST! in order for the r.blit thing to work
######### you have to store all the colbH and colbW in a separate thing!
############ this is the thing you can store it in
############ actually do this for all colliders and interactables


init python:
    input_TT_1 = "Place an ANSWER here.\nStart typing text below:"
    input_TT_2 = ""
    input_TT_3 = "\nPress ENTER when done.\nTo close this message press the down arrow key."
    class Keycheething():
        def __init__(self):

            self.colbX = [0, 1470, -1, -1]
            self.colbY = [0, 0, -20, -20]
            self.colbW = [550, 550, 1, 1]
            self.colbH = [1080, 1080, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            self.intX = [-100, -200, 900, 1200, 600, -200]
            self.intY = [-100, -200, 500, 80, 100, -200]
            self.intW = [1, 150, 120, 120, 120, 1]
            self.intH = [1, 220, 170, 170, 170, 1]

            self.xp = 900
            self.yp = 900

    class Fernweh_leere_1_cor():
        def __init__(self):

            self.colbX = [0, 1620, -6, -6]
            self.colbY = [0, 0, -20, -20]
            self.colbW = [300, 300, 1, 1]
            self.colbH = [1080, 1080, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 860, 500, -200, 1200, -200]
            self.intY = [-100, 80, 500, -200, 500, -200]
            self.intW = [1, 150, 120, 1, 120, 1]
            self.intH = [1, 220, 170, 1, 170, 1]

            self.xp = 900
            self.yp = 900

    class Fernweh_leere_2_cor():
        def __init__(self):

            self.colbX = [200, -6, -6, -6]
            self.colbY = [400, 20, -20, -20]
            self.colbW = [1450, 1, 1, 1]
            self.colbH = [100, 1, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            self.intX = [-80, 900, -200, 860, -200, -200]
            self.intY = [-80, 800, -200, 100, -200, -200]
            self.intW = [1, 150, 1, 120, 1, 1]
            self.intH = [1, 220, 1, 170, 1, 1]

            self.xp = 600
            self.yp = 900


############ TEXT TO DISPLAY for DIALOGUE 1
    class d1_leere():
        def __init__(self):
            #self.text1 = "Forbidden into the shadows you may grow"
            #self.text2 = "Forever you will be unknown"
            self.text1 = ["{b}L{/b}isten and h{b}E{/b}ar my pl{b}E{/b}a.\n1, 5, 3."]
            self.text2 = ["fe{b}R{/b}nweh, listen to m{b}E{/b}.\n4, 2."]

    class d1_compass():
        def __init__(self):
            self.text1 = ["We were lost at sea\nI didn't know where to go\nbut then I found a..."]
            self.text2 = ["The answer is a 7 letter word"]

    class d1_broken():
        def __init__(self):
            self.text1 = ["When mirrors are ______ it brings bad luck.\nWhen love is ______ can it ever heal?"]
            self.text2 = ["X\n RX\n   X\n     XN"]


############ ROOM STRUCTURES OF DIALOGUE 2
    class CorMeum_time_1():
        def __init__(self):

            self.colbX = [0, 1220, 0, 1220]
            self.colbY = [0, 0, 700, 700]
            self.colbW = [700, 700, 700, 700]
            self.colbH = [400, 400, 400, 400]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 860, 100, -100, 900, 1500]
            self.intY = [-100, 80, 500, -100, 900, 450]
            self.intW = [1, 150, 120, 1, 120, 150]
            self.intH = [1, 220, 170, 1, 170, 220]

            self.xp = 900
            self.yp = 500

    class CorMeum_time_3():
        def __init__(self):

            self.colbX = [0, 1620, -6, -6]
            self.colbY = [0, 0, -20, -20]
            self.colbW = [300, 300, 1, 1]
            self.colbH = [1080, 1080, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 860, -200, 900, -200, -200]
            self.intY = [-100, 80,-200, 800, -200, -200]
            self.intW = [1, 150, 1, 120, 1, 1]
            self.intH = [1, 220, 1, 170, 1, 1]

            self.xp = 900
            self.yp = 300

    class CorMeum_time_2():
        def __init__(self):

            self.colbX = [400, -6, -6, -6]
            self.colbY = [450, -20, -20, -20]
            self.colbW = [1100, 1, 1, 1]
            self.colbH = [130, 1, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 860, 100, 900, -100, -1100]
            self.intY = [-100, 800, 450, 80, -100, -550]
            self.intW = [1, 150, 120, 120, 1, 1]
            self.intH = [1, 220, 170, 170, 1, 1]

            self.xp = 750
            self.yp = 900

    #### twomind
    class CorMeum_twomind():
        def __init__(self):

            self.colbX = [0, 1470, -1, -1]
            self.colbY = [0, 0, -20, -20]
            self.colbW = [550, 550, 1, 1]
            self.colbH = [1080, 1080, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            self.intX = [-100, -200, 900, 1200, 600, -200]
            self.intY = [-100, -200, 500, 80, 100, -200]
            self.intW = [1, 150, 120, 120, 120, 1]
            self.intH = [1, 220, 170, 170, 170, 1]

            self.xp = 900
            self.yp = 900



############ TEXT TO DISPLAY for DIALOGUE 2

    class d2_time():
        def __init__(self):
            self.text1 = ["Here are hints for the FINAL answer.\nThe first is the first letter\nof the answer from {b}before{/b}...\nThe second, third and fourth though\nare for you to discover."]
            self.text2 = ["There is no {b}I{/b} in team.\nBut there is a {b}ME{/b}.\n\n The second, third and fourth letters are in the 2 lines above."]
    class d2_time2():
        def __init__(self):
            self.text1 = ["______ (first letter T) is the feeling\nof dread at the possibility of something frightening\n,while horror is the shock of seeing the frightening thing."]
            self.text2 = [""]
    class d2_nascent():
        def __init__(self):
            self.text1 = ["Like our mind, the final answer is split in two!\nThe first half is for you to find.\nThe second half is your previous answer\nto get the key.\n\nfirst half + old answer = final answer!"]
            self.text2 = ["{u}How to decode the cipher{/u}:\n   L -> B\n\n\{u}First half of the final answer{/u}:\n   XK -> ??"]
    class d2_nascent2():
        def __init__(self):
            self.text1 = ["The beasts can hunt you down using their noses.\nThey sniff to find your _____(last letter t).\nWhat a smell!"]
            self.text2 = [""]
    class d2_necromancy():
        def __init__(self):
            self.text1 = ["The final answer includes the previous answer to get the key.\nBut the previous answer needs its last letter gone!\n\n _ _ _  +  (last answer minus last letter)  + CY"]
            self.text2 = ["{u}How to decode the cipher{/u}:\n   L -> B\n\n{u}First half of the final answer{/u}:\n   XOM -> ???"]
    class d2_necromancy2():
        def __init__(self):
            self.text1 = ["What a beautiful love story!\nWhat a wonderful _______ (first letter R)"]
            self.text2 = [""]


    class d2_twomind():
        def __init__(self):
            self.text1 = ["Cor Meum. Cor and Meum.\nCor assimilate with us.\nMeum assimilate with us.\nWe are one."]
            self.text2 = ["Don't you see? Nobody can discover that we are\n{u}TWO MINDS{/u}.\nNobody.\nMake sure nobody knows that answer."]




############ ROOM STRUCTURES OF DIALOGUE 3
    class Deulithoteq_hire_1():
        def __init__(self):

            self.colbX = [0, 600, 1320, -20]
            self.colbY = [450, 830, 830, -20]
            self.colbW = [1920, 100, 100, 1]
            self.colbH = [100, 370, 370, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 150, -100, 880, -100, 1720]
            self.intY = [-100, 710, -100, 80, -100, 710]
            self.intW = [1, 150, 1, 120, 1, 150]
            self.intH = [1, 220, 1, 170, 1, 220]

            self.xp = 900
            self.yp = 900

    class Deulithoteq_hire_2():
        def __init__(self):

            self.colbX = [0, 1050, -20, -20]
            self.colbY = [0, 850, -20, -20]
            self.colbW = [600, 900, 1, 1]
            self.colbH = [500, 300, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 1500, 860, -100, -100, 150]
            self.intY = [-100, 80, 500, -100, -100, 860]
            self.intW = [1, 150, 120, 1, 1, 150]
            self.intH = [1, 220, 170, 1, 1, 220]

            self.xp = 1300
            self.yp = 200

    class Deulithoteq_hire_3():
        def __init__(self):

            self.colbX = [400, -6, -6, -6]
            self.colbY = [450, -20, -20, -20]
            self.colbW = [1100, 1, 1, 1]
            self.colbH = [130, 1, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 200, 900, 1700, 860, 200]
            self.intY = [-100, 800, 80, 450, 800, 100]
            self.intW = [1, 150, 120, 120, 120, 150]
            self.intH = [1, 220, 170, 170, 170, 220]

            self.xp = 350
            self.yp = 900

    class Deulithoteq_hire_4():
        def __init__(self):

            self.colbX = [400, -6, -6, -6]
            self.colbY = [450, -20, -20, -20]
            self.colbW = [1100, 1, 1, 1]
            self.colbH = [130, 1, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 100, 900, 200, 860, 1700]
            self.intY = [-100, 800, 80, 450, 800, 100]
            self.intW = [1, 150, 120, 120, 120, 150]
            self.intH = [1, 220, 170, 170, 170, 220]

            self.xp = 300
            self.yp = 900

    class Deulithoteq_hire_5():
        def __init__(self):

            self.colbX = [400, -6, -6, -6]
            self.colbY = [450, -20, -20, -20]
            self.colbW = [1100, 1, 1, 1]
            self.colbH = [130, 1, 1, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 100, 900, -200, 860, 1700]
            self.intY = [-100, 70, 80, -200, 800, 690]
            self.intW = [1, 150, 120, 1, 120, 150]
            self.intH = [1, 220, 170, 1, 170, 220]

            self.xp = 250
            self.yp = 120

    class Deulithoteq_hire_6():
        def __init__(self):

            self.colbX = [0, 600, 1320, -20]
            self.colbY = [450, 830, 830, -20]
            self.colbW = [1920, 100, 100, 1]
            self.colbH = [100, 370, 370, 1]

            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS ANOTHER TEXT
            ##### SIXTH ITEM IS THE DOOR

            self.intX = [-100, 150, -100, 880, -100, 1720]
            self.intY = [-100, 80, -100, 80, -100, 80]
            self.intW = [1, 150, 1, 120, 1, 150]
            self.intH = [1, 220, 1, 170, 1, 220]

            self.xp = 1540
            self.yp = 100

############ TEXT TO DISPLAY for DIALOGUE 3
    class d3_hire2():
        def __init__(self):
            self.text1 = ["{u}The final answer is not hire.\nThe final answer is money.{/u}"]
            self.text2 = [""]
    class d3_hire3():
        def __init__(self):
            self.text1 = ["zanreb -> ??????"]
            self.text2 = ["436251 -> 123456"]
    class d3_hire4():
        def __init__(self):
            self.text1 = ["There's always a job to do.\nBut who says you have to do it yourself if you have money?\n You can just co______on (input FULL word for answer)\nsomeone else to do it."]
            self.text2 = ["I told you! There are clear instructions,\nI paid you to do this for me.\nI thought that people could be bought.\nGuess I wasn't paying enough."]
    class d3_hire5():
        def __init__(self):
            self.text1 = ["( Anything written in ( brackets ) is true. )\n( Anything written in {color=#4553F0}blue{/color} is true. )"]
            self.text2 = ["{color=#4553F0}If anything written in brackets is true, then...\nanything written underlined is false.{/color}"]

    class d3_power2():
        def __init__(self):
            self.text1 = ["|| The final answer is power.  ||\n{color=#4553F0}The final answer is success.{/color}"]
            self.text2 = [""]
    class d3_power3():
        def __init__(self):
            self.text1 = ["avacet -> ??????"]
            self.text2 = ["235146 -> 123456"]
    class d3_power4():
        def __init__(self):
            self.text1 = ["Finally, after years having been invisible\nI can say it was to my advantage.\nBecause in ob_____ty (input FULL word for answer)\nnobody knows you were there."]
            self.text2 = ["The shadow man was always there.\nHe seemed unimportant, inconspicuous or unknown.\nHe says words that are unclear and difficult to understand."]
    class d3_power5():
        def __init__(self):
            self.text1 = ["{color=#4553F0}Anything written in between || two lines || is false.{/color}"]
            self.text2 = ["{u}Anything written underlined is true.\nAnything written in blue is false.{/u}"]

    class d3_siphon2():
        def __init__(self):
            self.text1 = ["|| The final answer is siphon. ||\n{color=#4553F0}The final answer is not quest.{/color}"]
            self.text2 = [""]
    class d3_siphon3():
        def __init__(self):
            self.text1 = ["cichorn -> ??????"]
            self.text2 = ["7612435 -> 1234567"]
    class d3_siphon4():
        def __init__(self):
            self.text1 = ["And then it took my soul.\nI was already mutated and didn't know why.\nI wish I had a ca______is. (input FULL word for answer)"]
            self.text2 = ["The dam is closed.\nThen the gates open and you let your\nflood of emotions release.\n\nFinally, a relief from your repressed emotions."]
    class d3_siphon5():
        def __init__(self):
            self.text1 = ["{u}Anything written in between  || two lines ||  is false.{/u}"]
            self.text2 = ["{color=#4553F0}Anything written in blue is true.\nAnything written underlined is false.{/color}"]


    class d3_surveiltime():
        def __init__(self):
            self.text1 = ["You may be curious as to how I could do this?\nIt's simple.\nI don't need to be there to hear anything.\nAll I need is my power of {u}SURVEIL{/u}.\nThat's the answer."]
            self.text2 = ["I can't overhear everything, only the last couple of seconds.\nBut it's enough to tell me Tashen will be in\nLusin-scape.\nNow hurry! Before it's too late."]



# screen countdown(cd_time):
#     zorder 99
#     frame:
#         xalign 0.1
#         yalign 0.1
#         add DynamicDisplayable(countdown("fail_jumpto"), length=cd_time)
screen text_timer( **kwargs ):

    zorder 99
    # @param: kwargs
    #
    # duration = 10.0,
    # success_label = 'success_label',
    # fail_label = 'fail_label',
    # screen = 'text_timer',
    # ok_style = 'text_timer_ok',
    # near_style = 'text_timer_near',
    # style_swap = 5.0,
    # text_format = "{minutes:02d}:{seconds:02d}:{micro_seconds[0]}"

    vbox:
        xalign 0.98
        yalign 0.02
        add DynamicDisplayable(text_countdown, **kwargs)

screen keychee_mind():
    add "images/bg/keychee_bg.png"
    add SnowBlossom("test/pinkp.png", count=100, yspeed=(-40,40))
    default rrow = insightDisplayable(Keycheething())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "-- TUTORIAL --"
                text "Right now you're using your INSIGHT to be in Keychee's mind."
                text "In here, you need to solve the puzzles written in text..."
                text "...and then, using the solution, type it into an input to escape."
                text ""
                text "To close this message press Z again or press the down arrow key."

    vbox:
        xalign 0.02
        yalign 0.9
        text "Use the arrow keys"
        text "Or WASD to move"

    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "What's in hackneyed, volleyer and keyed?" style "text_insight"
                text "Whatever it is, it's the answer to input!" style "text_insight"
                text "\nNormally there'd be a timer, but this can be adjusted from the preferences menu."
                text "If you can't figure it out, use the BACKSPACE to escape and continue."



    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "Here's an input you need to do to win!"
                text "To undo, use the delete key on your keyboard."
                text "Start typing in the answer:"
                input default "" length 12
                text "To close this message press the down arrow key."



##############################################
#################### F E R N W E H   S C R E E N
##############################################

screen fernweeh_leere_1(target):
    add "images/bg/fernweh_bg.png"
    add "fog_test3"
    add "fog_test4"
    default rrow = insightDisplayable(Fernweh_leere_1_cor())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"



    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text2:
                    text "[item]" style "text_insight"

screen fernweeh_leere_2():
    add "images/bg/fernweh_bg.png"
    add "fog_test3"
    add "fog_test4"
    default rrow = insightDisplayable(Fernweh_leere_2_cor())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen fernweeh_victory():
    add "images/bg/fernweh_bg.png"
    add "fog_test3"
    add "fog_test4"
    default rrow = insightDisplayable(Fernweh_leere_2_cor())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "Place your mark here."
                text "Type anything you want:"
                input default "" length 14

##############################################
#################### C O R   M E U M   S C R E E N
##############################################

screen cormeum_time_1(target):
    add "images/bg/cormeum_bg.png"
    add "water_effect" ypos 280
    add "images/bg/cor_core_bg.png"
    default rrow = insightDisplayable(CorMeum_time_1())

    add rrow

    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"

    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text2:
                    text "[item]" style "text_insight"

screen cormeum_time_2(target):
    add "images/bg/cormeum_bg.png"
    add "water_effect" ypos 280
    add "images/bg/cor_core_bg.png"
    default rrow = insightDisplayable(CorMeum_time_2())

    add rrow

    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"

    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen cormeum_time_3():
    add "images/bg/cormeum_bg.png"
    add "water_effect" ypos 280
    add "images/bg/cor_core_bg.png"
    default rrow = insightDisplayable(CorMeum_time_3())

    add rrow

    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen cormeum_twomind(target):
    add "images/bg/cormeum_bg.png"
    add "water_effect" ypos 280
    add "images/bg/cor_core_bg.png"
    default rrow = insightDisplayable(CorMeum_twomind())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"


    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text2:
                    text "[item]" style "text_insight"

    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen cormeum_victory():
    add "images/bg/cormeum_bg.png"
    add "water_effect" ypos 280
    add "images/bg/cor_core_bg.png"
    default rrow = insightDisplayable(Fernweh_leere_2_cor())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "Place your mark here."
                text "Type anything you want:"
                input default "" length 14

##############################################
#################### D E U L I T H O T E Q   S C R E E N
##############################################

screen deulithoteq_hire_1():
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(Deulithoteq_hire_1())

    add rrow
    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0
    if "key_2" in inventory:
        add "images/test/key2.png" xalign 0.88 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"

screen deulithoteq_hire_2(target):
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(Deulithoteq_hire_2())

    add rrow
    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0
    if "key_2" in inventory:
        add "images/test/key2.png" xalign 0.88 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"

screen deulithoteq_hire_3(target):
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(Deulithoteq_hire_3())

    add rrow
    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0
    if "key_2" in inventory:
        add "images/test/key2.png" xalign 0.88 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"


    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text2:
                    text "[item]" style "text_insight"

    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen deulithoteq_hire_4(target):
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(Deulithoteq_hire_4())

    add rrow
    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0
    if "key_2" in inventory:
        add "images/test/key2.png" xalign 0.88 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"


    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text2:
                    text "[item]" style "text_insight"

    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen deulithoteq_hire_5(target):
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(Deulithoteq_hire_5())

    add rrow
    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0
    if "key_2" in inventory:
        add "images/test/key2.png" xalign 0.88 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"


    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text2:
                    text "[item]" style "text_insight"

screen deulithoteq_hire_6():
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(Deulithoteq_hire_6())

    add rrow
    if "key_1" in inventory:
        add "images/test/key1.png" xalign 1.0 yalign 1.0
    if "key_2" in inventory:
        add "images/test/key2.png" xalign 0.88 yalign 1.0

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"

    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "Be careful you only have ONE CHANCE to get this right!"
                text "When you press ENTER, that's it! That's the FINAL ANSWER."
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen deu_twomind(target):
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(CorMeum_twomind())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showtext == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text1:
                    text "[item]" style "text_insight"


    if showtext2 == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                for item in target.text2:
                    text "[item]" style "text_insight"

    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "[input_TT_1]"
                text "[input_TT_2]"
                input default "" length 12
                text "[input_TT_3]"

screen deu_victory():
    add "images/bg/deulithoteq_bg.png"
    add SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
    add SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
    default rrow = insightDisplayable(Fernweh_leere_2_cor())

    add rrow

    text _("Press the BACKSPACE key to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 45
        style "text_insight"

    if showkey == True:
        text _("Press Z to interact"):
            xpos 1240
            xanchor 0.5
            ypos 25
            size 45
            style "text_insight"


    if showinput == True:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "Place your mark here."
                text "Type anything you want:"
                input default "" length 14
