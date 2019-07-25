## WorkShop 4

### 1. 제곱근 값을 찾아봅시다.

```python
def root(num):
    result = 1
    start = 1
    end = num
    while abs(result ** 2 - num) >= 1e-15:
        result = (start+end)/2
        if result **2 < num:   # result 2 
            start = result
        else:
            end = result
        print(result)
root(2)
```