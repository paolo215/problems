
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



def zero_sub_array(arr):
    sub_arrays = []

    length = len(arr)    
    for i in range(length):
        for j in range(i+1, length):
            sub_array = arr[i:j+1]
            if sum(sub_array) == 0:
                sub_arrays.append(sub_array)

    return sub_arrays
