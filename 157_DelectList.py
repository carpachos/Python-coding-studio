# 리스트 x 에 표준입력으로 입력후 마지막 5개 요소 삭제뒤 튜플로 변환후 출력
x = input().split()
del x[len(x)-5::1]
x = tuple(x)
print(x)