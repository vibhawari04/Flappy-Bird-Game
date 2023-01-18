import pygame

def button(screen,position,text,size,colors="white on black"):
    fg,bg=colors.split(" on ")
    font=pygame.font.SysFont("calibri",size)
    text_render=font.render(text,1,fg,bg)
    x,y,w,h=text_render.get_rect()
    x,y=position

    pygame.draw.line(screen,(150,150,150),(x,y),(x+w,y),5,)
    pygame.draw.line(screen,(150, 150, 150),(x, y-2), (x,y+h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y+h), (x + w, y+h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x+w, y+h), [x + w, y], 5)
    pygame.draw.rect(screen,(100,100,100),(x,y,w,h))

    return screen.blit(text_render,(x,y))