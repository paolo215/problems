import random


p = ["O", "O", "O", "X"]
w = 10
h = 10

def display(matrix):
    for i in matrix:
        print i

def path(p):
    up = [p[0],p[1]+1]
    right = [p[0]+1, p[1]]
    down = [p[0], p[1]-1]
    left = [p[0]-1, p[1]]
    directions = [up, down, left, right]
    return directions

def BFS(matrix, start, end):
    Q = []
    dist = dict([])
    prev = dict([])
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            s = str(a)+str(b)
            dist[s] = float("inf")
            prev[s] = None


    Q.insert(0, start)
    start_string = str(start[0])+str(start[1])
    dist[start_string] = 0
    while Q != []:
        a = Q.pop(0)
        directions = path(a)
        #matrix[a[0]][a[1]] = "X"
        for i in directions:
            try:
                d = str(i[0])+str(i[1])
                s = str(a[0])+str(a[1])
                if dist[str(a[0])+str(a[1])] + 1 < dist[d] and matrix[i[0]][i[1]] == "O":
                    dist[d] = dist[s] + 1
                    Q.insert(0, i)
                    prev[d] = s
            except (IndexError, KeyError) as e:
                pass

    b = str(end[1])+str(end[0])
    #print b
    #print matrix[int(b[0])]
    while(b != start_string and prev[b] != None):
        matrix[int(b[0])][int(b[1])] = "."
        b = prev[b]

    if b == start_string:
        matrix[int(b[0])][int(b[1])] = "."

    a = dist[str(end[1])+str(end[0])]
    if a == float("inf"):
        a = -1;
    return a

matrix = [[p[random.randint(0,3)] for x in range(w)] for x in range(h)]
display(matrix)
print str(BFS(matrix, [0,0], [w-1, h-1])) + " steps"
display(matrix)
