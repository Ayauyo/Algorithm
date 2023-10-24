n = int(input())
arr = [
    tuple(input().split())
    for _ in range(n)
]

a, b, c = 0, 0, 0

def change(score_a, score_b, score_c):

    if score_a > score_b and score_a > score_c:
        return 1
    elif score_b > score_a and score_b > score_c:     
        return 2
    elif score_c > score_a and score_c > score_b:     
        return 3
    elif score_a == score_b and score_a > score_c:     
        return 4
    elif score_c == score_a and score_c > score_b:     
        return 5
    elif score_c == score_b and score_c > score_a:     
        return 6
    elif score_a == score_b == score_c:
        return 7

ans = 0
for person, score in arr:
    value = int(score)

    if person == 'A':
        if change(a, b, c) != change(a + value, b, c):
            ans += 1
        a += value
    elif person == 'B':
        if change(a, b, c) != change(a, b + value, c):
            ans += 1
        b += value
    else:
        if change(a, b, c) != change(a, b, c + value):
            ans += 1
        c += value     

print(ans)