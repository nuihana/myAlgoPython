import sys

inputCnt = int(sys.stdin.readline().strip())

q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0

for i in range(inputCnt):
    points = list(map(int, sys.stdin.readline().split()))
    if points[0] == 0 or points[1] == 0:
        axis += 1
    else:
        if points[0] > 0:
            if points[1] > 0:
                q1 += 1
            else:
                q4 += 1
        else:
            if points[1] > 0:
                q2 += 1
            else:
                q3 += 1

print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"Q4: {q4}")
print(f"AXIS: {axis}")
