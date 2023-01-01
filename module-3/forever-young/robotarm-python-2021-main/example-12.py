from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
color = "red"
rechts = 9
links = 9
for b in range(9):
    robotArm.grab()
    if robotArm.scan() == color:
        for f in range(rechts-b):
            robotArm.moveRight()
        robotArm.drop()
        for t in range(links-b):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
robotArm.wait()