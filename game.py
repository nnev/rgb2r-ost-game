#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import pygame
import cwiid
import timer
import pprint
import random
from cb import *
from view_start import *
from view_solved import *
from view_players import *
from view_question import *
from view_end import *
from players import *
from question import *
from questions import *
from wiimote import *
from pygame.locals import *

FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

questions.init()

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("rgb2r - soundtrack-rätsel")
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 500)
pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
clock = pygame.time.Clock()

#vs = ViewEnd(screen)
vs = ViewPlayers(screen)
#q = questions.next_question()
#vs = ViewQuestion(screen, q, 1)

def new_view(n):
    global vs
    if n != None:
        vs = n

@staticmethod
def wiimote_cb(wiimote):
    new_view(vs.handle_wiimote(wiimote, 'a'))

CB.set_cb(wiimote_cb)

#w.set_cb(wiimote_cb)

running = 1
while running:
    # Maximal 30 frames pro Sekunde
    time_passed = clock.tick(30)
    # Bildschirm schwarz füllen
    screen.fill((0, 0, 0))
    # Events abarbeiten
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == K_RIGHT:
                current_round += 1
                q = questions[current_round]
                questions.remove(q)
                vs = ViewQuestion(screen, pl, q, current_round)
            else:
                # Alle druckbaren Zeichen werden an handle_key_u übergeben
                if event.unicode != u'':
                    vs.handle_key_u(event.unicode)
                else:
                    # Der Rest an handle_key
                    vs.handle_key(event.key)
    # Timer aktualisieren/triggern
    timer.update(time_passed)
    new_view(vs.render(screen))
    # Bildschirm aktualisieren
    pygame.display.flip()
