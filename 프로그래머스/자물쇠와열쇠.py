def spin(key):
    size = len(key)
    tmp = [[0] * size for _ in range(size)]
    for y in range(size):
        for x in range(size):
            tmp[y][size-1-x] = key[x][y]
    return tmp

def check(key,lock,y,x, length):
    for dy in range(length):
        for dx in range(length):
            if -1<dy-y<len(key) and -1< dx-x<len(key):
                if lock[dy][dx] + key[dy-y][dx-x] != 1:
                    return False
            else:
                if not lock[dy][dx]:
                    return False
    return True

def solution(key, lock):
    length = len(lock)
    for y in range(-length,length):
        for x in range(-length,length):
            for _ in range(4):
                key = spin(key)
                if check(key,lock,y,x,length):
                    return True
    return False