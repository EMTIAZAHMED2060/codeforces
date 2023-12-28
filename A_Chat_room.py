# problem link :
#     https://codeforces.com/contest/58/problem/A

s = input()
hello = "hello"
i = 0
for letter in s:
    if letter == hello[i]:
        i += 1
        if i == len(hello):
            print("YES")
            break
 
if i != len(hello):
    print("NO")