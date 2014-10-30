from Base import *

class InClass (BaseClass):
    def printHam(self):
        self.x = 17

class InClass2 (BaseClass):
    def printHam(self):
        print ("Ham2")

class InInClass (Inclass, Inclass2):
    printHam()
    print (BaseClass.x)
