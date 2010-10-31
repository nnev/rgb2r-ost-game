#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

class Question:
    # startpos ist ein float
    def __init__(self, gametitle, gamecover, sound, startpos, description, scenepic, difficulty):
        print "init question"
        self.gametitle = gametitle
        self.gamecover = gamecover
        self.sound = sound
        self.startpos = startpos
        self.description = description
        self.scenepic = scenepic
        self.difficulty = difficulty
        self.tries = []

    def add_try(self, bdaddr):
        self.tries.append(bdaddr)

    def already_tried(self, bdaddr):
        return bdaddr in self.tries
