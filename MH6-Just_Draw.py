#Setup code for pygame programs

from pygame import *
from math import *

from tkinter import *
from tkinter import filedialog
base = Tk()
base.withdraw()

width,height=800,600
screen=display.set_mode((width,height))

RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)


mx,my = 0,0
omx,omy = 0,0

sx,sy = 0,0
rx,ry = 0,0



mouse.set_visible(False)
drawing = False

ele = image.load("elephant_white.png").convert()
brushTip = image.load("brush.png")
eraseTip = image.load("eraser.png")
cpTip = image.load("dropper.png")


th = 5
col = BLACK
tool = "brush"
drawTip = brushTip
temp = ele


screen.fill(WHITE)
ele.set_alpha(128)
screen.blit(ele,(0,0))
screenshot = screen.copy()
imgX,imgY = 0,0

zoom = True

running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

        if evt.type == MOUSEBUTTONDOWN:

            if evt.button == 1:
                sx,sy = evt.pos
                if tool == "cpicker":
                    col = screen.get_at((sx,sy))

            if evt.button == 2:
                if tool != "cpicker":
                    tool = "cpicker"
                elif tool == "cpicker":
                    tool = "brush"

            if evt.button == 3:
                if tool != "eraser":
                    tool = "eraser"
                elif tool == "eraser":
                    tool = "brush"

            if evt.button == 4:
                if th < 100:
                    th += 1

            if evt.button == 5:
                if th > 1:
                    th -= 1

        
        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                rx,ry = evt.pos

        
        if evt.type == KEYDOWN:        
            """
            if evt.key == K_Z:
                zx,zy = mx,my
                if zx-100 > 0 and zy-75 > 0:
                    imgX = zx-100
                    imgY = zy-75
                    zoomRect = Rect(imgX,imgY,200,150)
            """
            if evt.key == K_l:
                filename = filedialog.askopenfilename()
                try:
                    temp = image.load(filename).convert()
                    temp.set_alpha(128)
                    screen.fill(WHITE)
                    screen.blit(temp,(0,0))
                    screenshot = screen.copy()
                except:
                    print("Could not load the image")
            
            if evt.key == K_r:
                screen.fill(WHITE)
                screen.blit(temp,(0,0))
                screenshot = screen.copy()
            
    
    screen.fill(WHITE)
    screen.blit(screenshot,(0,0))

   
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()


    if tool == "brush":
        drawTip = brushTip
    elif tool == "eraser":
        drawTip = eraseTip
    elif tool == "cpicker":
        drawTip = cpTip

    if mb[0] == 1:
        drawing = True

        if tool == "brush":
            draw.circle(screen,col,(mx,my),th)
            dx=mx-omx
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist):
                   cx=int(omx+i*dx/dist)
                   cy=int(omy+i*dy/dist)
                   draw.circle(screen,col,(cx,cy),th)
            screenshot = screen.copy()

        elif tool == "eraser":
            draw.circle(screen,WHITE,(mx,my),th)
            dx=mx-omx
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist):
                   cx=int(omx+i*dx/dist)
                   cy=int(omy+i*dy/dist)
                   draw.circle(screen,WHITE,(cx,cy),th)
            screenshot = screen.copy()
    
    else:
        drawing = False


    if not drawing:
        screen.blit(drawTip,(mx-10,my-(drawTip.get_height()-10)))
      

    display.flip()

    omx,omy = mx,my
            
quit()
