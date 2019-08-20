## WorkShop 15

### 1.

``` 
'Base is everywhere!' 이라는 문자를 공유하는 서로 다른 2개의 view를 나타낸 것이다. 템플릿 확정(template Extending)을 활용하여 아래와 같이 보여지는 3개의 html 파일을 작성하시오.
```



* urls.py

```python
urlpatterns = [
    path('one/',view.one),
    path('two/',view.two)
]
```

* base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  {% block css %} {% blockend %}
</head>
<body>
  <h1>Base is everywhere!</h1>
  {% block body %}
  {% endblock %}
</body>
</html>
```

* views.py

```python
def one(request):
    return render(request,'one.html')
def two(request):
    return render(request,'two.html')
```



* one.html

```html
{% extends 'base.html' %}
{% block body %}
  <h2> I am ONE! </h2>
{% endblock %}
```

* two.html
```html
{% extends 'base.html' %}
{% block body %}
  <h2> I am TWO! </h2>
{% endblock %}
```