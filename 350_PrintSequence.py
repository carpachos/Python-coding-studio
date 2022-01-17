# 높은 가격 순서대로 출력하기
# 표준입력 : 물품가격 여러개 문자열, 구분 ; 가격길이 9 천단위 , 필수
# 51900;83000;158000;367500;250000;59200;128500;1304000

prices=list(map(int,input().split(';')))
prices.sort(reverse=True) #내림차순 정렬
for i in prices:
    print('{0:>9,}'.format(i))       # {인덱스:<길이}.format(값)