# problem link : 
#     https://codeforces.com/contest/339/problem/A


p = input().split('+')
p = '+'.join(reversed(p))
p = '+'.join(sorted(p.split('+')))
 
print(p)