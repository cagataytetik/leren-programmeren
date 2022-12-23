from RobotArm import RobotArm
robotArm = RobotArm('exercise 4')
robotArm.speed = 3
for a in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    if a != 4:
        for b in range(2): 
            robotArm.moveLeft()
for c in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
robotArm.wait()