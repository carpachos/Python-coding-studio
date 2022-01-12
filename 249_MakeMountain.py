# 산 모양으로 별 출력하기
# 표준 입력 : 삼각형의 높이(자연수)

height = int(input())
for i in range((height)): #층
  for j in range(height-i): #띄어쓰기
    print(" ", end="")
  for k in range(2*i+1):
    print("*", end="")
  print()