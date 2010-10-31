#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
import pprint
from cb import *
from timer import *
from textobj import *
from players import *
from wiimote import *
from questions import *
from view_question import *
from pygame.locals import *


class ViewEnd:
    def __init__(self, screen):
        print "initiating view"
        font = pygame.font.Font(None, 72)
        self.font = font
        self.res = None
        self.headline = TextObj(screen, font, "Highscores", "center", 50)
        font = pygame.font.Font(None, 36)
        self.sfont = font
        s = players.scores()
        s = sorted(s, key=lambda f: f['score'], reverse=True)
        self.player_names = []
        for c in range(0, len(s)):
            self.player_names.append(TextObj(screen, font, s[c]['name'] + ': ' + str(s[c]['score']), "center", 200 + (c * 100)))
        self.screen = screen

    def handle_key(self, key):
        print "handling key"
        if key == K_DOWN:
            print "user pressed down"

    def handle_key_u(self, key):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.headline.render()
        for t in self.player_names:
            t.render()
        return self.res
