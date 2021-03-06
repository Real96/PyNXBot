import sys
from nxbot import SWSHBot
from structure import Den,Screen

class RaidBot(SWSHBot):
        
        def __init__(self,ip,port = 6000):
                SWSHBot.__init__(self,ip,port)
                from structure import EncounterNest8Archive, NestHoleDistributionEncounter8Archive
                buf = bytearray(open('../resources/bytes/local_raid','rb').read())
                Den.LOCALTABLE = EncounterNest8Archive.GetRootAsEncounterNest8Archive(buf,0)
                buf = self.readEventBlock_RaidEncounter('Event/Current/')
                Den.EVENTTABLE = NestHoleDistributionEncounter8Archive.GetRootAsNestHoleDistributionEncounter8Archive(buf,0x20)
                self.resets = 0

        def increaseResets(self):
                self.resets += 1

        def setTargetDen(self, denId):
                self.denID = denId - 1

        def getDenData(self):
                return Den(self.readDen(self.denID))

        def quitGame(self,needHome = True):
                if needHome:
                        self.click("HOME")
                        self.pause(0.8)
                self.click("X")
                self.pause(0.2)
                self.click("X")
                self.pause(0.4)
                self.click("A")
                self.pause(0.2)
                self.click("A")
                self.pause(3)

        def enterGame(self):
                self.click("A")
                self.pause(0.2)
                self.click("A")
                self.pause(1.3)
                self.click("A")
                self.pause(0.2)
                self.click("A")

        def closeGame(self):
                c = input("Close the game? (y/n): ")
                if c == 'y' or c == 'Y':
                        h = input("Need HOME button pressing? (y/n): ")
                        if h == 'y' or h == 'Y':
                                needHome = True
                        else:
                                needHome = False
                        print("Closing game...")
                        self.quitGame(needHome)
                print("Exiting...")
                self.pause(0.5)
                self.close()
                        
        def skipAnimation(self): #luxray = False
                self.enterGame()
                skip = False
                while skip == False:
                        self.currScreen = Screen(self.readScreenOff())
                        if self.currScreen.isIntroAnimationSkippable():
                                skip = True
                        self.pause(0.3)
                #self.pause(20.5)
                #self.currScreen.isIntroAnimationSkippable()
                #if luxray:
                        #self.pause(1.3)
                print("Skip animation")
                for i in range(5):
                        self.click("A") #A to skip anim
                        self.pause(0.5)
                #self.pause(8)
                skipped = False
                while skipped == False:
                        self.currScreen = Screen(self.readOverworldCheck())
                        if self.currScreen.overworldCheck():
                                skipped = True
                        self.pause(0.5)

        def saveGame(self):
                print("Saving...")
                self.click("X")
                self.pause(1.2)
                self.click("R")
                self.pause(1.5)
                self.click("A")
                self.pause(4)

        def getWatts(self):
                self.click("A")
                self.pause(1.5)
                self.click("A")
                self.pause(1.2)
                self.click("A")
                self.pause(1.2)
                self.saveGame()

        def throwPiece(self):
                self.click("A") #A on den
                print("A on den")
                self.pause(0.5)
                self.click("A")
                self.pause(1.3)
                self.click("A") #A to throw whishing piece
                print("Throw Wishing Piece in den")
                self.pause(1.4)
                self.click("A") #A to save
                print("Saving...")
                self.pause(1)
                self.click("HOME") #Home
                print("HOME clicked")
                self.pause(0.5)

        def foundActions(self):
                print("Found after", self.resets, "resets")
                a = input("Continue searching? (y/n): ")
                if a != "y" and a != "Y":
                    self.closeGame()
                    sys.exit(0)
                else:
                    self.increaseResets()
                    print("Resets:", self.resets)

        def notfoundActions(self,i=0,bot='raid'):
                if i == 0 and bot == 'raid':
                    print("Research skipped")
                self.increaseResets()
                if bot == 'raid':
                        print("Nothing found - Resets:", self.resets)
                else:
                        print("Wrong Species / Stars - Resets:", self.resets)
