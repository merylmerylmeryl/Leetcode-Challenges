def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def fibonacciRecursive(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)

count = 0

for i in fibonacci():
    count += 1
    print(i)
    if count == 100:
        break
