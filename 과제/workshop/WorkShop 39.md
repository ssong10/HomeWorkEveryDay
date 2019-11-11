## WorkShop 39

> Axios를 활용하여, 아래 그림과 같이 'Get Posts' 버튼을 클릭하면 특정 URL로 HTTP요청을 보내어 임의의 Post의 리스트를 가져와 보여주는 앱을 만들어 봅시다.

```html
<div id="app">
    <button v-model="getPost">
        Get Posts!
    </button>
    <li v-for="post in posts"><strong>{{post.title}}</strong> - <span>{{post.body}}</span></li>
</div>
<script>
	const app = new Vue({
        el : "#app",
        data : {
            posts: []
        },
        methods :{
            getPost :function() {
                axios.GET('https://jsonplaceholder.typicode.com/posts')
                	.then(response => {
                    	this.posts = response.data
                })
            }
        }
    })
</script>
```



