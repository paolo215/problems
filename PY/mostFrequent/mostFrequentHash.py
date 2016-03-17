#Setting up data structure
hash1 = dict([])
a = open("test.txt", "r")
array = a.read()
array = array.split(" ")
a.close()
for i in array:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1

#Searching for most frequent word
freq = 0
freqWord = ""
for item in hash1:
    if freq < hash1[item]:
        freq = hash1[item]
        freqWord = item
print freqWord

