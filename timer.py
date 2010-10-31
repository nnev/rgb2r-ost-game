#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
from pygame.locals import *

def update(time_passed):
    for t in Timer.timers:
        t.update(time_passed)

class Timer:
    timers = []

	def __init__(self, interval, oneshot, cb):
        print "initiating timer"
        self.time = 0
        self.interval = interval
        self.oneshot = oneshot
        self.cb = cb
        Timer.timers.append(self)

    def remaining(self):
        rem = (self.interval - self.time) / 1000
        if rem >= 0:
            return rem
        return 0

    def update(self, time_passed):
        self.time += time_passed
        if self.time > self.interval:
            print "timer should trigger"
            self.cb()
            if self.oneshot:
                Timer.timers.remove(self)
            else:
                self.time = 0
