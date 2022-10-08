def func1():
    print('called func1')

def func2(f):
    f()

func2(func1)