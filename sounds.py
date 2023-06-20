import pygame
from pygame import mixer
import random


mixer.init()
path = "soundeffects/"


def come_here():
    sound1 = path+"ch.mp3"
    sound2 = path+"goh.mp3"
    sound = [sound1,sound2]
    choice = random.choice(sound)
    mixer.music.load(choice)
    mixer.music.play()

def unwisely():
    choice = path+"unwisely.mp3"
    mixer.music.load(choice)
    mixer.music.play()


def punch_sound():
    pass
