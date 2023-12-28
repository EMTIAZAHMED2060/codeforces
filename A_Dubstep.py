# problem link :
#     https://codeforces.com/contest/208/problem/A
s = input().strip()
 
s = s.replace("WUB", " ")
 
words = s.split()
 
original_song = " ".join(words)
 
print(original_song)