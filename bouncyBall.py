import random
import pygame, os
import gameObjects, userInterface, recordMgtSystem, constants

class BouncyBall(object):
    def __init__(self):
        # Initializations
        pygame.init() # Initialize pygame module
        pygame.display.set_caption('Bouncy Ball') # Set display caption
        self.screenWidth = constants.SCREEN_WIDTH # Screen width
        self.screenHeight = constants.SCREEN_HEIGHT # Screen height
        self.bitDepth = 32 # Display bit depth
        self.displayFlags = 0 # No display flags(0)
        self.frameRate = 45 # Game frame rate(fps)
        '''Create display'''
        self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight),self.displayFlags,self.bitDepth)
        self.clock = pygame.time.Clock() # Create clock object for time functions
        
        # Minor loadings
        '''
        load icon
        load loading scene
        '''
        
        # Before loop initializations
        self.running = True
        self.sceneId = 'loading'
        self.gameScene = None # Game Scene (Loaded level)
        self.playAreaRect = pygame.Rect(0,0,660,660)
        self.testAudio()
        self.loadAudio()
        self.playMusic()
        
        self.levelRes = {}
        self.loadImages()
        self.loadLevel()
        
    def run(self):
        # Game loop
        while self.running:
            self.screen.fill((255,255,255))# Clear screen
            
            self.events = pygame.event.get()
            self.pressedKeys = pygame.key.get_pressed()
            self.mouseState = pygame.mouse.get_pressed()
            self.mousePosition = pygame.mouse.get_pos()
            
            # Event handling
            for event in self.events:
                # Handle exit event
                if event.type == pygame.QUIT:
                    self.running = False
                    continue
                
                
            # Scenes
            if self.sceneId == 'loading':
                # update and render
                pass
            
            elif self.sceneId == 'gameScene':
                self.gameScene.update(self.events, self.pressedKeys, self.mouseState, self.mousePosition)
                self.screen.blit(self.images['gameBackground'],(0,0)) # Render background
                self.screen.blit(self.images['soloSideBar'],(660,0))
                self.gameScene.renderForeGround(self.screen)
                
            pygame.display.update()
            self.clock.tick(self.frameRate)
            
    def exit(self):
        # Clean up memory and close all theads
        pass
    
    def loadImages(self):
        self.images = {
            'gameBackground' : pygame.image.load('res/backgrounds/bg-1.png'),
            'soloSideBar' : pygame.image.load('res/backgrounds/solo.png')
            
            
        }
        self.levelRes['blocks']={
            'block1' : pygame.image.load('res/blocks/block1.png'),
            'block-1' : pygame.image.load('res/blocks/block-1.png'),
            'block2' : pygame.image.load('res/blocks/block2.png'),
            'block3' : pygame.image.load('res/blocks/block3.png'),
            'block4' : pygame.image.load('res/blocks/block4.png'),
            'block5' : pygame.image.load('res/blocks/block5.png')
        }
        self.levelRes['balls'] = {
            'ball': pygame.image.load('res/balls/ball.png')
        }
        self.levelRes['bats'] = {
            'bat1' : pygame.image.load('res/bats/bat1.png'),
            'bat2' : pygame.image.load('res/bats/bat2.png'),
            'bat3' : pygame.image.load('res/bats/bat3.png'),
            'bat4' : pygame.image.load('res/bats/bat4.png'),
            'bat5' : pygame.image.load('res/bats/bat5.png'),
            'bat6' : pygame.image.load('res/bats/bat6.png'),
            'bat7' : pygame.image.load('res/bats/bat7.png'),
            'bat8' : pygame.image.load('res/bats/bat8.png')
        }
        self.levelRes['powerUps'] = {
            constants.ADD3 : pygame.image.load('res/powerups/add3.png'),
            constants.ADD5 : pygame.image.load('res/powerups/add5.png'),
            constants.MULTIPLY3 : pygame.image.load('res/powerups/multiply3.png'),
            constants.MULTIPLY5 : pygame.image.load('res/powerups/multiply5.png'),
            constants.ADDLIFE : pygame.image.load('res/powerups/addlife.png')
            
        }
    
    def testAudio(self):
        try:
            pygame.mixer.init()
            self.audio = True
        except:
            self.audio = False
    
    def playMusic(self):
        if self.audio:
            pygame.mixer.music.play(-1)
            
    def loadAudio(self):
        if self.audio:
            self.sounds = {
            
            }
            self.music = pygame.mixer.music.load('res/audio/monody.wav')
        
    def loadScenes(self):
        pass
        
    def loadLevel(self):
        mode = 'solo'
        level = '1'
        batRank = 1
        if mode == 'solo': 
            with open('res/levels/solo/level_'+level+'.inf')as gameFile:
                content = gameFile.readlines()
                speedInfo = content[0].split(',')
                addInfo = content[1].split(',')
                multipyInfo = content[2].split(',')
                extraInfo = content[3].split(',')
                initSpeed , maxSpeed = int(speedInfo[0]), int(speedInfo[1])
                add3, add5 = int(addInfo[0]), int(addInfo[1])
                multiply3, multiply5 = int(multipyInfo[0]), int(multipyInfo[1])
                addLife  = int(extraInfo[0])
                
            # Game scene
            self.gameScene = gameObjects.soloScene(self.playAreaRect, initSpeed, batRank, self.levelRes)
            
            matrixData = pygame.image.load('res/levels/solo/level_'+level+'.png')
            matrixWidth = matrixData.get_width()
            matrixHeight = matrixData.get_height()
            
            for y in range(matrixHeight):
                for x in range(matrixWidth):
                    color = matrixData.get_at((x,y))
                    if color == (0,255,0): # Normal block
                        block = gameObjects.Block((x,y),1,self.levelRes['blocks'])
                        self.gameScene.blocks.append(block)
                    elif color == (0,0,0): #  Grey undestroyable block
                        self.gameScene.blocks.append(gameObjects.Block((x,y),-1,self.levelRes['blocks']))
                    elif color == (0,255,255): # Sky blue block
                        block = gameObjects.Block((x,y),2,self.levelRes['blocks'])
                        self.gameScene.blocks.append(block)
                    elif color == (255,255,0): # Yellow block
                        block = gameObjects.Block((x,y),3,self.levelRes['blocks'])
                        self.gameScene.blocks.append(block)
                    elif color == (255,127,0): # Orange block
                        block = gameObjects.Block((x,y),4,self.levelRes['blocks'])
                        self.gameScene.blocks.append(block)
                    elif color == (255,0,0): # Red block
                        block = gameObjects.Block((x,y),5,self.levelRes['blocks'])
                        self.gameScene.blocks.append(block)
            
            blocks = len(self.gameScene.blocks)
            for i in range(add3):
                randomBlock = self.gameScene.blocks[random.randrange(blocks)]
                powerUp = gameObjects.PowerUp(constants.ADD3, randomBlock.rect.center, self.levelRes['powerUps'])
                randomBlock.powerUps.append(powerUp)
            for i in range(add5):
                randomBlock = self.gameScene.blocks[random.randrange(blocks)]
                powerUp = gameObjects.PowerUp(constants.ADD5, randomBlock.rect.center, self.levelRes['powerUps'])
                randomBlock.powerUps.append(powerUp)
            for i in range(multiply3):
                randomBlock = self.gameScene.blocks[random.randrange(blocks)]
                powerUp = gameObjects.PowerUp(constants.MULTIPLY3, randomBlock.rect.center, self.levelRes['powerUps'])
                randomBlock.powerUps.append(powerUp)
            for i in range(multiply5):
                randomBlock = self.gameScene.blocks[random.randrange(blocks)]
                powerUp = gameObjects.PowerUp(constants.MULTIPLY5, randomBlock.rect.center, self.levelRes['powerUps'])
                randomBlock.powerUps.append(powerUp)
            for i in range(addLife):
                randomBlock = self.gameScene.blocks[random.randrange(blocks)]
                powerUp = gameObjects.PowerUp(constants.ADDLIFE, randomBlock.rect.center, self.levelRes['powerUps'])
                randomBlock.powerUps.append(powerUp)
                
            self.sceneId = 'gameScene'
        
            
    
    
    
bouncyBall = BouncyBall()
bouncyBall.run()
bouncyBall.exit()
