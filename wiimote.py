#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

import cwiid
import random

class Wiimote:
    def __init__(self, player, bdaddr):
        if bdaddr != None:
            wm = cwiid.Wiimote(bdaddr)
        else:
            wm = cwiid.Wiimote()
        wm.rpt_mode = cwiid.RPT_BTN
        wm.led = cwiid.LED2_ON
        wm.enable(cwiid.FLAG_MESG_IFC | cwiid.FLAG_REPEAT_BTN)
        wm.mesg_callback = self.get_msg()
        self.wm = wm
        self.player = player
        self.bdaddr = random.randrange(0, 500000)

    def get_msg(self):
        def msg(messages, button=[0]):
            for msg in messages:
                if msg[0] == cwiid.MESG_BTN and self.wm.state['buttons'] & cwiid.BTN_A:
                    self.cb(self)
        return msg
    
    def set_cb(self, cb):
        self.cb = cb
