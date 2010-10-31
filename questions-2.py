#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

from question import *

class questions:
    q = []
    cur = -1

    @classmethod
    def init(cls):
# nummer 1:
        q = Question(
            "Super Mario 64",
            "/home/michael/rgb2r/soundtracks/super_mario_64_N64/cover.jpg",
            "/home/michael/rgb2r/soundtracks/super_mario_64_N64/05 Super Mario 64 Main Theme.mp3",
            0.0,
            "Main theme",
            "/home/michael/rgb2r/soundtracks/super_mario_64_N64/maintheme.jpg",
            "leicht")
        questions.q.append(q)

        q = Question(
            "Tony Hawk's Pro Skater 2",
            "/home/michael/rgb2r/soundtracks/thps2_PSX/cover.jpg",
            "/home/michael/rgb2r/soundtracks/thps2_PSX/12_-_consumed-heavy_metal_winners.mp3",
            0.0,
            "",
            "/home/michael/rgb2r/soundtracks/thps2_PSX/scene.jpg",
            "mittel")

        questions.q.append(q)

        q = Question(
            "Mario Kart 64",
            "/home/michael/rgb2r/soundtracks/mario_kart_64_N64/cover.png",
            "/home/michael/rgb2r/soundtracks/mario_kart_64_N64/Moo Moo Farm.mp3",
            0.0,
            "Moo Moo Farm",
            "/home/michael/rgb2r/soundtracks/mario_kart_64_N64/moomoo.jpg",
            "mittel")

        questions.q.append(q)

        q = Question(
            "Perfect Dark",
            "/home/michael/rgb2r/soundtracks/perfect_dark_N64/cover.jpg",
            "/home/michael/rgb2r/soundtracks/perfect_dark_N64/1-10_-_area_51-infiltration.mp3",
            4.0,
            "Area 51",
            "/home/michael/rgb2r/soundtracks/perfect_dark_N64/area51.jpg",
            "schwer")

        questions.q.append(q)

        q = Question(
            "Prince of Persia",
            "/home/michael/rgb2r/soundtracks/Prince_of_Persia_DOS/prince.png",
            "/home/michael/rgb2r/soundtracks/Prince_of_Persia_DOS/prince.ogg",
            0.0,
            "",
            None,
            "leicht")

        questions.q.append(q)

        q = Question(
            "Zelda: Ocarina of Time",
            "/home/michael/rgb2r/soundtracks/zelda_ocarina_of_time_N64/cover.png",
            "/home/michael/rgb2r/soundtracks/zelda_ocarina_of_time_N64/81 - Ocarina of Time.mp3",
            0.0,
            "Ocarina of Time",
            "/home/michael/rgb2r/soundtracks/zelda_ocarina_of_time_N64/ocarinascene.jpg",
            "mittel")

        questions.q.append(q)

        q = Question(
            "Tekken",
            "/home/michael/rgb2r/soundtracks/tekken_PSX/cover.png",
            "/home/michael/rgb2r/soundtracks/tekken_PSX/05_character_select_bgm.mp3",
            0.0,
            "Character select",
            None,
            "schwer")
        questions.q.append(q)
        q = Question(
            "Zelda: Ocarina of Time",
            "/home/michael/rgb2r/soundtracks/zelda_ocarina_of_time_N64/cover.png",
            "/home/michael/rgb2r/soundtracks/zelda_ocarina_of_time_N64/23 - Hyrule Castle Courtyard.mp3",
            0.0,
            "Schlossgarten",
            "/home/michael/rgb2r/soundtracks/zelda_ocarina_of_time_N64/courtyard.jpg",
            "schwer")

        questions.q.append(q)

        q = Question(
            "Tetris",
            "/home/michael/rgb2r/soundtracks/tetris_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/tetris_GB/tetris-gameboy-03.mp3.mp3",
            0.0,
            "",
            None,
            "leicht")

        questions.q.append(q)

        q = Question(
            "Day of the Tentacle",
            "/home/michael/rgb2r/soundtracks/day_of_the_tentacle_PC/cover.jpg",
            "/home/michael/rgb2r/soundtracks/day_of_the_tentacle_PC/01-intro.mp3.mp3",
            0.0,
            "Einleitung",
            None,
            "leicht")

        questions.q.append(q)

        q = Question(
            "Super Mario Land 2",
            "/home/michael/rgb2r/soundtracks/super_mario_land_2_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/super_mario_land_2_GB/01_-_choose_your_pipe.mp3",
            0.0,
            "Choose your pipe",
            "/home/michael/rgb2r/soundtracks/super_mario_land_2_GB/choosepipe.png",
            "leicht")

        questions.q.append(q)

        q = Question(
            "Yoshi's Story",
            "/home/michael/rgb2r/soundtracks/yoshis_story_N64/cover.jpg",
            "/home/michael/rgb2r/soundtracks/yoshis_story_N64/27_happy_together.mp3.mp3",
            0.0,
            "Happy together",
            "/home/michael/rgb2r/soundtracks/yoshis_story_N64/happy.jpg",
            "schwer")

        questions.q.append(q)



        q = Question(
            "Sonic",
            "/home/michael/rgb2r/soundtracks/sonic/cover.jpg",
            "/home/michael/rgb2r/soundtracks/sonic/15_ending_1.mp3.mp3",
            0.0,
            "Spielende",
            None,
            "schwer")

        questions.q.append(q)

    @classmethod
    def next_question(cls, screen):
        questions.cur += 1
        if questions.cur >= len(questions.q):
            # We are done. Return the final points view
            return None
        return questions.q[questions.cur]
