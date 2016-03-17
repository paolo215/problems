
def subarray(arr):
    high = arr[0]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            s = sum(arr[i:j+1])
            if s> high:
                high = s

    return high


a = [-6, -1, 6, -1, -4, 1, 5]
print subarray(a)
