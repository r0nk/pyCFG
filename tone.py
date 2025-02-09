from array import array
from time import sleep

import pygame
from pygame.mixer import Sound, get_init, pre_init

class Note(Sound):

    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

def pluck(freq):
    n = Note(freq)
    n.play(-1)
    sleep(0.2)
    n.stop()

if __name__ == "__main__":
    pre_init(44100, -16, 1, 1024)
    pygame.init()
    pluck(440)
    pluck(450)
    pluck(460)
    pluck(470)
    pluck(480)
    pluck(470)
    pluck(450)
    pluck(460)
    pluck(440)
