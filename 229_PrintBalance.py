# 교통카드 잔액 출력
# 표준 입력 : 정수
charge = int(input())
while True:
  charge -= 1350
  if charge < 0:
    break
  else:
    print(charge)