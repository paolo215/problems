#pvprograms.weebly.com
#Average of an array

def main():
    test = int(input())
    for i in range(test):
        user = input()
        user = user.split(' ')
        ans = 0
        for a in range(len(user)-1):
            user[a] = int(user[a])
            ans += user[a]
        ans = round(ans/(len(user)-1))
        print(ans, end=' ')
    
main()
