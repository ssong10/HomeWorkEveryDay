## WorkShop 36

> v-bind 디렉티브의 class 또는 style 전달인자를 사용하여 아래와 같이 'Toggle' 버튼을 클릭 할 때 마다 작성된 문장이 빨강과 파랑으로 변경되도록 하는 앱을 만들어 봅시다.

```html
<div id="app">
    <button @click='Toggle'>
        Toggle
    </button>
    <h1 :style="{color:color}">
        빨강과 파랑을 섞으면 보라색이 됩니다.
    </h1>
    <script>
    	const app = new Vue({
            el : '#app',
            data : {
                color : 'red'
            },
            methods :{
                Toggle:function(){
                    if (this.color ==='red'){
                        this.color = 'blue'
                    } else {
                        this.color = 'red'
                    }
                }
            }
        })
    </script>
</div>
```

