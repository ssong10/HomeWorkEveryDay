## HomeWork 39

### 1.

> 아래 그림과 같이 새로운 글을 작성하기 위해 Axios를 사용하여 '/articles/create/'로 POST요청을 보내려 할 때, 아래의 빈칸 (a),(b)에 들어갈 코드를 작성하시오.

```html
createArticle: function() {
	axios.POST(,{
		title:'안녕하세요.',
		body:'반갑습니다.',
	}).then((response) => {
		// ...	
	})
}
```

### 2.

> CORS가 무엇이 약자인지 작성하고, 의미하는 바가 무엇인지 간단하게 작성하시오.

Cross-Origin Resource Sharing 표준은 웹 브라우저가 사용하는 정보를 읽을 수 있도록 허가된 출처 집합을 서버에게 알려주도록 허용하는 HTPP를 추가함으로써 동작한다.

