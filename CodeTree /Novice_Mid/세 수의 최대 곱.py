n = int(input())
arr = tuple(map(int, input().split()))

#양 양 양
case_1 = -1000

sorted_arr = sorted(arr)

if sorted_arr[-1] > 0 and sorted_arr[-2] > 0 and sorted_arr[-3]:
    case_1 = sorted_arr[-1] * sorted_arr[-2] * sorted_arr[-3]
   
#양 양 음
case_2 = -1000

minuses = []
pluses = []

for i in range(n):
    if arr[i] < 0:
        minuses.append(arr[i])
    elif arr[i] > 0:
        pluses.append(arr[i])

sorted_minuses, sorted_pluses = sorted(minuses), sorted(pluses)

if len(sorted_minuses) >= 1 and len(sorted_pluses) >= 2:
    case_2 = sorted_pluses[0] * sorted_pluses[1] * sorted_minuses[-1]

#양 음 음
case_3 = -1000

minuses = []
pluses = []

for i in range(n):
    if arr[i] < 0:
        minuses.append(arr[i])
    elif arr[i] > 0:
        pluses.append(arr[i])

sorted_minuses, sorted_pluses = sorted(minuses), sorted(pluses)

if len(sorted_minuses) >= 2 and len(sorted_pluses) >= 1:
    case_2 = sorted_pluses[-1] * sorted_minuses[0] * sorted_minuses[1]

#음 음 음
case_4 = -1000
minuses = []


for i in range(n):
    if arr[i] < 0:
        minuses.append(arr[i])

sorted_minuses = sorted(minuses)

if len(sorted_minuses) >= 3:
    case_4 = sorted_minuses[-1] * sorted_minuses[-2] * sorted_minuses[-3]

#0 포함
case_5 = -1000
for i in range(n):
    if arr[i] == 0:
        case_5 = 0
        break

print(max(case_1, case_2, case_3, case_4, case_5))
