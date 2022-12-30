from RobotArm import RobotArm
robotArm = RobotArm('exercise 2')
robotArm.speed = 3
robotArm.grab()
for o in range (9):
    robotArm.moveRight()
robotArm.drop()
for s in range (5):
    robotArm.moveLeft()
robotArm.grab()
for m in range(5):
    robotArm.moveRight()
robotArm.drop()
for s in range (2):
    robotArm.moveLeft()
robotArm.grab()
for s in range (2):
    robotArm.moveRight()
robotArm.drop()
robotArm.wait()