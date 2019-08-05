## Workshop 11

### bootstrap component를 이용하여 web 꾸미기

### 1. navigation bar

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>  
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/Ssong10">Git</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Python</a>
        </li>
      </ul>
    </div>
  </nav>
```

> navbar를 이용하여 navigation 상태창.
>
> Home은 아직 버튼에 target 이나 설정을 해주지 않아서 반응이 없는 모습입니다.
>
> Git에는 git link를 연결해 두었고
>
> Python은 aria-disabled로 효과가 없는 list입니다.



### 2. login forms

```html
  <div class="p-5">
    <form>
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
      </div>
      <div class="form-group">
        <label for="pwd_confirmation">Password Confirmation</label>
        <input type="password" class="form-control" id="pwd_confirmation" placeholder="Password Confirmation">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
```

> 이메일, password, Password Confirmation 3개의 div와 버튼을 하나의 form에 넣어둔 형태입니다.
>
> password, password confirmation은 input type을 password로 하여 타이핑한 글자가 나타나지 않게 해두었습니다.
>
> email address에 기본값을 주어서 submit을 눌렀을 때 이메일 형태에 맞게 하라고 메세지가 뜹니다.



### 3. Card-group

```html
<div class="card-group mx-5" style="max-width:45rem;">
    <div class="card">
      <img src="2wlq.jpg" class="card-img-top" alt="2wlq">
      <div class="card-body">
        <h5 class="card-title">아이유 2집</h5>
        <p class="card-text">Last Fantasy</p>
        <a href="https://www.youtube.com/watch?v=NJR8Inf77Ac" class="btn btn-primary">너랑 나 youtube</a>
      </div>
    </div>
    <div class="card">
      <img src="3wlq.jpg" class="card-img-top" alt="3wlq">
      <div class="card-body">
        <h5 class="card-title">아이유 3집</h5>
        <p class="card-text">Modern Times</p>
        <a href="https://www.youtube.com/watch?v=Q0xvVgKJxfs" class="btn btn-primary">분홍신 youtube</a>
      </div>
    </div>
    <div class="card">
      <img src="4wlq.jpg" class="card-img-top" alt="4wlq">
      <div class="card-body">
        <h5 class="card-title">아이유 4집</h5>
        <p class="card-text">Palette</p>
        <a href="https://www.youtube.com/watch?v=d9IxdwEFk1c" class="btn btn-primary">팔레트 youtube</a>
      </div>
    </div>
  </div>
```

> 카드 3개의 div가 하나의 card-group component로 묶여있는 형태입니다.
>
> card-group 최대폭을 주어서 커지지않게 설정을 하였습니다
>
> 하나의 카드마다 사진, title, text, 링크로 이루어져있습니다. 
>
> 링크에는 강사님이 좋아하실만한 유튜브 링크를 설정해 두었습니다.