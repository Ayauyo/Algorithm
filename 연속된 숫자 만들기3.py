a, b, c = tuple(map(int, input().split()))


# case_1 : 3명 연속될 경우
if a + 2 == b + 1 == c:
    print(0)
# case_2 : 2명 연속될 경우    
elif a + 1 == b or b + 1 == c:
    if a + 1 == b:
        print(c - b - 1)
    elif b + 1 == c:
        print(b - a - 1)
# case_3 : 아무도 연속되지 않을 경우        
else:
    if b - a > c - b:
        print(b - a - 1)
    else:
        print(c - b - 1)            
