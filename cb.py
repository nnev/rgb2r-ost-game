#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

class CB:
    @classmethod
    def set_cb(cls, cb):
        CB.cb = cb

    @classmethod
    def get_cb(cls):
        return CB.cb
