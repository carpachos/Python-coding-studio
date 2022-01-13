# 5와 7의 배수 공배수 처리하기
# 표준 입력 : 정수 두개 (1~1000) < (10~1000)
# 5의 배수 Fizz 7의 배수 Buzz 공배수 FizzBuzz 출력

one = int(input())
two = int(input())

if 1 <= one <= 1000 and 10 <= two <= 1000 and one < two:
  for i in range(one, (two+1)):
    if i % 35 == 0:
      print("FizzBuzz")
    elif i % 5 == 0:
      print("Fizz")
    elif i % 7 == 0:
      print("Buzz")
    else:
      print(i)