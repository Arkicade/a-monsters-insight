
init python:
    showkey = False
    showtext = False
    showtext2 = False
    showinput = False

init python:
    class moveDisplayable(renpy.Displayable):

        import pygame

        def __init__(self):

            renpy.Displayable.__init__(self)

            self.SPR = renpy.load_image("images/test/arrow_up.png")
            self.spriteUp    = renpy.load_image("images/test/arrow_up.png")
            self.spriteDown  = renpy.load_image("images/test/arrow_down.png")
            self.spriteLeft  = renpy.load_image("images/test/arrow_left.png")
            self.spriteRight = renpy.load_image("images/test/arrow_right.png")

            self.oldkey = renpy.load_image("images/test/oldkey.png")
            self.olddoor = renpy.load_image("images/test/olddoor.png")
            self.oldint = renpy.load_image("images/test/oldint.png")
            self.oldinp = renpy.load_image("images/test/oldinp.png")

            self.colbox = renpy.load_image("images/test/colbox.png")

            self.winner = None

            self.move_left = False
            self.move_right = False
            self.move_up = False
            self.move_down = False
            self.collided = False

            self.xp = 900
            self.yp = 900

            ### displayables


            self.colbX = [600, 900, -1000, -1000]
            self.colbY = [200, 700, -1000, -1000]
            self.colbW = [400, 300, 1, 1]
            self.colbH = [400, 300, 1, 1]


            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT

            self.intX = [200,10, -1000, -1000]
            self.intY = [900,500, -1000, -1000]
            self.intW = [120,150, 1, 1]
            self.intH = [120,220, 1, 1]


            self.interact_time = True
            self.interact_type = 0

            self.box1 = Solid("#000000", xsize=self.colbW[0], ysize=self.colbH[0])
            self.box2 = Solid("#000000", xsize=self.colbW[1], ysize=self.colbH[1])
            self.box3 = Solid("#000000", xsize=self.colbW[2], ysize=self.colbH[2])
            self.box4 = Solid("#000000", xsize=self.colbW[3], ysize=self.colbH[3])

            #self.colbox = rect("#ffffff", xsize=100,ysize=100)

            #rend = renpy.Render(width, height)
            #ca = rend.canvas()

            #surfacee = renpy.load_surface("images/test/arrow_up.png")
            # The sizes of some of the images.
            #self.PADDLE_WIDTH = 12
        #def visit(self):
            #return [self.SPR, self.xp, self.yp]
            #return [ self.paddle, self.ball ]

        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)


            # Draw the arrow.
            #arrow = renpy.render(self.SPR, width, height, st, at)
            ## because the image IS A RENDER we can place it straight in

            r.blit(self.colbox, (self.xp,self.yp))

            ## drawing the wallS
            block1 = renpy.render(self.box1, width, height, st, at)
            r.blit(block1, (self.colbX[0], self.colbY[0]))

            block2 = renpy.render(self.box2, width, height, st, at)
            r.blit(block2, (self.colbX[1], self.colbY[1]))

            block3 = renpy.render(self.box3, width, height, st, at)
            r.blit(block3, (self.colbX[2], self.colbY[2]))

            block4 = renpy.render(self.box4, width, height, st, at)
            r.blit(block4, (self.colbX[2], self.colbY[2]))

            r.blit(self.oldkey, (self.intX[0], self.intY[0]))

            r.blit(self.olddoor, (self.intX[1], self.intY[1]))

            r.blit(self.oldint, (self.intX[2], self.intY[2]))

            r.blit(self.oldinp, (self.intX[3], self.intY[3]))

            r.blit(self.SPR, (self.xp,self.yp))

            #ca.rect("#ffffff", [self.xp,self.yp,100,100], 2)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.

        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.

            if ev.type == pygame.KEYUP:
                self.move_right = False
                self.move_left = False
                self.move_up = False
                self.move_down = False

            if ev.type == pygame.KEYDOWN: # if any keys are pressed

               if renpy.map_event(ev, 'K_a') or renpy.map_event(ev, 'K_LEFT') and showtext == False and showinput == False: # if key a
                   self.SPR = self.spriteLeft
                   self.move_left = True

                   ## YOU DEFINE A GLOBAL VARIABLE LIKE THIS!!!!!
                   #globals() ['showkey'] = True


               elif renpy.map_event(ev, 'K_d') or renpy.map_event(ev, 'K_RIGHT') and showtext == False and showinput == False: # if key a
                   self.SPR = self.spriteRight
                   self.move_right = True
                   #self.xp += 5

               elif renpy.map_event(ev, 'K_w') or renpy.map_event(ev, 'K_UP') and showtext == False and showinput == False: # if key a
                   self.SPR = self.spriteUp
                   self.move_up = True
                   #self.yp += -5

               elif renpy.map_event(ev, 'K_s') or renpy.map_event(ev, 'K_DOWN') and showtext == False and showinput == False: # if key a
                   self.SPR = self.spriteDown
                   self.move_down = True
                   #self.yp += 5

               elif renpy.map_event(ev, 'K_DOWN') and (showinput or showtext):
                   if showinput:
                       globals() ['showinput'] = not showinput
                   elif showtext:
                       globals() ['showtext'] = not showtext


               elif renpy.map_event(ev, 'K_z') and self.interact_time == False:
                   renpy.timeout(0)
                   if self.interact_type == 0:
                       self.winner = "you"


                   elif self.interact_type == 1:
                       self.winner = "room"

                   elif self.interact_type == 2:
                       globals() ['showtext'] = not showtext

                   elif self.interact_type == 3:
                       globals() ['showinput'] = not showinput

               elif renpy.map_event(ev, 'K_BACKSPACE'): # if key a
                    #self.SPR = self.spriteDown
                    self.winner = "backspace"
                    self.interact_time = False
                    globals() ['showtext'] = False
                    globals() ['showinput'] = False


                    #self.SPR = self.spriteDown
                    renpy.timeout(0)

               elif renpy.map_event(ev, 'K_RETURN'): # if key a
                    #self.SPR = self.spriteDown
                    #self.winner = "eileen"
                    self.interact_time = False
                    globals() ['showtext'] = False
                    globals() ['showinput'] = False
                    renpy.timeout(0)



                #elif renpy.map_event(ev, 'K_z') and self.interact_time == False:
                    #self.winner = "you"
                    #renpy.timeout(0)




            def checkcol(COLX, COLY, COLW, COLH, _x, _y, direction, IT):
                x1 = _x + 5 ## the +10 is for extra padding
                y1 = _y + 5
                x2 = _x + 95 # change 100 depending on how big the sprite
                y2 = _y + 95
                canpass = True
                #xb = 0
                #IT = 1

                if direction == "left":
                    for xb in range(len(COLX)):
                        if x1 < (COLX[xb]+COLW[xb]) and y2 > COLY[xb] and y1 < (COLY[xb] +COLH[xb]) and x2 > (COLX[xb]+COLW[xb]):
                            canpass = False
                            IT = xb

                elif direction == "right":
                    for xb in range(len(COLX)):
                        if x2 > COLX[xb] and y2 > COLY[xb] and y1 < (COLY[xb] +COLH[xb]) and x1 < COLX[xb]:
                            canpass = False
                            IT = xb

                elif direction == "up":
                    for xb in range(len(COLX)):
                        if ( (x1 > COLX[xb] and x2 < (COLX[xb] + COLW[xb])) or ( x1 < (COLX[xb]+COLW[xb]) and x2 > (COLX[xb]+COLW[xb]) ) or (x2 > COLX[xb] and x1 < COLX[xb])) and y1 < (COLY[xb] +COLH[xb]) and y2 > (COLY[xb] +COLH[xb]):
                            canpass = False
                            IT = xb

                elif direction == "down":
                    for xb in range(len(COLX)):
                        if ( (x1 > COLX[xb] and x2 < (COLX[xb] + COLW[xb])) or ( x1 < (COLX[xb]+COLW[xb]) and x2 > (COLX[xb]+COLW[xb]) ) or (x2 > COLX[xb] and x1 < COLX[xb])) and y2 > COLY[xb] and y1 < COLY[xb]:
                            canpass = False
                            IT = xb

                return canpass,IT

            nb = 0
            if self.move_right:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "right", self.interact_type)
                no_collision,nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "right", nb)
                if no_collision and self.interact_time:
                    self.xp += 7
                    if self.xp > 1800:
                        self.xp = 1800


            elif self.move_left:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "left", self.interact_type)
                no_collision, nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "left", nb)
                if no_collision and self.interact_time:
                    self.xp += -7
                    if self.xp < 0:
                        self.xp = 0

            elif self.move_up:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "up", self.interact_type)
                no_collision,nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "up", nb)
                if no_collision and self.interact_time:
                    self.yp += -7
                    if self.yp < 0:
                        self.yp = 0

            elif self.move_down:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "down", self.interact_type)
                no_collision,nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "down", nb)
                if no_collision and self.interact_time:
                    self.yp += 7
                    if self.yp > 1000:
                        self.yp = 1000


            if self.interact_time == False:
                globals() ['showkey'] = True

            else:
                globals() ['showkey'] = False


            renpy.restart_interaction()


            if self.winner:
                return self.winner

            #return global showkey


    class insightDisplayable(renpy.Displayable):

        import pygame

        def __init__(self, child):

            renpy.Displayable.__init__(self)

            self.SPR = renpy.load_image("images/test/arrow_up_new2.png")
            self.spriteUp    = renpy.load_image("images/test/arrow_up_new2.png")
            self.spriteDown  = renpy.load_image("images/test/arrow_down_new.png")
            self.spriteLeft  = renpy.load_image("images/test/arrow_left_new.png")
            self.spriteRight = renpy.load_image("images/test/arrow_right_new.png")

            self.child = child

            self.oldkey = renpy.load_image("images/test/oldkey.png")
            self.olddoor = renpy.load_image("images/test/newdoor.png")
            self.oldint = renpy.load_image("images/test/newint.png")
            self.oldinp = renpy.load_image("images/test/newinp.png")

            self.colbox = renpy.load_image("images/test/colbox.png")

            self.winner = None

            self.move_left = False
            self.move_right = False
            self.move_up = False
            self.move_down = False
            self.collided = False

            self.xp = child.xp
            self.yp = child.yp

            ### displayables

            self.colbX = [child.colbX[0], child.colbX[1], child.colbX[2], child.colbX[3]]
            self.colbY = [child.colbY[0], child.colbY[1], child.colbY[2], child.colbY[3]]
            self.colbW = [child.colbW[0], child.colbW[1], child.colbW[2], child.colbW[3]]
            self.colbH = [child.colbH[0], child.colbH[1], child.colbH[2], child.colbH[3]]


            ##### FIRST ITEM IS THE KEY!!!
            ##### SECOND ITEM IS THE DOOR
            #### THIRD IITEM IS THE TEXT
            ##### FOURTH ITEM IS INPUT
            ##### FIFTH ITEM IS FOR SECOND TEXT
            self.intX = [child.intX[0], child.intX[1], child.intX[2], child.intX[3], child.intX[4], child.intX[5]]
            self.intY = [child.intY[0], child.intY[1], child.intY[2], child.intY[3], child.intY[4], child.intY[5]]
            self.intW = [child.intW[0], child.intW[1], child.intW[2], child.intW[3], child.intW[4], child.intW[5]]
            self.intH = [child.intH[0], child.intH[1], child.intH[2], child.intH[3], child.intH[4], child.intH[5]]


            self.interact_time = True
            self.interact_type = 0

            self.box1 = Solid("#000000", xsize=self.colbW[0], ysize=self.colbH[0])
            self.box2 = Solid("#000000", xsize=self.colbW[1], ysize=self.colbH[1])
            self.box3 = Solid("#000000", xsize=self.colbW[2], ysize=self.colbH[2])
            self.box4 = Solid("#000000", xsize=self.colbW[3], ysize=self.colbH[3])

            #self.colbox = rect("#ffffff", xsize=100,ysize=100)

            #rend = renpy.Render(width, height)
            #ca = rend.canvas()

            #surfacee = renpy.load_surface("images/test/arrow_up.png")
            # The sizes of some of the images.
            #self.PADDLE_WIDTH = 12
        #def visit(self):
            #return [self.SPR, self.xp, self.yp]
            #return [ self.paddle, self.ball ]

        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)


            # Draw the arrow.
            #arrow = renpy.render(self.SPR, width, height, st, at)
            ## because the image IS A RENDER we can place it straight in

            r.blit(self.colbox, (self.xp,self.yp))

            ## drawing the wallS
            block1 = renpy.render(self.box1, width, height, st, at)
            r.blit(block1, (self.colbX[0], self.colbY[0]))

            block2 = renpy.render(self.box2, width, height, st, at)
            r.blit(block2, (self.colbX[1], self.colbY[1]))

            block3 = renpy.render(self.box3, width, height, st, at)
            r.blit(block3, (self.colbX[2], self.colbY[2]))

            block4 = renpy.render(self.box4, width, height, st, at)
            r.blit(block4, (self.colbX[3], self.colbY[3]))

            r.blit(self.oldkey, (self.intX[0], self.intY[0]))

            r.blit(self.olddoor, (self.intX[1], self.intY[1]))

            r.blit(self.olddoor, (self.intX[5], self.intY[5]))

            r.blit(self.oldint, (self.intX[2], self.intY[2]))

            r.blit(self.oldint, (self.intX[4], self.intY[4]))

            r.blit(self.oldinp, (self.intX[3], self.intY[3]))

            r.blit(self.SPR, (self.xp,self.yp))

            #ca.rect("#ffffff", [self.xp,self.yp,100,100], 2)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.

        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.

            if ev.type == pygame.KEYUP:
                self.move_right = False
                self.move_left = False
                self.move_up = False
                self.move_down = False

            if ev.type == pygame.KEYDOWN: # if any keys are pressed

               if renpy.map_event(ev, 'K_a') or renpy.map_event(ev, 'K_LEFT') and showtext == False and showinput == False and showtext2 == False: # if key a
                   self.SPR = self.spriteLeft
                   self.move_left = True

                   ## YOU DEFINE A GLOBAL VARIABLE LIKE THIS!!!!!
                   #globals() ['showkey'] = True

               elif renpy.map_event(ev, 'K_d') or renpy.map_event(ev, 'K_RIGHT') and showtext == False and showinput == False and showtext2 == False: # if key a
                   self.SPR = self.spriteRight
                   self.move_right = True
                   #self.xp += 5

               elif renpy.map_event(ev, 'K_w') or renpy.map_event(ev, 'K_UP') and showtext == False and showinput == False and showtext2 == False: # if key a
                   self.SPR = self.spriteUp
                   self.move_up = True
                   #self.yp += -5

               elif renpy.map_event(ev, 'K_s') or renpy.map_event(ev, 'K_DOWN') and showtext == False and showinput == False and showtext2 == False: # if key a
                   self.SPR = self.spriteDown
                   self.move_down = True
                   #self.yp += 5

               elif renpy.map_event(ev, 'K_DOWN') and (showinput or showtext or showtext2):
                   if showinput:
                       globals() ['showinput'] = not showinput
                   elif showtext:
                       globals() ['showtext'] = not showtext
                   elif showtext2:
                        globals() ['showtext2'] = False

               elif renpy.map_event(ev, 'K_z') and self.interact_time == False:
                   renpy.timeout(0)

                   ############### interact time!!

                   #### KEY
                   if self.interact_type == 0:
                       self.winner = "you"

                   elif self.interact_type == 1:
                       self.winner = "room"

                   elif self.interact_type == 2:
                       globals() ['showtext'] = not showtext

                   elif self.interact_type == 5:
                       self.winner = "room2"

                   elif self.interact_type == 4:
                        globals() ['showtext2'] = not showtext2

                   elif self.interact_type == 3:
                       globals() ['showinput'] = not showinput

               elif renpy.map_event(ev, 'K_BACKSPACE'): # if key a
                    #self.SPR = self.spriteDown
                    self.winner = "backspace"
                    self.interact_time = False
                    globals() ['showtext'] = False
                    globals() ['showinput'] = False
                    
                    #self.SPR = self.spriteDown
                    renpy.timeout(0)

               elif renpy.map_event(ev, 'K_RETURN'): # if key a
                    #self.SPR = self.spriteDown
                    #self.winner = "eileen"
                    self.interact_time = False
                    globals() ['showtext'] = False
                    globals() ['showinput'] = False
                    renpy.timeout(0)

                #elif renpy.map_event(ev, 'K_z') and self.interact_time == False:
                    #self.winner = "you"
                    #renpy.timeout(0)

            def checkcol(COLX, COLY, COLW, COLH, _x, _y, direction, IT):
                x1 = _x + 5 ## the +10 is for extra padding
                y1 = _y + 5
                x2 = _x + 95 # change 100 depending on how big the sprite
                y2 = _y + 95
                canpass = True
                #xb = 0
                #IT = 1

                if direction == "left":
                    for xb in range(len(COLX)):
                        if x1 < (COLX[xb]+COLW[xb]) and y2 > COLY[xb] and y1 < (COLY[xb] +COLH[xb]) and x2 > (COLX[xb]+COLW[xb]):
                            canpass = False
                            IT = xb

                elif direction == "right":
                    for xb in range(len(COLX)):
                        if x2 > COLX[xb] and y2 > COLY[xb] and y1 < (COLY[xb] +COLH[xb]) and x1 < COLX[xb]:
                            canpass = False
                            IT = xb

                elif direction == "up":
                    for xb in range(len(COLX)):
                        if ( (x1 > COLX[xb] and x2 < (COLX[xb] + COLW[xb])) or ( x1 < (COLX[xb]+COLW[xb]) and x2 > (COLX[xb]+COLW[xb]) ) or (x2 > COLX[xb] and x1 < COLX[xb])) and y1 < (COLY[xb] +COLH[xb]) and y2 > (COLY[xb] +COLH[xb]):
                            canpass = False
                            IT = xb

                elif direction == "down":
                    for xb in range(len(COLX)):
                        if ( (x1 > COLX[xb] and x2 < (COLX[xb] + COLW[xb])) or ( x1 < (COLX[xb]+COLW[xb]) and x2 > (COLX[xb]+COLW[xb]) ) or (x2 > COLX[xb] and x1 < COLX[xb])) and y2 > COLY[xb] and y1 < COLY[xb]:
                            canpass = False
                            IT = xb

                return canpass,IT

            nb = 0
            if self.move_right:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "right", self.interact_type)
                no_collision,nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "right", nb)
                if no_collision and self.interact_time:
                    self.xp += 8
                    if self.xp > 1800:
                        self.xp = 1800


            elif self.move_left:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "left", self.interact_type)
                no_collision, nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "left", nb)
                if no_collision and self.interact_time:
                    self.xp += -8
                    if self.xp < 0:
                        self.xp = 0

            elif self.move_up:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "up", self.interact_type)
                no_collision,nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "up", nb)
                if no_collision and self.interact_time:
                    self.yp += -8
                    if self.yp < 0:
                        self.yp = 0

            elif self.move_down:
                self.interact_time, self.interact_type = checkcol(self.intX, self.intY, self.intW, self.intH, self.xp, self.yp, "down", self.interact_type)
                no_collision,nb = checkcol(self.colbX, self.colbY, self.colbW, self.colbH, self.xp, self.yp, "down", nb)
                if no_collision and self.interact_time:
                    self.yp += 8
                    if self.yp > 1000:
                        self.yp = 1000

            if self.interact_time == False:
                globals() ['showkey'] = True

            else:
                globals() ['showkey'] = False
                
            renpy.restart_interaction()

            if self.winner:
                return self.winner
            #return global showkey

screen arrowtest():
    default rrow = moveDisplayable()

    #$ rrow.colbX = [900, 1400]

    #add "bg pong field"

    add rrow

    text _("Press the BACKSPACE to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 40

    if showkey == True:
        text _("Press the Z to interact"):
            xpos 1140
            xanchor 0.5
            ypos 25
            size 40

screen arrowtwo():

    default rrow = moveDisplayable()

    $ rrow.colbX = [100, -1000, -1000, -1000]
    #$ rrow.colbW = [100, -1]
    $ rrow.intX = [-100, 1700, 300, 600]
    $ rrow.intY = [-100, 500, 800, 200]
    $ rrow.intW = [1, 150, 120, 120]
    $ rrow.intH = [1, 220, 170, 170]

    add rrow

    text _("Press the BACKSPACE to exit"):
        xpos 540
        xanchor 0.5
        ypos 25
        size 40
        
    if showkey:
        text _("Press the Z to interact"):
            xpos 1140
            xanchor 0.5
            ypos 25
            size 40

    if showtext:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "Hi there! Here's some text."
                text "To close this message press Z again or press the down arrow key."

    if showinput:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 0.07
            ypadding 0.07

            vbox:
                #xpadding 100
                #ypadding 100
                text "Here's an input you need to do."
                input default "Type Here" length 12
                text "To close this message press the down arrow key."

label demo_minigame:
    e "That makes it possible to create all kinds of minigames. Would you like to play some pong?"
    $ import time
    $ start = time.time()
    jump play_newroom

label play_newroom:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False

    call screen arrowtwo with fade

    $ quick_menu = True
    if _return == "eileen":
        window show
        e "I win!"
    elif _return == "room":
        window hide
        jump play_newroom
    else:
        $ name = _return
        window show
        e "You just put in [name] correct?"
    jump play_done

label play_done:
    menu:
        e "Would you like to play again?"
        "Sure.":
            jump play_newroom
        "No thanks.":
            pass
    return
