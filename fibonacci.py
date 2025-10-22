def fibonacci(n):
    print(f"First {n} fibonacci numbers:")
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print(a)
    else:
        print(a, b, end=' ')
        for i in range(n-2):
            c = a + b
            print(c, end=' ')
            a, b = b, c

n = int(input("Enter the no. for fibonacci series: "))
fibonacci(n)
