



def generate(n, A, output):
    if n == 1:
        output.append("".join(map(str, A)))
    else:
        for i in range(0, n-1):
            generate(n-1, A, output)
            if n % 2 == 0:
                A[i], A[n-1] = A[n-1], A[i]
            else:
                A[0], A[n-1] = A[n-1], A[0]
        generate(n-1, A, output)



array = range(5)
output = []
generate(len(array), array, output)
print output, len(output)
