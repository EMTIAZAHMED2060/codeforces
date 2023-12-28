# problem link :
#     https://codeforces.com/contest/133/problem/A

def output(n):
    for c in n:
        if c in "HQ9":
            return "YES"
    return "NO"
 
n = input()
print(output(n))