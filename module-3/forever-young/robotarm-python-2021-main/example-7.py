from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for n in range(5):
    for v in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for z in range(2):
        robotArm.moveRight()
robotArm.wait()