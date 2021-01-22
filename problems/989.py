"""
989. 数组形式的整数加法
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
"""

def addToArrayForm(A, K):
    k_list = [int(x) for x in list(str(K))]

    a_list = A
    if len(k_list) > len(a_list):
        k_list, a_list = a_list, k_list

    for i in range(len(k_list)):
        sum = k_list.pop() + a_list[len(a_list) - i - 1]
        a_list[len(a_list) - i - 1] = sum % 10
        if sum > 9:
            last = 1
            while last != 0:
                 index = len(a_list) - i - 2
                 if index < 0:
                     a_list.insert(0, 1)
                     last = 0
                 else:
                     asum = a_list[index] + 1
                     if asum > 9:
                         i += 1
                     else:
                         last = 0

                     a_list[index] = asum % 10

    return a_list

def addToArrayForm2(A, K):
    n = len(A) - 1
    while K != 0:
        sum = A[n] + K
        K, A[n] = sum // 10, sum % 10
        n -= 1
        if n == -1 and K:
            A.insert(0, 0)
            n = 0
    return A


print(addToArrayForm([9,9,], 1))
print(addToArrayForm2([9,9,], 1))