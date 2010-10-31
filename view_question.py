#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
import datetime
from textobj import *
from timer import *
from pygame.locals import *
from view_solved import *
from view_solve import *
from players import *

class ViewQuestion:
	def __init__(self, screen, question, current_round):
        print "initiating view"
        self.res = None
        self.screen = screen
        self.question = question
        self.font = pygame.font.Font(None, 32)
        self.rgb2r_logo = pygame.image.load("rgb2r.jpg")
        r = self.rgb2r_logo.get_rect()
        self.rgb2r_logo = pygame.transform.scale(self.rgb2r_logo, (r.width / 2, r.height / 2))
        r = self.rgb2r_logo.get_rect()
        r.top = 50
        r.centerx = screen.get_rect().centerx
        self.rgb2r_logo_rect = r
        self.playing = False

        self.round = TextObj(screen, self.font, "Runde " + str(current_round) + "/13", "center", 250)
        self.level = TextObj(screen, self.font, "Stufe: " + self.question.difficulty, "center", 325)
        self.progress = TextObj(screen, self.font, "Position: /", "center", 400)
        self.instruction = TextObj(screen, self.font, u"Drücke A um aufzulösen!", "center", 475)


    def handle_key(self, key):
        pass

    def handle_key_u(self, key):
        if key == ' ':
            print "playing %s" % self.question.sound
            pygame.mixer.music.load(self.question.sound)
            pygame.mixer.music.play()
            self.playing = True
        elif key == 'r':
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
            self.playing = True
        elif key == 's':
            pygame.mixer.music.stop()
            self.playing = False
        elif key == u'\r':
            self.res = view_solved.ViewSolved(self.screen, self.question)

    def handle_wiimote(self, wiimote, button):
        print "handle wiimote from %d" % wiimote.bdaddr
        if self.question.already_tried(wiimote.bdaddr):
            print "nope, this wiimote has already tried"
            return
        self.question.add_try(wiimote.bdaddr)
        pygame.mixer.music.stop()
        self.playing = False
        return ViewSolve(self.screen, wiimote.player, self.question, self)

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.rgb2r_logo, self.rgb2r_logo_rect)
        self.round.render()
        self.level.render()
        if self.playing and pygame.mixer.music.get_pos() > -1:
            self.progress.set_text("Position: " + str(datetime.timedelta(seconds=pygame.mixer.music.get_pos() / 1000)))
        self.progress.render()
        self.instruction.render()
        # Overlay for scores
        pygame.draw.line(screen, (255, 255, 255), (600, 0), (600, 220), 2)
        pygame.draw.line(screen, (255, 255, 255), (600, 220), (800, 220), 2)
        y = 20
        for s in players.scores():
            name = TextObj(screen, self.font, s['name'], 620, y)
            name.render()
            score = TextObj(screen, self.font, str(s['score']), 750, y)
            score.render()
            y += 50
# TODO: länge für die stücke einbauen
        #if pygame.mixer.music.get_pos() / 1000 > 3:
            #return ViewSolved(self.screen, self.question)
        return self.res
