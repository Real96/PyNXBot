import sys
from nxbot import SWSHBot
from structure import PK8,Screen

class BerryBot(SWSHBot):
    def __init__(self,ip,port = 6000):
        SWSHBot.__init__(self,ip,port)
        self.resets = 0

    def increaseResets(self):
                self.resets += 1

    def shakeTree(self):
        for i in range(3):
            self.click("A")
            self.pause(1)
        print("Shaking...")
        self.pause(3.2)
        self.click("A")
        self.pause(1.3)

    def battleRun(self):
        menu = False
        i = 0
        while menu == False and i <= 20:
            self.currScreen = Screen(self.readBattleStart())
            if self.currScreen.battleMenuAppeared():
                menu = True
            else:
                self.click("B")
                self.pause(0.5)
            i += 1
        self.pause(0.5)
        print("Running from battle...")
        self.click("DUP")
        self.pause(0.5)
        self.click("A")

    def battleCheck(self):
        if PK8(self.readWild()).isValid():
                print("Battle started!")
                self.battleRun()
                return True
        return False

    def continueShaking(self,shakes = 0):
        battle = False
        for i in range(shakes):
            self.click("A")
            print("Shaking...")
            self.pause(1.6)
            print("Battle check")
            self.pause(1.6)
            if self.battleCheck():
                self.pause(5.6)
                battle = True
                print("Picking what's left...")
                break
            self.click("A")
            self.pause(1.3)
        self.click("B")
        if battle is not True:
            print("Picking everything...")

    def pickEverything(self):
        picked = False
        i = 0
        while picked == False and i <= 20:
            self.currScreen = Screen(self.readOverworldCheck())
            if self.currScreen.overworldCheck():
                picked = True
            else:
                self.click("B")
                self.pause(0.5)
            i += 1

    def stopBot(self):
        print("Exiting...")
        self.pause(0.5)
        self.pickEverything()
        self.close()
