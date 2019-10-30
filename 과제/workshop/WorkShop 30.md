## WorkShop 30

### 아래의 Python 코드를 JavaScript 코드로 다시 작성하시오.
▪ 변수 및 함수 이름은 JavaScript naming convention(lowerCamelCase)을 따른다.
▪ Python의 F String은 JavaScript의 Template Literal을 사용한다.

```python 
def concat(str1, str2):
    return f'{str1} - {str2}'

def check_long_str(string):
    if len(string) > 10:
        return True
    else:
        return False
    
if check_long_str(concat('Happy','Hacking')):
    print('LONG STRING')
else:
    print('SHORT STRING')
```



```javascript
let concat = function (str1,str2) {
    return `${str1} - ${str2}`
}
let check_long_str = function (string) {
    return (string.length > 10 ? 'LONG STRING' :'SHORT STRING')
}

console.log(check_long_str(concat('Happy','Hacking')))
```

