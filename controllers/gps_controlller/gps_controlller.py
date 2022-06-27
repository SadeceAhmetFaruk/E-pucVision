"""gps_controlller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,CameraRecognitionObject,Keyboard,DistanceSensor
import math



def get_bearing_in_degrees(x):
    north = x
    rad = math.atan2(north[0], north[2])
    bearing = (rad - 1.5708) / math.pi * 180.0
    # if bearing < 0.0:
    #  bearing = bearing   360.0
    return bearing


def baslat(robot):

    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28

    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")

    left_motor.setPosition(float("inf"))
    right_motor.setPosition(float("inf"))

    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    # Distance Sensors 
    ps0 = robot.getDevice("ps0")
    ps1 = robot.getDevice("ps1")
    ps2 = robot.getDevice("ps2")
    ps3 = robot.getDevice("ps3")
    ps4 = robot.getDevice("ps4")
    ps5 = robot.getDevice("ps5")
    ps6 = robot.getDevice("ps6")
    ps7 = robot.getDevice("ps7")
    
    ps0.enable(timestep)
    ps1.enable(timestep)
    ps2.enable(timestep)
    ps3.enable(timestep)
    ps4.enable(timestep)
    ps5.enable(timestep)
    ps6.enable(timestep)
    ps7.enable(timestep)
    
    
   
    #Keyboard Control 
    keyboard = Keyboard()
    keyboard.enable(timestep)

    # Gps

    gps = robot.getDevice("gps")
    gps.enable(timestep)

    # compass

    compass = robot.getDevice("compass")
    compass.enable(timestep)

    # Camera
    camera = robot.getDevice("camera1")
    camera.enable(timestep)
    camera.getSamplingPeriod()
    # Camera Recognation
    camera.recognitionEnable(timestep)
    
    isWorkingRecognition = camera.hasRecognition()
    # Testing 
    print("----- modül test alanı -----")
    print(f"Kameranın Tanımlaması : {isWorkingRecognition}")
    print("----------------------------------")
    
    
    toplam = 0 
    while robot.step(timestep) != -1:
        ps0_val = ps0.getValue()
        ps1_val = ps1.getValue()
        ps2_val = ps2.getValue()
        ps3_val = ps3.getValue()
        ps4_val = ps4.getValue()
        ps5_val = ps5.getValue()
        ps6_val = ps6.getValue()
        ps7_val = ps7.getValue()
    
        number_of_objects = camera.getRecognitionNumberOfObjects()
        
        if (toplam<number_of_objects):
            toplam = number_of_objects
        
        
        gps_values = gps.getValues()
        compass_values = compass.getValues()
        
        
        # Gps values changing 
        msg = "Compass Values: " 
        for each_val in gps_values:
            msg  =  "{0:0.5f}".format(get_bearing_in_degrees(gps_values))
        
        if(number_of_objects > 1):
            if(ps7_val == 70 and ps0_val==70):
                left_motor.setVelocity(0.0)
                right_motor.setVelocity(0.0)
            left_motor.setVelocity(max_speed)
            right_motor.setVelocity(max_speed)    
            print(f"Tanımlanan cisim sayısı {number_of_objects} Bu Yangının Konumu ise {msg}")
        else:
            left_motor.setVelocity(-max_speed* 0.25)
            right_motor.setVelocity(max_speed)
        
        key = keyboard.getKey()
        if (key == 315):
            left_motor.setVelocity(max_speed)
            right_motor.setVelocity(max_speed)
        elif (key==317):
            left_motor.setVelocity(-max_speed)
            right_motor.setVelocity(-max_speed)
        elif(key==316):
            left_motor.setVelocity(max_speed)
            right_motor.setVelocity(-max_speed)
        elif(key==314):
            left_motor.setVelocity(-max_speed)
            right_motor.setVelocity(max_speed)
        elif(key==Keyboard.CONTROL+ord('M')):
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(0.0)
            print("----------------------------------------------------")
            print(f"Toplam yangın sayısı {toplam} olarak yakalanmıştır.")
            print(f"Aracınızın şuan ki konumu {gps_values} veya {msg}.")
        
if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    baslat(robot)
    
