import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

ledPin = 12
buttonPin = 16

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/lamp_and_audio_pi/Mirror_audio_HOME.mp3")
counter = 0

while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState == False:
        GPIO.output(ledPin, GPIO.HIGH)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(0.0)
        while pygame.mixer.music.get_busy() == True:
            buttonState = GPIO.input(buttonPin)
            counter = counter+1
#             print(counter)
            if counter > 20000:
                pygame.mixer.music.set_volume(0.8)
            if buttonState == True:
                pygame.mixer.music.set_volume(0.0)
                pygame.mixer.music.stop()        
                counter = 0
                break
            else:
                continue
    else:
        pygame.mixer.music.set_volume(0.0)
        counter = 0
        GPIO.output(ledPin, GPIO.LOW)
