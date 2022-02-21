# 파일에서 회문인 단어 출력하기
# 파일 입출력 word421.txt

file = open('word421.txt', 'r')
word = file.read()

str = word.split()
for j in str: # j = 각 단어(리스트안)
  j.rstrip('/n') # 오른쪽 특정문자 제거 ?꼭 추가 해야되는지 없어도 정상실행?
  Palindrome = True # 회문 판별
  for i in range(len(j)//2):
    if j[i] != j[-1-i]:
      Palindrome = False
      break
  if(Palindrome == True):
    print(j)
  
file.close()