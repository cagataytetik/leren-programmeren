from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 4

for a in range(1, 5):
  for b in range(a):
    robotArm.grab()
    for c in range(5):
      robotArm.moveRight()
    robotArm.drop()
    for c in range(5 - int(b == a - 1)):
        robotArm.moveLeft()


robotArm.wait()