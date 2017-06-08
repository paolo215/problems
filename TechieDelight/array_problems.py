
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

# Given a limited range array of size n where array contains elements between
# 1 to n-1 with one element repeating, find the duplicate nubmer in it.
def find_duplicate(arr):
    nums = {}
    duplicate = None
    for i in arr:
        if not i in nums:
            nums[i] = True
        else:
            duplicate = i
    return duplicate


# Given an array of integers, find largest sub-array formed by consecutive
# integers. The sub-array should contain all distinct values
def largest_sub_array_formed_by_consecutive_integers(arr):
    length = len(arr)
    winner = None
    for i in range(length):
        for j in range(i+1, length+1):
            sub_array = arr[i:j]
            sorted_array = sorted(sub_array)
            is_consecutive = True
            for k in range(1, len(sorted_array)):
                diff = sorted_array[k] - sorted_array[k-1]
                if diff != 1:
                    is_consecutive = False
            if is_consecutive and (winner == None or (len(winner) < len(sub_array))):
                winner = sub_array

    return winner
                    
def main():
    arr = input("Array: ")
    

if "__main__" == __name__:
    main()

