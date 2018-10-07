import time
def fib(n):
    """
    Recursive implementation of fibonacci series
    :param n: Any integer >0

    :return:  Fibonacci number of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fastFib(n, memo = {}):
    """
    Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


for i in range(121):
    start = time.time()
    print('fib(' + str(i) + ') =', fastFib(i))
    end = time.time()
    fibmt=end-start
    if i>20 and i<30:
        start = time.time()
        fibresult=fib(i)
        end = time.time()
        fibt=end-start
        print("For {}:Time taken by recurive fib:{} and time taken by fib with memo:{}".format(i,fibt,fibmt))

