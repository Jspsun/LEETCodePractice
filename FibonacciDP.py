def fib(n):
    if n < 0:
        return -1
    memo = [0, 1]
    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[n]

print fib(999000)
