## HomeWork 36

### 1.

> 아래와 같은 템플릿 코드와 Vue 인스턴스의 data속성이 있을 때, 어떠한 HTML 코드가 렌더링 되는지 작성하시오.

```html
<div class="static" v-bind:class="{active:isActive, 'error': hasError}">
</div>
~~~
data: {
	isActive:true,
	hasError: false,
}
```

class="active"



### 2.

> 아래와 같은 템플릿 코드와 Vue 인스턴스의 data속성이 있을 때, 어떠한 HTML코드가 렌더링 되는지 작성하시오.

```html
<div v-bind:style="{color:activeColor, fontsize:fontSize + 'px'}">
</div>
~~~
data : {
	activeColor : 'red',
	fontSize: 30
}
```

style="color:red;fontSize:30px"

