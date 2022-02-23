# 사칙연산 함수 만들기
# 표준입력 : 숫자 2개 결과는 무조건 실수

x, y = map(int, input().split())

def calc(x,y):
  return x+y, x-y, x*y, x/y

a,s,m,d = calc(x,y)
print("덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}".format(a,s,m,d))