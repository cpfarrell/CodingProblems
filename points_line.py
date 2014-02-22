# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def count_points(self, points):
        counts = {}
        for point in points:
            combo = (point.x, point.y)
            if combo in counts:
                counts[combo]+=1
            else:
                        counts[combo]=1
        return [(Point(x, y), counts[x, y]) for x, y in counts]

    def max_min(val1, val2):
        return max(val1, val2), min(val1, val2)

    def gcf(self, val1, val2):
        diff = val1 % val2
        if diff == 0:
            return val2
        elif diff == 1:
            return 1
        else:
            return self.gcf(val2, diff)

    def line(self, point1, point2):
        rise = point1.y - point2.y
        run = point1.x - point2.x
        if run<0:
            run = -1*run
            rise = -1*rise
        if run == 0:
            rise = 1
        elif rise == 0:
            run = 1
        else:
            factor = self.gcf(max(abs(rise), abs(run)), min(abs(rise), abs(run)))
            rise = rise/factor
            run = run/factor
        b = run*point1.y - rise * point1.x
        return rise, run, b
    
    def maxPoints(self, points):
        if points is None:
            return None
        if len(points)<2:
            return len(points)
        
        points = self.count_points(points)

        if len(points)==1:
            return points[0][1]

        all_lines = {}
        for i, (point, count) in enumerate(points):
            new_lines = set([])
            for j, (sec_point, sec_count) in enumerate(points[i+1:]):
                line = self.line(point, sec_point)
                if line not in all_lines:
                    all_lines[line] = count + sec_count
                    new_lines.add(line)
                elif line in new_lines:
                    all_lines[line] += sec_count

        return max(all_lines[line] for line in all_lines)

s = Solution()
points = [(40,-23),(9,138),(429,115),(50,-17),(-3,80),(-10,33),(5,-21),(-3,80),(-6,-65),(-18,26),(-6,-65),(5,72),(0,77),(-9,86),(10,-2),(-8,85),(21,130),(18,-6),(-18,26),(-1,-15),(10,-2),(8,69),(-4,63),(0,3),(-4,40),(-7,84),(-8,7),(30,154),(16,-5),(6,90),(18,-6),(5,77),(-4,77),(7,-13),(-1,-45),(16,-5),(-9,86),(-16,11),(-7,84),(1,76),(3,77),(10,67),(1,-37),(-10,-81),(4,-11),(-20,13),(-10,77),(6,-17),(-27,2),(-10,-81),(10,-1),(-9,1),(-8,43),(2,2),(2,-21),(3,82),(8,-1),(10,-1),(-9,1),(-12,42),(16,-5),(-5,-61),(20,-7),(9,-35),(10,6),(12,106),(5,-21),(-5,82),(6,71),(-15,34),(-10,87),(-14,-12),(12,106),(-5,82),(-46,-45),(-4,63),(16,-5),(4,1),(-3,-53),(0,-17),(9,98),(-18,26),(-9,86),(2,77),(-2,-49),(1,76),(-3,-38),(-8,7),(-17,-37),(5,72),(10,-37),(-4,-57),(-3,-53),(3,74),(-3,-11),(-8,7),(1,88),(-12,42),(1,-37),(2,77),(-6,77),(5,72),(-4,-57),(-18,-33),(-12,42),(-9,86),(2,77),(-8,77),(-3,77),(9,-42),(16,41),(-29,-37),(0,-41),(-21,18),(-27,-34),(0,77),(3,74),(-7,-69),(-21,18),(27,146),(-20,13),(21,130),(-6,-65),(14,-4),(0,3),(9,-5),(6,-29),(-2,73),(-1,-15),(1,76),(-4,77),(6,-29)]
points = [Point(point[0], point[1]) for point in points]
print s.maxPoints(points)
