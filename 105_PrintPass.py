#표준입력 국어 영어 수학 과학, 국어 90점이상, 
#영어 80점 초과, 수학 85점 초과, 과학 80점 
#이상일때 합격 합격 - true출력 반대의경우 false
Korean, English, Math, Science = input().split()

Korean = int(Korean)
English = int(English)
Math = int(Math)
Science = int(Science)

if(Korean >= 90):
  if(English > 80):
    if(Math > 85):
      if(Science >= 80):
        print("True")
      else:
        print("False")
    else:
      print("False")    
  else:
    print("False")
else:
  print("False")