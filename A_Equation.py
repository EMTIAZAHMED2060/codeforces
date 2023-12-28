# problem link : 
#     https://codeforces.com/contest/1269/problem/A

def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
 
n = int(input())
for i in range(n + 4, 10**9 + 1):
    if is_composite(i) and is_composite(i - n):
        print(i, i - n)
        break