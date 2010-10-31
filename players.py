#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

class player:
    def __init__(self, name):
        print "init player with name %s and wiimote " % (name)
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

class players:
    players = []

    @classmethod
    def get_player_by_name(cls, name):
        for p in players.players:
            if p.name == name:
                return p
        return None

    @classmethod
    def dump(cls):
        print "-- DUMP --"
        for p in players.players:
            print "player %s with %d points" % (p.name, p.score)
        print "-- END OF DUMP --"

    @classmethod
    def add_player(cls, name):
        p = player(name)
        players.players.append(p)
        return p

    @classmethod
    def score(cls, name, points):
        p = players.get_player_by_name(name)
        p.add_score(points)
        players.dump()

    @classmethod
    def scores(cls):
        return map(lambda x: {'name': x.name, 'score': x.score}, players.players)
