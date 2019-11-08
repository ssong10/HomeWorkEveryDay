## WorkShop 34

> 다음과 같은 Vue 인스턴스가 있을 때, v-for 와 v-if 디렉티브를 활용하여 짝수만 나타나도록 하는 리스트를 작성하시오.

```html
var app = new Vue({
	el: '#app',
	data: {
	numbers: [0,1,2,3,4,5,6,7,8,9],
	},
})
```



```html
<div id='app'>
  <li v-for="number in numbers" v-if="!(number%2)">
      {{number}}
  </li>
</div>
```

