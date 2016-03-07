#pvprograms.weebly.com
#Vowel Count


test = int(input())
vowels = ['a','o','u','i','e','y']
while(test != 0):
    count = 0
    user = input()
    for i in range(len(user)):
        if(user[i] in vowels):
            count+=1
    print(count, end=' ')
    test -= 1
