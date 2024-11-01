#Adding Sound Effects
#Download a sound file and name the sound file roll_sound.wav


import pygame


pygame.mixer.init()
roll_sound = pygame.mixer.Sound('roll_sound.wav')  # Ensure the sound file is in the same folder
