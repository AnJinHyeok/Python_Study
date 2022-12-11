from collections import deque

n, m = map(int, input().split())
box = [[int(d) for d in input().split(" ")] for _ in range(m)]
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#print(box)

def search(r, c):
    search_list = []
    #print("start")
    for i, j in D:
        if r + i < m and r + i >= 0 and c + j < n and c + j >= 0:
            if box[r + i][c + j] == 0:
                box[r + i][c + j] = 1
                search_list.append((r + i, c + j))
    return search_list

def BFS(n, m, box):
    count = 0
    deq = deque()
    
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                deq.append((i, j))
    #print(deq)
    while deq:
        for _ in range(len(deq)):
            r, c = deq.popleft()
            #print(r, c)
            for tomato in search(r, c):
                deq.append(tomato)
        count += 1
        #print(box)
    
    for i in range(m):
        for j in range(n):
            if box[i][j] == 0:
                return -1
    return count - 1

print(BFS(n, m, box))

#print(box)