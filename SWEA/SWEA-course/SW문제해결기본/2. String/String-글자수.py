for tc in range(int(input())):
    a,b = input(), input()
    a_dict = {}
    b_dict = {}
    result =[]
    for i in a:
        if not i in a_dict:
            a_dict[i] =1
        else:
            a_dict[i] += 1
    for i in b:
        if not i in b_dict:
            b_dict[i] =1
        else:
            b_dict[i] += 1
    a_max = max(a_dict.values())
    for idx, value in a_dict.items():
            result.append(b_dict.pop(idx))
    print(f'#{tc+1} {max(result)}')