# problem link : 
#     https://codeforces.com/contest/158/problem/A

n, k = map(int, input().split())
scores = list(map(int, input().split()))
 
k_score = scores[k-1]
num_advancers = 0
for score in scores:
    if score > 0 and score >= k_score:
        num_advancers += 1
    else:
        break
 
print(num_advancers)