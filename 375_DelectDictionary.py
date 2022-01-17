# 딕셔너리에서 특정 값 삭제하기
# 표준 입력 : 문자열(키)과 숫자(값) 여러개 각각 두줄
# A B C D
# 10 20 30 40
#키가 D인 키-값 쌍과 값이 30인 키-값 쌍을 삭제 

Keys = input().split()
Values = map(int, input().split())

X = dict(zip(Keys, Values))

del X['D']
# 딕셔너리 표현식 사용 *일반 반복문 사용시 딕셔너리의 크기변경으로 인하여 오류발생*
X = {Key: Value for Key, Value in X.items() if Value != 30}

print(X)