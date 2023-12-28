
# problem link : 
#     https://codeforces.com/contest/116




n = int(input())
max_passengers = 0
passengers = 0
 
for i in range(n):
    a, b = map(int, input().split())
    passengers -= a 
    passengers += b 
    max_passengers = max(max_passengers, passengers)
 
print(max_passengers)