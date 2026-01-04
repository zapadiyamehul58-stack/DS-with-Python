
data=read_csv("aa.csv")
leg=int(input("enter leg:"))
fly=int(input("enter fly:"))

def animal (leg,habit,sound):
    if leg == 0 and habit == 'water':
        return 'fish'
    
    if leg == 2 and habit == 'air' and sound == 'chirp':
        return 'bitd'
    
    if leg == 4 and habit == 'land' and sound == 'meow':
        return 'cat'
    
    if leg == 4 and habit == 'land' and sound == 'bark':
        return 'dog'
    
    if leg == 4 and habit == 'land' and sound == 'rorr':
        return 'lion'
    
    return "invalid input:"
print(animal(data))
#print(animal(0,'water','blub'))
###print(animal(4,'land','ror'))
#print(animal(8,'land','hiss'))
