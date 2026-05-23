'''
class avengers:
    def __init__():
        pass    
    def fight(self,avenger):
        print(f"{avenger} is fighiting. dishum dishum")


#obj
avenger = avengers()
avenger.fight('Iron man')
avenger.fight('Captain America')
avenger.fight('Thor Chaddi')

'''

#Constructor
class avengers:
    def __init__(self,avenger):
        self.avenger = avenger
        
    def fight(self):
        return f"{self.avenger} is fighiting. dishum dishum"

avenger = avengers('iron man')

f1 = avenger.fight()
print(f1)