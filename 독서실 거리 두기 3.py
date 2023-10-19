import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(input())


# 현재 있는 사람들은 원래 있던 자리에 그대로 두고 최대한 거리를 두면서 자리배치를 한다.
# 최대한의 거리두기 = 한 명을 더 집어넣었을 때 가장 가까운 두 사람 간의 거리를 최대로 하고 싶다

# 가장 먼 구간 찾기
longest = 0
start_num = finish_num = -1

for i in range(n):

    if arr[i] == '1':

        for j in range(i + 1, n):

            if arr[j] == '1':

                if j - i > longest:
                    longest = j - i
                    start_num = i
                    finish_num = j

                break        

ans_num = (start_num + finish_num) // 2

arr[ans_num] = '1'


ans = INT_MAX
for i in range(n):
    if arr[i] == '1':
        for j in range(i + 1, n):
            if arr[j] == '1':
                ans = min(ans, j - i)

                break

print(ans)