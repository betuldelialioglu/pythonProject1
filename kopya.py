class block():
    def __init__(self, xy):
        self.minx = min(xy[0], xy[2])
        self.maxx = max(xy[0], xy[2])
        self.miny = min(xy[1], xy[3])
        self.maxy = max(xy[1], xy[3])
        self.centerx = (xy[0] + xy[2])/2
        self.area_firmus = (self.maxx - self.minx) * (self.maxy - self.miny)
    def condition1(xy1 , xy2):
        if min(xy1.miny, xy2.miny) == 0:
            return 1
        else:
            return 0
    def condition2(xy1 , xy2):
        if xy1.miny == xy2.maxy or xy1.maxy == xy2.miny:
            if min(xy1.maxx, xy2.maxx) - max(xy1.minx, xy2.minx) > 0.001:
                return 1
            else:
                return 0
        else:
            return 0
    def condition3(xy1 , xy2):
        if xy1.miny > xy2.miny:
            if xy2.minx <= xy1.centerx <= xy2.maxx:
                return 1
            else:
                return 0
        else:
            if xy1.minx <= xy2.centerx <= xy1.maxx:
                return 1
            else:
                return 0
    def condition_checker(xy1, xy2):
        if block.condition1(xy1, xy2) and block.condition2(xy1, xy2) and block.condition3(xy1, xy2):
            return "FIRMUS"
        if block.condition1(xy1, xy2) and block.condition2(xy1, xy2) and block.condition3(xy1, xy2) == 0:
            return "ADDENDUM"
        else:
            return "DAMNARE"
    def area_or_coordinate(xy1, xy2):
        if block.condition_checker(xy1, xy2) == "FIRMUS":
            return xy1.area_firmus + xy2.area_firmus
        if block.condition_checker(xy1, xy2) == "ADDENDUM":
            if xy1.miny > xy2.miny:
                if xy1.centerx > xy2.maxx:
                    return [2*xy2.maxx - xy1.maxx, xy1.miny, xy1.maxx, xy1.maxy]
                else:
                    return[xy1.maxx, xy1.miny, 2*xy2.minx - xy1.minx, xy1.maxy]
            else:
                if xy2.centerx > xy1.maxx:
                    return [2*xy1.maxx - xy2.maxx, xy2.miny, xy2.maxx, xy2.maxy]
                else:
                    return[xy2.maxx, xy2.miny, 2*xy1.minx - xy2.minx, xy2.maxy]
        else:
            if  min(xy1.maxx, xy2.maxx) - max(xy1.minx, xy2.minx) < 0 or min(xy1.maxy, xy2.maxy) - max(xy1.miny, xy2.miny) < 0:
                return xy1.area_firmus + xy2.area_firmus
            else:

                return xy1.area_firmus + xy2.area_firmus - (min(xy1.maxx, xy2.maxx) - max(xy1.minx, xy2.minx))*(min(xy1.maxy, xy2.maxy) - max(xy1.miny, xy2.miny))
def is_firmus(corners1, corners2):

    xy1 = block(corners1)
    xy2 = block(corners2)

    return [block.condition_checker(xy1, xy2), block.area_or_coordinate(xy1, xy2)]
print(is_firmus([-0.5,10,-6,13],[-7,0,3,10]))
print(is_firmus([0.5,19,9.5,9],[3.8,9,5.5,0]))
print(is_firmus([-8,11,2,5],[1,0,-2,5]))
print(is_firmus([-7,5,7,10],[9.5,12.6,-1,10]))
print(is_firmus([-3,7,5,15],[-7,0,7,5]))
print(is_firmus([6,4,3.9,-1],[0.5,14.2,9.5,4]))
print(is_firmus([0,0,2.4,5.2],[-8.7,10,0,0]))
print(is_firmus([0,10,-8.7,0],[-4,9,-1,14]))





