from RobotArm import RobotArm
robotArm = RobotArm('exercise 5')
robotArm.speed = 4
for h in range(7):
    robotArm.moveRight()
robotArm.grab()
for h in range(1):
    robotArm.moveRight()
robotArm.drop()
for s in range(7):
    for h in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    for h in range(1):
        robotArm.moveRight()
    robotArm.drop()
robotArm.wait()
