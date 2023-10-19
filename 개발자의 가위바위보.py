n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

a_list = []

for i in range(n):
    a_list.append(arr[i][0] - arr[i][1])


ans1, ans2 = 0, 0
for i in range(len(a_list)):
    if a_list[i] == -1 or a_list[i] == 2:
        ans2 += 1
    elif a_list[i] == -2 or a_list[i] == 1:
        ans1 += 1

print(max(ans1, ans2))

# case_1
# 가위 바위 보 가위 바위 보...
# 1    2    3   1    2   3
# 숫자가 2 작거나 1 큰 경우 승리
# -2, 1

# case_2
# 가위 보 주먹 가위 보 주먹
# 1    2   3   1   2   3
# 숫자가 1 작거나 2 큰 경우 이김
# -1, 2