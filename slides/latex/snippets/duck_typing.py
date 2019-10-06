class Duck:
    """ This is a duck - it quacks"""
    
    def quack(self):
        print('Quack!')
        
class Goose:
    """ This is a goose - it quacks too"""
    
    def quack(self):
        print('Quack!')

class Penguin:
    """ This is a penguin -- I don't quack!"""
    pass 

birds = [Duck(), Goose(), Penguin()]

for bird in birds:
    bird.quack()
