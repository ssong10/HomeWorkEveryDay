def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i):
            a,b = phone_book[j] , phone_book[i]
            if len(a) > len(b):
                a,b = b,a
            if a == b[:len(a)]:
                return False
    return True