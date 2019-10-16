## WorkShop 26

### 1.

> 아래의 회원가입 페이지는 Django.contrib.auto.forms  모듈의 UserCreationForm 클래스를 활용한 것이다. 아래와 같은 페이지를 만들기 위하여 views.py 와 templates(signup.html)에 작성하여야 하는 코드를 작성하시오.

```python
# views.py
from Django.contrib.auto.forms import UserCreationForm

def signup(request):
    if request.method =="POST":
    	form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' :form
    }
    return render(request,'accounts/signup.html',context)
```

```html
<!-- signup.html --!>

{% extends 'articles/base.html' %}
{% block body %}
<form action="" method="POST" class="form">
  	{% csrf_token %}
	{{ form }}
	<input type="submit" class="btn btn-primary">가입하기</input>
</form>
{% endblock %}
```

