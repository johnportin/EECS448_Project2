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

p.init()

class Piece(p.sprite.Sprite):
    def __init__(self,png,pos):
        super(Piece,self).__init__()
        self.surf = p.image.load(png)
        self.rect = self.surf.get_rect()
        self.rect.center = pos

    def update(self,move):
        self.rect.center = move

class pyBoard:
    assetNameKeys = ["x1","x2","x3","x4","x5","x6","player1","player2","hit","miss"]
    playersList = ["p1","p2"]
    ships = ["x1","x2","x3","x4","x5","x6"]
    
    def __init__(self,assetsFolderPath = "/defaultAssets/"):
        
        #PNG Info. Basically, I'm just digging through the provided assets folder and seeing if
        #it gives me anything containing my assetNameKeys, if it finds them, it stores that path
        #with my key in a dictionary. 
        assetsFolder = glob.Glob(assetsFolderPath)
        self.assetsList = {}
        for asset in assetsFolder:
            print(asset)
            for key in self.assetNameKeys:
                if(asset.find(key) != -1):
                    self.assetsList[key] = asset

        #If an asset is not found, this will insert our own default asset, I'll add error handling later for if they delete that
        for key in self.assetNameKeys:
            if(self.assetsList.get(key) == None):
                self.assetsList[key] = "/defaultAssets/" + key 


        #CleanPlate info. Basically, this will be what I use to draw an empty board each frame.
        #I May make this customizable later
        self.screenDim = [800,800]
        self.boardDim = [600,600]
        self.lineSpace = 75
        self.letters = ["A","B","C","D","E","F","G","H","I","J"]
        self.numbers = ["1","2","3","4","5","6","7","8","9","10"]

        #Live Info
        self.spriteDict = {}
        self.spritePos = {}
        self.coordDict = {}



        self.screen = p.display.set_mode(self.screenDim)
        self.board = p.Rect((100,100),self.boardDim)
        
        #creates an empty dictionary for checking whats at a given coordinate, used with piece dictionary
        for x in range(10):
            for y in range(10):
                c = str(x) + "," + str(y)
                self.coordDict[c] = ""
    
        
    

    def text_objects(self,text,font):
        textSurface = font.render(text,True,(0,0,0))
        return textSurface, textSurface.get_rect()

    def placeGridLabels(self):
        textType = p.font.Font('freesansbold.ttf', 20)
        for letter in self.letters:
            textSurf, textRect = self.text_objects(letter, textType)
            x = ord(letter) - 65
            pos = x*75 + 137
            textRect.center = (pos, 720)
            self.screen.blit(textSurf,textRect)

        for number in self.numbers:
            textSurf, textRect = self.text_objects(number, textType)
            x = int(number) - 1
            pos = 663- x*75
            textRect.center = (80, pos)
            self.screen.blit(textSurf,textRect)

    def coordToBoard(self,coord):
        x = 137 + coord[0]*75
        y = 137 + coord[1]*75
        return((x,y))

    def createPieceDicts(self):
        for piece in self.pawnList:
            for x in range(8):
                key = str(piece) + str(x)
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


        for piece in self.pieceList:
            for x in range(2):
                key = str(piece) + str(x)
                if key[0] == "b":
                    coordX = 2+x*3
                elif key[0] == "r":
                    coordX = 7*x
                elif key[0] == "h":
                    coordX = 1+x*5

                if key[1] == "W":
                    coordY = 7
                else:
                    coordY = 0

                pos = (coordX,coordY)
                self.spritePos[key] = pos
                cKey = str(pos[0]) + "," + str(pos[1])
                self.coordDict[cKey] = key

        for piece in self.royalList:
            key = str(piece)
            if key == "kW":
                pos = (4,7)
            elif key == "qW":
                pos = (3,7)
            elif key == "kG":
                pos = (4,0)
            elif key == "qG":
                pos = (3,0)

            self.spritePos[key] = pos
            cKey = str(pos[0]) + "," + str(pos[1])
            self.coordDict[cKey] = key

    #From Chessboard, only for reference
    def createPieceSurf(self):
        for x in self.spritePos:
            t = x[0] + x[1]
            if t == "kW":
                png = self.kWPNG
            elif t == "kG":
                png = self.kGPNG
            elif t == "pW":
                png = self.pWPNG
            elif t == "pG":
                png = self.pGPNG
            elif t == "rW":
                png = self.rWPNG
            elif t == "rG":
                png = self.rGPNG
            elif t == "hW":
                png = self.hWPNG
            elif t == "hG":
                png = self.hGPNG
            elif t == "qW":
                png = self.qWPNG
            elif t == "qG":
                png = self.qGPNG
            elif t == "bW":
                png = self.bWPNG
            elif t == "bG":
                png = self.bGPNG

            boardPos = self.coordToBoard(self.spritePos[x])
            self.spriteDict[x] = Piece(png, boardPos)

            
                
    def drawBoard(self):
        self.screen.fill((62,187,56))

        p.draw.rect(self.screen,(187,147,56),self.board)

        for x in range(1,8):
            xPos = 100+(x)*75
            p.draw.line(self.screen, (0,0,0), (xPos,100), (xPos,700))

        for x in range(1,8):
            yPos = 100+(x)*75
            p.draw.line(self.screen, (0,0,0), (100,yPos), (700,yPos))

    def createCleanPlate(self):
        self.drawBoard()
        self.placeGridLabels()
        self.createPieceDicts()

    def updateBoard(self):
        self.screen.fill((0,0,0))
        self.createCleanPlate()
        for x in self.spritePos:
            self.screen.blit(self.spriteDict[x].surf, self.spriteDict[x].rect)


    def printInfo(self):
        print(self.coordDict)
        print(self.spritePos)

        
    #From Chessboard, only for reference
    def move(self,movement):
        x1 = ord(movement[0][0]) - 65
        y1 = 8 - int(movement[0][1])
        x2 = ord(movement[1][0]) - 65
        y2 = 8 - int(movement[1][1])
        start = str(x1) + "," + str(y1)
        key = self.coordDict[start]
        end = self.coordToBoard((x2,y2))
        self.spriteDict[key].update(end)
        self.coordDict[start] = ""
        fin = str(x2) + "," + str(y2)
        self.coordDict[fin] = key
        self.updateBoard()

    def beginGame(function):
        print("HAHA")

    def command(self, *args):
        if(args[0] == "Move"):
            self.move(args[1])
            p.display.flip()
        elif(args[0] == "Scream"):
            self.printInfo()
        elif(args[0] == "GraveMove"):
            self.graveMove(args[1])
            p.display.flip()
        elif(args[0] == "Start"):
            self.createCleanPlate()
            self.createPieceSurf()
            self.updateBoard()
            p.display.flip()
        elif(args[0] == "Quit"):
            run = True
            print("X out of the window now")
            while run:
                for event in p.event.get():
                    if event.type == p.QUIT:
                        print("trying to quit")
                        run = False
            p.quit()
        else:
            print("wut?")

