## WorkShop 14

> num 이라는 app 대신 `services` app에 `push`와 `pull`을 만들어준다.

> 모든 요소는 services 폴더 내에서 활용

### templates

> path : services/templates/services/

* push.html

  ```html
  <h1>Push Number</h1>
  <form action="/services/pull">
    <input name="num" type="number">
    <input type="submit" value="push!">
  </form>
  ```

  > 나머지 기본적인 셋팅은 `base.html` 을 활용하였다.

* pull.html

  ```html
  <h1>Pull Number</h1>
  <h2>Pull 해보니 {{number}} 입니다!</h2>
  ```

### urls.py

> path : services/urls.py

```python
urlpatterns = [
    path('pull/',views.pull),
    path('push/',views.push)
]
```

> 기존의 `urlpatterns` 에 위의 url을 추가해 준다.



### views.py

> path : services/views.py

```python
def push(request):
    return render(request, 'services/push.html')

def pull(request):
    num = request.GET.get('num')
    context = {
        'num' : num
    }
    return render(request,'services/pull.html',context)
```

