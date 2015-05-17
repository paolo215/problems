#pvprograms.weebly.com
#Greatest Common Divisor

test = int(input())
for i in range(test):
    data = input()
    data = data.split(' ')
    for a in range(len(data)):
        data[a] = int(data[a])
    a = data[0]
    b = data[1]
    while b:
        temp = a
        a = b
        b = int(temp % b)
        
        
    GCD = a
    if GCD == 0:
        GCD = 1
    LCM = int((data[0] * data[1]) / GCD)
    print("(" + str(GCD) + " " + str(LCM) + ") ")
