#pvprograms.weebly.com
#Fahrenheit to Celsius

a = input()
a = a.split(' ')
for i in range(len(a)):
    a[i] = int(a[i])

values = a[0]
#removes the number
a.pop(0)
for b in range(values):
    celsius = round((a[b]-32)/1.8)
    print(celsius, end=' ')
