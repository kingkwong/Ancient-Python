from abc import ABCMeta, abstractmethod

class Human(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def run(self):
        pass

class Robot(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def vacuum(self):
        pass

class Cyborg(Human,Robot):
    pass

x = Cyborg()
