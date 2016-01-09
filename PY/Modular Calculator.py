#pvprograms.weebly.com
#Modular calculator

user = int(input())
calc = ' '
while(calc[0] != '%'):
    calc = input()
    calc = calc.split(' ')
    operator = calc[0]
    num = int(calc[1])
    if(operator == '+'):
        user += num
    elif(operator == '-'):
        user -= num
    elif(operator == '*'):
        user *= num
    elif(operator == '/'):
        user /= num
    elif(operator == '^'):
        user = user**num
    else:
        user %= num
print(user)
