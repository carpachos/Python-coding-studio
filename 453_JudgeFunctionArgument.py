# 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
# 표준 입력 : 4개과목 점수 , 표준출력 : 가장높은점수 낮은점수 평균점수 출력(실수)

ko, en, ma, sc = map(int, input().split())

def get_min_max_score(*score):
  return min(score), max(score)
# 가변 인수
  
def get_aver(**score):
  return (sum(score.values())/len(score))
# 키워드 인수

min_score, max_score = get_min_max_score(ko, en ,ma ,sc)
aver_score = get_aver(ko = ko, en = en, ma = ma, sc =sc)

print("낮은 점수 : {}, 높은 점수 : {}, 평균 점수 : {}".format(min_score, max_score, aver_score))