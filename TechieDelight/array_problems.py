
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


# Given an array of integers, print all subarrays having 0 sum.
def zero_sub_array(arr):
    sub_arrays = []

    length = len(arr)    
    for i in range(length):
        for j in range(i+1, length+1):
            sub_array = arr[i:j]
            if sum(sub_array) == 0:
                sub_arrays.append(sub_array)

    return sub_arrays

# Given a binary array, sort it in linear time and constant
# space. Output should print all zeros followed by all ones
def binary_array_sort(arr):
    size = 0
    zeros = 0
    for i in arr:
        if i == 0:
            zeros += 1
        size += 1
    sorted_arr = []

    for i in range(zeros):
        sorted_arr.append(0)


    for i in range(size - zeros):
        sorted_arr.append(1)        

    return sorted_arr

def main():
    arr = input("Array: ")
    

if "__main__" == __name__:
    main()

