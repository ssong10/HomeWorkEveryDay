## HomeWork 14

### 1. 

```
Django는 MTV로 이루어진 Web Framework 이다. MTV가 무엇의 약자인지 작성하시오.
```

> M :  `Model`
>
> T :  `Template`
>
> V: `View`



### 2. 

```
Django 프로젝트에서 page 앱을 생성하려고 할 때 입력해야 하는 명령어를 작성하시오.
```

```bash
$ python manage.py startapp page 
```



### 3.

```
pages 앱을 생성한 후, Django 프로젝트의 설정 파일인 settings.py에서 리스트로 된 변수 __(a)__에 생성된 앱의 이름을 추가해 주어야 한다. (a)에 들어갈 변수 이름을 작성하시오.
```

```python
INSTALLED_APPS = [
    'pages', 
]
```
