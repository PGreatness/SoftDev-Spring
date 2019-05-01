import random
""" 
def make_HTML_heading(f):
    txt = f()
    def inner():
        return f"<h1>{txt}</h1>"
    return inner

@make_HTML_heading
def greet():
    greetings = ['hello', 'welcome', 'ayo!', 'hola', 'bonjour', 'word up']
    return random.choice(greetings)

print(greet())
"""

def memoize(f):
    memo = {}
    def helper(n):
        if n not in memo.keys():
            memo[n] = f(n)
        return memo[n]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(4)) # 3 
print(fib(5)) # 5
print(fib(6)) # 8
print(fib(40)) # some ridiculously large number
