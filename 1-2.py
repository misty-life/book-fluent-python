from math import hypot

class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # 객체를 문자열로 표현하기 위한 특별 메서드
    # __repr__() 메서드를 구현하지 않으면 <Vector object at 0x블라블라 와 같은 형태로 출력된다.
    # 가능하면 표현된 객체를 재생성하는 데 필요한 소스 코드와 일치해야 한다.
    # 파이썬 인터프리터는 __str__() 메서드가 구현되어 있지 않을 때 __repr__() 메서드를 호출한다.
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    # 기본적으로 사용자 정의 클래스의 객체는 True이다.
    # __bool__() 메서드를 구현하지 않으면 __len__() 메서드에서 0을 반환하면 False, 그 외는 True로 간주한다.
    # abs 연산이 없기 때문에 return bool(self.x or self.y) 를 이용하면 더 빠르다.
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

# len()은 빈번하게 발생되는 연산이기 때문에, 성능을 위해 CPython에서는 단순히 C 언어 구조체의 필드를 읽어온다.
# 특별 메서드를 구현하면 사용자 정의 객체도 내장형 객체처럼 동작하게 되어 Pythonic한 코딩 스타일을 구사할 수 있게 된다.