def f1():
    f2()
    print('f1')

def f2():
    print('f2')

f1()
f2()