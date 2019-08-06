## WorkShop 12

* bootstrap cdn 링크를 통하여 불러온다.

  > link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/~~~"

* 추가한 스타일

```html
  <style>
  .row > div {
    border:1px solid black;
  }
  .row {
    margin:30px;
    background-color:moccasin;
  }
  </style>
```

>  row 안의 div에는 테두리를 설정해 주었고.
>
>  row는 margin을 주어서 여유있게 보이게 하였다.
>
>  row의 배경색상도 넣어주었다.

* 4개의 행 만들기

```html
  <div class="row">
    <div class="rounded col-sm-12 col-md-6 col-lg-3">1</div>
    <div class="rounded col-sm-12 col-md-6 col-lg-3">2</div>
    <div class="rounded col-sm-12 col-md-6 col-lg-3">3</div>
    <div class="rounded col-sm-12 col-md-6 col-lg-3">4</div>
  </div>
```

> 가로 해상도에 따른 설정을 맞추기 위하여
>
> 스마트폰(sm) 일때는 12칸으로 설정을 하여 한줄 다 들어가게 설정을 하였고,
>
> 태블릿PC(md)일 떄는 6칸으로 설정을 하여 한줄에 2개의 div가 들어가게 하였고,
>
> 노트북(lg)일 때는 3칸으로 설정을 하여 한줄에 4개의 div가 들어가게 설정하였다.
>
> 그 밖에 rounded 설정으로 테두리 부드럽게 처리하였다.
>