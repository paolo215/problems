#pvprograms.weebly.com
#Body Mass Index

test = int(input())
for i in range(test):
    user = input()
    user = user.split(' ')
    weight = int(user[0])
    height = float(user[1])
    BMI = weight/(height**2)
    if(BMI < 18.5):
        ans = "under"
    elif(18.5 <= BMI and BMI < 25.0):
        ans = "normal"
    elif(25.0 <= BMI and BMI < 30.0):
        ans = "over"
    else:
        ans = "obese"
    print(ans, end=' ')
