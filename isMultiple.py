import random

def is_multiple(n, m):
    # n-type: int
    # m-type: int
    # ret-type: bool

    return m % n == 0

def is_even(k):
    # k-type: int
    # ret-type: bool
    return is_multiple(2, k)

def minmax(data):
    # data-type: list of 1 or more ints
    # ret-type: tuple len(2) of smallest and largest numbers
    minVal = maxVal = data[0]

    for i in range(len(data)):
        minVal = data[i] if data[i] < minVal else minVal
        maxVal = data[i] if data[i] > maxVal else maxVal

    return (minVal, maxVal)

def sum_of_squares(n):
    # n-type: int
    # ret-type: int. Sum of the squares of all positive ints smaller than n
    return sum([k*k for k in range(n)])

def sum_of_odd_squares(n):
    # n-type: int
    # ret-type: int. Sum of the squares of all odd positive ints smaller than n
    return sum([k*k for k in range(n) if k%2!=0])

def merylChoice(data):
    # data-type: list of ints
    # ret-type: int. A randomly selected element from data
    return data[random.randint(0, len(data)-1)]

def merylReverse(data):
    # data-type: list of ints
    # Reverse the elements in data
    i = 0
    j = -1
    while abs(i) <= abs(j) and i <= len(data) // 2:
        print(i, j)
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
    
def is_odd_product(data):
    # data-type: list of ints
    # ret-type: tuple of nums that make odd product
    odds = []
    for i in range(len(data)):
        if data[i] % 2 != 0:
            odds += [data[i]]
            if len(odds) == 2:
                break
    return odds if len(odds) == 2 else None

def is_all_different(data):
    # data-type: list of ints
    # ret-type: bool. True if all nums are different from each other,
    # False if otherwise
    return True if len(data) == len(set(data)) else False
