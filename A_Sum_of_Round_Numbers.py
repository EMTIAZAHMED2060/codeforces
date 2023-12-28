# problem link :
#     https://codeforces.com/contest/1352/problem/A

loop = int(input())
net_total = []
net_list = []
for i in range(loop):
    total = 0
    l1 = []
    l2 = []
    n = int(input())
    tem = n
    pwr = 10**len(str(n))
    if n % 10 == 0 and n < 10:
        total += 1
        print(total)
        print(n)
    else:
        while tem > n or pwr > 0:
            unit = tem // pwr
            l1.append(unit*pwr)
            tem %= pwr
            pwr //= 10
            total += 1
        for i in l1:
            if i != 0:
                l2.append(i)
        net_total.append(len(l2))
        net_list.append(l2)
for i in range(len(net_total)):
    print(net_total[i])
    for j in net_list[i]:
        print(j, end=" ")
    print()