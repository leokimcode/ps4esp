import pygame
import json, os
import socket 

   

################# UDP SEND RECEIVE ################
UDP_IP = "192.168.1.177"
UDP_PORT = 8888
localPort = 3241

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # this means we are using UDPcntrl questions mark for comment
sock.bind(("", localPort)) #automatic ip, localPort

def moveLeft():
    print("moving left")
    sock.sendto(b"move left", (UDP_IP, UDP_PORT))

def moveRight():
    print("moving right")
    sock.sendto(b"move right", (UDP_IP, UDP_PORT))

def moveUp():
    print("moving up")
    sock.sendto(b"move up", (UDP_IP, UDP_PORT))

def moveDown():
    print("moving down")
    sock.sendto(b"move down", (UDP_IP, UDP_PORT))

################################# LOAD UP ####################################
pygame.init()
running = True
LEFT, RIGHT, UP, DOWN = False, False, False, False
clock = pygame.time.Clock()
###########################################################################################

#######################Initialize /ntroller#################################
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)
# 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
# 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }

################################ START OF GAME LOOP####################################3
while running:
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass

        # HANDLES BUTTON PRESSES
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['left_arrow']:
                LEFT = True
                print("left button pressed")
                moveLeft()
            if event.button == button_keys['right_arrow']:
                RIGHT = True
                print("right button pressed")
                moveRight()
            if event.button == button_keys['down_arrow']:
                DOWN = True
                print("down button pressed")
                moveDown()
            if event.button == button_keys['up_arrow']:
                UP = True
                print("up button pressed")
                moveUp()

        # HANDLES BUTTON RELEASES
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['left_arrow']:
                LEFT = False
                print("left button released")
            if event.button == button_keys['right_arrow']:
                RIGHT = False
                print("right button released")
            if event.button == button_keys['down_arrow']:
                DOWN = False
                print("down button released")
            if event.button == button_keys['up_arrow']:
                UP = False
                print("up button released")

        #HANDLES ANALOG INPUTS
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            # print(analog_keys)
            # Horizontal Analog
            if abs(analog_keys[0]) > .4:
                if analog_keys[0] < -.7:
                    LEFT = True
                else:
                    LEFT = False
                if analog_keys[0] > .7:
                    RIGHT = True
                else:
                    RIGHT = False
            # Vertical Analog
            if abs(analog_keys[1]) > .4:
                if analog_keys[1] < -.7:
                    UP = True
                else:
                    UP = False
                if analog_keys[1] > .7:
                    DOWN = True
                else:
                    DOWN = False
    
