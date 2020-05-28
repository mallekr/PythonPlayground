from functools import reduce


def factors(n):
    #return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
    for i in range(1, 1000000):
        if n % i == 0:
            print(i)

    print(n // 287035)

print(factors(58836051389031984116367394234179806555576871688966092712821586590838813981451212979687476042120243010722 +
              4246948833))

