from random import randint
def chooseRandLaunchDeg():
    randomLaunchDeg = randint(0, 360)
    randomNum = randint(0, 1)
    if randomNum == 0:
        allLaunchDeg = []
        for i in range(35, -1, -1):
            allLaunchDeg.append(i)
        for j in range(360, 324, -1):
            allLaunchDeg.append(j)
        k = randint(0, len(allLaunchDeg))
        randomLaunchDeg = allLaunchDeg[k]
    elif randomNum == 1:
        randomLaunchDeg = randint(135, 235)
    return randomLaunchDeg
while 7 == 7:
    print(chooseRandLaunchDeg())