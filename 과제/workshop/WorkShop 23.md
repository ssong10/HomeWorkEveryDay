## WorkShop 23

>Django의 Fixture 기능을 활용하여 myapp의 Musician 모델에 데이터를 일괄 삽입하려
>할 때, 아래와 같이 데이터를 삽입하기 위하여 필요한 json 파일을 작성하시오.



python manage.py loaddata musicians.json

> musicians.json

```json
[
{
"model": "Myapp.musicians",
"pk": 1,
"fields": {
	"first_name": "John",
    "last_name" : 'Lennon'
 },
{
"model": "Myapp.musicians",
"pk": 2,
"fields": {
	"first_name": "Paul",
    "last_name" : 'McCartney'
 },  
]
```



