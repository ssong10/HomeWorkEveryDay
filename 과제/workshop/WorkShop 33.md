## WorkShop 33

> 다음은 Vue 인스턴스를 사용하여 렌더링한 DOM의 결과물이다.

```html
~~~
<body>
	<div id="app">
    	{{message}}
    </div>
    
    <script>
    	var app = new Vue({
            el: '#app',
            data: {
                message: 'Hello,World!'
            }
        })
    </script>
```

