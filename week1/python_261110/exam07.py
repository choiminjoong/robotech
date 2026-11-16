# 클래스 -> 객체를 표현하기 위한 문법의 일종. 프로그래밍으로 객체를 만들 때 사용하는 것.

# 전사, 마법사, 궁수, 자동차, 비행기, 사람, 강아지, 고양이 -> object
# -> 현실, 가상, 개념

# 속성 -> attribute
# 능력(기능) -> method
# 전사 클래스 - 체력, 마나, 공격력 -> 속성
            # - 공격하다, 방어하다 -> 메소드

class Person():
  def __init__(self, name, age, hobby, weight):
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.hobby = hobby
    self.__weight = weight # 언더바2개로 private 속성 부여

  def introduce(self):
    print("{}, 저는 {} 입니다.".format(self.hello,self.__weight)) # 클래스 내부에서 접근

jin = Person('a', 22, 't',38) # 이때 __init__ 메서드는 실행됐다.
jin.introduce()
jin.__init__('a', 22, 't',13)
jin.hello = 13
jin.__weight = 3
jin.introduce()


#testddddd