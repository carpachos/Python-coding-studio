# 교통카드 시스템 만들기
# 표준입력 : 나이(7이상), 카드안금액: 9000

age = int(input())
Balance = 9000
if age < 7:
  print(" 7이상 입력해주세요")
elif age <= 12:
  Balance = Balance - 650
elif age <= 18:
  Balance = Balance - 1050
else:
  Balance = Balance -1250
print(Balance)