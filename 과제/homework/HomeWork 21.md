## HomeWork 21

### 1. 1:N

> Question 모델과 Comment 모델이 1:N 관계를 형성하고 있을 때, 하나의 Question을 보여주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html파일이 있을 때, 모든  Comment의 content를 h3 태그를 이용하여 출력하는 for문을 작성하시오

```html
{% extends 'base.html' %}
{% block body %}
<h1> {{ question.title }} </h1>

# DTL 에서는 () [] 을 사용할 수 없음.
# a[3]은 a.3
# dict['key'] = dict.key

{% for comment in question.comment_set.all %}
	<h3> {{comment.content}} </h3>
{% endfor %}

{% endblock %}
```

### 2. urls.py

> comment를 작성하는 폼을 만들기 위하여 form 태그 안에 action 속성값으로 넣어야 하는 경로를 작성
```python
# urls.py
app_name = 'question'
urlpatterns = [
   path('', views.index, name='index'),
   path('create/', views.create, name='create'),
   path('<int:pk>/', views.detail, name='detail'),
   path('<int:pk>/update/', views.update, name='update'),
   path('<int:pk>/comments/create/', views.comments_create, name='comments_create'),
]
```

```html
  <form action="{% url 'question:comments_create' question.pk %}">
```

