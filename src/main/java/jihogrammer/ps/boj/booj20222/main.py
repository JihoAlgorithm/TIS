n, k = map(int, input().split())

if n % k == 0: print(k)
else: print(n // (n // k + 1))