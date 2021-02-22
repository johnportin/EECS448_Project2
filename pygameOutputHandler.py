"""
Current plans:
-Finish modyfying pyboard code to function with new ruleset[ ]
--Setup method[ ]
---piece dictionary[ ]
---sprite dictionary[ ]

-Draw empty board[ ]
--choose colors[ ]
--place extra details[ ]


-Create parser for game logic[ ]
--create update method to replace board.command[]
-create method for game logic to pass in data[ ]


Stretch Goals:
-Figure out async, as its applications seem incredible[ ]
--async FX method to tie to mouse position[ ]
--async animation method for on click stuff


Misc Goals:
-Make/find assets[ ]
--fill folder and test assets collecting
-modify piece class[ ]
--color modification
--transperancy key (see pygame surface color key)
-Look through pygame for other 


"""

from time import sleep
import pygame as p
import glob
import os

from pygame import event

p.init()

class Piece(p.sprite.Sprite):
    def __init__(self,png,pos):
        super(Piece,self).__init__()
        self.surf = p.image.load(png)
        self.rect = self.surf.get_rect()
        self.rect.center = pos
        p.Surface.set_colorkey(self.surf,[0,0,0])

    def update(self,move):
        self.rect.center = move



class pyBoard:
    assetNameKeys = ["BS 1","BS 2","BS 3","BS 4","BS 5","BS 6","hit","miss"]
    ships = ["x1","x2","x3","x4","x5","x6"]
    
    def __init__(self,assetsFolderPath = "/Assets/",screen = (850,850)):
        #PNG Info. Basically, I'm just digging through the provided assets folder and seeing if
        #it gives me anything containing my assetNameKeys, if it finds them, it stores that path
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #with my key in a dictionary. 
        print(dir_path)
        print(assetsFolderPath)

        assetsFolder = glob.glob(dir_path + assetsFolderPath + "*")
        self.assetsList = {}
        for asset in assetsFolder:
            for key in self.assetNameKeys:
                if(asset.find(key) != -1):
                    self.assetsList[key] = asset
        
        for ass in self.assetsList.keys():
            print(ass)

        #CleanPlate info. Basically, this will be what I use to draw an empty board each frame.
        #I May make this customizable later
        self.screenDim = screen
        self.boardDim = p.Rect(50,50,screen[0]-100, screen[1]-100)
        self.lineSpace = screen[0]/10
        self.letters = ["A","B","C","D","E","F","G","H","I","J"]
        self.numbers = ["1","2","3","4","5","6","7","8","9","10"]

        #Live Info
        self.spriteDict = {}
        self.spritePos = {}
        self.coordDict = {}
        self.gameBegin = 1#1 = game setup, 0 = game ready
        self.turn = 0 

        #creates an empty dictionary for checking whats at a given coordinate, used with piece dictionary
        for x in range(10):
            for y in range(10):
                c = str(x) + "," + str(y)
                self.coordDict[c] = ""
    

    #Used to place text on screen
    def text_objects(self,text,font):
        textSurface = font.render(text,True,(0,0,0))
        return textSurface, textSurface.get_rect()

    #Adds letters and numbers to screen
    def placeGridLabels(self):
        textType = p.font.Font('freesansbold.ttf', 20)
        for letter in self.letters:
            textSurf, textRect = self.text_objects(letter, textType)
            x = ord(letter) - 65
            pos = x*75 + 87
            textRect.center = (pos, 825)
            self.screen.blit(textSurf,textRect)

        for number in self.numbers:
            textSurf, textRect = self.text_objects(number, textType)
            x = int(number) - 1
            pos = 760- x*75
            textRect.center = (25, pos)
            self.screen.blit(textSurf,textRect)

    #Quick helper function for getting board coordinates
    def coordToBoard(self,coord):
        x = 87.5 + coord[0]*75
        y = 87.5 + coord[1]*75
        return((x,y))

    #Unused for time being :(
    def createPieceDicts(self, player):
        for piece in self.ships:
            for x in range(8):
                key = str(piece) + str(player)
                if piece == "pW":
                    coordX = x
                    coordY = 6
                    pos = (coordX,coordY)
                if piece == "pG":
                    coordX = x
                    coordY = 1
                    pos = (coordX,coordY)
                self.spritePos[key] = pos
                cKey = str(pos[0]) + "," + str(pos[1])
                self.coordDict[cKey] = key


    #Creates a sprite at coordinate to represent hit or miss
    def addShot(self,mark,coord):
        if(mark == "hit"):
            png = self.assetsList["hit"]
        else:
            png = self.assetsList["miss"]
        pos = self.coordToBoard(coord)
        self.spriteDict[str(self.turn)] = Piece(png, pos)
        self.turn += 1
          
    #Used to draw the initial board           
    def drawBoard(self):
        self.screen.fill((128,128,128))
        p.draw.rect(self.screen,(83,209,212),self.boardDim)

        for x in range(0,11):
            xPos = 50+(x)*75
            p.draw.line(self.screen, (0,0,0), (xPos,50), (xPos,800))

        for x in range(0,11):
            yPos = 50+(x)*75
            p.draw.line(self.screen, (0,0,0), (50,yPos), (800,yPos))

    #Function used to redraw the board per frame of game
    def createCleanPlate(self):
        self.drawBoard()
        self.placeGridLabels()
        

    #Function used to update the board per game interraction
    def __updateBoard(self):
        self.screen.fill((0,0,0))
        self.createCleanPlate()
        for x in self.spritePos:
            self.screen.blit(self.spriteDict[x].surf, self.spriteDict[x].rect)


    #Prints current game info
    def printInfo(self):
        print(self.coordDict)
        print(self.spritePos)

        
    #Called on start of game, contains info from setup.txt
    def beginGame(self,packet):
        self.screen = p.display.set_mode(size = (850,850))
        gameName = packet[0]
        p.display.set_caption(gameName)
        icon = p.image.load(packet[1])
        p.display.set_icon(icon)
        self.gameBegin = 1
        self.createCleanPlate()
        p.display.flip()

    #Will place ships, unnessecary for now
    def placeShips(self,ships,player):
        self.createPieceDicts(player)
        self.createPieceSurf(player)
        for ship in ships:
            print(ship)

    #prompts user to exit
    def quitGame(self):
        run = True
        print("X out of the window now")
        while run:
            for event in p.event.get():
                if event.type == p.QUIT:
                    print("trying to quit")
                    run = False
        p.quit()

    #Bublic facing update call, will eventually use extra info 
    def updateBoard(self):
        self.__updateBoard()
        p.display.flip()



