# problem link : 
#     https://codeforces.com/contest/236/problem/A

name = input()
distinct_chars = []
for char in name:
    if char not in distinct_chars:
        distinct_chars.append(char)
count_distinct_chars = len(distinct_chars)
if count_distinct_chars % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")