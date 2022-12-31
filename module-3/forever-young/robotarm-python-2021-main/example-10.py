from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for r in range(5):
    for x in range(r): robotArm.moveRight()
    robotArm.grab()
    for q in range(9 -r -r): robotArm.moveRight()
    robotArm.drop()
    for p in range(9 + r): robotArm.moveLeft()
robotArm.wait()