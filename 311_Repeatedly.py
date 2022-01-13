# 2의 거듭제곱 리스트 생성하기
# 표준 입력 : 정수 두개 (1~20) < (10~30)
# 첫번째 정수부터 두번째 정수 까지를 지수로하는 2의 거듭제곱 리스트 출력

index_start = int(input())
index_fin = int(input())
a = []

for i in range(index_start, index_fin+1):
  value = 1
  for j in range(i):
    value = value *2
  a.append(value)

print(a)