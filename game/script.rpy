# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Morgo the Destroyer of Worlds")
define FDSS = Character("squizz defecator of the deceased")

define quick_fade = Fade(0.15,0.05,0.2)


define mc = Character(window_background="gui/u_saybox.png", what_color="#626262")
define mc_s = Character("You, the silver-tongued", window_background="gui/u_saybox.png", what_color="#585656", who_color="#BEBEBE", who_font="fonts/Coves Bold.otf",what_font="fonts/Coves Bold.otf", what_size=44)
define k = Character("Keychee, the parasite", color="#f7ea82")
define f = Character("Fernweh of the Lost",color="#cce4e6")
define cm = Character("Cor Meum, where one is all", color="#bf3326")
define c = Character("Cor, one half of all", color="#ff3108")
define me = Character("Meum, one half of all", color="#6b6aac")
define d = Character("Deulithoteq, the one who hears all", color="#e6617c")
define ear = Character("Earwurm, a lackey of Deulithoteq", color="#ffffff")
define z = Character("Voices", what_font = "fonts/Brushstroke Horror.otf", what_size=52, color="#ffffff")

#define mo = Character("Conspicio Mater")


define ending = Character(
    None,
    window_background = None,
    what_size = 63,
    what_outlines = [(5, "#000", 0, 0)],
    what_font = "fonts/Coves Bold.otf",
    what_xalign =0.5,
    what_textalign=0.5)


define narr = Character(
    None,
    window_background = None,
    what_size = 55,
    what_outlines = [(5, "#000", 0, 0)],
    what_font = "fonts/Coves Bold.otf",
    what_xalign =0.5,
    what_textalign=0.5)

define mo = Character(
    None,
    window_background = None,
    what_size = 60,
    what_outlines = [(5, "#ED2F2F", 0, 0)],
    what_font = "fonts/Coves Bold.otf",
    what_xalign =0.5,
    what_textalign=0.5)


define k_narr = Character(
    None,
    window_background = None,
    what_size = 55,
    what_prefix = "Keychee: ",
    what_color = "#f7ea82",
    what_outlines = [(5, "#e62e87", 0, 0)],
    what_font = "fonts/Coves Bold.otf",
    what_xalign =0.5,
    what_textalign=0.5)

define mc_narr = Character(
    None,
    window_background = None,
    what_size = 55,
    what_prefix = "You: ",
    what_outlines = [(5, "#ED2F2F", 0, 0)],
    what_font = "fonts/Coves Bold.otf",
    what_xalign =0.5,
    what_textalign=0.5)

#define m = Character("My Melody", color="#F94FB3",ctc="ctc_heart")



### what_outlines = [(1, "#008000", 0, 0)])
## these exist too.
# first number is the size of the outline in pixels
# followed by a string giving the hex-code of the color of the outline
## and the x and y offsets

###  what_outlines = [(0, "#808080, 2, 2)])
# this can act as a drop shadow

image girl1 = "images/test/girl1_noline.png"
image girl2 = "images/test/girl2.png"
image mask = "images/test/mask1.png"
image blurtest = "images/test/blur.png"

image particle = SnowBlossom("test/particle.png", count = 200, yspeed=(-20,-80))
image around_particle  = SnowBlossom("test/particle.png", count = 200, yspeed=(-60, 60))
image on_moon_particle = SnowBlossom("test/particle.png", count= 100, yspeed=(-40,40))
image blue_p = SnowBlossom("test/bluep.png", count=100, yspeed=(-40,40))
image pink_p = SnowBlossom("test/pinkp.png", count=100, yspeed=(-40,40))
image leaf_p = SnowBlossom("test/leafp.png", count=50, yspeed=(-40,40))
image leaf_p2 = SnowBlossom("test/leafp2.png", count=50, yspeed=(-40,40))
image lily_p = SnowBlossom("test/lilyp.png", count=7, xspeed=(-20, -50), yspeed=(-30, -50))
image lily_p2 = SnowBlossom("test/lilyp2.png", count=7, xspeed=(-20, -50), yspeed=(-30, -50))

#########################################################
#########################################################
############### B A C K G R O U N D S #####################
#########################################################
#########################################################

image black = "images/bg/black.png"
image white = "images/bg/white.png"
image chasm = "images/bg/chasm.png"
image sewer = "images/bg/sewer.png"
image solas = "images/bg/solas.png"
image river = "images/bg/river.png"
image riverlong = "images/bg/riverlong.png"
image silker = "images/bg/silker2.png"
image silkerf = "images/bg/silker3f.png"
image home = "images/bg/home4.png"
image homeb = "images/bg/homeback.png"
image homef = "images/bg/homefront.png"
image mater = "images/bg/mater.png"
image cardianf = "images/bg/cardian_front.png"
image cardianb = "images/bg/cardian_back.png"

image shargoth = "images/char/shargoth.png"
image bloody_shargoth = "images/char/bloody_shargoth.png"

image blurry_chasm:
    alpha 0.0
    linear 20.5 alpha 1.0


image mock_title = "images/bg/mockup_title.png"
image mock_zoom:
    "images/bg/mockup_title.png"
    zoom 1.28
    linear 0.4 zoom 0.95
image chapter1 = "images/bg/chapter1.png"
image chapter2 = "images/bg/chapter2.png"
image chapter3 = "images/bg/chapter3.png"

image mouth_f:
    xalign 0.1
    yalign 0.5
    "images/char/mouth/f3.png"
image mouth_s:
    xalign 0.9
    yalign 0.5
    "images/char/mouth/s3.png"

image mouth_move_f:
    xalign 0.1
    yalign 0.5
    "images/char/mouth/f1.png"
    pause 0.17
    "images/char/mouth/f2.png"
    pause 0.17
    "images/char/mouth/f3.png"
    pause 0.17
    "images/char/mouth/f2.png"
    pause 0.17
    repeat

image mouth_move_s:
    xalign 0.9
    yalign 0.5
    "images/char/mouth/s1.png"
    pause 0.17
    "images/char/mouth/s2.png"
    pause 0.17
    "images/char/mouth/s3.png"
    pause 0.17
    "images/char/mouth/s2.png"
    pause 0.17
    repeat

image newspaper_bg:
    "images/bg/newspaper_1.png"
    pause 0.3
    "images/bg/newspaper_2.png"
    pause 0.3
    "images/bg/newspaper_3.png"
    pause 0.3
    repeat

image tut1 = "images/tut/1.png"
image tut2 = "images/tut/2.png"
image tut3 = "images/tut/3.png"
image tut4 = "images/tut/4.png"
image tut5 = "images/tut/5.png"
image tut6 = "images/tut/6.png"
image tut7 = "images/tut/7.png"
image tut8 = "images/tut/8.png"
image tut9 = "images/tut/9.png"
image tut10 = "images/tut/10.png"

#########################################################
#########################################################
############### C H A R A C T E R S #####################
#########################################################
#########################################################

image fernwehs = "images/char/fernweh.png"
image fernweh_tilt = "images/char/fernweh_side.png"
image f_eye_forward = "images/char/fernweh_eye_forward.png"
image f_eye_side = "images/char/fernweh_eye_side.png"
image f_eye_tilt = "images/char/fernweh_eye_tilt.png"
image f_smile = "images/char/fernweh_smile.png"
image oneblink = "images/char/fernweh_eye_one.png"

########## forward eyes
image fernweh_f_eyes:
    "images/char/fernweh_eye/f_0.png"
    pause 3.6
    "images/char/fernweh_eye/f_1.png"
    pause 0.1
    "images/char/fernweh_eye/f_2.png"
    pause 0.2
    "images/char/fernweh_eye/f_1.png"
    pause 0.1
    "images/char/fernweh_eye/f_0.png"
    pause 3.0
    repeat

########## tilt eyes
image fernweh_t_eyes:
    "images/char/fernweh_eye/t_0.png"
    pause 3.7
    "images/char/fernweh_eye/t_1.png"
    pause 0.1
    "images/char/fernweh_eye/t_2.png"
    pause 0.2
    "images/char/fernweh_eye/t_1.png"
    pause 0.1
    "images/char/fernweh_eye/t_0.png"
    pause 3.0
    repeat

########## side eyes
image fernweh_s_eyes:
    "images/char/fernweh_eye/s_0.png"
    pause 3.6
    "images/char/fernweh_eye/s_1.png"
    pause 0.1
    "images/char/fernweh_eye/s_2.png"
    pause 0.2
    "images/char/fernweh_eye/s_1.png"
    pause 0.1
    "images/char/fernweh_eye/s_0.png"
    pause 3.0
    repeat

layeredimage fernweh:
    group baselayer:
        attribute normal:
            "images/char/fernweh.png"
        attribute tilt:
            "images/char/fernweh_side.png"
        attribute turn:
            "images/char/fernweh_turn.png"
        attribute front:
            "images/char/fernweh_front.png"

    group eyeblink:
        attribute noblink:
            "images/char/cormeum/nothing.png"
        attribute frontblink:
            "fernweh_f_eyes"
        attribute tiltblink:
            "fernweh_t_eyes"
        attribute turnblink:
            "fernweh_s_eyes"
        attribute oneblink:
            "images/char/fernweh_eye_one.png"

    group mouth:
        attribute nomouth:
            "images/char/cormeum/nothing.png"
        attribute smile:
            "images/char/fernweh_smile.png"
        attribute scream:
            "images/char/fernweh_scream.png"

    group arm:
        attribute noarm:
            "images/char/cormeum/nothing.png"
        attribute up:
            "images/char/fernweh_arm_up.png"
        attribute point:
            "images/char/fernweh_arm_point.png"


image fog_test:
    "test/fog.png"
    xalign 1.0
    linear 19.5 xalign 0.0
    repeat

image fog_test2:
    "test/fog2.png"
    xalign 1.0
    linear 15.5 xalign 0.0
    repeat


image fog_test3:
    "test/fog3.png"
    xalign 1.0
    linear 19.5 xalign 0.0
    repeat

image fog_test4:
    "test/fog4.png"
    xalign 1.0
    linear 15.5 xalign 0.0
    repeat

image water_effect:
    "images/water/1.png"
    pause 0.1
    "images/water/2.png"
    pause 0.1
    "images/water/3.png"
    pause 0.1
    "images/water/4.png"
    pause 0.1
    "images/water/5.png"
    pause 0.1
    "images/water/6.png"
    pause 0.1
    "images/water/7.png"
    pause 0.1
    "images/water/8.png"
    pause 0.1
    "images/water/9.png"
    pause 0.1
    "images/water/10.png"
    pause 0.1
    repeat

image falling_test:
    "images/bg/falling.png"
    yalign 0.0
    linear 2.5 yalign 1.0
    repeat



#############################
############# C O R    M E U M
###########################
image cormeums = "images/char/cormeum.png"


layeredimage cormeum:
    group baselayer:
        attribute base:
            "images/char/cormeum/base.png"
        attribute smile:
            "images/char/cormeum/smile.png"
        attribute sad:
            "images/char/cormeum/sad.png"
        attribute closed:
            "images/char/cormeum/closed.png"

    group overeye:
        attribute n:
            "images/char/cormeum/nothing.png"
        attribute squint:
            "images/char/cormeum/squint.png"

    group eyeblink:
        attribute blink:
            "cormeum_eyes"

    group overlay:
        attribute nosplit:
            "images/char/cormeum/nothing.png"
        attribute split:
            "images/char/cormeum/split.png"
        attribute csplit:
            "images/char/cormeum/cor_split.png"
        attribute msplit:
            "images/char/cormeum/meum_split.png"

    group death:
        attribute c_dead:
            "images/char/cormeum/c_dead.png"
        attribute m_dead:
            "images/char/cormeum/m_dead.png"


        #attribute 4:
            #"images/char/cormeum/close_4.png"
        #attribute 3:
            #"images/char/cormeum/close_3.png"
        #attribute 2:
            #"images/char/cormeum/close_2.png"
        #attribute 1:
            #"images/char/cormeum/close_1.png"

image cormeum_eyes:
    "images/char/cormeum/nothing.png"
    pause 3.5
    "images/char/cormeum/close_1.png"
    pause 0.1
    "images/char/cormeum/close_2.png"
    pause 0.2
    "images/char/cormeum/close_3.png"
    pause 0.08
    "images/char/cormeum/close_4.png"
    pause 0.2
    "images/char/cormeum/close_3.png"
    pause 0.1
    "images/char/cormeum/close_2.png"
    pause 0.1
    "images/char/cormeum/close_1.png"
    pause 0.08
    "images/char/cormeum/nothing.png"
    pause 3.0
    repeat


#############################
############# D E U L I T H O T E Q
###########################
image deu = "images/char/deulithoteq.png"
image deu_smile = "images/char/deu_smile.png"
image deu_frown = "images/char/deu_frown.png"
image deu_sad = "images/char/deu_sad.png"
image deu_down = "images/char/deulithoteq_down.png"
image deu_up = "images/char/deulithoteq_up.png"
image deu_side = "images/char/deulithoteq_side.png"
image wurm1 = "images/char/wurm_1.png"
image wurm2 = "images/char/wurm_2.png"


#############################
############# K E Y C H E E
###########################

############ eyes when keychee is sitting down
image keychee_c_eyes:
    "images/char/cormeum/nothing.png"
    pause 3.5
    "images/char/keychee_eye/close_1.png"
    pause 0.1
    "images/char/keychee_eye/close_2.png"
    pause 0.2
    "images/char/keychee_eye/close_1.png"
    pause 0.1
    "images/char/cormeum/nothing.png"
    pause 2.0
    repeat

########## eyes when keychee is standing up
image keychee_u_eyes:
    "images/char/cormeum/nothing.png"
    pause 3.5
    "images/char/keychee_eye/up_1.png"
    pause 0.1
    "images/char/keychee_eye/up_2.png"
    pause 0.2
    "images/char/keychee_eye/up_1.png"
    pause 0.1
    "images/char/cormeum/nothing.png"
    pause 2.0
    repeat

image keychee_h_eyes:
    "images/char/cormeum/nothing.png"
    pause 3.5
    "images/char/keychee_eye/h_1.png"
    pause 0.1
    "images/char/keychee_eye/h_2.png"
    pause 0.2
    "images/char/keychee_eye/h_1.png"
    pause 0.1
    "images/char/cormeum/nothing.png"
    pause 2.0
    repeat

image keychees = "images/char/keychee.png"
image keychee_up = "images/char/keychee_up.png"
image keychee_hands = "images/char/keychee_hands.png"

image food_prep:
    "images/food/1_1.png"
    pause 0.1
    "images/food/1_2.png"
    pause 0.1
    "images/food/1_3.png"
    pause 0.1
    repeat

image food_ready = "images/food/2.png"

image zine_cor = "images/bg/zine_cor.png"
image zine_fer = "images/bg/zine_fernweh.png"

image stut_1 = "gui/stat/tut_1.png"
image stut_2 = "gui/stat/tut_2.png"

layeredimage keychee:
    group baselayer:
        attribute down:
            "images/char/keychee.png"
        attribute up:
            "images/char/keychee_up.png"
        attribute hands:
            "images/char/keychee_hands.png"


    group eye_sign:
        attribute nosquint:
            "images/char/cormeum/nothing.png"
        attribute downsquint:
            "images/char/keychee_eye/keychee_down_squint.png"
        attribute upsquint:
            "images/char/keychee_eye/keychee_up_squint.png"
        attribute handssquint:
            "images/char/keychee_eye/keychee_hands_squint.png"

    group eyeblink:
        attribute blinkdown:
            "keychee_c_eyes"
        attribute blinkup:
            "keychee_u_eyes"
        attribute blinkhands:
            "keychee_h_eyes"

    group mouth:
        attribute nomouth:
            "images/char/cormeum/nothing.png"
        attribute hands_smile:
            "images/char/keychee_eye/keychee_hands_smile.png"
        attribute up_closed:
            "images/char/keychee_eye/keychee_up_closed.png"

        attribute up_smile:
            "images/char/keychee_eye/keychee_up_smile.png"

        attribute down_open:
            "images/char/keychee_eye/keychee_down_open.png"

        attribute down_smirk:
            "images/char/keychee_eye/keychee_down_smirk.png"

    group juice:
        attribute juice_1:
            "images/char/keychee_eye/juice_1.png"
        attribute juice_2:
            "images/char/keychee_eye/juice_2.png"
        attribute juice_3:
            "images/char/keychee_eye/juice_3.png"





init python:
    # Use a widescreen resolution.
    config.screen_width = 1920
    config.screen_height = 1080

init:
    $ config.keymap['screenshot'].remove('s')
    $ config.keymap['accessibility'].remove('K_a')
    $ config.keymap['accessibility'].append('x')


############## remember to add 2 menus in the beginning
############ these will determine stats
############# make the beginning shorter?
################ do a strategy layout before


##########################################
#########################################
######### P A R A L L E X
###########################################

init 800 python:
    class MouseParallax(renpy.Displayable):
        def __init__(self,layer_info):
            super(renpy.Displayable,self).__init__()
            self.xoffset,self.yoffset=0.0,0.0
            self.sort_layer=sorted(layer_info,reverse=True)
            cflayer=[]
            masteryet=False
            for m,n in self.sort_layer:
                if(not masteryet)and(m<41):
                    cflayer.append("master")
                    masteryet=True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient","screens","overlay"])
            config.layers=cflayer
            config.overlay_functions.append(self.overlay)
            return
        def render(self,width,height,st,at):
            return renpy.Render(width,height)
        def parallax(self,m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(function=func)
        def overlay(self):
            ui.add(self)
            for m,n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)],n)
            return
        def event(self,ev,x,y,st):
            import pygame
            if ev.type==pygame.MOUSEMOTION:
                self.xoffset,self.yoffset=((float)(x)/(config.screen_width))-0.5,((float)(y)/(config.screen_height))-0.5
            return
    MouseParallax([(40,"farback"),(20,"back"),(-20,"front"),(-40,"inyourface"), (0,"credit"),(-40,"particle")])

    def trans(d, st, at, disp=None, m=None):
        d.xoffset, d.yoffset = int(round(m*disp.xoffset)), int(round(m*disp.yoffset))
        return 0



# show background_image onlayer farback
# show midground_image onlayer back
# show sprite1 onlayer front
# show sprite2 onlayer inyourface

# Other things to note: When using this layered method
#you must hide each layer individually to display new images. You cannot just 'wipe' the scene by putting
# Scene black
#
# you have to go
# hide background_image onlayer farback
# hide midground_image  onlayer back
# hide sprite1 onlayer front
# hide sprite2 onlayer inyourface

## REMEMBER TO PUT WHERE THEY'RE PLACED ON THE IMAGE


default emotion_hints = False
default test_text = True
default insight_timer = True
default interlocutor_state = False

default points = 2
default charisma = 0
default reputable = 0
default supreme = 0
default knowledge = 0
default intellect = 1
default perception = 0

default temp_charisma = 0
default temp_reputable = 0
default temp_supreme = 0
default temp_knowledge = 0
default temp_intellect = 0

default fernweh_outcome = "lose"
default fernweh_door = 8
default fernweh_sig = ""
default fernweh_str = ""
default cormeum_outcome = "lose"
default cormeum_door = 6
default cormeum_sig = ""
default cormeum_str = ""
default deulithoteq_outcome = "lose"
default deulithoteq_door = 5
default deulithoteq_sig = ""

default keywords = []
default fer_keywords = []
default cor_keywords = []
default deu_keywords = []
default event_track = ["twomind"]
default inventory = []

default ferQlost = False
default ferQsoul = False
default ferQmap = False
default ferQskeptic = False
default ferQmist = False
default ferQfaces = False
default ferQchasm = False
default ferQfernweh = False

default corQvena = False
default corQpain = False
default corQrapture = False
default corQcollective = False
default corQdeath = False
default corQcor = False
default corQmeum = False
default corQcormeum = False
default corQfunphare = False

default deuQsurveil = False
default deuQwurm = False
default deuQrecruit = False
default deuQcontract = False
default deuQinformation = False
default deuQsecret = False
default deuQgoal = False
default deuQmutant = False

default extra_menu = False
#default deuQmater = False
### MATER keyword?
#default deuQmutant = False
### MUTANT keyword?
#default deuQbusiness = False
### BUSINESS keyword?


init python:
    _preferences.set_volume('music', 0.9)
    renpy.music.register_channel("nature", "sfx", True)
    renpy.music.register_channel("ambient", "music", True)
    #met_fer = True
    #met_cor = True
    #met_deu = True
    met_fer = False
    met_cor = False
    met_deu = False
    #keywords = ["chasm","lost","soul","rapture","pain","vena cava","earwurm","surveil"]
    #fer_keywords = ["chasm","lost","soul"]
    #cor_keywords = ["rapture","pain","vena cava"]
    #deu_keywords = ["earwurm","surveil"]
    #keywords = []
    #fer_keywords = []
    #cor_keywords = []
    #deu_keywords = []
    #event_track = []
    #inventory = []

image flower_far = "images/bg/flowers_farback.png"
image flower_back = "images/bg/flowers_back.png"
image flower_front = "images/bg/flower_monster_in_front.png"
image flower_face = "images/bg/flowers_inyourface.png"

image gris_far = "images/bg/gris_farback.png"
image gris_back = "images/bg/gris_back.png"
image gris_front = "images/bg/gris_front.png"

image fool_back = "images/bg/fool_back.png"
image fool_front = "images/bg/fool_front.png"

image sun_back = "images/bg/sun_back.png"
image sun_front = "images/bg/sun_front.png"

image who_back = "images/bg/who_back.png"
image who_front = "images/bg/who_front.png"

image credits1 = "images/bg/credits_1.png"
image credits2:
    "images/bg/credits_2_3.png"
    pause 0.3
    "images/bg/credits_2_1.png"
    pause 0.3
    "images/bg/credits_2_2.png"
    pause 0.3
    repeat
image credits3 = "images/bg/credits_3.png"
image credits4 = "images/bg/credits_4.png"
image credits5 = "images/bg/credits_5.png"
image credits6:
    "images/bg/credits_6_1.png"
    pause 1.5
    "images/bg/credits_6_2.png"
    pause 0.1
    "images/bg/credits_6_3.png"
    pause 0.2
    "images/bg/credits_6_2.png"
    pause 0.1
    "images/bg/credits_6_1.png"
    pause 1.0
    repeat
image credits7 = "images/bg/credits_7.png"

image banner_back = "images/bg/banner_back.png"
image banner_front:
    "images/bg/banner_front.png"
    xpos 0
    linear 0.6 xpos 800
image hand = "images/bg/hand.png"
image hand_zoom:
    "images/bg/hand.png"
    alpha 0.1 zoom 0.7
    linear 1.0 alpha 1.0 zoom 1.0

########################################
######################################
label start:
    stop music fadeout 2.0
    scene black

    #jump escapefailure_d2

    jump the_start


    #jump chapter2
    #jump itch_banner
    #jump start_d2


    ### CGS here
    #jump escapefailure_d2
    #jump end_rule
    #jump end_gris
    #jump end_fool
    #jump end_rabbit
    #jump end_achilles

    #jump d2_win
    #jump chapter3
    #jump phase6_d2_nascent
    #jump phase6_d2_time
    #jump phase3_afterinsight_d2
    #jump itch_thumb
    #jump promo_insight
    #jump phase5_d1_Leere
    #jump phase6_d3_lackey_d5
    #jump phase6_d3_S2_d5
    #jump phase2_d3
    #jump phase6_d2_cerebrum



label itch_banner:
    $ quick_menu = False
    window hide
    pause 1.0
    show flower_far onlayer farback with dissolve
    show flower_back onlayer back with dissolve
    show lily_p onlayer back
    show lily_p2 onlayer back
    show mock_title onlayer front with dissolve
    show around_particle onlayer back
    show lily_p onlayer inyourface
    show lily_p2 onlayer inyourface


    call screen flowers() with dissolve

label itch_thumb:
    $ quick_menu = False
    window hide
    pause 1.0
    show flower_far onlayer farback with dissolve
    show flower_back onlayer back with dissolve
    show lily_p onlayer back with dissolve
    show lily_p2 onlayer back with dissolve
    show flower_front onlayer front with dissolve
    show around_particle onlayer back with dissolve
    show flower_face onlayer inyourface with dissolve
    show lily_p onlayer inyourface with dissolve
    show lily_p2 onlayer inyourface with dissolve


    call screen flowers() with dissolve

label promo_insight:
    window hide
    $ quick_menu = False

    call screen fernweeh_leere_2() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump promo_2

    elif search == "backspace":
        window show
        "Despite all the searching, you couldn't find the answer..."

label promo_2:
    window hide
    $ quick_menu = False

    call screen cormeum_time_3() with quick_fade
    #$rrow.xp = 900
    #$rrow.yp = 1000

    $ quick_menu = True

    $ search = _return
    $ search = search.lower()

    if search == "room":
        jump promo_3

    elif search == "backspace":
        window show
        if insight_timer:
            hide screen text_timer
        "Despite all the searching, you couldn't find the answer..."
    else:
        $showinput = False
        "Incorrect answer."
        jump promo_3

label promo_3:
    window hide
    $ quick_menu = False

    call screen deulithoteq_hire_2(d3_hire4()) with quick_fade
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
        "You got the second key."
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
    return

label test:
    show blur onlayer back with fade

    show girl1 onlayer front with dissolve
    #show mask onlayer inyourface with dissolve
    show blue_p onlayer inyourface with dissolve
    e "You've created a new Ren'Py game."
    #$ failstate = True
    #show screen text_timer
    show screen text_timer(duration=22.0, text_format = "{minutes:02d}:{seconds:02d}", fail_label="fail_label2" )
    e "JFSDLKJLFSD"
    e "JFSDLKJLFSD"
    e "JFSDLKJLFSD"
    hide screen text_timer
    e "Ok you should be safe"
    call screen keyword_inv
    e "Ok you should be safe"
    e "Ok you should be safe"
    e "Ok you should be safe"

    call screen stat_screen


    python:
        prompt = renpy.input("Type your prompt word here:", length=32)
        prompt = prompt.strip()

    if "chasm" in prompt:
        mc_s "So... about the chasm."
    else:
        mc "I say nothing substantial."

    mc_s "Look I'm saying something."

    hide girl1 onlayer front with dissolve
    show girl2 onlayer front with dissolve
    if perception > 1:

        e "So I was playing {a=jump:p1}a game{/a} on my nintendo Switch."
    else:
        e "So I was playing a game on my nintendo switch."

    hide girl2 onlayer front with dissolve
    mc "Ok"
    jump demo_minigame

label p1:
    mc_s "What game were you playing?"
    e "Super mario bros 2."
    mc "Ok"
    jump demo_minigame


label success_label:
    "Success"
    return

label fail_label:
    "Too slow"
    return

label fail_label2:
    "this is a new fail label LOL"
    return
