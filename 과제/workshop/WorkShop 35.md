## WorkShop 35

> v-on 디렉티브를 활용하여, 다음과 같이 '+1' 버튼을 누르면 숫자가 하나씩 증가하는 Counter앱을 만들어 봅시다.

```html
<div id="app">
    <button v-on:click="countUp">+1</button>
    <p>counter : {{ counter }}</p>
</div>
~~~
<script>
    const app = new Vue({
      el : '#app',
      data : {
        counter : 0,
      },
      methods :{
        countUp : function(){
          this.counter++
        }
      }
    })
</script>
```

