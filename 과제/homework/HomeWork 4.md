## HomeWork 4

### 1. 변수 찾을때 접근하는 공간 순서

```
LEGB Rule
Local scope : 정의된 함수
Enclosed scope: 상위 함수
Global scope: 함수 밖의 변수 혹은 import된 모듈
Built in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
```
### 2. 옳지 않은 것을 고르시오.

```
1) 함수는 오직 하나의 객체만 반환할 수 있어서. 'return a,b'처럼 쓸 수 없다.
## return a,b로 쓰게 되면 (a,b)라는 하나의 튜플 객체로 출력하게 된다.
	
2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
## return 이 없으면 출력후 함수는 None값을 반환한다.

3) 함수의 인자(parameter)는 함수를 선언할 때 설정한 값이며, 인수(argument)는 함수를 호출할 때 넘겨주는 값이다.
## parameter는 def 설정할때 쓰는 값. argument는 함수 호출할 때 쓰는 값.

4) 가변 인자를 설정할때는 인자 앞에 *을 붙이고, 이 때는 함수 내에서 tuple로 처리된다.
## *args 로 사용하게 되면 args( , , ) 튜플로 처리가 된다.
```
### 3.  재귀 함수를 쓰는 장점과 단점

```
장점 : 코드가 직관적이고 이해하기 쉽게 되어있다 (팩토리얼)
단점 : 함수사용을 여러 번 반복하기 때문에 횟수가 커지면 stack overflow가 발생
```
