#1558

sitFile = open("sitting.txt", "a")
standFile = open("standing.txt","a")
walkFile = open("walking.txt", "a")
fallFile = open("falling.txt", "a")

for i in range(820, 1559):
    i = str(i)
    action = (input(i+': '))

    if action == 1:
        sitFile.write(i+' ')
    elif action == 2:
        standFile.write(i+' ')
    elif action == 3:
        walkFile.write(i+' ')
    elif action == 4:
        fallFile.write(i+' ')
    else:
        continue

sitFile.close()
standFile.close()
walkFile.close()
fallFile.close()


for sit in sitting:
    file.write(sit+' ')

for stand in standing:
    file.write(stand+' ')

for walk in walking:
    file.write(walk+' ')

for fall in falling:
    file.write(fall+' ')


