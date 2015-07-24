#!/usr/bin/python
num = 4
def a(func):
    num = 1
    print 'a:',num
    def __a():
        num = 2
        print '__a:',num
        func()
    return __a
@a
def b():
    num = 3
    print 'b:',num
b()
print 'g:',num
print "__name__:",__name__
if __name__ == "__main__"
