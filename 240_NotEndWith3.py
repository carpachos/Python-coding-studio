# 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
# 표준 입력 : 정수2개 (1~200) < (10~200)

one = int(input())
two = int(input())

if 0 < one <= 200 and 10 <= two <= 200 and one < two:
  while True:
    if one > two:
      break
    else:
      if one % 10 != 3:
        print(one, end = " ")
        one += 1
      else:
        one += 1
else:
  print("조건에 맞춰 주세요")