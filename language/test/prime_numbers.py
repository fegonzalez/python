for n in range(2, 10):    # 2, 3, .., 10-1
    for x in range(2, n): # 2, 3, .., n-1
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
