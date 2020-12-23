import module as m
import pygame 
import os


pygame.init()

clock = pygame.time.Clock()
#fps

heightWin = 448
widthWin = 1366  
sizeWin = (1366, 448)
# велечина окна

win = pygame.display.set_mode(sizeWin)
pygame.display.set_caption('its me MARIO!!!')



x = 100
y = 365
xbg = 0
xMin, xMax, yMin, yMax = 670, 700, 275, 235 
# изначальные кординаты 

heightS, widthS = 37, 37
heightB, widthB = 66, 33
heightBD, widthBD = 47, 34
#высота, шырина
speed = 7.0

isjump = False
jumpCount, downCount = 10.5, 7.5

# параметры прыжка

file_path = os.path.dirname(__file__)

pygame.mixer.music.load((file_path + "\saundtrek.mp3"))
pygame.mixer.music.set_volume(0.1)

a = 0
run_plus = True

pleyer = pygame.Surface((37, 37))

sprite_path = os.path.join(file_path, "sprite/bg.png")  
bg = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Lmario-stand-r.png")
pleyerSRS = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Lmario-stand-l.png")
pleyerSLS = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Lmario-jump-r.png")
pleyerJRS = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Lmario-jump-l.png")
pleyerJLS = pygame.image.load(sprite_path)

sprite_path = os.path.join(file_path, "sprite/Bmario-stand-r.png")
pleyer1 = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Bmario-stand-l.png")
pleyerSLB = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Bmario-jump-r.png")
pleyerJRB = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Bmario-jump-l.png")
pleyerJLB = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Bmario-Down-r.png")
pleyerDRB = pygame.image.load(sprite_path)
sprite_path = os.path.join(file_path, "sprite/Bmario-Down-l.png")
pleyerDLB = pygame.image.load(sprite_path)


#bg = pygame.image.load("D:/GAME_MARIO/bg.png")
#pleyerSRS = pygame.image.load("D:/GAME_MARIO/sprits/statusS/Lmario-stand-r-2.png")
#pleyerSLS = pygame.image.load("D:/GAME_MARIO/sprits/statusS/Lmario-stand-l-2.png")
#pleyerJRS = pygame.image.load("D:/GAME_MARIO/sprits/statusS/Lmario-jump-r-2.png")
#pleyerJLS = pygame.image.load("D:/GAME_MARIO/sprits/statusS/Lmario-jump-l-2.png")
#pleyerSLB = pygame.image.load("D:\GAME_MARIO/sprits/statusB/Bmario-stand-l-2.png")
#pleyerSRB = pygame.image.load("D:\GAME_MARIO/sprits/statusB/Bmario-stand-r-2.png")
#pleyerJLB = pygame.image.load("D:\GAME_MARIO/sprits/statusB/Bmario-jump-l-2.png")
#pleyerJRB = pygame.image.load("D:\GAME_MARIO/sprits/statusB/Bmario-jump-r-2.png")
#pleyerDLB = pygame.image.load("D:\GAME_MARIO/sprits/statusB/Bmario-Down-l.png")
#pleyerDRB = pygame.image.load("D:\GAME_MARIO/sprits/statusB/Bmario-Down-r.png")
# объявляем изображения

class colaider ():
    xMin = 0
    xMax = 0
    yMin = 0
    yMax = 0




statusSp = 2  
statusB, statusD, Winner, p, DownUp, Chets = False, False, False, False, False, False
score = 0
time = 24000

trumpet1 = colaider()
trumpet1.xMin = 865
trumpet1.xMax = 960
trumpet1.yMax = 290
trumpet1.yMin = 365

trumpet2 = colaider()
trumpet2.xMin = 1190
trumpet2.xMax = 1275
trumpet2.yMax = 265
trumpet2.yMin = 365

trumpet3 = colaider()
trumpet3.xMin = 1448
trumpet3.xMax = 1535
trumpet3.yMax = 235
trumpet3.yMin = 365

trumpet4 = colaider()
trumpet4.xMin = 1800
trumpet4.xMax = 1885
trumpet4.yMax = 235
trumpet4.yMin = 365

#keys = pygame.key.get_pressed() 
# зажатие или нажатия клавиш

xMin, xMax, yMin, yMax = 670, 700, 275, 235

grib = m.gribchek(xMin, xMax, yMin, yMax, x, y, statusB, score)
def gribchek(xMin, xMax, yMin, yMax, x, y, statusB, score):
    if x >= xMin and x <= xMax and y <= yMin and y >= yMax:
        statusB = True
        score += 100

run = True

pygame.mixer.music.play(-1)

while run:
    clock.tick(60)
#fps
    keys = pygame.key.get_pressed() 
# зажатие или нажатия клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# условия закрытия игры

    time -= 1

    statusD = False

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        statusD = True 
# условие для преседания

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if x > 136:
                if y < trumpet1.yMax + 20 or x <= trumpet1.xMin + 10 or x >= trumpet1.xMax:
                    if y < trumpet2.yMax + 20 or x <= trumpet2.xMin or x >= trumpet2.xMax + 5:
                        if y < trumpet3.yMax + 20 or x <= trumpet3.xMin + 10 or x >= trumpet3.xMax:
                            if y < trumpet4.yMax + 20 or x <= trumpet4.xMin + 10 or x >= trumpet4.xMax:
                                x -= speed 
                                statusSp = 1
                                statusD = False
            elif xbg < 0:
                xbg += speed
                xMin += speed
                xMax += speed
                trumpet1.xMin += speed
                trumpet1.xMax += speed
                trumpet2.xMin += speed
                trumpet2.xMax += speed
                trumpet3.xMin += speed
                trumpet3.xMax += speed                
                trumpet4.xMin += speed
                trumpet4.xMax += speed


# движение в лево

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if x < 1230 :
            if y < trumpet1.yMax + 20 or x <= trumpet1.xMin or x >= trumpet1.xMax - 10:
                if y < trumpet2.yMax + 20 or x <= trumpet2.xMin or x >= trumpet2.xMax - 10: 
                    if y < trumpet3.yMax + 20 or x <= trumpet3.xMin or x >= trumpet3.xMax - 10:
                        if y < trumpet4.yMax + 20 or x <= trumpet4.xMin or x >= trumpet4.xMax - 10:
                            x += speed 
                            statusSp = 2
                            statusD = False

        elif xbg > -6768 + 1366:
            xbg -= speed
            xMin -= speed
            xMax -= speed
            trumpet1.xMin -= speed
            trumpet1.xMax -= speed
            trumpet2.xMin -= speed
            trumpet2.xMax -= speed
            trumpet3.xMin -= speed
            trumpet3.xMax -= speed
            trumpet4.xMin -= speed
            trumpet4.xMax -= speed

# движение в право 
    if Chets == True:
        if keys[pygame.K_q] and y > 0:
            y -= speed - 4  
            statusD = False 
# движение в вверх
# "y -= speed"  потомушто у пайгейм другая система кординат 

        if keys[pygame.K_e] and y < 410:
            y += speed - 4 
            statusD = False
# движение в вниз
# "y += speed"  потомушто у пайгейм другая система кординат         
    '''
    xMin, xMax, yMin, yMax = 670, 700, 275, 235   
    m.gribchek(670, 700, 275, 235, x, y, statusB, score)
    '''
    if x >= xMin and x <= xMax and y <= yMin and y >= yMax:
        statusB = True
        score += 100
    '''
    def gribchek(xMin, xMax, yMin, yMax, x, y, statusB, score):
        if x >= xMin and x <= xMax and y <= yMin and y >= yMax:
            statusB = True
            score += 100
    '''          

# Ето грибочек :)
    
    if keys[pygame.K_r]:
        statusB = False
    if keys[pygame.K_t]:
        statusB = True
# переключатса между: маленькой , большой

    if keys[pygame.K_MINUS] and speed >= 2.5: 
#        jumpMin -= 1
        speed -= 0.1
    if keys[pygame.K_EQUALS] and speed <= 11.5:
#        jumpMin += 1
        speed += 0.1

    if keys[pygame.K_c]:
        if Chets == False:
            Chets = True
        else:
            Chets = False

    if not(isjump) :
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            isjump = True
            statusD = False
# условия активацыи прыжка

        
    else:
        if jumpCount >= -10.5 and DownUp == False:
            if jumpCount > 0:
                y -= (jumpCount ** 2) / 5            
            else:
                    if y < trumpet1.yMax or x <= trumpet1.xMin or x >= trumpet1.xMax:
                        if y < trumpet2.yMax or x <= trumpet2.xMin or x >= trumpet2.xMax:
                            if y < trumpet3.yMax or x <= trumpet3.xMin or x >= trumpet3.xMax:
                                if y < trumpet4.yMax or x <= trumpet4.xMin or x >= trumpet4.xMax:
                                    y += (jumpCount ** 2) / 5
                                else:
                                    y -= 10
                            else:
                                y -= 10
                        else:
                            y -= 6
                    else:
                        y -= 1

            #  тут должнобыть условие                
            jumpCount -= 0.5
# прыжок
        else:
            isjump = False
            jumpCount = 10.5
# остановка прыжка
    if isjump == False and Chets == False :
        if y < 365 - 1.5: 
            if y < trumpet1.yMax or x <= trumpet1.xMin or x >= trumpet1.xMax:
                if y < trumpet2.yMax or x <= trumpet2.xMin or x >= trumpet2.xMax:
                    if y < trumpet3.yMax or x <= trumpet3.xMin or x >= trumpet3.xMax:
                        if y < trumpet4.yMax or x <= trumpet4.xMin or x >= trumpet4.xMax:
                            DownUp = True
        else:
            DownUp = False

        if DownUp == True:
            if downCount >= 0.5:            
                if y < trumpet1.yMax or x <= trumpet1.xMin or x >= trumpet1.xMax:
                    if y < trumpet2.yMax or x <= trumpet2.xMin or x >= trumpet2.xMax:
                        if y < trumpet3.yMax or x <= trumpet3.xMin or x >= trumpet3.xMax:
                            if y < trumpet4.yMax or x <= trumpet4.xMin or x >= trumpet4.xMax:                        
                                y += (downCount ** 2) / 5
          
                downCount -= 0.5
# прыжок
            else:
                DownUp = False
                downCount = 7.5




#    if y <= trumpet1.yMax 

#    else:
#        if jumpCount >= -10.5:
#            if jumpCount < 0:
#                if y < trumpet1.yMax or x <= trumpet1.xMin or x >= trumpet1.xMax:
#                    if y < trumpet2.yMax or x <= trumpet2.xMin or x >= trumpet2.xMax:
#                        y += (jumpCount ** 2) / 5
#            
#            else:
#                y -= (jumpCount ** 2) / 5
#            jumpCount -= 0.5
#    if isjump == False:
#        if x < trumpet1.xMin or x > trumpet1.xMax :
#            if y < trumpet1.yMin and y < trumpet1.yMax - 20:
#                y += fallCount 

    if y > 365:
        y = 365

    Up, Down = False, False


    xxx = (xbg - (xbg * 2)) + x 

    if xxx >= 6335:
        Winner = True

    time1, time2 = str(time), ("Time:")  
    time_text = (time2 + time1)
    x1, x2 = str(round(xxx, 2)), ("X:")
    text1 = (x2 + x1)
    y1, y2 = str(round(y, 2)), ("Y:")
    text2 = (y2 + y1)
    score1, score2 = str(score), ("Score:")
    text3 = (score2 + score1)
    speed1, speed2 = str(round(speed, 2)), ('Speed:') 
    text4 = (speed2 + speed1)
    win.blit(bg, (xbg, 0))
    m.print_text(text1, 10, 10, (255, 255, 255), win, 20)
    m.print_text(text2, 150, 10, (255, 255, 255),win, 20)
    m.print_text(text3, 1160, 10, (255, 255, 255),win, 20)
    m.print_text(time_text, 900, 10, (255, 255, 255), win, 20)
    m.print_text(text4, 700, 10, (255, 255, 255), win, 20)
    if Winner == True:
        m.print_text('YOU WIN', 500, 200, (255, 255, 255,), win, 50)
        score += 10
        time -= 29

    if statusB == False: 
        if isjump == True :
            if statusSp == 1:
                win.blit(pleyerJLS, (x, y))
            elif statusSp == 2:
                win.blit(pleyerJRS, (x, y))
        else:
            if statusSp == 1:
                win.blit(pleyerSLS, (x, y))
            elif statusSp == 2:
                win.blit(pleyerSRS, (x, y))
    if statusB == True: 
        if statusD == True :
            if statusSp == 1:
                win.blit(pleyerDLB, (x, y - 10))
            elif statusSp == 2:
                win.blit(pleyerDRB, (x, y - 10))
        else:        
            if isjump == True :
                if statusSp == 1:
                    win.blit(pleyerJLB, (x, y - 30))
                elif statusSp == 2:
                    win.blit(pleyerJRB, (x, y - 30))
            else:
                if statusSp == 1:
                    win.blit(pleyerSLB, (x, y - 30))
                elif statusSp == 2:
                    win.blit(pleyer1, (x, y - 30))     
# вот ето все (с 285 до 333) ето условия рисования      
# ето временое отображение характеристик
    
    if time <= 0 :
        if Winner == False:
            m.print_text('YOU LOSE', 500, 200, (255, 255, 255,), win, 50) 
            pygame.display.update()
            pygame.time.delay(10000)
            run = False 
        else: 
            run = False
    pygame.display.update()
















#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------____-----____----__________----_____-----------_____---------________________-------------------------------------------------------------------------------
#-----|\___\---|\___\-|\__________\--|\____\---------|\____\-------|\_______________\------------------------------------------------------------------------------
#-----| |  |---| |  |-| |   ______|--| |   |---------| |   |-------| |   ________   |------------------------------------------------------------------------------
#-----| |  |___| |  |-| |  |_____----| |   |---------| |   |-------| |   |----| |   |------------------------------------------------------------------------------
#-----| |  |____\|  |-| |  |_____\---| |   |---------| |   |-------| |   |----| |   |------------------------------------------------------------------------------
#-----| |           |-| |   ______|--| |   |---------| |   |-------| |   |----| |   |------------------------------------------------------------------------------
#-----| |  |"""|"|  |-| |  |_____----| |   |_____----| |   |_____--| |   |____| |   |------------------------------------------------------------------------------
#-----| |  |---| |  |-| |  |_____\---| |   |_____\---| |   |_____\-| |   |_____\|   |------------------------------------------------------------------------------
#------\|__|----\|__|--\|_________|---\|_________|--- \|_________|--\|              |------------------------------------------------------------------------------
#--------------------------------------------------------------------""""""""""""""""------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
