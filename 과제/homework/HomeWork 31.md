## HomeWork 31

###  1. 

> DOM에서 특정 요소를 선택하 때, document.querySelector() 뿐만 아니라document.querySelectorAll() 역시 사용할 수 있다. 이 둘의 차이를 간단하게 작성하시오.

document.querySelector() : 특정 name이나 id를 제한하지 않고 css선택자를 사용하여 요소를 찾는다.

document.querySelectAll() : 동일하게 작동하나 해당 선택자에 해당하는 모든 요소를 가져온다



### 2. 

> DOM에 요소를 추가할 때, ‘innerHTML += ...‘의 방법과 ‘appendChild()’ 함수를 사용하는 방법이 있다. 이 둘의 차이를 간단하게 작성하시오.

innterHTML : Dom객체의 Property로 존재한다. 속성에 대해 얻거나 할당하거나 하는 동작을 취한다는 뜻이다.  해당 Dom 객체 내부의 HTML을 주어진 인자로 교체하거나 아니면 반환한다.(공격에 취약하다.)

appendChild Method : 인자를 Dom 객체를 받아 해당 객체의 자식 리스트 맨 마지막에 더해주는 기능을 한다.

