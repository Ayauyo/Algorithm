a, b, x, y = tuple(map(int, input().split()))

ans1 = ans2 = ans3 = 0

ans1 = abs(a - x) + abs(y - b)
ans2 = abs(a - y) + abs(x - b)
ans3 = abs(b - a)

if ans1 <= ans2 and ans1 <= ans3:
    print(ans1)

elif ans2 <= ans3:
    print(ans2)   

else:
    print(ans3)

# min함수를 통해서 코드를 더 짧게 만들 수 있음
