## WorkShop 10

### 1. 아래의 코드에서 몇 단락이 빨간색으로 변하는지 확인해보자

```HTML
<style>
  #ssafy > p:nth-of-type(2) {
    color:blue;
  }
</style>
<div id="ssafy">
  <h2>어떻게 선택될까?</h2>
  <p>첫번째 단락</p>
  <p>두번째 단락</p>
  <p>세번째 단락</p>
  <p>네번째 단락</p>
</div>
```

* #ssafy > p:nth-child(2) 를 사용하게 되면 ssafy 자식의 모든 태그 중에서 해당 태그에 style적용하게 된다. 하지만 해당 프로퍼티가 `<p>`가 아닐 경우에는 변하지 않는다.

  > 따라서 첫번째 단락이 변하게 되고 
  >
  > #ssafy>p:nth-child(1) 일 경우는 <h2> 태그라 변하지 않는다.

* #ssafy > p:nth-of-type(2) : ssafy 의 자식 중에서 `<p>`만 넘버링을 해서 해당 태그에 style을 적용하게 된다.

  > 두번째단락이 변하게 된다.