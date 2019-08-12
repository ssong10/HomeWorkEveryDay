## HomeWork 13

### 1. Django 서버를 실행하는 명령어

```bash
$ python manage.py runserver
```

### 2. 

```
Django는 요청에 대한 응답을 할 때, 기본적으로 허용된 도메인으로부터 온 요청에 한해서만 응답을 하도록 설정되어 있다. settings.py 파일에서 특정 도메인을 허용하기 위해 수정해야 하는 변수명을 찾아 작성하시오.
```
```python
ALLOWED_HOST = ['*'] # 주소명을 적어준다.
```

### 3. 

```
주소 '/ssafy' 로 요청이 들어왔을 때 실행되는 함수가 views.py 파일 안의 ssafy 함수일 때, 요청에 응답할 수 있도록 urls.py 에 추가하여야 하는 코드를 작성하시오.
```

```python
from pages import views
# pages app의 views.py 파일을 불러온다.
urlpatterns = [
    path('admin/', admin.site.urls),
	path('ssafy/', views.ssafy),
    path(~~)
]
```

> ssafy의 url설정을 통하여 url과 해당하는 views의 함수를 이용하여 path설정을 해준다.
