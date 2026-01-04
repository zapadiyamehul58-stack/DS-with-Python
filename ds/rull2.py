

def animal(leg, habit, sound):
    if leg == 0 and habit == 'water':
        return 'fish'
    if leg == 2 and habit == 'air' and sound == 'chirp':
        return 'bird'
    if leg == 4 and habit == 'land' and sound == 'meow':
        return 'cat'
    if leg == 4 and habit == 'land' and sound == 'bark':
        return 'dog'
    if leg == 4 and habit == 'land' and sound == 'roar': 
        return 'lion'
    return 'invalid input'
sound_input = input("Enter sound (e.g., chirp, meow, bark, roar): ")

print(animal(leg, habit_input, sound_input))

# print(animal(0, 'water', 'blub'))
# print(animal(4, 'land', 'roar'))
# print(animal(8, 'land', 'hiss')) 
