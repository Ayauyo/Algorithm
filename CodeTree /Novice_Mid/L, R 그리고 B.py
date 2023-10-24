arr = [
    list(input())
    for _ in range(10)
]

b = []
r = []
l = []

for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            b.append(i)
            b.append(j)
        elif arr[i][j] == 'R':
            r.append(i)
            r.append(j)
        elif arr[i][j] == 'L':
            l.append(i)
            l.append(j)          

if b[0] == r[0] == l[0] and ((b[1] < r[1] and r[1] < l[1]) or (l[1] < r[1] and r[1] < b[1])) :
    print(abs(l[0] - b[0]) + abs(l[1] - b[1]) + 1)

elif b[1] == r[1] == l[1] and ((b[0] < r[0] and r[0] < l[0]) or (l[0] < r[0] and r[0] < b[0])):
    print(abs(l[0] - b[0]) + abs(l[1] - b[1]) + 1)
else:

    print(abs(l[0] - b[0]) + abs(l[1] - b[1]) - 1)
