## WorkShop 16

### models.py

```python
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f'<{self.name}>'
```

### 인스턴스 생성

```python
student = Student()
student.name = '이승열'
student.email = 'leesy1403@naver.com'
# student = student(이름='이승열', email='leesy1403@naver.com', birthday='1993-02-06', age ='27')

student.save()

student = Student.objects.create(이름='이승열', email='leesy1403@naver.com', birthday='1993-02-06', age ='27')
```



### admin.py

```python
from django.contrib import admin
from .models import Student
admin.site.register(Student)	
```

