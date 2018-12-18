class Ship():
##    shipType = ""
##    damage = -1
##    hp = -1
##    masts = -1
##    aRange = -1 #attack range
##    accuracy = -1
##    speed = -1
##    carry = -1
##    sight = -1

    def __init__(self, ship):
        self.shipType=ship
        if(ship) == "galley":
            self.damage=self.hp=self.masts=self.aRange=self.accuracy=self.speed=self.carry=self.sight=3
        elif
            
    def __str__(self):
        rv = "Ship:\nType: " + str(self.shipType) + "\nDamage: " + str(self.damage)
        rv += "\nHp: " + str(self.hp) + "\nMasts: " + str(self.masts)
        rv += "\nRange: " + str(self.aRange) + "\nAccuracy: " + str(self.accuracy)
        rv += "\nSpeed: " + str(self.speed) + "\nCarry " + str(self.carry) + "\nSight: " + str(self.sight)
        return rv
