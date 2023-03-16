import sys


def setPossibleTeam(idx):
    if idx == memberCnt:
        solve()
        return
    splitTeam[idx] = 1
    setPossibleTeam(idx + 1)
    splitTeam[idx] = 0
    setPossibleTeam(idx + 1)


def solve():
    global ans
    start, link = 0, 0
    for i in range(memberCnt):
        for j in range(memberCnt):
            if splitTeam[i] and splitTeam[j]:
                start += memberPower[i][j]
            elif not splitTeam[i] and not splitTeam[j]:
                link += memberPower[i][j]
    ans = min(ans, abs(start - link))
    return


memberCnt = int(sys.stdin.readline())
memberPower = [[0 for _ in range(memberCnt)] for _ in range(memberCnt)]
splitTeam = [0] * memberCnt
ans = 99999

for i in range(memberCnt):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(memberCnt):
        memberPower[i][j] = tmp[j]
setPossibleTeam(0)

print(ans)
