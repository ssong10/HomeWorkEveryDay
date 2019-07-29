a=1
def func1():
    a=5
    def func2():
        print(a,end="")
    func2()
func1()
print(a)