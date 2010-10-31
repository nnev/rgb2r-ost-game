#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim:ts=4:sw=4:expandtab

from question import *

class questions:
    q = []
    cur = -1

    @classmethod
    def init(cls):

        q = Question(
            "Pokemon",
            "/home/michael/rgb2r/soundtracks/pokemon_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/pokemon_GB/101_-_opening.mp3",
            0.0,
            "Opening",
            None,
            "leicht")
        questions.q.append(q)

        q = Question(
            "Sonic",
            "/home/michael/rgb2r/soundtracks/sonic/cover.jpg",
            "/home/michael/rgb2r/soundtracks/sonic/02_emerald_hill_zone.mp3.mp3",
            0.0,
            "Emerald Hill Zone",
            None,
            "leicht")

        questions.q.append(q)

        q = Question(
            "F-Zero X",
            "/home/michael/rgb2r/soundtracks/f_zero_x_N64/cover.jpg",
            "/home/michael/rgb2r/soundtracks/f_zero_x_N64/01_endless_challenge.mp3",
            0.0,
            "Endless Challenge",
            None,
            "leicht")
        questions.q.append(q)

        q = Question(
            "Earthworm Jim",
            "/home/michael/rgb2r/soundtracks/earthworm_jim_SNES/cover.jpg",
            "/home/michael/rgb2r/soundtracks/earthworm_jim_SNES/mike_miller_-_earthworm_jim_(snes)_-_01_-_new_junk_city.mp3",
            0.0,
            "New Junk City",
            None,
            "mittel")
        questions.q.append(q)

        q = Question(
            "Super Mario Land 2",
            "/home/michael/rgb2r/soundtracks/super_mario_land_2_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/super_mario_land_2_GB/tokata.mp3",
            0.0,
            "Tokata's Song",
            None,
            "schwer")
        questions.q.append(q)

        q = Question(
            "Tetris",
            "/home/michael/rgb2r/soundtracks/tetris_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/tetris_GB/tetris-gameboy-04.mp3.mp3",
            0.0,
            "",
            None,
            "leicht")
        questions.q.append(q)

        q = Question(
            "Rayman",
            "/home/michael/rgb2r/soundtracks/rayman_PSX/cover.jpg",
            "/home/michael/rgb2r/soundtracks/rayman_PSX/04_rocketfly.mp3",
            0.0,
            "Rocketfly",
            None,
            "schwer")
        questions.q.append(q)

        q = Question(
            "Crash Bandicoot",
            "/home/michael/rgb2r/soundtracks/crash_bandicoot_PSX/cover.png",
            "/home/michael/rgb2r/soundtracks/crash_bandicoot_PSX/09_-_jungle_rollers,_rolling_stones.mp3",
            0.0,
            "Jungle Rollers, Rolling Stones",
            None,
            "schwer")
        questions.q.append(q)

        q = Question(
            "Jet Force Gemini",
            "/home/michael/rgb2r/soundtracks/jet_force_gemini_N64/cover.jpg",
            "/home/michael/rgb2r/soundtracks/jet_force_gemini_N64/08_ss_anubis.mp3",
            0.0,
            "SS Anubis",
            None,
            "schwer")
        questions.q.append(q)

        q = Question(
            "Zelda: Links awakening",
            "/home/michael/rgb2r/soundtracks/zelda_links_awakening_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/zelda_links_awakening_GB/01_-_title_theme.mp3",
            0.0,
            "Title theme",
            None,
            "leicht")
        questions.q.append(q)


        q = Question(
            "Megaman",
            "/home/michael/rgb2r/soundtracks/mega_man_1_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/mega_man_1_GB/02_-_guts_man.mp3",
            0.0,
            "Guts Man",
            None,
            "mittel")
        questions.q.append(q)

        q = Question(
            "Mortal Kombat",
            "/home/michael/rgb2r/soundtracks/mortal_kombat/cover.jpg",
            "/home/michael/rgb2r/soundtracks/mortal_kombat/01.mp3",
            0.0,
            "",
            None,
            "schwer")
        questions.q.append(q)

        q = Question(
            "Kirby's Dreamland",
            "/home/michael/rgb2r/soundtracks/kirbys_dreamland_GB/cover.jpg",
            "/home/michael/rgb2r/soundtracks/kirbys_dreamland_GB/01-bubbley_clouds.mp3",
            0.0,
            "Bubbley Clouds",
            None,
            "mittel")
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
