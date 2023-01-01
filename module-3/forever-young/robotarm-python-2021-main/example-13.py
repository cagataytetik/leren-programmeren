from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
a =1
while a < 9: 
    robotArm.grab()
    if robotArm.scan() == '':
        break
    for b in range(a):
        robotArm.moveRight()
    robotArm.drop()
    for c in range(a):
        robotArm.moveLeft()
    a = a +1

robotArm.wait()