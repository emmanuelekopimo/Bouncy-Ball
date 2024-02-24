import pygame

def invertColor(color):
    r = 255-color[0]
    g = 255-color[1]
    b = 255-color[2]
    return (r,g,b)

def collideRect(point, rect):
    x,y =point
    if x<rect.left:
        return False
    elif x>rect.right:
        return False
    elif y<rect.top:
        return False
    elif y>rect.bottom:
        return False
    else:
        return True
    
def collideRectSection(point, rect):
    xPosition, yPosition = rect.topleft
    width ,height = rect.width, rect.height
    surface = pygame.Surface((width,height))
    rect = surface.get_rect()
    pygame.draw.polygon(surface, (255,0,0),[rect.topleft,rect.center,rect.topright])
    pygame.draw.polygon(surface, (0,255,0),[rect.bottomleft,rect.center,rect.bottomright])
    pygame.draw.polygon(surface, (0,0,255),[rect.topleft,rect.center,rect.bottomleft])
    pygame.draw.polygon(surface, (255,255,0),[rect.bottomright,rect.center,rect.topright])
    nx , ny = point[0]-xPosition, point[1]-yPosition
    if nx==20:
        nx=19
    if ny==20:
        ny=19
    print(nx,ny)
    colorPicked = surface.get_at((nx,ny))
    if colorPicked==(255,0,0):
        return 'top'
    elif colorPicked==(0,255,0):
        return 'bottom'
    elif colorPicked==(0,0,255):
        return 'left'
    elif colorPicked==(255,255,0):
        return 'right'
    else:
        print('Polygon detection failed')
        