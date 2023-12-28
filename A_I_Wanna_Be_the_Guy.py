
# problem link :
#             https://codeforces.com/problemset/problem/469/A


n = int(input())
x_levels = list(map(int, input().split()[1:]))
y_levels = list(map(int, input().split()[1:]))

all_levels = list(range(1, n + 1))

if all(level in x_levels or level in y_levels for level in all_levels):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
