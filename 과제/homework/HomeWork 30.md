## HomeWork 30

### 1. 

> JavaScript는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5까지는 ‘var’ 키워드로 변수를
> 선언했다면, ES6 이후로는 ‘let’과 ‘const’ 키워드가 등장했다. ‘let’과 ‘const’의 차이점과
> 언제 사용하는지에 대하여 간단하게 작성하시오.

> let은 재할당은 가능하지만 재선언이 불가능하다. -> 변수 선언을 하고 바뀌는 값에 사용한다.
>
> const 는 재할당과 재선언이 둘다 불가능 하기 때문에 변하지 않는 상수에 사용을 한다.



### 2. 

> JavaScript에서는 Key – Value로 이루어진 자료 구조를 Object라고 한다. Object와
> JSON의 차이를 간단하게 작성하시오.

> Object 는 딕셔너리 형태로 key값을 통해 접근할 수 있는 model을 의미하고 
>
> JSON 은 Object를 String형식으로 바꾸어서 쭉 나열한 형태를 의미한다.



### 3. 

>아래의 코드가 있을 때, ‘value’에 접근하는 두 가지 방법을 코드로 작성하시오

```python
const myObject = {
    key:'value'
}
```

myObject['key']

myObject.key