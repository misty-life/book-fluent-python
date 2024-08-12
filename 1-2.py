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
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

# p. 48