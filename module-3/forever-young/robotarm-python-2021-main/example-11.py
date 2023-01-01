from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
v = 0
while v < 9:
    robotArm.grab()
    if robotArm.scan() == "white":
        v = v +1
        robotArm.moveRight()
    robotArm.drop()
    robotArm.moveRight()
    v = v +1
robotArm.wait()