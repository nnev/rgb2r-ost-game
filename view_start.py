#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
from pygame.locals import *

class ViewStart:
	def __init__(self, screen):
        print "initiating view"
        self.font = pygame.font.Font(None, 64)

        self.rgb2r_logo = pygame.image.load("rgb2r.jpg")
        r = self.rgb2r_logo.get_rect()
        r.top = 50
        r.centerx = screen.get_rect().centerx
        self.rgb2r_logo_rect = r

        self.title = self.font.render(u"Soundtrack-Rätsel", True, (255, 255, 255), (0, 0, 0))
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = screen.get_rect().centerx
        self.title_rect.centery = screen.get_rect().centery

        self.start = self.font.render("INSERT COIN TO START", True, (255, 255, 255), (0, 0, 0))
        self.start_rect = self.start.get_rect()
        self.start_rect.centerx = screen.get_rect().centerx
        self.start_rect.top = screen.get_rect().bottom - 150

    def handle_key(self, key):
        print "handling key"
        if key == K_DOWN:
            print "user pressed down"

    def handle_wiimote(self, bdaddr, key):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.rgb2r_logo, self.rgb2r_logo_rect)
        screen.blit(self.title, self.title_rect)
        screen.blit(self.start, self.start_rect)
