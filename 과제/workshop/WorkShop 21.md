## WorkShop 21

### 투표를 위한 설문 앱을 만들려고 한다.

> 이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇 표를 받았는지 기록하는 기능을 가지고 있다. 설문 앱은 Question 모델과 Choice모델로 구성되어 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N관계를 형성하고 있다.

* Question 하나를 보여주는 페이지에서 Choice를 위의 오른쪽 그림과 같이 출력하려고 한다.

  HTML 파일에 아래와 같은 코드가 작성되있다고 할 때, Choice의 내용과 투표수를 출력하는 코드를 작성하시오.

```html
<h1> {{ question.title}}   </h1>
<ul>
    {% for choice in question.choice_set.all %}
<li><h3>{{ choice.content }} : {{ choice.votes }}표 </h3></li>
	{% endfor %}
</ul>
```

