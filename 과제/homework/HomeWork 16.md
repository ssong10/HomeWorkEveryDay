## HomeWork 16

### 1. Django 에서 선언한 Model을 실제 Datebase에 반영하는 과정

> 마이그레이션 (migration)

### 2. Model의 필드를 정의할때, CharField의 필수 인자

> `max_length = n` , 최대 n개의 문자 저장



### 3. 

```
Django에서 사용 가능한 모듈 및 메서드를 대화식  Python Shell에서 사용하려고 할 때, 어떠한 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.
```


  ```bash
$ python manage.py shell
$ python manage.py shell_plus
  ```

* shell` 에서는 내가 활용할 모델 import 해야 한다.

  ```python
  from articles.models import Article
  ```

* `shell_plus` 는 `django_extensions` 를 설치 후 `INSTALLED_APPS` 에 등록하고 활용해야 한다.

  ```bash
  $ pip install django-extensions
  ```

  ```python
  # crud/settings.py
  INSTALLED_APPS = [
      'django_extensions',
      ... ,
  ]
  ```