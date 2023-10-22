n = int(input())
changes = [
    list(input().split())
    for _ in range(n)
]

a, b = 0, 0
cnt = 0

for i in range(n):

    score = int(changes[i][1])   

    if a == b:
        if changes[i][0] == 'A':
            a += score
        else:
            b += score
        if a > b or a < b:
            cnt += 1

    elif a > b:
        if changes[i][0] == 'A':
            a += score
        else:
            b += score
        if a == b or a < b:
            cnt += 1
    else:
        if changes[i][0] == 'A':
            a += score
        else:
            b += score
        if a == b or a > b:
            cnt += 1

print(cnt)