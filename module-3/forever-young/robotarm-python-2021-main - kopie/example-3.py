from RobotArm import RobotArm
robotArm = RobotArm('exercise 3')
robotArm.speed = 3
for k in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
robotArm.wait()