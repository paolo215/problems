def subarray(arr):
    return sort(0, len(arr) -1, arr)
    

def sort(left, right, arr):
    if left == right:
        return arr[left]
    else:
        middle = ((left + right) / 2)
        a = [sort(left, middle, arr), sort(middle+1, right, arr),
                cross(left, middle, right, arr)]
        return max(a)
def cross(left, center, right, arr):
    #return sum([sum(arr[left:center+1]), sum(arr[center+1:right+1])])
    leftSum = rightSum = -float("inf")
    cLeft = cRight = 0
    for i in range(center, left-1, -1):
        cLeft += arr[i]
        leftSum = max([cLeft, leftSum])

    for i in range(center+1, right):
        cRight += arr[i]
        rightSum = max([cRight, rightSum])

    return leftSum + rightSum

a = [-6, -1, 6, -1, -4, 1, 5, -3]
b = [-2, -3, 4, -1, -2, 1, 5, -3]
c = [-2, -3, 4, 1, 1, 5, -3]
d = [3, 4, 4, -1, -1, -1 , -1]
d = list(reversed(d))
print subarray(a)
print subarray(b)
print subarray(c)
print subarray(d)
