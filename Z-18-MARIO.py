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
jumpCount, downCount = 10.5, 8.5

a = 0
run_plus = True

# параметры прыжка

file_path = os.path.dirname(__file__)

pygame.mixer.music.load((file_path + "\saundtrek.mp3"))
pygame.mixer.music.set_volume(0.05)

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
# загрузка файлов


statusSp = 2  
statusB, statusD, Winner, p, DownUp, Chets = False, False, False, False, False, False
score = 0
time = 24000

class colaider ():
    xMin = 0
    xMax = 0
    yMin = 0
    yMax = 0


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
trumpet4.xMax = 1890
trumpet4.yMax = 235
trumpet4.yMin = 365

trumpet5 = colaider()
trumpet5.xMin = 5195
trumpet5.xMax = 5276
trumpet5.yMax = 300
trumpet5.yMin = 365

trumpet6 = colaider()
trumpet6.xMin = 5705
trumpet6.xMax = 5785
trumpet6.yMax = 300
trumpet6.yMin = 365

block1 = colaider()
block1.xMin = 485
block1.xMax = 545
block1.yMax = 235
block1.yMin = 305
# 
block2 = colaider()
block2.xMin = 613
block2.xMax = 800
block2.yMax = 235
block2.yMin = 305

block3 = colaider()
block3.xMin = 675
block3.xMax = 735
block3.yMax = 105
block3.yMin = 180

block4 = colaider()
block4.xMin = 2020
block4.xMax = 2080
block4.yMax = 205
block4.yMin = 270

block5 = colaider()
block5.xMin = 2435
block5.xMax = 2560
block5.yMax = 235
block5.yMin = 305

block6 = colaider()
block6.xMin = 2531
block6.xMax = 2815
block6.yMax = 107
block6.yMin = 180

block7 = colaider()
block7.xMin = 2885
block7.xMax = 3040
block7.yMax = 107
block7.yMin = 180

block8 = colaider()
block8.xMin = 2980
block8.xMax = 3040
block8.yMax = 235
block8.yMin = 305

block9 = colaider()
block9.xMin = 3175
block9.xMax = 3260
block9.yMax = 235
block9.yMin = 305

block10 = colaider()
block10.xMin = 3365
block10.xMax = 3420
block10.yMax = 235
block10.yMin = 305

block11 = colaider()
block11.xMin = 3460
block11.xMax = 3520
block11.yMax = 235
block11.yMin = 305

block12 = colaider()
block12.xMin = 3555
block12.xMax = 3615
block12.yMax = 235
block12.yMin = 305

block13 = colaider()
block13.xMin = 3460
block13.xMax = 3520
block13.yMax = 107
block13.yMin = 180

block14 = colaider()
block14.xMin = 3750
block14.xMax = 3810
block14.yMax = 235
block14.yMin = 305

block15 = colaider()
block15.xMin = 3845
block15.xMax = 3965
block15.yMax = 107
block15.yMin = 180

block16 = colaider()
block16.xMin = 4070
block16.xMax = 4225
block16.yMax = 107
block16.yMin = 180

block17 = colaider()
block17.xMin = 4100
block17.xMax = 4190
block17.yMax = 235
block17.yMin = 305

# лесница {
block18 = colaider()
block18.xMin = 4260
block18.xMax = 4415
block18.yMax = 330
block18.yMin = 365

block19 = colaider()
block19.xMin = 4290
block19.xMax = 4415
block19.yMax = 300
block19.yMin = 365

block20 = colaider()
block20.xMin = 4320
block20.xMax = 4415
block20.yMax = 270
block20.yMin = 365

block21 = colaider()
block21.xMin = 4350
block21.xMax = 4415
block21.yMax = 236
block21.yMin = 365
# }

# loesneza1 {
block22 = colaider()
block22.xMin = 4450
block22.xMax = 4610
block22.yMax = 330
block22.yMin = 365

block23 = colaider()
block23.xMin = 4450
block23.xMax = 4575
block23.yMax = 300
block23.yMin = 365

block24 = colaider()
block24.xMin = 4450
block24.xMax = 4545
block24.yMax = 255
block24.yMin = 365

block25 = colaider()
block25.xMin = 4450
block25.xMax = 4510
block25.yMax = 240
block25.yMin = 365
# }

# loesneza2 {
block26 = colaider()
block26.xMin = 4705
block26.xMax = 4895
block26.yMax = 330
block26.yMin = 365

block27 = colaider()
block27.xMin = 4740
block27.xMax = 4895
block27.yMax = 300
block27.yMin = 365

block28 = colaider()
block28.xMin = 4770
block28.xMax = 4895
block28.yMax = 255
block28.yMin = 365

block29 = colaider()
block29.xMin = 4800
block29.xMax = 4895
block29.yMax = 240
block29.yMin = 365
# }

# loesneza3 {
block30 = colaider()
block30.xMin = 4930
block30.xMax = 5090
block30.yMax = 330
block30.yMin = 365

block31 = colaider()
block31.xMin = 4930
block31.xMax = 5060
block31.yMax = 300
block31.yMin = 365

block32 = colaider()
block32.xMin = 4930
block32.xMax = 5025
block32.yMax = 255
block32.yMin = 365

block33 = colaider()
block33.xMin = 4930
block33.xMax = 4995
block33.yMax = 240
block33.yMin = 365
# }

block34 = colaider()
block34.xMin = 5350
block34.xMax = 5505
block34.yMax = 240
block34.yMin = 305

# loesneza3 {
#1
block35 = colaider()
block35.xMin = 5785
block35.xMax = 6080
block35.yMax = 320
block35.yMin = 365
#2
block36 = colaider()
block36.xMin = 5795
block36.xMax = 6080
block36.yMax = 290
block36.yMin = 365
#3
block37 = colaider()
block37.xMin = 5825
block37.xMax = 6080
block37.yMax = 260
block37.yMin = 365
#4
block38 = colaider()
block38.xMin = 5860
block38.xMax = 6080
block38.yMax = 230
block38.yMin = 365
#5
block39 = colaider()
block39.xMin = 5895
block39.xMax = 6080
block39.yMax = 200
block39.yMin = 365
#6
block40 = colaider()
block40.xMin = 5925
block40.xMax = 6080
block40.yMax = 170
block40.yMin = 365
#7
block41 = colaider()
block41.xMin = 5960
block41.xMax = 6080
block41.yMax = 140
block41.yMin = 365
#8
block42 = colaider()
block42.xMin = 5985
block42.xMax = 6080
block42.yMax = 110
block42.yMin = 365
# }

pit1 = colaider()
pit1.xMin = 2205
pit1.xMax = 2245
# база данных

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
                if y < trumpet1.yMax + 20 or x <= trumpet1.xMin + 5 or x >= trumpet1.xMax:
                    if y < trumpet2.yMax + 10 or x <= trumpet2.xMin + 5 or x >= trumpet2.xMax + 5:
                        if y < trumpet3.yMax + 10 or x <= trumpet3.xMin + 10 or x >= trumpet3.xMax:
                            if y < trumpet4.yMax + 10 or x <= trumpet4.xMin + 10 or x >= trumpet4.xMax:
                                if y < block1.yMax + 10 or y > block1.yMin or x <= block1.xMin + 10 or x >= block1.xMax:
                                    if y < block2.yMax + 10 or  y > block2.yMin or x <= block2.xMin + 10 or x >= block2.xMax:
                                        if y < block3.yMax + 10 or y > block3.yMin or x <= block3.xMin + 10 or x >= block3.xMax:
                                            if y < block4.yMax + 10 or y > block4.yMin or x <= block4.xMin + 10 or x >= block4.xMax:
                                                if y < block5.yMax + 10 or y > block5.yMin or x <= block5.xMin + 10 or x >= block5.xMax:
                                                    if y < block6.yMax + 10 or y > block6.yMin or x <= block6.xMin + 10 or x >= block6.xMax:
                                                        if y < block7.yMax + 10 or y > block7.yMin or x <= block7.xMin + 10 or x >= block7.xMax:
                                                            if y < block8.yMax + 10 or y > block8.yMin or x <= block8.xMin + 10 or x >= block8.xMax:
                                                                if y < block9.yMax + 10 or y > block9.yMin or x <= block9.xMin + 10 or x >= block9.xMax:
                                                                    if y < block10.yMax + 10 or y > block10.yMin or x <= block10.xMin + 10 or x >= block10.xMax:
                                                                        if y < block11.yMax + 10 or y > block11.yMin or x <= block11.xMin + 10 or x >= block11.xMax:
                                                                            if y < block12.yMax + 10 or y > block12.yMin or x <= block12.xMin + 10 or x >= block12.xMax:
                                                                                if y < block13.yMax + 10 or y > block13.yMin or x <= block13.xMin + 10 or x >= block13.xMax:
                                                                                    if y < block14.yMax + 10 or y > block14.yMin or x <= block14.xMin + 10 or x >= block14.xMax:
                                                                                        if y < block15.yMax + 10 or y > block15.yMin or x <= block15.xMin + 10 or x >= block15.xMax:
                                                                                            if y < block16.yMax + 10 or y > block16.yMin or x <= block16.xMin + 10 or x >= block16.xMax:
                                                                                                if y < block17.yMax + 10 or y > block17.yMin or x <= block17.xMin + 10 or x >= block17.xMax:
                                                                                                    if y < block18.yMax + 10 or y > block18.yMin or x <= block18.xMin + 10 or x >= block18.xMax:
                                                                                                        if y < block19.yMax + 10 or y > block19.yMin or x <= block19.xMin + 10 or x >= block19.xMax:
                                                                                                            if y < block20.yMax + 10 or y > block20.yMin or x <= block20.xMin + 10 or x >= block20.xMax:
                                                                                                                if y < block21.yMax + 10  or y > block21.yMin or x <= block21.xMin + 10 or x >= block21.xMax:
                                                                                                                    if y < block22.yMax + 10  or y > block22.yMin or x <= block22.xMin + 10 or x >= block22.xMax:
                                                                                                                        if y < block23.yMax + 10  or y > block23.yMin or x <= block23.xMin + 10 or x >= block23.xMax:
                                                                                                                            if y < block24.yMax + 10  or y > block24.yMin or x <= block24.xMin + 10 or x >= block24.xMax:
                                                                                                                                if y < block25.yMax + 10  or y > block25.yMin or x <= block25.xMin + 10 or x >= block25.xMax:
                                                                                                                                    if y < block26.yMax + 10  or y > block26.yMin or x <= block26.xMin + 10 or x >= block26.xMax:
                                                                                                                                        if y < block27.yMax + 10  or y > block27.yMin or x <= block27.xMin + 10 or x >= block27.xMax:
                                                                                                                                            if y < block28.yMax + 10  or y > block28.yMin or x <= block28.xMin + 10 or x >= block28.xMax:
                                                                                                                                                if y < block29.yMax + 10  or y > block29.yMin or x <= block29.xMin + 10 or x >= block29.xMax:
                                                                                                                                                    if y < block30.yMax + 10  or y > block30.yMin or x <= block30.xMin + 10 or x >= block30.xMax:
                                                                                                                                                        if y < block31.yMax + 10  or y > block31.yMin or x <= block31.xMin + 10 or x >= block31.xMax:
                                                                                                                                                            if y < block32.yMax + 10  or y > block32.yMin or x <= block32.xMin + 10 or x >= block32.xMax:
                                                                                                                                                                if y < block33.yMax + 10  or y > block33.yMin or x <= block33.xMin + 10 or x >= block33.xMax:
                                                                                                                                                                    if y < trumpet5.yMax + 10 or x <= trumpet5.xMin + 10 or x >= trumpet5.xMax:
                                                                                                                                                                        if y < trumpet6.yMax + 10 or x <= trumpet6.xMin + 10 or x >= trumpet6.xMax:
                                                                                                                                                                            if y < block34.yMax + 10  or y > block34.yMin or x <= block34.xMin + 10 or x >= block34.xMax:
                                                                                                                                                                                if y < block35.yMax + 10  or y > block35.yMin or x <= block35.xMin + 10 or x >= block35.xMax:
                                                                                                                                                                                    if y < block36.yMax + 10  or y > block36.yMin or x <= block36.xMin + 10 or x >= block36.xMax:
                                                                                                                                                                                        if y < block37.yMax + 10  or y > block37.yMin or x <= block37.xMin + 10 or x >= block37.xMax:
                                                                                                                                                                                            if y < block38.yMax + 10  or y > block38.yMin or x <= block38.xMin + 10 or x >= block38.xMax:
                                                                                                                                                                                                if y < block39.yMax + 10  or y > block39.yMin or x <= block39.xMin + 10 or x >= block39.xMax:
                                                                                                                                                                                                    if y < block40.yMax + 10  or y > block40.yMin or x <= block40.xMin + 10 or x >= block40.xMax:
                                                                                                                                                                                                        if y < block41.yMax + 10  or y > block41.yMin or x <= block41.xMin + 10 or x >= block41.xMax:
                                                                                                                                                                                                            if y < block42.yMax + 10  or y > block42.yMin or x <= block42.xMin + 10 or x >= block42.xMax:
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
                trumpet5.xMin += speed
                trumpet5.xMax += speed
                trumpet6.xMin += speed
                trumpet6.xMax += speed
                block1.xMin += speed
                block1.xMax += speed
                block2.xMin += speed
                block2.xMax += speed
                block3.xMin += speed
                block3.xMax += speed
                block4.xMin += speed
                block4.xMax += speed
                block5.xMin += speed
                block5.xMax += speed
                block6.xMin += speed
                block6.xMax += speed
                block7.xMin += speed
                block7.xMax += speed
                block8.xMin += speed
                block8.xMax += speed
                block9.xMin += speed
                block9.xMax += speed
                block10.xMin += speed
                block10.xMax += speed
                block11.xMin += speed
                block11.xMax += speed
                block12.xMin += speed
                block12.xMax += speed
                block13.xMin += speed
                block13.xMax += speed
                block14.xMin += speed
                block14.xMax += speed
                block15.xMin += speed
                block15.xMax += speed
                block16.xMin += speed
                block16.xMax += speed
                block17.xMin += speed
                block17.xMax += speed
                block18.xMin += speed
                block18.xMax += speed
                block19.xMin += speed
                block19.xMax += speed
                block20.xMin += speed
                block20.xMax += speed
                block21.xMin += speed
                block21.xMax += speed
                block22.xMin += speed
                block22.xMax += speed
                block23.xMin += speed
                block23.xMax += speed
                block24.xMin += speed
                block24.xMax += speed
                block25.xMin += speed
                block25.xMax += speed
                block26.xMin += speed
                block26.xMax += speed
                block27.xMin += speed
                block27.xMax += speed
                block28.xMin += speed
                block28.xMax += speed
                block29.xMin += speed
                block29.xMax += speed
                block30.xMin += speed
                block30.xMax += speed
                block31.xMin += speed
                block31.xMax += speed
                block32.xMin += speed
                block32.xMax += speed
                block33.xMin += speed
                block33.xMax += speed
                block34.xMin += speed
                block34.xMax += speed
                block35.xMin += speed
                block35.xMax += speed
                block36.xMin += speed
                block36.xMax += speed
                block37.xMin += speed
                block37.xMax += speed
                block38.xMin += speed
                block38.xMax += speed
                block39.xMin += speed
                block39.xMax += speed
                block40.xMin += speed
                block40.xMax += speed
                block41.xMin += speed
                block41.xMax += speed
                block42.xMin += speed
                block42.xMax += speed
                pit1.xMin += speed
                pit1.xMax += speed


# движение в лево

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if x < 1230 :
            if y < trumpet1.yMax + 20 or x <= trumpet1.xMin or x >= trumpet1.xMax - 10:
                if y < trumpet2.yMax + 20 or x <= trumpet2.xMin or x >= trumpet2.xMax - 10: 
                    if y < trumpet3.yMax + 20 or x <= trumpet3.xMin or x >= trumpet3.xMax - 10:
                        if y < trumpet4.yMax + 20 or x <= trumpet4.xMin or x >= trumpet4.xMax - 10:
                            if y < block1.yMax + 20 or y > block1.yMin or x <= block1.xMin or x >= block1.xMax - 10:
                                if y < block2.yMax + 20 or y > block2.yMin or x <= block2.xMin or x >= block2.xMax - 10:
                                    if y < block3.yMax + 20 or y > block3.yMin or x <= block3.xMin or x >= block3.xMax - 10:
                                        if y < block4.yMax + 20 or y > block4.yMin or x <= block4.xMin or x >= block4.xMax - 10:
                                            if y < block5.yMax + 20 or y > block5.yMin or x <= block5.xMin or x >= block5.xMax - 10:
                                                if y < block6.yMax + 20 or y > block6.yMin or x <= block6.xMin or x >= block6.xMax - 10:
                                                    if y < block7.yMax + 20 or y > block7.yMin or x <= block7.xMin or x >= block7.xMax - 10:
                                                        if y < block8.yMax + 20 or y > block8.yMin or x <= block8.xMin or x >= block8.xMax - 10:
                                                            if y < block9.yMax + 20 or y > block9.yMin or x <= block9.xMin or x >= block9.xMax - 10:
                                                                if y < block10.yMax + 20 or y > block10.yMin or x <= block10.xMin or x >= block10.xMax - 10:
                                                                    if y < block11.yMax + 20 or y > block11.yMin or x <= block11.xMin or x >= block11.xMax - 10:
                                                                        if y < block12.yMax + 20 or y > block12.yMin or x <= block12.xMin or x >= block12.xMax - 10:
                                                                            if y < block13.yMax + 20 or y > block13.yMin or x <= block13.xMin or x >= block13.xMax - 10:
                                                                                if y < block14.yMax + 20 or y > block14.yMin or x <= block14.xMin or x >= block14.xMax - 10:
                                                                                    if y < block15.yMax + 20 or y > block15.yMin or x <= block15.xMin or x >= block15.xMax - 10:
                                                                                        if y < block16.yMax + 20 or y > block16.yMin or x <= block16.xMin or x >= block16.xMax - 10:
                                                                                            if y < block17.yMax + 20 or y > block17.yMin or x <= block17.xMin or x >= block17.xMax - 10:
                                                                                                if y < block18.yMax + 20 or y > block18.yMin  or x <= block18.xMin - 5 or x >= block18.xMax - 10:
                                                                                                    if y < block19.yMax + 20 or y > block19.yMin or x <= block19.xMin - 10 or x >= block19.xMax - 10:
                                                                                                        if y < block20.yMax + 20 or y > block20.yMin or x <= block20.xMin - 10 or x >= block20.xMax - 10:
                                                                                                            if y < block21.yMax + 20 or y > block21.yMin or x <= block21.xMin - 10 or x >= block21.xMax - 10:
                                                                                                                if y < block22.yMax + 20 or y > block22.yMin or x <= block22.xMin - 10 or x >= block22.xMax - 10:
                                                                                                                    if y < block23.yMax + 20 or y > block23.yMin or x <= block23.xMin - 10 or x >= block23.xMax - 10:
                                                                                                                        if y < block24.yMax + 20 or y > block24.yMin or x <= block24.xMin - 10 or x >= block24.xMax - 10:
                                                                                                                            if y < block25.yMax + 20 or y > block25.yMin or x <= block25.xMin - 10 or x >= block25.xMax - 10:
                                                                                                                                if y < block26.yMax + 20 or y > block26.yMin or x <= block26.xMin - 10 or x >= block26.xMax - 10:
                                                                                                                                    if y < block27.yMax + 20 or y > block27.yMin or x <= block27.xMin - 10 or x >= block27.xMax - 10:
                                                                                                                                        if y < block28.yMax + 20 or y > block28.yMin or x <= block28.xMin - 10 or x >= block28.xMax - 10:
                                                                                                                                            if y < block29.yMax + 20 or y > block29.yMin or x <= block29.xMin - 10 or x >= block29.xMax - 10:
                                                                                                                                                if y < block30.yMax + 20 or y > block30.yMin or x <= block30.xMin - 10 or x >= block30.xMax - 10:
                                                                                                                                                    if y < block31.yMax + 20 or y > block31.yMin or x <= block31.xMin - 10 or x >= block31.xMax - 10:
                                                                                                                                                        if y < block32.yMax + 20 or y > block32.yMin or x <= block32.xMin - 10 or x >= block32.xMax - 10:
                                                                                                                                                            if y < block33.yMax + 20 or y > block33.yMin or x <= block33.xMin - 10 or x >= block33.xMax - 10:
                                                                                                                                                                if y < block34.yMax + 20 or y > block34.yMin or x <= block34.xMin - 10 or x >= block34.xMax - 10:
                                                                                                                                                                    if y < trumpet5.yMax + 20 or x <= trumpet5.xMin or x >= trumpet5.xMax - 10:
                                                                                                                                                                        if y < trumpet6.yMax + 20 or x <= trumpet6.xMin or x >= trumpet6.xMax - 10:
                                                                                                                                                                            if y < block35.yMax + 20 or y > block35.yMin or x <= block35.xMin - 10 or x >= block35.xMax - 10:
                                                                                                                                                                                if y < block36.yMax + 20 or y > block36.yMin or x <= block36.xMin - 10 or x >= block36.xMax - 10:
                                                                                                                                                                                    if y < block37.yMax + 20 or y > block37.yMin or x <= block37.xMin - 10 or x >= block37.xMax - 10:
                                                                                                                                                                                        if y < block38.yMax + 20 or y > block38.yMin or x <= block38.xMin - 10 or x >= block38.xMax - 10:
                                                                                                                                                                                            if y < block39.yMax + 20 or y > block39.yMin or x <= block39.xMin - 10 or x >= block39.xMax - 10:
                                                                                                                                                                                                if y < block40.yMax + 20 or y > block40.yMin or x <= block40.xMin - 10 or x >= block40.xMax - 10:
                                                                                                                                                                                                    if y < block41.yMax + 20 or y > block41.yMin or x <= block41.xMin - 10 or x >= block41.xMax - 10:
                                                                                                                                                                                                        if y < block42.yMax + 20 or y > block42.yMin or x <= block42.xMin - 10 or x >= block42.xMax - 10:
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
            trumpet5.xMin -= speed
            trumpet5.xMax -= speed
            trumpet6.xMin -= speed
            trumpet6.xMax -= speed
            block1.xMin -= speed
            block1.xMax -= speed
            block2.xMin -= speed
            block2.xMax -= speed
            block3.xMin -= speed
            block3.xMax -= speed
            block4.xMin -= speed
            block4.xMax -= speed
            block5.xMin -= speed
            block5.xMax -= speed
            block6.xMin -= speed
            block6.xMax -= speed
            block7.xMin -= speed
            block7.xMax -= speed
            block8.xMin -= speed
            block8.xMax -= speed
            block9.xMin -= speed
            block9.xMax -= speed
            block10.xMin -= speed
            block10.xMax -= speed
            block11.xMin -= speed
            block11.xMax -= speed
            block12.xMin -= speed
            block12.xMax -= speed
            block13.xMin -= speed
            block13.xMax -= speed
            block14.xMin -= speed
            block14.xMax -= speed
            block15.xMin -= speed
            block15.xMax -= speed
            block16.xMin -= speed
            block16.xMax -= speed
            block17.xMin -= speed
            block17.xMax -= speed
            block18.xMin -= speed
            block18.xMax -= speed
            block19.xMin -= speed
            block19.xMax -= speed
            block20.xMin -= speed
            block20.xMax -= speed
            block21.xMin -= speed
            block21.xMax -= speed
            block22.xMin -= speed
            block22.xMax -= speed
            block23.xMin -= speed
            block23.xMax -= speed
            block24.xMin -= speed
            block24.xMax -= speed
            block25.xMin -= speed
            block25.xMax -= speed
            block26.xMin -= speed
            block26.xMax -= speed
            block27.xMin -= speed
            block27.xMax -= speed
            block28.xMin -= speed
            block28.xMax -= speed
            block29.xMin -= speed
            block29.xMax -= speed
            block30.xMin -= speed
            block30.xMax -= speed
            block31.xMin -= speed
            block31.xMax -= speed
            block32.xMin -= speed
            block32.xMax -= speed
            block33.xMin -= speed
            block33.xMax -= speed
            block34.xMin -= speed
            block34.xMax -= speed
            block35.xMin -= speed
            block35.xMax -= speed
            block36.xMin -= speed
            block36.xMax -= speed
            block37.xMin -= speed
            block37.xMax -= speed
            block38.xMin -= speed
            block38.xMax -= speed
            block39.xMin -= speed
            block39.xMax -= speed
            block40.xMin -= speed
            block40.xMax -= speed
            block41.xMin -= speed
            block41.xMax -= speed
            block42.xMin -= speed
            block42.xMax -= speed
            pit1.xMin -= speed
            pit1.xMax -= speed

# движение в право 
    if Chets == True:
        if keys[pygame.K_q] and y > 0:
            y -= speed   
            statusD = False 
# движение в вверх
# "y -= speed"  потомушто у пайгейм другая система кординат 

        if keys[pygame.K_e] and y < 410:
            y += speed  
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

    if keys[pygame.K_MINUS] and speed >= 2.1: 
#        jumpMin -= 1
        speed -= 0.1
    if keys[pygame.K_EQUALS] and speed <= 11.9:
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
                if y < block1.yMax + 10 or y > block1.yMin or x <= block1.xMin - 5 or x >= block1.xMax - 5:
                    if y < block2.yMax + 10 or y > block2.yMin or x <= block2.xMin - 5 or x >= block2.xMax - 5:
                        if y < block3.yMax + 10 or y > block3.yMin or x <= block3.xMin - 5 or x >= block3.xMax - 5:
                            if y < block4.yMax + 10 or y > block4.yMin or x <= block4.xMin - 5 or x >= block4.xMax - 5:
                                if y < block5.yMax + 10 or y > block5.yMin or x <= block5.xMin - 5 or x >= block5.xMax - 5:
                                    if y < block6.yMax + 10 or y > block6.yMin or x <= block6.xMin - 5 or x >= block6.xMax - 5:
                                        if y < block7.yMax + 10 or y > block7.yMin or x <= block7.xMin - 5 or x >= block7.xMax - 5:
                                            if y < block8.yMax + 10 or y > block8.yMin or x <= block8.xMin - 5 or x >= block8.xMax - 5:
                                                if y < block9.yMax + 10 or y > block9.yMin or x <= block9.xMin - 5 or x >= block9.xMax - 5:
                                                    if y < block10.yMax + 10 or y > block10.yMin or x <= block10.xMin - 5 or x >= block10.xMax - 5:
                                                        if y < block11.yMax + 10 or y > block11.yMin or x <= block11.xMin - 5 or x >= block11.xMax - 5:
                                                            if y < block12.yMax + 10 or y > block12.yMin or x <= block12.xMin - 5 or x >= block12.xMax - 5:
                                                                if y < block13.yMax + 10 or y > block13.yMin or x <= block13.xMin - 5 or x >= block13.xMax - 5:
                                                                    if y < block14.yMax + 10 or y > block14.yMin or x <= block14.xMin - 5 or x >= block14.xMax - 5:
                                                                        if y < block15.yMax + 10 or y > block15.yMin or x <= block15.xMin - 5 or x >= block15.xMax - 5:
                                                                            if y < block16.yMax + 10 or y > block16.yMin or x <= block16.xMin - 5 or x >= block16.xMax - 5:
                                                                                if y < block17.yMax + 10 or y > block17.yMin or x <= block17.xMin - 5 or x >= block17.xMax - 5:
                                                                                    if y < block18.yMax + 10 or y > block18.yMin or x <= block18.xMin - 5 or x >= block18.xMax - 5:
                                                                                        if y < block19.yMax + 10 or y > block19.yMin or x <= block19.xMin - 5 or x >= block19.xMax - 5:
                                                                                            if y < block20.yMax + 10 or y > block20.yMin or x <= block20.xMin - 5 or x >= block20.xMax - 5:
                                                                                                if y < block21.yMax + 10 or y > block21.yMin or x <= block21.xMin - 5 or x >= block21.xMax - 5:
                                                                                                    if y < block22.yMax + 10 or y > block22.yMin or x <= block22.xMin - 5 or x >= block22.xMax - 5:
                                                                                                        if y < block23.yMax + 10 or y > block23.yMin or x <= block23.xMin - 5 or x >= block23.xMax - 5:
                                                                                                            if y < block24.yMax + 10 or y > block24.yMin or x <= block24.xMin - 5 or x >= block24.xMax - 5:
                                                                                                                if y < block25.yMax + 10 or y > block25.yMin or x <= block25.xMin - 5 or x >= block25.xMax - 5:
                                                                                                                    if y < block26.yMax + 10 or y > block26.yMin or x <= block26.xMin - 5 or x >= block26.xMax - 5:
                                                                                                                        if y < block27.yMax + 10 or y > block27.yMin or x <= block27.xMin - 5 or x >= block27.xMax - 5:
                                                                                                                            if y < block28.yMax + 10 or y > block28.yMin or x <= block28.xMin - 5 or x >= block28.xMax - 5:
                                                                                                                                if y < block29.yMax + 10 or y > block29.yMin or x <= block29.xMin - 5 or x >= block29.xMax - 5:
                                                                                                                                    if y < block30.yMax + 10 or y > block30.yMin or x <= block30.xMin - 5 or x >= block30.xMax - 5:
                                                                                                                                        if y < block31.yMax + 10 or y > block31.yMin or x <= block31.xMin - 5 or x >= block31.xMax - 5:
                                                                                                                                            if y < block32.yMax + 10 or y > block32.yMin or x <= block32.xMin - 5 or x >= block32.xMax - 5:
                                                                                                                                                if y < block33.yMax + 10 or y > block33.yMin or x <= block33.xMin - 5 or x >= block33.xMax - 5:
                                                                                                                                                    if y < block34.yMax + 10 or y > block34.yMin or x <= block34.xMin - 5 or x >= block34.xMax - 5:
                                                                                                                                                        if y < block35.yMax + 10 or y > block35.yMin or x <= block35.xMin - 5 or x >= block35.xMax - 5:
                                                                                                                                                            if y < block36.yMax + 10 or y > block36.yMin or x <= block36.xMin - 5 or x >= block36.xMax - 5:
                                                                                                                                                                if y < block37.yMax + 10 or y > block37.yMin or x <= block37.xMin - 5 or x >= block37.xMax - 5:
                                                                                                                                                                    if y < block38.yMax + 10 or y > block38.yMin or x <= block38.xMin - 5 or x >= block38.xMax - 5:
                                                                                                                                                                        if y < block39.yMax + 10 or y > block39.yMin or x <= block39.xMin - 5 or x >= block39.xMax - 5:
                                                                                                                                                                            if y < block40.yMax + 10 or y > block40.yMin or x <= block40.xMin - 5 or x >= block40.xMax - 5:
                                                                                                                                                                                if y < block41.yMax + 10 or y > block41.yMin or x <= block41.xMin - 5 or x >= block41.xMax - 5:
                                                                                                                                                                                    if y < block42.yMax + 10 or y > block42.yMin or x <= block42.xMin - 5 or x >= block42.xMax - 5:
                                                                                                                                                                                        y -= (jumpCount ** 2) / 5            
            else:
                    if y < trumpet1.yMax or x <= trumpet1.xMin or x >= trumpet1.xMax - 5:
                        if y < trumpet2.yMax or x <= trumpet2.xMin or x >= trumpet2.xMax - 5:
                            if y < trumpet3.yMax or x <= trumpet3.xMin or x >= trumpet3.xMax - 5:
                                if y < trumpet4.yMax or x <= trumpet4.xMin or x >= trumpet4.xMax - 5:
                                    if y < block1.yMax or x <= block1.xMin or x >= block1.xMax - 5:
                                        if y < block2.yMax or x <= block2.xMin or x >= block2.xMax - 5:
                                            if y < block3.yMax or x <= block3.xMin or x >= block3.xMax - 5: 
                                                if y < block4.yMax or x <= block4.xMin or x >= block4.xMax - 5:
                                                    if y < block5.yMax or x <= block5.xMin or x >= block5.xMax - 5:
                                                        if y < block6.yMax or x <= block6.xMin or x >= block6.xMax - 5:
                                                            if y < block7.yMax or x <= block7.xMin or x >= block7.xMax - 5: 
                                                                if y < block8.yMax or x <= block8.xMin or x >= block8.xMax - 5:
                                                                    if y < block9.yMax or x <= block9.xMin or x >= block9.xMax - 5:
                                                                        if y < block10.yMax or x <= block10.xMin or x >= block10.xMax - 5:
                                                                            if y < block11.yMax or x <= block11.xMin or x >= block11.xMax - 5:
                                                                                if y < block12.yMax or x <= block12.xMin or x >= block12.xMax - 5:
                                                                                    if y < block13.yMax or x <= block13.xMin or x >= block13.xMax - 5:
                                                                                        if y < block14.yMax or x <= block14.xMin or x >= block14.xMax - 5:
                                                                                            if y < block15.yMax or x <= block15.xMin or x >= block15.xMax - 5:
                                                                                                if y < block16.yMax or x <= block16.xMin or x >= block16.xMax - 5:
                                                                                                    if y < block17.yMax or x <= block17.xMin or x >= block17.xMax - 5:
                                                                                                        if y < block18.yMax or x <= block18.xMin or x >= block18.xMax - 5:
                                                                                                            if y < block19.yMax or x <= block19.xMin or x >= block19.xMax - 5: 
                                                                                                                if y < block20.yMax or x <= block20.xMin or x >= block20.xMax - 5:
                                                                                                                    if y < block21.yMax or x <= block21.xMin or x >= block21.xMax - 5: 
                                                                                                                        if y < block22.yMax or x <= block22.xMin or x >= block22.xMax - 5:
                                                                                                                            if y < block23.yMax or x <= block23.xMin or x >= block23.xMax - 5: 
                                                                                                                                if y < block24.yMax or x <= block24.xMin or x >= block24.xMax - 5 :
                                                                                                                                    if y < block25.yMax or x <= block25.xMin or x >= block25.xMax - 5:
                                                                                                                                        if y < block26.yMax or x <= block26.xMin or x >= block26.xMax - 5:
                                                                                                                                            if y < block27.yMax or x <= block27.xMin or x >= block27.xMax - 5: 
                                                                                                                                                if y < block28.yMax or x <= block28.xMin or x >= block28.xMax - 5:
                                                                                                                                                    if y < block29.yMax or x <= block29.xMin or x >= block29.xMax - 5: 
                                                                                                                                                        if y < block30.yMax or x <= block30.xMin or x >= block30.xMax - 5:
                                                                                                                                                            if y < block31.yMax or x <= block31.xMin or x >= block31.xMax - 5: 
                                                                                                                                                                if y < block32.yMax or x <= block32.xMin or x >= block32.xMax - 5:
                                                                                                                                                                    if y < block33.yMax or x <= block33.xMin or x >= block33.xMax - 5:
                                                                                                                                                                        if y < trumpet5.yMax or x <= trumpet5.xMin or x >= trumpet5.xMax - 5:
                                                                                                                                                                            if y < trumpet6.yMax or x <= trumpet6.xMin or x >= trumpet6.xMax - 5:
                                                                                                                                                                                if y < block34.yMax or x <= block34.xMin or x >= block34.xMax - 5:
                                                                                                                                                                                    #
                                                                                                                                                                                    if y < block35.yMax or x <= block35.xMin or x >= block35.xMax - 5:  
                                                                                                                                                                                        if y < block36.yMax or x <= block36.xMin or x >= block36.xMax - 5:  
                                                                                                                                                                                            if y < block37.yMax or x <= block37.xMin or x >= block37.xMax - 5: 
                                                                                                                                                                                                if y < block38.yMax or x <= block38.xMin or x >= block38.xMax - 5:  
                                                                                                                                                                                                    if y < block39.yMax or x <= block39.xMin or x >= block39.xMax - 5:    
                                                                                                                                                                                                        if y < block40.yMax or x <= block40.xMin or x >= block40.xMax - 5:  
                                                                                                                                                                                                            if y < block41.yMax or x <= block41.xMin or x >= block41.xMax - 5:  
                                                                                                                                                                                                                if y < block42.yMax or x <= block42.xMin or x >= block42.xMax - 5:                                                                            
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
                            if y > block1.yMin - 10 or y < block1.yMax or x <= block1.xMin + 20 or x >= block1.xMax - 20:
                                if y > block2.yMin - 10 or y < block2.yMax or x <= block2.xMin + 20 or x >= block2.xMax - 20:
                                    if y > block3.yMin - 10 or y < block3.yMax or x <= block3.xMin + 20 or x >= block3.xMax - 20:
                                        if y > block4.yMin - 10 or y < block4.yMax or x <= block4.xMin + 20 or x >= block4.xMax - 20:
                                            if y > block5.yMin - 10 or y < block5.yMax or x <= block5.xMin + 20 or x >= block5.xMax - 20:
                                                if y > block6.yMin - 10 or y < block6.yMax or x <= block6.xMin + 20 or x >= block6.xMax - 20:
                                                    if y > block7.yMin - 10 or y < block7.yMax or x <= block7.xMin + 20 or x >= block7.xMax - 20:
                                                        if y > block8.yMin - 10 or y < block8.yMax or x <= block8.xMin + 20 or x >= block8.xMax - 20:
                                                            if y > block9.yMin - 10 or y < block9.yMax or x <= block9.xMin + 20 or x >= block9.xMax - 20:
                                                                if y > block10.yMin - 10 or y < block10.yMax or x <= block10.xMin + 20 or x >= block10.xMax - 20:
                                                                    if y > block11.yMin - 10 or y < block11.yMax or x <= block11.xMin + 20 or x >= block11.xMax - 20:
                                                                        if y > block12.yMin - 10 or y < block12.yMax or x <= block12.xMin + 20 or x >= block12.xMax - 20:
                                                                            if y > block13.yMin - 10 or y < block13.yMax or x <= block13.xMin + 20 or x >= block13.xMax - 20:
                                                                                if y > block14.yMin - 10 or y < block14.yMax or x <= block14.xMin + 20 or x >= block14.xMax - 20:
                                                                                    if y > block15.yMin - 10 or y < block15.yMax or x <= block15.xMin + 20 or x >= block15.xMax - 20:
                                                                                        if y > block16.yMin - 10 or y < block16.yMax or x <= block16.xMin + 20 or x >= block16.xMax - 20:
                                                                                            if y > block17.yMin - 10 or y < block17.yMax or x <= block17.xMin + 20 or x >= block17.xMax - 20:
                                                                                                if y > block18.yMin - 10 or y < block18.yMax or x <= block18.xMin + 20 or x >= block18.xMax - 20:
                                                                                                    if y > block19.yMin - 10 or y < block19.yMax or x <= block19.xMin + 20 or x >= block19.xMax - 20:
                                                                                                        if y > block20.yMin - 10 or y < block20.yMax or x <= block20.xMin + 20 or x >= block20.xMax - 20:
                                                                                                            if y > block21.yMin - 10 or y < block21.yMax or x <= block21.xMin + 20 or x >= block21.xMax - 20:
                                                                                                                if y > block22.yMin - 10 or y < block22.yMax or x <= block22.xMin + 20 or x >= block22.xMax - 20:
                                                                                                                    if y > block23.yMin - 10 or y < block23.yMax or x <= block23.xMin + 20 or x >= block23.xMax - 20:
                                                                                                                        if y > block24.yMin - 10 or y < block24.yMax or x <= block24.xMin + 20 or x >= block24.xMax - 20:
                                                                                                                            if y > block25.yMin - 10 or y < block25.yMax or x <= block25.xMin + 20 or x >= block25.xMax - 20:
                                                                                                                                if y > block26.yMin - 10 or y < block26.yMax or x <= block26.xMin + 20 or x >= block26.xMax - 20:
                                                                                                                                    if y > block27.yMin - 10 or y < block27.yMax or x <= block27.xMin + 20 or x >= block27.xMax - 20:
                                                                                                                                        if y > block28.yMin - 10 or y < block28.yMax or x <= block28.xMin + 20 or x >= block28.xMax - 20:
                                                                                                                                            if y > block29.yMin - 10 or y < block29.yMax or x <= block29.xMin + 20 or x >= block29.xMax - 20:
                                                                                                                                                if y > block30.yMin - 10 or y < block30.yMax or x <= block30.xMin + 20 or x >= block30.xMax - 20:
                                                                                                                                                    if y > block31.yMin - 10 or y < block31.yMax or x <= block31.xMin + 20 or x >= block31.xMax - 20:
                                                                                                                                                        if y > block32.yMin - 10 or y < block32.yMax or x <= block32.xMin + 20 or x >= block32.xMax - 20:
                                                                                                                                                            if y > block33.yMin - 10 or y < block33.yMax or x <= block33.xMin + 20 or x >= block33.xMax - 20:
                                                                                                                                                                if y < trumpet5.yMax or x <= trumpet5.xMin or x >= trumpet5.xMax:
                                                                                                                                                                    if y < trumpet6.yMax or x <= trumpet6.xMin or x >= trumpet6.xMax:
                                                                                                                                                                        if y > block34.yMin - 10 or y < block34.yMax or x <= block34.xMin + 20 or x >= block34.xMax - 20:
                                                                                                                                                                            #
                                                                                                                                                                            if y > block35.yMin - 10 or y < block35.yMax or x <= block35.xMin + 20 or x >= block35.xMax - 20:
                                                                                                                                                                                if y > block36.yMin - 10 or y < block36.yMax or x <= block36.xMin + 20 or x >= block36.xMax - 20:
                                                                                                                                                                                    if y > block37.yMin - 10 or y < block37.yMax or x <= block37.xMin + 20 or x >= block37.xMax - 20:
                                                                                                                                                                                        if y > block38.yMin - 10 or y < block38.yMax or x <= block38.xMin + 20 or x >= block38.xMax - 20:
                                                                                                                                                                                            if y > block39.yMin - 10 or y < block39.yMax or x <= block39.xMin + 20 or x >= block39.xMax - 20:
                                                                                                                                                                                                if y > block40.yMin - 10 or y < block40.yMax or x <= block40.xMin + 20 or x >= block40.xMax - 20:
                                                                                                                                                                                                    if y > block41.yMin - 10 or y < block41.yMax or x <= block41.xMin + 20 or x >= block41.xMax - 20:
                                                                                                                                                                                                        if y > block42.yMin - 10 or y < block42.yMax or x <= block42.xMin + 20 or x >= block42.xMax - 20:
                                                                                                                                                                                                            if x >= pit1.xMin or x <= pit1.xMax:           
                                                                                                                                                                                                                DownUp = True
        else:
            DownUp = False

        if DownUp == True:
            if downCount >= 0.5:            
                if y < trumpet1.yMax or x <= trumpet1.xMin or x >= trumpet1.xMax:
                    if y < trumpet2.yMax or x <= trumpet2.xMin or x >= trumpet2.xMax:
                        if y < trumpet3.yMax or x <= trumpet3.xMin or x >= trumpet3.xMax:
                            if y < trumpet4.yMax or x <= trumpet4.xMin or x >= trumpet4.xMax:
                                if y > block1.yMin - 10 or y < block1.yMax or x <= block1.xMin or x >= block1.xMax:
                                    if y > block2.yMin - 10 or y < block2.yMax or x <= block2.xMin or x >= block2.xMax:
                                        if y > block3.yMin - 10 or y < block3.yMax or x <= block3.xMin or x >= block3.xMax: 
                                            if y > block4.yMin - 10 or y < block4.yMax or x <= block4.xMin or x >= block4.xMax:
                                                if y > block5.yMin - 10 or y < block5.yMax or x <= block5.xMin or x >= block5.xMax:
                                                    if y > block6.yMin - 10 or y < block6.yMax or x <= block6.xMin or x >= block6.xMax:
                                                        if y > block7.yMin - 10 or y < block7.yMax or x <= block7.xMin or x >= block7.xMax:
                                                            if y > block8.yMin - 10 or y < block8.yMax or x <= block8.xMin or x >= block8.xMax:
                                                                if y > block9.yMin - 10 or y < block9.yMax or x <= block9.xMin or x >= block9.xMax:
                                                                    if y > block10.yMin - 10 or y < block10.yMax or x <= block10.xMin or x >= block10.xMax:
                                                                        if y > block11.yMin - 10 or y < block11.yMax or x <= block11.xMin or x >= block11.xMax:
                                                                            if y > block12.yMin - 10 or y < block12.yMax or x <= block12.xMin or x >= block12.xMax:
                                                                                if y > block13.yMin - 10 or y < block13.yMax or x <= block13.xMin or x >= block13.xMax:
                                                                                    if y > block14.yMin - 10 or y < block14.yMax or x <= block14.xMin or x >= block14.xMax:
                                                                                        if y > block15.yMin - 10 or y < block15.yMax or x <= block15.xMin or x >= block15.xMax:
                                                                                            if y > block16.yMin - 10 or y < block16.yMax or x <= block16.xMin or x >= block16.xMax:
                                                                                                if y > block17.yMin - 10 or y < block17.yMax or x <= block17.xMin or x >= block17.xMax:
                                                                                                    if y > block18.yMin - 10 or y < block18.yMax or x <= block18.xMin or x >= block18.xMax:
                                                                                                        if y > block19.yMin - 10 or y < block19.yMax or x <= block19.xMin or x >= block19.xMax:
                                                                                                            if y > block20.yMin - 10 or y < block20.yMax or x <= block20.xMin or x >= block20.xMax:
                                                                                                                if y > block21.yMin - 10 or y < block21.yMax or x <= block21.xMin or x >= block21.xMax:
                                                                                                                    if y > block22.yMin - 10 or y < block22.yMax or x <= block22.xMin or x >= block22.xMax:
                                                                                                                        if y > block23.yMin - 10 or y < block23.yMax or x <= block23.xMin or x >= block23.xMax:
                                                                                                                            if y > block24.yMin - 10 or y < block24.yMax or x <= block24.xMin or x >= block24.xMax:
                                                                                                                                if y > block25.yMin - 10 or y < block25.yMax or x <= block25.xMin or x >= block25.xMax:
                                                                                                                                    if y > block26.yMin - 10 or y < block26.yMax or x <= block26.xMin or x >= block26.xMax:
                                                                                                                                        if y > block27.yMin - 10 or y < block27.yMax or x <= block27.xMin or x >= block27.xMax:
                                                                                                                                            if y > block28.yMin - 10 or y < block28.yMax or x <= block28.xMin or x >= block28.xMax:
                                                                                                                                                if y > block29.yMin - 10 or y < block29.yMax or x <= block29.xMin or x >= block29.xMax:
                                                                                                                                                    if y > block30.yMin - 10 or y < block30.yMax or x <= block30.xMin or x >= block30.xMax:
                                                                                                                                                        if y > block31.yMin - 10 or y < block31.yMax or x <= block31.xMin or x >= block31.xMax:
                                                                                                                                                            if y > block32.yMin - 10 or y < block32.yMax or x <= block32.xMin or x >= block32.xMax:
                                                                                                                                                                if y > block33.yMin - 10 or y < block33.yMax or x <= block33.xMin or x >= block33.xMax:
                                                                                                                                                                    if y < trumpet5.yMax or x <= trumpet5.xMin or x >= trumpet5.xMax:
                                                                                                                                                                        if y < trumpet6.yMax or x <= trumpet6.xMin or x >= trumpet6.xMax:
                                                                                                                                                                            if y > block34.yMin - 10 or y < block34.yMax or x <= block34.xMin or x >= block34.xMax:
                                                                                                                                                                                #
                                                                                                                                                                                if y > block35.yMin - 10 or y < block35.yMax or x <= block35.xMin or x >= block35.xMax:  
                                                                                                                                                                                    if y > block36.yMin - 10 or y < block36.yMax or x <= block36.xMin or x >= block36.xMax:
                                                                                                                                                                                        if y > block37.yMin - 10 or y < block37.yMax or x <= block37.xMin or x >= block37.xMax: 
                                                                                                                                                                                            if y > block38.yMin - 10 or y < block38.yMax or x <= block38.xMin or x >= block38.xMax:
                                                                                                                                                                                                if y > block39.yMin - 10 or y < block39.yMax or x <= block39.xMin or x >= block39.xMax:
                                                                                                                                                                                                    if y > block40.yMin - 10 or y < block40.yMax or x <= block40.xMin or x >= block40.xMax:
                                                                                                                                                                                                        if y > block41.yMin - 10 or y < block41.yMax or x <= block41.xMin or x >= block41.xMax:
                                                                                                                                                                                                            if y > block42.yMin - 10 or y < block42.yMax or x <= block42.xMin or x >= block42.xMax:                                                                                                                                                           
                                                                                                                                                                                                                if x >= pit1.xMin or x <= pit1.xMax:                       
                                                                                                                                                                                                                    y += (downCount ** 2) / 5
          
                downCount -= 0.5
# прыжок
            else:
                DownUp = False
                downCount = 7.5

#pit1.xMin = 2205
#pit1.xMax = 2245

#    if x >= pit1.xMin or x <= pit1.xMax : 
#        Down = True
#    else:
    if y > 365:
        y = 365


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
    
    if time <= 0 or y >= 448:
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
