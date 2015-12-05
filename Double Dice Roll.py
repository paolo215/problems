a = int(input())
for i in range(a):
    string = input()
    string = string.split(" ")
    string = [int(int(f)%6+ 1 ) for f in string]
    print(sum(string), end ='')

