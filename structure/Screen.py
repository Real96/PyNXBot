from structure.ByteStruct import ByteStruct

class Screen(ByteStruct):
    BATTLEMENU = 0xFF000000FF000000

    def getScreenOffShort(self):
        return self.getushort(0x0)

    def getScreenOff(self):
        return self.getulong(0x0)

    def isIntroAnimationSkippable(self):
        #print(f"{self.getScreenOffShort():0X}")
        return self.getScreenOffShort() != 0x0

    def overworldCheck(self):
        #print(f"{self.getbyte(0x0):0X}")
        return self.getbyte(0x0)

    def battleMenuAppeared(self):
        #print(f"{self.getScreenOff():0X}")
        return self.getScreenOff() == self.BATTLEMENU
