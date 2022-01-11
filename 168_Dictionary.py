#딕셔너리에 게임 능력치 저장하기
x = input().split() # 능력치이름
y = input().split() # 능력치숫자

diction = dict(zip(x,y))
print(diction)