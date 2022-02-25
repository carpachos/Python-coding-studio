# 게임 캐릭터 클래스 만들기
# 표준 입력 : 개릭터 능력치(체력, 마나, AP)
# 클래스 : Annie 표준출력 : tibbers 스킬의 피해량

class Annie:
  def __init__(self, health, mana, power):
    self.health = health
    self.mana = mana
    self.power = power
  def tibbers(self):
    print("티버 : 피해량 {0}".format(self.power * 0.65 + 400))

health, mana, power = map(int, input().split())

x= Annie(health = health, mana = mana, power = power)
x.tibbers()