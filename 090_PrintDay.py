#표준입력 년-월-일  T시:분:초 출력하기
year, month, day, hour, minute, second = input().split()
print(year, month, day, sep = '-', end = ' ')
print(" T", end = '')
print(hour, minute, second, sep = ':', end = ' ')