n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

x1 = 100
x2 = 0

left, right = 0, 0

for i in range(n):
    if arr[i][0] <= x1:
        x1 = arr[i][0]
        left = i

    if arr[i][1] >= x2:
        x2 = arr[i][1]
        right = i

ans_1, ans_2 = 0, 0

x1 = 100
x2 = 0
for i in range(n):

    if i == left:
        continue
    x1 = min(x1, arr[i][0])
    x2 = max(x2, arr[i][1])   

ans_1 = x2 - x1

x1 = 100
x2 = 0
for i in range(n):

    if i == right:
        continue
    x1 = min(x1, arr[i][0])
    x2 = max(x2, arr[i][1])   

ans_2 = x2 - x1

print(min(ans_1, ans_2))