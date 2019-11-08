### WorkShop 38

>  Axios를 활용하여, 아래 그림과 같이 ‘Get {N} Dogs!’ 버튼을 클릭하면 Dog API URL로 HTTP 요청을 보내어 임의의 강아지 사진을 지정한 개수만큼 가져와 보여주는 앱을 만 들어 봅시다 

>  요청을 보낼 API URL은 `https://dog.ceo/api/breeds/image/random/{N}`입니다. 어떠한 형태로 데이터를 가져올 수 있는지 브라우저 주소창에 입력하여 확인해 보세요 

```html
  <div id='app'>
    <select v-model="num">
      <option v-for="number in numbers" v-vind:value="number">{{number}}</option>
    </select>
    <button v-on:click="getDog()">Get {{num}} Dogs!</button>
    <img v-for="imageUrl in imageUrls" v-bind:src="imageUrl" height="200px" width="200px" alt="">
  </div>
```

```html
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data : {
        num : '1',
        numbers:[1,2,3,4,5,6,7,8,9],
        imageUrls : []
      },
      methods: {
        getDog : function(){
          axios.get(`https://dog.ceo/api/breeds/image/random/${this.num}`)
            .then(response => {
              this.imageUrls = response.data.message
              })
        }
      }
    })
  </script>
```

