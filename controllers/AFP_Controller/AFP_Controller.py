"""AFP_controlller controller."""
from controller import Robot, CameraRecognitionObject
def baslat(robot):
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    left_motor.setPosition(float("inf"))
    right_motor.setPosition(float("inf"))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
# Camera
    camera = robot.getDevice("camera1")
    camera.enable(timestep)
    camera.getSamplingPeriod()
    # Camera Recognation
    camera.recognitionEnable(timestep)
isWorkingRecognition = camera.hasRecognition()
    # Testing
    print(" - - - modül test alanı - - -")
    print(f"Kameranın Tanımlaması : {isWorkingRecognition}")
    print(" - - - - - - - - - - - - - - - - - ")
while robot.step(timestep) != -1:
        print(f"Tanımlanan cisim sayısı {number_of_objects}")
if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    baslat(robot)
