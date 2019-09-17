## HomeWork 20

### 1. School모델과 Student 모델 1:N 관계

```python
class School(models.Model):
    name = models.CharField(max_length=20)

class Student(models.Model): # 클래스 선언 : 단수형 + CamelCase
    name = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # 클래스 단수형 + 소문자
    
# 메서드, 함수, 변수 : snake_case
```

### 2. Question 모델과 Comment 모델은 1:N관계를 형성하고있다

```python
question = Questions.objects.get(id=id)
```

> 위와 같은 코드가 있을 때, views.py에서 해당 Question 의 모든 Comment를 가져오기 위한 코드를 작성하시오. (단, related_name은 설정하지 않았다고 가정한다.)
>

 ```
 comments = question.comment_set.all()
 ```

### 3. 1:N관계 설정할 때, ForeignKey 를 이용해서 1에 해당하는 클래스를 지정한다.

> 지정한 클래스가 Movie일 때, ForeignKey로 지정된 컬럼의 이름은 무엇인가?

```
Movie_id
```
