## WorkShop 20

### 1. 투표를 위한 설문앱

> 이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇 표를 받았는지 기록하는 기능을 가지고 있다. 설문 앱은 Question모델과 Choice 모델로 구성되어 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 형성하고 있다.

> 위와같은 컬럼을 가지고 있는 Question 모델과 Choice 모델을 정의하는 models.py코드를 작성하시오.

```python
from django.db import models

class Question(models.Model):
    title = models.CharField(max_lenght=20)
    
class Choice(models.Model):
    content = models.CharField(max_lenght=20)
    votes = models.IntegerField()
    question = models.ForeignKey(question, on_delete=models.CASCADE)
```

