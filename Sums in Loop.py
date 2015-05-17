#pvprograms.weebly.com
#Sums in Loop

def main():
    test = int(input()) #number of test cases
    nums = [] #List of lists
    for i in range(test):
        a = input()
        #split the string - separated with space
        a = a.split(' ')
        #turn them to int first before appending to the main lists
        a[0] = int(a[0])
        a[1] = int(a[1])
        #append a to the nums list
        nums.append(a)
    #print the sum of the sub list - a
    for a in nums:
        print(sum(a), end=" ")

#call main function
main()
