## HomeWork 26

### 1. 

> 로그인을 한 사용자만 게시물을 작성할 수 있도록 코드를 작성하려고 한다.
>
> 아래의 빈칸 (a), (b)에 들어갈 코드를 작성하시오.

```python
from (a) import (b)

@(b)
def create(request):
    if request.method =="POST":
        article_form = ArticleForm(request.POST)
```

> (a) = django.contrib.auth.decorators
>
> (b) = login.required



### 2.

> Article 모델에 사용자 정보가 담긴 모델과 1:N 관계를 형성하기 위한 칼럼을 추가하려
> 고 한다. 아래의 빈 칸 (a), (b)에 들어갈 코드를 작성하시오.

```python
from django.db import models
from django.conf import (a)

class Article(models.Model):
    user = models.ForeingKey((b), on_delete=models.CASCADE)
```

