import module as m
import pygame 


pygame.init()

clock = pygame.time.Clock()
#fps

heightWin = 448
widthWin = 6768  
sizeWin = (1366, 448)
# велечина окна

win = pygame.display.set_mode(sizeWin)
pygame.display.set_caption('its me MARIO!!!')

x = 100
y = 365
xbg = 0
# изначальные кординаты игрока

heightS, widthS = 37, 37
heightB, widthB = 66, 33
heightBD, widthBD = 47, 34
#высота, шырина
speed = 10.0

jumpMin = 9
isjump = False
jumpCount = jumpMin
# параметры прыжка

bg = pygame.image.load("D:/VS_code/GAME/bg.png")
pleyerSRS = pygame.image.load("D:/GAME/Lmario-stand-r-2.png")
pleyerSLS = pygame.image.load("D:/GAME/Lmario-stand-l-2.png")
pleyerJRS = pygame.image.load("D:/GAME/Lmario-jump-r-2.png")
pleyerJLS = pygame.image.load("D:/GAME/Lmario-jump-l-2.png")
pleyerSLB = pygame.image.load("D:/GAME/Bmario-stand-l-2.png")
pleyerSRB = pygame.image.load("D:/GAME/Bmario-stand-r-2.png")
pleyerJLB = pygame.image.load("D:/GAME/Bmario-jump-l-2.png")
pleyerJRB = pygame.image.load("D:/GAME/Bmario-jump-r-2.png")
pleyerDLB = pygame.image.load("D:/GAME/Bmario-Down-l.png")
pleyerDRB = pygame.image.load("D:/GAME/Bmario-Down-r.png")
# объявляем изображения

statusSp = 2  
statusB, statusD = False, False

#keys = pygame.key.get_pressed() 
# зажатие или нажатия клавиш

run = True

while run:
    clock.tick(18)
#fps
    keys = pygame.key.get_pressed() 
# зажатие или нажатия клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# условия закрытия игры

    statusD = False

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        statusD = True 
# условие для преседания

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if x > 0:
            x -= speed 
            statusSp = 1
            statusD = False
        elif xbg < 0:
            xbg += speed
# движение в лево
# иначе движение камеры

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
        if x < 1340:
            x += speed 
            statusSp = 2
            statusD = False
        elif xbg < 6768:
            xbg -= speed
# движение в право 
# иначе движение камеры

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

    xMin, xMax, yMin, yMax = 670, 700, 275, 235   

    #def gribchek(xMin, xMax, yMin, yMax):
    if x >= xMin and x <= xMax and y <= yMin and y >= yMax:
        statusB = True
            
    #m.gribchek(670, 700, 275, 235, x, y, statusB)
    
# Ето грибочек :)
    
    if keys[pygame.K_r]:
        statusB = False
    if keys[pygame.K_t]:
        statusB = True
# переключатса между: маленькой , большой

#    if keys[pygame.K_MINUS]: 
#        jumpMin -= 1
#        speed -= 1
#    if keys[pygame.K_p]:
#        jumpMin += 1
#        speed += 1
    if not(isjump):
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            isjump = True
            statusD = False
# условия активацыи прыжка

    else:
        if jumpCount >= -jumpMin:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
# прыжок
        else:
            isjump = False
            jumpCount = jumpMin
# остановка прыжка



    win.blit(bg, (xbg, 0))
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
                    win.blit(pleyerSRB, (x, y - 30))     
# вот ето все (с 131 до 159) ето условия рисования того или иного марио       
    print(speed, x, y, statusB)
# ето временое отображение характеристик
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
