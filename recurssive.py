def fibonacci(n):
    print("fibonacci had been called with n = " + str(n))
    if n == 0 or n == 1:
        return 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        print("Intermidiate result for ", fibonacci(n-1), " + fibonacci(", n-2, "): ", res)
        return res
print(fibonacci(5))
