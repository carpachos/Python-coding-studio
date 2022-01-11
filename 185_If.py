# 온라인 할인쿠폰 시스템 만들기
# 표준입력 : 가격(정수), 쿠폰이름

price = int(input())
coupon = input()

if coupon == 'Cash3000':
  price -= 3000
if coupon == 'Cash5000':
  price -= 5000
print(price)