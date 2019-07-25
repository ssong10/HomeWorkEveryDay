## WorkShop 3

### 1. palindromemordnilap

```python
def palindrome(word):
    word = str(word)
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return print('not palindrome')
    return print('palindrome')
palindrome('palindromemordnilap')
```

```python
# 궁극의 뒤집기마스터
a[::-1]

def palindrome(word):
    return word == word[::-1]
```

