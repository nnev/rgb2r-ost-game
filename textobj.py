#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

class TextObj:
    def __init__(self, screen, font, text, x, y):
        self.font = font
        self.text = font.render(text, True, (255, 255, 255), (0, 0, 0))
        self.rawtext = text
        self.x = x
        self.y = y
        self.screen = screen
        self.recalc()

    def recalc(self):
        self.rect = self.text.get_rect()
        if self.x == "center":
            self.rect.centerx = self.screen.get_rect().centerx
        else:
            self.rect.left = self.x

        if self.y == "center":
            self.rect.centery = self.screen.get_rect().centery
        else:
            self.rect.top = self.y

        #print "self.rect = (%d, %d, %d, %d)" % (self.rect.left, self.rect.top, self.rect.width, self.rect.height)

    def get_text(self):
        return self.rawtext

    def set_text(self, text):
        self.text = self.font.render(text, True, (255, 255, 255), (0, 0, 0))
        self.rawtext = text
        self.recalc()

    def render(self):
        self.screen.blit(self.text, self.rect)
