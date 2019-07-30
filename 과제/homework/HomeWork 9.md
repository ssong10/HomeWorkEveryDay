## HomeWork 9

### 1. HTML

> Hyper Text Markup Language



### 2. 맞으면 T, 틀리면 F

웹 표준을 만드는 곳은 Mozilla 재단이다.

> HTML5 -> W3C 에서 제정을 하고있다.

표(table)을 만들때에는 반드시 `<th>`태그를 사용해야한다.

> 아니다. `<td>`로도 만들수있다 `<th>` 는 맨윗줄 제목,볼드체로 사용된다.

제목(Heading)태그는 제목 이외에는 사용하지 않는 것이 좋다.

> 제목 태그는 제목에 사용하는게 접근성이나 재사용에 좋다.

인용문을 가리키는 태그는`<blockquote>`이다

> `<q>`  로 썼다.`/q>`  . `<blockquote>` 도 가능하다.



### 3. HTML5에서 새롭게 추가된 시맨틱(semantic)

```text
div   header   h1   section   footer
a     form    span
```

> header,   section,  footer



### 4. 아래 로그인 Form을 생성하는 HTML

ID :  user               (대충 이렇게 생겼다는 로그인창)

PWD : \****           `로그인`

```html
  <form action="">
    <label for="id">ID : </label>
    <input id="id" type="text" placeholder="user"><br>
    <label for="pwd">PWD :</label>
    <input id="pwd" type="password">
    <input type="submit" value="로그인">
  </form>
```

