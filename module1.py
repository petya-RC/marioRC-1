import pygame
import os


file_path = os.path.dirname(__file__)

pygame.mixer.music.load((file_path + "\saundtrek.mp3"))
pygame.mixer.music.set_volume(0.05)


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
















