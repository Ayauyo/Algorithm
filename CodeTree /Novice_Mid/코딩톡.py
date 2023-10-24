import sys

# n명의 사람
# m개의 메세지 수
# 번호 p의 메세지
# c는 카톡 보낸 사람
# u명의 읽지 않은 사람 수

n, m, p = tuple(map(int, input().split()))
info = [
    tuple(input().split())
    for _ in range(m)
]

if int(info[p - 1][1]) == 0:
    sys.exit()

for i in range(n):

    person = chr(ord('A') + i)
    read = False

    for c, u in info:
        u = int(u)
        if u >= int(info[p - 1][1]) and c == person:
            read = True
    
    if read == False:
        print(person, end=" ")     
