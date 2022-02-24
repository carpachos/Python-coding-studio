# 재귀호출로 피보나치 수 구하기
# 표준입력 :10~30의 정수
def fib(count):
  if count == 0: # 피보나치 첫부분
    return 0
  elif count == 1: # 피보나치 두번째 부분
    return 1
  else:
    return fib(count-1) + fib(count-2)
  

n = int(input())
print(fib(n))