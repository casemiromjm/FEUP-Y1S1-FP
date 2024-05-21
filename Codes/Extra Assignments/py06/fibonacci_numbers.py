def fib(n):
    fibonacciSequence = [0,1]
    if n == 1:
        fibonacciSequence.remove(1)
        return fibonacciSequence
    elif n == 2:
        return fibonacciSequence
    else:
        for i in range(n-2):
            fib_num = fibonacciSequence[len(fibonacciSequence) - 1] + fibonacciSequence [len(fibonacciSequence) - 2]
            fibonacciSequence.append(fib_num)
        return fibonacciSequence