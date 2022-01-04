# 시작값-10 종료값 10 표준입력 정수 정수만큼 증가하는 튜플을 생성하고 출력
number = int(input())

tp = tuple(range(-10,10,number))
print(tp)