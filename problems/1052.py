"""
1052. 爱生气的书店老板
"""

def maxSatisfied(customers, grumpy, x):
    n = len(customers)
    res = sum([x for x, y in zip(customers, grumpy) if y == 0])
    max_v = cur_sum = sum([x * y for x, y in zip(customers[:x], grumpy[:x])])
    for i in range(x, n):
        cur_sum = cur_sum - customers[i-x] * grumpy[i-x] + customers[i] * grumpy[i]
        max_v = max(max_v, cur_sum)
    return res + max_v
    # n = len(customers)
    # if n <= x:
    #     return sum(customers)
    # res = sum([customers[i] for i in range(n) if grumpy[i] == 0])
    # grum_list = []
    # for i in range(n):
    #     if grumpy[i] == 1:
    #         grum_list.append(customers[i])
    #     else:
    #         grum_list.append(0)
    # cur = 0
    # cur_sum = max_value = sum(grum_list[:x])
    # while cur < n - x:
    #     cur_sum = cur_sum - grum_list[cur] + grum_list[cur+x]
    #     max_value = max(max_value, cur_sum)
    #     cur += 1
    # res += max_value
    # return res

print(maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))