a, b, c = tuple(map(int, input().split()))

# case_1 = 정렬이 되어있는 상황 = 0번
# case_2 = 붙어 있는 사람 두 명이 한 칸 띄어져 있는 상황 = 1번
# case_3 = 3개 모두 연속되지 않은 상황 = 2번

if a + 2 == b + 1 == c:
    print(0)
elif a + 2 == b or b + 2 == c:
    print(1)
else:
    print(2)        
