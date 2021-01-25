"""
1232. 缀点成线
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，
其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
"""

class XYCheck:
    def __init__(self, coordinates):
        self.a = self.b = 0
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        self.a = float(y1 - y2)/float(x1 - x2)
        self.b = float(y1 - x1 * self.a)
    def check(self, x, y):
        return self.a * x + self.b == y

def checkStraightLine(coordinates):
    check = XYCheck(coordinates)
    for x, y in coordinates[2:]:
        if check.check(x, y) == False:
            return False
    return True


def checkStraightLine2(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    A = y2 - y1
    B = -(x2 - x1)
    for x, y in coordinates[2:]:
        if A * (x - x1) + B * (y - y1) != 0:
            return False
    return True

print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) #true
print(checkStraightLine2([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) #true
print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) #false
print(checkStraightLine2([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) #false

"""
https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/solution/da-qia-by-shun-zi-6-6s1g/
将原列表的点移动相同的距离,使其经过原点,
利用方程式 A * x + B * y = 0, 得出常数A和B,
带入后续的点进行计算, 一旦发现结果不为0, 直接返回结果
"""

print("========NEXT===斜率计算=======")

def xielv(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    for x, y in coordinates[2:]:
        if (x1 - x2) * (y2 - y) != (x2 - x) * (y1 - y2):
            return False
    return True

print(xielv([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) #true
print(xielv([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) #false
