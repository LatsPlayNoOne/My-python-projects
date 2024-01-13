from pygame import mixer 
from time import sleep

mixer.init() # Initialization
mixer.music.load("SONGNAME") # Load song
mixer.music.play() # Play song
while mixer.music.get_busy(): # Waiting for end
    sleep(1)