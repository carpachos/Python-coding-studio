# 공약수 구하기
# 표준입력 : 양의 정수 두개

x, y = input().split()
x = int(x)
y = int(y)

a = {i for i in range(x) if i != 0 and x % i == 0}
b = {i for i in range(y) if i != 0 and y % i == 0}

a.add(x)
b.add(y)

divisor = a & b

result = 0
if type(divisor) == set:
  result = sum(divisor)

print(divisor)

