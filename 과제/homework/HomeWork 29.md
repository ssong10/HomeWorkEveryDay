## HomeWork 29

### 1. 

> HTTP 상태 코드에서 200 ok는 요청에 대해 성공적으로 수행하였음을 나타낸다.
> 아래의 HTTP 응답 코드의 의미를 작성하시오.

> 404 :  Not Found , 페이지를 찾을 수 없음 -> 잘못된 오브젝트 요청 등

> 405: Method Not allowed -> 허용되지않은 Method 형태로 요청

> 500: internal server error -> 서버에러, 요청 처리 과정에서 예외 발생시 



### 2. 

> Django 모델에서 지정된 레코드에 값이 없을 때, 404 에러를 표시하도록 하는 shortcut함수와 해당 함수를 import 하는 코드를 작성하시오.

```python 
from django.shortcuts import get_object_or_404
```



### 3. 

> 아래의 설명 중 REST API 설계 기본 규칙에 어긋난 것을 고르시오.
>
> < 1 번 CRUD 동사표현 못들어간다 >

1) 필요한 경우 자원에 CRUD 동사 표현이 들어갈 수 있다.

2) 자원은 대문자보다 소문자를 사용한다.

3) URL 에 HTTP Method를 사용하지 않는다.

4) 자원간의 연관 관계가 있는 경우 `articles/1/comments/` 와 같이 작성한다.

5) URL에서 변하는 부분은 `/articles/<int:article_pk>/`와 같이 유일한 값이다.