from attr import set_run_validators


class robot():
    
    sitting=False
    standing=False
    lying_down=True
    legs=2
    arms=2
    eyes=4
    wheels=2
    def post(self,position):
        if position=="s":
            self.sitting=True
            return "it is sitting"
        if position=="t":
            self.standing=True
            return "it is standing"
        if position=="l":
            return "it still lying down"
    def physical_feat(self):
        return f"My robot has {self.legs} legs, {self.arms} arms, {self.wheels} wheels, {self.eyes} eyes"

miRobot=robot()
position=input("what is it doing right now?")
miRobot.post(position)
print(f"{miRobot.physical_feat()} and {miRobot.post(position)}")