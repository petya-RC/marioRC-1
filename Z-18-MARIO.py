import pygame

pygame.init()

clock = pygame.time.Clock()

heightWin = 448
widthWin = 6768  #1347
sizeWin = (1366, 448)

win = pygame.display.set_mode(sizeWin)

pygame.display.set_caption('its me MARIO!!!')

x = 100
y = 365
height = 20
width = 20
speed = 10.0



jumpMin = 9
isjump = False
datp = False
jumpCount = jumpMin

bg = pygame.image.load("D:/VS_code/GAME/bg.png")
pleyerSRS = pygame.image.load("D:/GAME/sprits/statusS/Lmario-stand-r-2.png")
pleyerSLS = pygame.image.load("D:/GAME/sprits/statusS/Lmario-stand-l-2.png")
pleyerJRS = pygame.image.load("D:/GAME/sprits/statusS/Lmario-jump-r-2.png")
pleyerJLS = pygame.image.load("D:/GAME/sprits/statusS/Lmario-jump-l-2.png")
pleyerSLB = pygame.image.load("D:/GAME/sprits/statusB/Bmario-stand-l-2.png")
pleyerSRB = pygame.image.load("D:/GAME/sprits/statusB/Bmario-stand-r-2.png")
pleyerJLB = pygame.image.load("D:/GAME/sprits/statusB/Bmario-jump-l-2.png")
pleyerJRB = pygame.image.load("D:/GAME/sprits/statusB/Bmario-jump-r-2.png")
pleyerDLB = pygame.image.load("D:/GAME/sprits/statusB/Bmario-Down-l.png")
pleyerDRB = pygame.image.load("D:/GAME/sprits/statusB/Bmario-Down-r.png")

statusSp = 2  
statusB = False
statusD = False

run = True

while run:
    clock.tick(18)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() 
    statusD = False
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        statusD = True 


    if keys[pygame.K_LEFT] or keys[pygame.K_a] and x > 0:
        x -= speed 
        statusSp = 1
        statusD = False

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and x < 1340:
        x += speed 
        statusSp = 2
        statusD = False

    if keys[pygame.K_e] and y < 410:
        y += speed - 4 
        statusD = False
        
    if keys[pygame.K_q] and y > 0:
        y -= speed - 4  
        statusD = False 
             
    def gribchek(xMin, xMax, yMin, yMax):
        if x >= xMin:
            if x <= xMax:
                if y <= yMin:
                    if y >= yMax:
                        statusB = True
    # Ето грибочек :)
    
    if keys[pygame.K_r]:
        if statusB == True and datp == False:
            statusB = False
            datp = True
        if statusB == False and datp == False:
            statusB = True
            datp = True
#    if keys[pygame.K_MINUS]: 
#        jumpMin -= 1
#    if keys[pygame.K_p]:
#        jumpMin += 1
    if not(isjump):
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            isjump = True
            statusD = False

    else:
        if jumpCount >= -jumpMin:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isjump = False
            jumpCount = jumpMin

    

    win.blit(bg, (0, 0))
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
    print(speed, x, y, statusB)
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
