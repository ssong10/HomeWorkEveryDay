## WorkShop 7

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')  
```

### 1. 위와 같은 Animal 클래스가 있을때.

```python
dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.run()  # 멍멍이! 달린다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat()  # 구구! 먹는다!
bird.fly()  # 구구! 푸드덕!
```

​	이런 출력이 되도록 Dog 와 Bird 클래스를 생성하시오.(상속 사용)

```python
class Dog(Animal):
    
    def walk(self):
        print(f'{self.name}! 달린다!')
        
    def run(self):
        print(f'{self.name}! 달린다!')

class Bird(Animal):
    
    def fly(self):
        print(f'{self.name}! 푸드덕!')    
```

