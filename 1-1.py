import collections

# namedtuple을 이용하면 메서드를 가지지 않는 일련의 속성으로 구성된 클래스를 만들 수 있다.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
# print(len(deck)) # 52
# print(deck[0]) # Card(rank='2', suit='spades')
# print(deck[-1]) # Card(rank='A', suit='hearts')

from random import choice

# random 모듈의 choice를 이용하면 시퀀스에서 항목을 무작위로 골라낼 수 있다.
# print(choice(deck))

# __getitem__() 메서드는 [] 연산자에 작업을 위임하기 때문에 deck 객체는 슬라이싱도 자동으로 지원한다.
# 슬라이싱을 사용할 수 있기 때문에 deck에서 손쉽게 ACE만 가져오는 것도 가능하다.
# print(deck[12::13])

# __getItem__() 특별 메서드를 구현했기 때문에 iterator로도 사용할 수 있다.
# for card in deck:
#     print(card)

# for card in reversed(deck):
#     print(card)

# 컬렉션에 __contains__() 메서드가 없다면 in 연산자는 차례대로 검색한다.
# print(Card('Q', 'hearts') in deck) # True

# 카드는 숫자(rank)로 순위를 정하고 랭크가 같은 경우 스페이드, 하트, 다이아몬드, 클로버(제일 낮음) 순으로 순위를 정한다.
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    # suit가 총 4개 이므로 카드의 순위는 랭크가 올라갈 때 4씩 증가한다.
    # suit_values[card.suit]은 시작하는 초기 값처럼 생각하면 등차 수열처럼 생각할 수 있다.
    return rank_value * len(suit_values) + suit_values[card.suit]

# 오름차순으로 카드 순위 나열
for card in sorted(deck, key=spades_high):
    print(card)

# p.42