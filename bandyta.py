from random import random
from math import pi, exp, sqrt

def sqr(value):
    return value * value

class Bandyta:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def distribution(self, x):
        return exp(sqr((x - self.mean)/self.std)/(-2))/(self.std * sqrt(2*pi))

    def pull(self, precision = 0.1):
        value = 0
        target_percent = random()
        n = 0
        while (value < target_percent):
            value += (self.distribution(n*precision) + self.distribution((n+1)*precision))*precision/2
            n += 1
        return n * precision