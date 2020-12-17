import module as m
import pygame 
import os


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
xMin, xMax, yMin, yMax = 670, 700, 275, 235 
# изначальные кординаты 

heightS, widthS = 37, 37
heightB, widthB = 66, 33
heightBD, widthBD = 47, 34
#высота, шырина
speed = 5.0

jumpMin = 10.5
isjump = False
jumpCount = jumpMin
# параметры прыжка

file_path = os.path.dirname(__file__)

# создаем папку "sprite"
file_sprite = (file_path + "\\sprite\\" )

file_sprite_folder = [(file_path + "\\bg.png"), (file_path + "\\Lmario-stand-r-2.png"), (file_path + "\\Lmario-stand-l-2.png"), (file_path + "\\Lmario-jump-r-2.png"),
(file_path + "\\Lmario-jump-l-2.png"), (file_path + "\\Bmario-stand-r-2.png"), (file_path + "\\Bmario-stand-l-2.png"), (file_path + "\\Bmario-jump-r-2.png"),
(file_path + "\\Bmario-jump-l-2.png"),(file_path + "\\Bmario-Down-r.png"),  (file_path + "\\Bmario-Down-l.png")]

sprite_list = ['bg.png', "Lmario-stand-r-2.png", "Lmario-stand-l-2.png", "Lmario-jump-r-2.png", "Lmario-jump-l-2.png", "Bmario-stand-r-2.png", "Bmario-stand-l-2.png", 
"Bmario-jump-r-2.png", "Bmario-jump-l-2.png", "Bmario-Down-r.png", "Bmario-Down-l.png"] 

a = 0
run_plus = True

if (os.path.exists(file_path + "\\sprite\\Bmario-Down-l.png")):
    sprite_path = os.path.join(file_path, "sprite/bg.png")  
    bg = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Lmario-stand-r-2.png")
    pleyerSRS = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Lmario-stand-l-2.png")
    pleyerSLS = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Lmario-jump-r-2.png")
    pleyerJRS = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Lmario-jump-l-2.png")
    pleyerJLS = pygame.image.load(sprite_path)
    prite_path = os.path.join(file_path, "sprite/Bmario-stand-r-2.png")
    pleyerSRB = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Bmario-stand-l-2.png")
    pleyerSLB = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Bmario-jump-r-2.png")
    pleyerJRB = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Bmario-jump-l-2.png")
    pleyerJLB = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Bmario-Down-r.png")
    pleyerDRB = pygame.image.load(sprite_path)
    sprite_path = os.path.join(file_path, "sprite/Bmario-Down-l.png")
    pleyerDLB = pygame.image.load(sprite_path)
else:
    while run_plus:
        if(os.path.exists(file_sprite)):
            for i in range(11):
                os.replace(file_sprite_folder[a], file_sprite + sprite_list[a])
                a += 1
                run_plus = False
        else:
            os.makedirs(file_sprite, exist_ok=True)


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

statusSp = 2  
statusB, statusD = False, False

#keys = pygame.key.get_pressed() 
# зажатие или нажатия клавиш

run = True

while run:
    clock.tick(60)
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
            xMin += speed
            xMax += speed


# движение в лево

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
        if x < 1340:
            x += speed 
            statusSp = 2
            statusD = False
        elif xbg < 6768:
            xbg -= speed
            xMin -= speed
            xMax -= speed

# движение в право 

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

    #xMin, xMax, yMin, yMax = 670, 700, 275, 235   

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
                y += (jumpCount ** 2) / 5
            else:
                y -= (jumpCount ** 2) / 5
            jumpCount -= 0.5
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
