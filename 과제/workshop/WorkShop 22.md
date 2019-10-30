## WorkShop 22

```python
class Person(models.Model):
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100,
                            validator=[EmailValidator(message = '이메일 형식이 아닙니다.')]
                            )
    age = models.IntegerField(
        validaotrs=[MinValueValidator(20,message = '미성년자는 노노')])
```

