class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = [(x[0], x[1]) for x in points]
        points_set = set(points)
        min_area = float("inf")

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                if xi == xj or yi == yj:
                    continue

                if (xi, yj) in points_set and (xj, yi) in points_set:
                    area = abs(xi - xj) * abs(yi - yj)
                    min_area = min(min_area, area)

        return min_area if min_area < float("inf") else 0
