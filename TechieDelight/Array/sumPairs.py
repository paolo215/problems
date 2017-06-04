# Find pair with given sum in the array
# Given an unsorted array of integers, find a pair with given sum in it.




def sumPairs(arr, total):
    pairs = []
    length = len(arr)
    for i in range(length):
        for j in range(i+1, length):
            if(arr[i] + arr[j] == total):
                pairs.append((arr[i], arr[j]))
    return pairs



if __name__ == "__main__":
    # Comma separated
    arr =  input("Array: ")
    total = int(input("Sum: "))
    
    pairs = sumPairs(arr, total)
    for i in pairs:
        print(i)

    print("===END===")
    
