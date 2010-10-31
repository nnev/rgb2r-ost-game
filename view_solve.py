#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
from timer import *
from textobj import *
from players import *
from questions import *
import view_question
import view_solved
from pygame.locals import *

class ViewSolve:
	def __init__(self, screen, player, question, original_view):
        print "initiating view"
        self.ov = original_view
        self.question = question
        self.player = player
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.sfont = pygame.font.Font(None, 48)
        self.timer = Timer(30000, True, self.get_timeout())
        self.res = None
        self.correct_game = False
        self.correct_console = False
        self.correct_scene = False
        self.correct_bonus = False
        self.points = 0

    def get_timeout(self):
        def timeout():
            print "Timeout! moep"
            print "done, adding points to " + self.player + " and going to the next question"
            players.score(self.player, self.points)
            self.res = self.ov
        return timeout

    def handle_key(self, key):
        pass

    def handle_key_u(self, key):
        print "handling unicode key"
        if key == 'g':
            print "game is correct"
            self.points += 10
            self.correct_game = True
        elif key == 'c':
            self.points += 1
            print "Console is correct"
            self.correct_console = True
        elif key == 's':
            print "scene is correct"
            self.points += 5
            self.correct_scene = True
        elif key == 'b':
            print "bonus points"
            self.points += 5
            self.correct_bonus = True
        elif key == 'q':
            print "quit, user wont solve"
            self.res = self.ov
        elif key == ' ':
            print "done, adding points to " + self.player + " and going to the next question"
            players.score(self.player, self.points)
            self.res = view_solved.ViewSolved(self.screen, self.question)

    def handle_wiimote(self, wiimote, key):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        TextObj(screen, self.font, self.player + u" möchte lösen!", "center", 100).render()
        TextObj(screen, self.font, "noch " + str(self.timer.remaining()) + " Sekunden!", "center", 500).render()
        if self.correct_game:
            TextObj(screen, self.sfont, u"Spiel richtig", "center", 200).render()
        if self.correct_console:
            TextObj(screen, self.sfont, u"Konsole richtig", "center", 250).render()
        if self.correct_scene:
            TextObj(screen, self.sfont, u"Szene richtig", "center", 300).render()
        if self.correct_bonus:
            TextObj(screen, self.sfont, u"Bonus!", "center", 350).render()
        
        TextObj(screen, self.sfont, u"+" + str(self.points), "center", 400).render()

        return self.res

