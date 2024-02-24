import pygame, random, math
import utils, constants

class soloScene(object):
    def __init__(self, playAreaRect, ballSpeed, batRank, levelRes):
        self.levelRes = levelRes
        self.ballSpeed = ballSpeed
        self.rect = playAreaRect
        self.batStartPos = self.rect.centerx, self.rect.bottom
        self.playerBat = bottomBat(self.batStartPos, self.rect, batRank, self.levelRes['bats'])
        ball = Ball(self.ballSpeed, self.playerBat.rect.centerx, self.playerBat.rect.top, self.levelRes['balls'])
        ball.yDirection = -1
        
        
        self.blocks = []
        self.balls = [ball,]
        self.powerUps = []
        self.current = constants.PLAYING
        self.life = 3
        
    def update(self, events, pressedKeys, mouseState, mousePosition):
        if self.current == constants.PLAYING: 
            self.playerBat.update(pressedKeys, self.balls) # Update bat
                
            for ball in self.balls:
                ball.update(self.blocks, self.powerUps) # Update ball
                if ball.rect.left<0:
                    ball.xDirection = 1
                if ball.rect.right>self.rect.right:
                    ball.xDirection = -1
                if ball.rect.top<0:
                    ball.yDirection = 1
                if ball.rect.top > constants.SCREEN_HEIGHT:
                        self.balls.remove(ball)
                            
                if len(self.balls)==0:
                    if self.life > 0:
                        self.life -= 1
                        self.balls.clear()
                        self.powerUps.clear()
                        newBall = Ball(self.ballSpeed, self.playerBat.rect.centerx, self.playerBat.rect.top, self.levelRes['balls'])
                        self.balls.append(newBall)
                    else:
                        self.current = constants.FAILED
            for powerUp in self.powerUps:
                powerUp.update()
                if self.playerBat.rect.collidepoint(powerUp.rect.center):
                    self.powerUps.remove(powerUp)
                    if powerUp.type == constants.ADD3:
                        ball1 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball2 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball3 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball1.rect.centerx = self.playerBat.rect.centerx
                        ball2.rect.centerx = self.playerBat.rect.centerx
                        ball3.rect.centerx = self.playerBat.rect.centerx
                        ball1.rect.bottom = self.playerBat.rect.top
                        ball2.rect.bottom = self.playerBat.rect.top
                        ball3.rect.bottom = self.playerBat.rect.top
                        ball1.angle = 45
                        ball2.angle = 90
                        ball3.angle = 45
                        ball1.xDirection, ball1.yDirection = 1, -1
                        ball2.xDirection, ball2.yDirection = 1, -1
                        ball3.xDirection, ball3.yDirection = -1, -1
                        self.balls.append(ball1)
                        self.balls.append(ball2)
                        self.balls.append(ball3)

                    elif powerUp.type == constants.ADD5:
                        ball1 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball2 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball3 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball4 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball5 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                        ball1.rect.centerx = self.playerBat.rect.centerx
                        ball2.rect.centerx = self.playerBat.rect.centerx
                        ball3.rect.centerx = self.playerBat.rect.centerx
                        ball4.rect.centerx = self.playerBat.rect.centerx
                        ball5.rect.centerx = self.playerBat.rect.centerx
                        ball1.rect.bottom = self.playerBat.rect.top
                        ball2.rect.bottom = self.playerBat.rect.top
                        ball3.rect.bottom = self.playerBat.rect.top
                        ball4.rect.bottom = self.playerBat.rect.top
                        ball5.rect.bottom = self.playerBat.rect.top
                        ball1.angle = 45
                        ball2.angle = 60
                        ball3.angle = 90
                        ball4.angle = 60
                        ball5.angle = 45
                        ball1.xDirection, ball1.yDirection = 1, -1
                        ball2.xDirection, ball2.yDirection = 1, -1
                        ball3.xDirection, ball3.yDirection = 1, -1
                        ball5.xDirection, ball3.yDirection = -1, -1
                        ball4.xDirection, ball3.yDirection = -1, -1
                        self.balls.append(ball1)
                        self.balls.append(ball2)
                        self.balls.append(ball3)
                        self.balls.append(ball4)
                        self.balls.append(ball5)

                    elif powerUp.type == constants.MULTIPLY3:
                        count = 0
                        balls = len(self.balls)
                        for ball in self.balls:
                            count +=1
                            ball1 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball2 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball3 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball1.rect.center = ball.rect.center
                            ball2.rect.center = ball.rect.center
                            ball3.rect.center = ball.rect.center
                            ball1.angle = 90
                            ball2.angle = 30
                            ball3.angle = 30
                            ball1.xDirection, ball1.yDirection = 1, -1
                            ball2.xDirection, ball2.yDirection = 1, 1
                            ball3.xDirection, ball3.yDirection = -1, 1
                            self.balls.append(ball1)
                            self.balls.append(ball2)
                            self.balls.append(ball3)
                            if balls == count:
                                break
                    
                    elif powerUp.type == constants.MULTIPLY5:
                        count = 0
                        balls = len(self.balls)
                        for ball in self.balls:
                            count +=1
                            ball1 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball2 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball3 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball4 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball5 = Ball(self.ballSpeed, 0,0, self.levelRes['balls'])
                            ball1.rect.center = ball.rect.center
                            ball2.rect.center = ball.rect.center
                            ball3.rect.center = ball.rect.center
                            ball4.rect.center = ball.rect.center
                            ball5.rect.center = ball.rect.center
                            ball1.angle = 90
                            ball2.angle = 18
                            ball3.angle = 54
                            ball4.angle = 54
                            ball5.angle = 18
                            ball1.xDirection, ball1.yDirection = 1, -1
                            ball2.xDirection, ball2.yDirection = 1, -1
                            ball3.xDirection, ball3.yDirection = 1, 1
                            ball4.xDirection, ball4.yDirection = -1, 1
                            ball5.xDirection, ball5.yDirection = -1, -1
                            self.balls.append(ball1)
                            self.balls.append(ball2)
                            self.balls.append(ball3)
                            self.balls.append(ball4)
                            self.balls.append(ball5)
                            if balls == count:
                                break
                            
                if not powerUp.active:
                    self.powerUps.remove(powerUp)
        elif self.current == constants.FAILED:
            pass
    
    def renderForeGround(self, surface):
        self.playerBat.render(surface) # Render player 
        for ball in self.balls:
            ball.render(surface)
        for block in self.blocks:
            block.render(surface)
        for powerUp in self.powerUps:
                powerUp.render(surface)
        
        
class Ball(object):
    def __init__(self, speed, xPosition, yPosition, levelRes):
        self.speed = speed
        self.levelRes = levelRes
        self.angle =  75
        self.xDirection = random.choice([-1,1])
        self.yDirection = random.choice([-1,1])
        self.rect = self.levelRes['ball'].get_rect()
        self.rect.center = (xPosition,yPosition)

        
    def update(self, blocks, powerUps):
        xResolved = math.cos(math.radians(self.angle))*self.speed*self.xDirection
        yResolved = math.sin(math.radians(self.angle))*self.speed*self.yDirection
        self.rect.move_ip(xResolved, yResolved)
        edges = [(self.rect.left+3,self.rect.top+3),(self.rect.right-3,self.rect.top+3),
                 (self.rect.left+3,self.rect.bottom-3),(self.rect.right-3,self.rect.bottom-3),
                 (self.rect.left,self.rect.centery),(self.rect.right,self.rect.centery),
                 (self.rect.centerx,self.rect.top),(self.rect.centerx,self.rect.bottom)]
        for block in blocks:
            for edge in edges:
                if utils.collideRect(edge, block.rect):
                    self.collideBlock(block, blocks, powerUps)
                    primaryDiagonal = self.rect.centerx + block.positiveDiagonal
                    secondaryDiagonal = - self.rect.centerx + block.negativeDiagonal
                    if self.rect.centery <= primaryDiagonal:
                        # Above primary diagonal
                        if self.rect.centery <= secondaryDiagonal:
                            # Above secondary diagonal
                            # Top section
                            self.yDirection = -1
                            break
                        elif self.rect.centery > secondaryDiagonal:
                            # Below secondary diagonal
                            # Right section
                            self.xDirection = 1
                            break
                    elif self.rect.centery > primaryDiagonal:
                        # Below primary diagonal
                        if self.rect.centery <= secondaryDiagonal:
                            # Above secondary diagonal
                            # Left section
                            self.xDirection = -1
                            break
                        elif self.rect.centery > secondaryDiagonal:
                            # Below secondary diagonal
                            # Bottom section
                            self.yDirection = 1
                            break
                    
                    
    def render(self, surface):
        surface.blit(self.levelRes['ball'], self.rect)
        
    def collideBlock(self, block, blockList, powerUps):
        if block.rank == -1:
            return
        else:
            block.rank -=1
            if block.rank == 0:
                blockList.remove(block)
                for powerUp in block.powerUps:
                    powerUps.append(powerUp)
                
            
        
class Block(object):
    def __init__(self, position, rank, levelRes):
        self.levelRes = levelRes # Required resources
        self.rank = rank # Rank (to detect type of block)
        x , y = position[0]*20, position[1]*20 # Position on screen
        self.rect = pygame.Rect(x, y, constants.BLOCK_WIDTH, constants.BLOCK_HEIGHT) # Bounding rectangle
        self.positiveDiagonal = self.rect.centery - self.rect.centerx
        self.negativeDiagonal = self.rect.centerx + self.rect.centery
        self.powerUps = []
                
    def update(self):
        pass
    
    def render(self, surface):
        surface.blit(self.levelRes['block'+str(self.rank)],self.rect)

class PowerUp(object):
    def __init__(self, type, position, levelRes):
        self.type = type
        self.surface = levelRes[self.type]
        self.rect= self.surface.get_rect()
        self.rect.center = position
        self.speed = self.type + random.randint(0,4)
        self.active = True
        
    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.top > constants.SCREEN_HEIGHT:
            self.active = False
    
    def render(self, surface):
        surface.blit(self.surface, self.rect)
        
class bottomBat(object):
    def __init__(self, startPos, playAreaRect, rank, levelRes):
        self.playAreaRect = playAreaRect # Play area rectangle
        self.startPos = startPos # Bat Start position
        self.speed = 2+rank # Bat Speed
        self.rank = rank
        self.surface = levelRes['bat'+str(self.rank)]
        self.rect = self.surface.get_rect()
        self.rect.centerx, self.rect.bottom = self.startPos # Position rectangle
        
    def update(self, pressedKeys, balls):
        # Handle key down
        if pressedKeys[pygame.K_LEFT] and self.rect.left > self.playAreaRect.left:
            self.rect.move_ip(-self.speed, 0)
            
        elif pressedKeys[pygame.K_RIGHT] and self.rect.right < self.playAreaRect.right:
            self.rect.move_ip(self.speed, 0)
        
        # Handle excess movements
        if self.rect.left < self.playAreaRect.left:
            self.rect.left = self.playAreaRect.left
        if self.rect.right > self.playAreaRect.right:
            self.rect.right = self.playAreaRect.right
        
        # Ball-to-bat collision dectection and respective deflection   
        for ball in balls:
            x,y = ball.rect.centerx, ball.rect.bottom # Ball center
            if self.rect.collidepoint(x,y):
                ball.rect.bottom = self.rect.top
                ball.yDirection = -1
                displacement = abs(ball.rect.centerx-self.rect.centerx)
                angleDeflect = int(round(displacement/constants.MAX_BAT_DISPLACEMENT*30, 0))
                if ball.rect.centerx>self.rect.centerx:
                    if ball.xDirection==1:
                        ball.angle-=angleDeflect
                        if ball.angle<15:
                            ball.angle=15
                    if ball.xDirection==-1:
                        ball.angle+=angleDeflect
                        if ball.angle>75:
                            ball.angle=75
                if ball.rect.centerx<self.rect.centerx:
                    if ball.xDirection==-1:
                        ball.angle-=angleDeflect
                        if ball.angle<15:
                            ball.angle=15
                    if ball.xDirection==1:
                        ball.angle+=angleDeflect
                        if ball.angle>75:
                            ball.angle=75
    
    def render(self, surface):
        surface.blit(self.surface, self.rect)