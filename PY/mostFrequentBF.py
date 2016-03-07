
#Setting up data structure
a = open("test.txt", "r")
array = a.read()
array = array.split(" ")
a.close()


#Search for most frequent word
mostIdx = 0
mostCounter = 0
counter = 0

for i in range(0, len(array)):
    counter = 0
    for z in range(0, len(array)):
        if array[i] == array[z]:
            counter += 1

    if mostCounter < counter:
        mostCounter = counter
        mostIdx = i

print array[mostIdx]
