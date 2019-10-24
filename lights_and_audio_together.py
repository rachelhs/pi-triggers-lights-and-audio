import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

ledPin = 12
buttonPin = 16

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init()
pygame.mixer.music.load("guitar.wav")

while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState == False:
        pygame.mixer.music.play()
        GPIO.output(ledPin, GPIO.HIGH)
        while pygame.mixer.music.get_busy() == True:
            buttonState = GPIO.input(buttonPin)
            if buttonState == True:                
                break
            else:
                continue
    else:
        pygame.mixer.music.stop()
        GPIO.output(ledPin, GPIO.LOW)