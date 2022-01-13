# 지뢰 찾기
# 표준 입력 : 가로값(정수) 세로값(정수) 문자(지뢰의 유*무.)

row = int(input())
col = int(input())
matrix = []

for i in range(row):  # . * 입력
    matrix.append(list(input()))

for i in range(row):    
    for j in range(col):
      if matrix[i][j] == '*':
        continue
      else:
        matrix[i][j] = 0
        for y in range(i - 1, i + 2):   
          for x in range(j - 1 ,j + 2): 
            if y < 0 or x < 0 or y >= row or x >= col: # 리스트의 범위설정
              continue
            elif matrix[y][x] == '*':
              matrix[i][j] += 1

for i in range(row):
  for j in range(col):
    print(matrix[i][j], end='')
  print()