#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
from timer import *
from questions import *
import view_question
import view_end
from pygame.locals import *

# Übersicht: Lösung des Rätsels (Spiel-Cover und -Name in groß)
STATE_SOLVED = 0
# Cover wird klein und bewegt sich nach oben links
STATE_MOVING = 1
# Szenen-Screenshot mit kurzem Text wird angezeigt
STATE_SCENE = 2

class ViewSolved:
	def __init__(self, screen, question):
        print "initiating view"
        self.res = None
        self.screen = screen
        self.question = question
        self.font = pygame.font.Font(None, 32)
        self.game_logo = pygame.image.load(question.gamecover)
        self.logorect = self.game_logo.get_rect()
        self.logorect.centerx = screen.get_rect().centerx
        self.logorect.centery = screen.get_rect().centery

        self.text = self.font.render("Das war aus: " + question.gametitle, True, (255, 255, 255), (0, 0, 0))
        self.textrect = self.text.get_rect()
        self.textrect.centerx = screen.get_rect().centerx
        self.textrect.top = self.logorect.bottom + 25

        self.state = STATE_SOLVED

        t = Timer(1000, True, self.get_start_animation())

    def get_start_animation(self):
        def start_animation():
            if self.question.scenepic != None:
                self.state = STATE_MOVING
                print "Starting animation (1s has passed)"
        return start_animation

    def handle_key(self, key):
        print "handling key"
        if key == K_DOWN:
            print "user pressed down"

    def handle_key_u(self, key):
        if key == ' ':
            q = questions.next_question(self.screen)
            if q == None:
                self.res = view_end.ViewEnd(self.screen)
            else:
                self.res = view_question.ViewQuestion(self.screen, q, questions.cur + 1)

    def handle_wiimote(self, wiimote, button):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.game_logo, self.logorect)
        if self.state == STATE_SOLVED:
            screen.blit(self.text, self.textrect)
        elif self.state == STATE_MOVING:
            if self.logorect.top > 50:
                self.logorect = self.logorect.move([-25, -25])
            else:
                self.game_logo = pygame.transform.scale(self.game_logo, (self.logorect.width / 2, self.logorect.height / 2))
                self.logorect = self.game_logo.get_rect()
                self.logorect.top = 25
                self.logorect.left = 25
                self.state = STATE_SCENE
                self.text = self.font.render(self.question.gametitle, True, (255, 255, 255), (0, 0, 0))
                self.textrect = self.text.get_rect()
                self.textrect.centerx = self.logorect.centerx
                self.textrect.top = self.logorect.bottom

                if self.question.scenepic != None:
                    self.scene_logo = pygame.image.load(self.question.scenepic)
                    r = self.scene_logo.get_rect()
                    h = int(500 * (float(r.height) / r.width))
                    self.scene_logo = pygame.transform.scale(self.scene_logo, (500, h))
                    self.scene_logo_rect = self.scene_logo.get_rect()
                    self.scene_logo_rect.centerx = screen.get_rect().centerx
                    self.scene_logo_rect.centery = screen.get_rect().centery

                self.scene_desc = self.font.render(self.question.description, True, (255, 255, 255), (0, 0, 0))
                r = self.scene_desc.get_rect()
                r.centerx = screen.get_rect().centerx
                if self.question.scenepic != None:
                    r.top = self.scene_logo_rect.bottom + 10
                else:
                    r.top = screen.get_rect().centery + 10
                self.scene_desc_rect = r

        elif self.state == STATE_SCENE:
            screen.blit(self.text, self.textrect)
            if self.question.scenepic != None:
                screen.blit(self.scene_logo, self.scene_logo_rect)
            screen.blit(self.scene_desc, self.scene_desc_rect)
        #screen.blit(self.rgb2r_logo, (800 / 2 - (300 / 2), 10))
        return self.res
