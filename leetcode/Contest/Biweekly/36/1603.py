# 1603. Design Parking System
# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:
    lst = [0,0,0]
    def __init__(self, big: int, medium: int, small: int):
        self.lst[0] = big
        self.lst[1] = medium
        self.lst[2] = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.lst[0] > 0:
                self.lst[0] -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.lst[1] > 0:
                self.lst[1] -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.lst[2] > 0:
                self.lst[2] -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)