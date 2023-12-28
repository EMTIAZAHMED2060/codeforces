# problem link : 
#     https://codeforces.com/contest/282/problem/A

n = int(input())
x = 0
 
for i in range(n):
    statement = input()
    if "++" in statement:
        x += 1
    else:
        x -= 1
 
print(x)