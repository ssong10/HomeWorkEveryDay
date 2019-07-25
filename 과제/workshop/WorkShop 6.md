## WorkShop 6

### 1. class Circle에서 반지름 3,  x, y가 (2, 4)인 원을 만들고 넓이와 둘레를 출력하시오.



```Python
class Circle:
    pi = 3.1415
    x, y, r = 0, 0, 0
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
```

```python
one = Circle(3, 2, 4)
print(one.area) # => 3.1415 * 3 * 3
print(one.circumference()) # => 2 * 3.1415 * 3
print(one.center())  # => (2,4)
```

