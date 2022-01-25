# 특정 문자가 들어있는 단어 찾기
# 파일입출력 : words.txt (문자열은 한줄로 저장) 문자 c가 포함된 단어 출력

file = open('words.txt', 'r')
words = file.read()

str = words.split() # 문자열 -> 리스트
for i in str:
  if 'c' in i:
    print(i.rstrip(',.')) # 오른쪽 특정문자 제거

file.close()