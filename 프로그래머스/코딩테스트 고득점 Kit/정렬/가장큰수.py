def big(num_list, num):
    length = max(map(lambda x:len(x),num_list))
    tmp = {}
    for i in range(len(num_list)):
        number = num_list[i]
        for _ in range(len(num_list[i]),length):
            number += num
        tmp[num_list[i]] = int(number)
    num_list.sort(key=lambda x:tmp[x],reverse=True)
    return num_list
    
def solution(numbers):
    result = []
    for i in range(9,-1,-1):
        tmp = []
        for number in numbers:
            if int(str(number)[0]) == i:
                tmp.append(str(number))
        if tmp:
            result += big(sorted(tmp,reverse=True),str(i))
    return ''.join(result)