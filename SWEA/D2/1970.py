# 두번째 풀이

for i in range(int(input())):
    result =[]
    b = int(input())
    won = [50000,10000,5000,1000,500,100,50,10]
    for j in won:
        a,b = divmod(b,j)
        result.append(str(a))
    print(f"#{i+1}\n{' '.join(result)}")

# 첫 번째풀이

# for tc in range(int(input())):
#     a,b = divmod(int(input()),50000)
#     b,c = divmod(b,10000)
#     c,d = divmod(c,5000)
#     d,e = divmod(d,1000)
#     e,f = divmod(e,500)
#     f,g = divmod(f,100)
#     g,h = divmod(g,50)
#     h,i = divmod(h,10)        
#     print(f"#{tc+1}\n{a} {b} {c} {d} {e} {f} {g} {h}")