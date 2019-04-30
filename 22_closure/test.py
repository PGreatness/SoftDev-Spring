'''
def inc(x):
    return x + 1

f = inc

print(f)

def adder(a, b):
    return a + b

def caller(c):
    print(c(2, 4))
    print(c(3, 5))

caller(adder)

def outer(x):
    def contains(l):
        return x in l
    return contains
contains_15 = outer(15)

print(contains_15([1, 4, 6, 14, 15, 17, 18, 19]))




def outer():
    x = 'foo'
    def inner():
        nonlocal x
        x = 'bar'
    inner()
    return x

outer()
'''
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    def access():
        nonlocal count
        return count
    return inc, access

c1, curr1 = make_counter()
c2, curr2 = make_counter()

print(c1())
print(f"Current 1: {curr1()}")
print(c1())
print(f"Current 1: {curr1()}")
print(c2())
print(f"Current 2: {curr2()}")
print(c1())
print(f"Current 1: {curr1()}")
print(c2())
print(f"Current 2: {curr2()}")
print(f"Current 1: {curr1()}")

def repeat(word):
    def num(number):
        a = ''
        for x in range(number):
            a += word
        return a
    return num

r1 = repeat('hello')
r2 = repeat('goodbye')

print(r1(2))
print(r2(2))
print(repeat('cool')(3))