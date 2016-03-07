#pvprograms.weebly.com
#Modulo and time difference
test = int(input())
for i in range(test):
    date = input()
    date = date.split(' ')
    for a in range(len(date)):
        date[a] = int(date[a])
    first = (date[0] * 24 * 3600) + (date[1] * 3600) + (date[2] * 60) + date[3]
    second =(date[4] * 24 * 3600) + (date[5] * 3600) + (date[6] * 60) + date[7]
    delta = abs(first - second)
    days = int(delta / (24 * 3600))
    delta = int(delta % (24 * 3600))
    hour = int(delta / 3600)
    delta = int(delta % 3600)
    minutes = int(delta / 60)
    delta = int(delta % 60)
    print("(" + str(days) + " " + str(hour) + " " + str(minutes) + " " + str(delta) + ") ")    
