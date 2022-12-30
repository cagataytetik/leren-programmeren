from RobotArm import RobotArm
robotArm = RobotArm('exercise 5')
robotArm.speed = 4
for s in range(1,8):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for p in range(1,8):
    for k in range(1,3):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()