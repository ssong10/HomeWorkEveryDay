## WorkShop 37 

> v-bind와 v-model 디렉티브를 활용하여, 다음과 같이 ‘Go!’ 링크를 누르면 입력 창에 작성한 URL로 이동 하도록 하는 ‘주소가 변하는 링크’를 만들어 봅시다 

```html
<div id="app">
    <input v-model="link">
    <a v-bind:href="link">Go!</a>
</div>

<script>
	const app = new Vue({
        el : "#app",
        data: {
            link:''
        }
    })
</script>
```

