## HomeWork 9

### 1. HTML

> Hyper Text Markup Language



### 2. 맞으면 T, 틀리면 F

웹 표준을 만드는 곳은 Mozilla 재단이다.

> HTML5 -> 

표(table)을 만들때에는 반드시 `<th>`태그를 사용해야한다.

> 아닌것같다. `<td>`로도 만들어지는거같던데

제목(Heading)태그는 제목 이외에는 사용하지 않는 것이 좋다.

> 제목이라...

인용문을 가리키는 태그는`<blockquote>`이다

> `<q>`  로 썼다.`/q>`



### 3. HTML5에서 새롭게 추가된 시맨틱(semantic)

```text
div   header   h1   section   footer
a     form    span
```

> header,   section,  footer



### 4. 아래 로그인 Form을 생성하는 HTML

ID :  user               (대충 이러한 느낌)

PWD : \****           `로그인`

```html
  <form>
    <label for="id">ID : </label>
    <input id="id" type="text" placeholder="user"><br>
    <label for="pwd">PWD :</label>
    <input id="pwd" type="password">
    <input type="submit" value="로그인">
  </form>
```

