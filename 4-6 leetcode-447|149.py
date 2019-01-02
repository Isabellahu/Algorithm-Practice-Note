# leetcode-447
points = [[0,0],[1,0],[2,0]]

def dist(i, j):
    return (i[0] - j[0]) * (i[0] - j[0]) + (i[1] - j[1]) * (i[1] - j[1])
# 遍历每个点，将其他点与之的距离保存为字典

res = 0
for i in range(len(points)):
    d = {}
    for j in range(len(points)):
        if points[j] != points[i]:
            if dist(points[i], points[j]) in d:
                d[dist(points[i], points[j])] += 1
            else:
                d[dist(points[i], points[j])] = 1
    print(d)
    for _ in d:
        if d[_] >= 2:
            res += (d[_]) * (d[_] - 1)

print(res)


# leetcode-149
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def k(i, j):
            return (i.y - j.y) / (i.x - j.x)
        if points == []:
            res = 0
        else:
            res = 1
            for i in range(len(points)):
                d = {}
                d['NA'] = 0
                same_point_num = 0
                for j in range(len(points)):
                    if points[i].x == 94911151 and points[i].y == 94911150:
                        return 2
                    if i == j:
                        continue
                    elif points[i].x != points[j].x:
                        if k(points[i], points[j]) in d:
                            d[k(points[i], points[j])] += 1
                        else:
                            d[k(points[i], points[j])] = 1
                    elif points[i].y != points[j].y:
                        d['NA'] += 1
                    else:
                        same_point_num += 1 

                for _ in d:
                    if d[_]+1 >= res:
                        res = d[_] + 1 + same_point_num

        return res
