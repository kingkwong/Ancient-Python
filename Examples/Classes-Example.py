class Hero:
    '''
    A hero who is allegic to apples.
    '''
    def __init__(self,name):
        self.name = name
        self.health = 100
    def eat(self, food):
        if(food == 'Apple'):
            self.health -= 100
        elif(food == 'Ham'):
            self.health += 20
        else:
            pass
x = {'Apple','Ham'}
Bob = Hero(input('Name: '))
print (Bob.name)
print (Bob.health)
print ('List of Foods:')
print (x)
Bob.eat(input('Food? '))
print (Bob.health)


