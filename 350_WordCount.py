#특정 단어 개수 세기
# 표준입력 : 문자열 (the 개수 출력 *them 등 개수x*)
# the grown-ups' this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography.

word = input().split()
count = 0
for words in word:  #for문으로 문자열이 'the'인지 판단
    if (words.strip(',.')=='the'):
        count+=1  #'the'맞으면 count에 1씩 적립
print(count)