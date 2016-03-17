
def powerSet(array):
    n = len(array)
    powerSet = []
    for i in range(0, (1 << n)):
        element = []
        for j in range(0,n):
            if (i >> j) % 2 != 0:
                element.append(array[j])
        powerSet.append(element)
    return powerSet

array = range(3)
print array, pow(2,len(array))
print powerSet(array)
