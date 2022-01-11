# 합격여부 판단하기 (평균 80점이상, 범위 벗어난경우 알려주기)
# 표준입력: 국,영,수,과 점수

ko, en, ma, sc = map(int, input().split())
if ko < 0 or ko > 100 or en < 0 or en > 100 or ma < 0 or ma > 100 or sc < 0 or sc > 100:
  print("잘못된 점수")
else:
  sum = ko+en+ma+sc
  aver = sum / 4
  if aver >= 80:
    print("합격")
  else :
    print("불합격")