import sys

hour, minute, second = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

# 초 계산
s1 = (second+time)%60  #최종 초
m1 = (second+time)//60

# 분 계산
m2 = (minute+m1)%60 # 최종 분
h1 = (minute+m1)//60

# 시 계산
h2 = (hour+h1)%24 # 최종 시각

print(f"{h2} {m2} {s1}")
