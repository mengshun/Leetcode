"""
628 三个数的最乘积
"""


def bubbleSort(array):
    # 冒泡排序
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def selectSort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        if minIndex != i:
            array[minIndex], array[i] = array[i], array[minIndex]

def maximunProduct(nums):
    if len(nums) == 3:
        return nums[0]*nums[1]*nums[2]
    def insertSort(array):
        #插入排序
        for i in range(1, len(array)):
            pre = i - 1
            cur = array[i]
            while pre >= 0 and cur < array[pre]:
                array[pre+1] = array[pre]
                pre -= 1
            array[pre+1] = cur

    #不影响原数据
    array = list(nums)
    #排序
    insertSort(array)
    # array.sort()  如果直接使用插入排序算法 在海量数据面前会超时 所以暂时使用系统的内置排序算法
    return max(array[0]*array[1]*array[-1], array[-3]*array[-2]*array[-1])

print(maximunProduct([-100,-98,-1,2,3,4]))


