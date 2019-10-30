## WorkShop 29

> 아래의 두 코드에 적절한 데코레이터를 사용하여 허용되지 않은 HTTP Method로 요청이 들어왔을 경우 405 Method Not Allowed 상태 코드를 반환하도록 하는 코드를 작성하시오.

```python
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        ~~~
    else:
        ~~~
    return render(~~)

@require_POST
def delete(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    article.delete()
    return redirect(~~)
```

