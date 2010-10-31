#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
import pprint
from cb import *
from timer import *
from textobj import *
from wiimote import *
from questions import *
from view_question import *
from pygame.locals import *

STATE_IDLE = 0
STATE_PLAYER1 = 1
STATE_PLAYER2 = 2
STATE_PLAYER3 = 3
STATE_PLAYER4 = 4
STATE_DONE = 5

class ViewPlayers:
    def __init__(self, screen):
        print "initiating view"
        font = pygame.font.Font(None, 72)
        self.font = font
        self.res = None
        self.headline = TextObj(screen, font, "Spieler einstellen", "center", 50)
        font = pygame.font.Font(None, 36)
        self.sfont = font
        self.state = STATE_IDLE
        self.player_desc = [
            TextObj(screen, font, "Spieler 1:", 100, 200),
            TextObj(screen, font, "Spieler 2:", 100, 300),
            TextObj(screen, font, "Spieler 3:", 100, 400),
            TextObj(screen, font, "Spieler 4:", 100, 500)
        ]
        self.player_names = [
            TextObj(screen, font, "", 250, 200),
            TextObj(screen, font, "", 250, 300),
            TextObj(screen, font, "", 250, 400),
            TextObj(screen, font, "", 250, 500)
        ]
        self.screen = screen

    def handle_key(self, key):
        print "handling key"
        if key == K_DOWN:
            print "user pressed down"

    def handle_key_u(self, key):
        if key == u'1':
            self.state = STATE_PLAYER1
        elif key == u'2':
            self.state = STATE_PLAYER2
        elif key == u'3':
            self.state = STATE_PLAYER3
        elif key == u'4':
            self.state = STATE_PLAYER4
        elif key == u'0':
            self.state = STATE_IDLE
        else:
            n = self.player_names[self.state - 1]
            if self.state < STATE_PLAYER1 or self.state > STATE_PLAYER4:
                if key == u'\r':
                    print "done with player setup"
                    q = questions.next_question(self.screen)
                    self.res = ViewQuestion(self.screen, q, 1)
                    for c in range(0, 4):
                        if len(self.player_names[c].get_text()) > 0:
                            players.add_player(self.player_names[c].get_text())
                    players.dump()
                return
            print "printable char %s entered" % key
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(key)
            # Handle backspace
            if key == u'\x08':
                n.set_text(n.get_text()[0:-1])
            elif key == u'\r':
                w = None
                c = 0
                while w == None:
                    TextObj(self.screen, self.font, u"Jetzt 1+2 drücken! (" + str(c) + ")", "center", "center").render()
                    pygame.display.flip()

                    try:
                        w = Wiimote(n.get_text(), None)
                        w.set_cb(CB.get_cb())
                    except:
                        w = None
                        c += 1
                self.state = STATE_IDLE
                print "done"
            else:
                n.set_text(n.get_text() + key)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.headline.render()
        for t in self.player_desc + self.player_names:
            t.render()
        if self.state >= STATE_PLAYER1 and self.state <= STATE_PLAYER4:
            TextObj(self.screen, self.sfont, ">", 50, 200 + ((self.state - 1) * 100)).render()
        return self.res
