import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
from zombie_game.menu import MenuMob
import pygame as pg
# from zombie_game.bullet import Bullet
from zombie_game.settings import *
# from zombie_game.player import *
# from zombie_game.item import *
# from zombie_game.menu import *
import zombie_game.functions
from os import path

class Event:
    def __init__(self, type, key, unicode):
        self.type = type
        self.key = key
        self.unicode = unicode

class TestMenuMob(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.menumob = MenuMob(self.game, self.game.menu.pos_x, self.game.menu.pos_y, 50, 50)
        pass

    def test0_animate(self):
        print("Test for MenuMob class:")
        self.menumob.animate((0, 0), (0, 0, self.game.menu.pos_x, self.game.menu.pos_y))
        print("\ttest animate : OK")
        pass

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        # self.game.menu.game_intro()
        pass

    def fake_set_mob_limit(self, i_value, top, bottom, pos, draw, previous, size=50):
        self.game.menu.i = self.possible_i()
        self.game.menu.set_position(OPTIONS_SPRITE_POS_X)

        return False

    def fake_game_choose_character(self):
        return "game_choose_character"

    def fake_game_options(self):
        return "game_options"

    def fake_quit_game(self):
        return "quit_game"

    def test1_game_intro(self):
        print("Test for Menu class:")
        self.possible_i = Mock()
        self.possible_i.side_effect = [0.56, 0.66, 0.76, 0.86]

        with patch("zombie_game.menu.Menu.set_mob_limit", new_callable=Mock) as mock_set_mob_limit:
            mock_set_mob_limit.side_effect = self.fake_set_mob_limit
            with patch("zombie_game.menu.Menu.game_choose_character", new_callable=Mock) as mock_game_choose_character:
                mock_game_choose_character.side_effect = self.fake_game_choose_character
                with patch("zombie_game.menu.Menu.game_options", new_callable=Mock) as mock_game_options:
                    mock_game_options.side_effect = self.fake_game_options
                    with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
                        mock_quit_game.side_effect = self.fake_quit_game
                        zombie_game.functions.quit_game = Mock()
                        zombie_game.functions.quit_game.side_effect = self.fake_quit_game

                        self.entry_name_list = Mock()
                        self.entry_name_list.side_effect = ["game_choose_character", "game_options", "game_options", "quit_game"]

                        for i in range(4):
                            self.assertEqual(self.game.menu.game_intro(), self.entry_name_list())
        print("\ttest game_intro : OK")

    def fake_game_intro(self):
        return "game_intro"

    def test2_game_options(self):
        self.possible_i = Mock()
        self.possible_i.side_effect = [0.31, 0.46, 0.61]

        with patch("zombie_game.menu.Menu.set_mob_limit", new_callable=Mock) as mock_set_mob_limit:
            mock_set_mob_limit.side_effect = self.fake_set_mob_limit
            with patch("zombie_game.menu.Menu.game_intro", new_callable=Mock) as mock_game_intro:
                mock_game_intro.side_effect = self.fake_game_intro
                with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
                    mock_quit_game.side_effect = self.fake_quit_game
                    zombie_game.functions.quit_game = Mock()
                    zombie_game.functions.quit_game.side_effect = self.fake_quit_game

                    self.entry_name_list = Mock()
                    self.entry_name_list.side_effect = ["", "", "game_intro"]

                    for i in range(3):
                        self.assertEqual(self.game.menu.game_options(), self.entry_name_list())
        print("\ttest game_options : OK")

    def fake_game_choosing_difficulty(self):
        pass

    def test3_game_choose_character(self):
        self.possible_i = Mock()
        self.possible_i.side_effect = [0.45, 0.6, 0.75]

        with patch("zombie_game.menu.Menu.set_mob_limit", new_callable=Mock) as mock_set_mob_limit:
            mock_set_mob_limit.side_effect = self.fake_set_mob_limit
            with patch("zombie_game.menu.Menu.game_choosing_difficulty", new_callable=Mock) as mock_game_choosing_difficulty:
                mock_game_choosing_difficulty.side_effect = self.fake_game_choosing_difficulty
                with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
                    mock_quit_game.side_effect = self.fake_quit_game
                    zombie_game.functions.quit_game = Mock()
                    zombie_game.functions.quit_game.side_effect = self.fake_quit_game

                    self.entry_name_list = Mock()
                    self.entry_name_list.side_effect = ["hitman1_", "womanGreen_", "soldier1_"]

                    for i in range(3):
                        self.assertEqual(self.game.menu.game_choose_character(), self.entry_name_list())
        print("\ttest game_choose_character : OK")

    def fake_game_input(self, difficult):
        return difficult

    def test4_game_choosing_difficulty(self):
        self.possible_i = Mock()
        self.possible_i.side_effect = [0.16, 0.36, 0.56, 0.76]

        with patch("zombie_game.menu.Menu.set_mob_limit", new_callable=Mock) as mock_set_mob_limit:
            mock_set_mob_limit.side_effect = self.fake_set_mob_limit
            with patch("zombie_game.menu.Menu.game_input", new_callable=Mock) as mock_game_input:
                mock_game_input.side_effect = self.fake_game_input
                with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
                    mock_quit_game.side_effect = self.fake_quit_game
                    zombie_game.functions.quit_game = Mock()
                    zombie_game.functions.quit_game.side_effect = self.fake_quit_game

                    self.entry_name_list = Mock()
                    self.entry_name_list.side_effect = ["easy", "normal", "hard", "hell"]

                    for i in range(3):
                        self.assertEqual(self.game.menu.game_choosing_difficulty(), self.entry_name_list())
        print("\ttest game_choosing_difficulty : OK")

    def fake_pg_display_flip(self):
        if self.counter == len(self.all_test):
            raise InterruptedError

    def fake_pg_event_get(self):
        return self.all_test

    def fake_game_choosing_difficulty2(self):
        self.tmp.append("game_choosing_difficulty")
        pass

    def fake_run(self):
        self.tmp.append("run")
        pass

    def fake_draw_input(self, word, b, c):
        self.counter += 1
        self.tmp.append(word)
        pass

    def fake_quit_game2(self):
        self.tmp.append("quit_game")
        pass

    def fake_isalpha(self, c):
        if self.assertIn(c, self.alpha):
            return True
        return False

    def test5_game_input(self):

        with patch("pygame.display.flip", new_callable=Mock) as mock_pg_display_flip: #for break infinite_while_loop
            mock_pg_display_flip.side_effect = self.fake_pg_display_flip

            with patch("pygame.event.get", new_callable=Mock) as mock_pg_event_get:
                mock_pg_event_get.side_effect = self.fake_pg_event_get

                with patch("zombie_game.menu.Menu.game_choosing_difficulty", new_callable=Mock) as mock_game_choosing_difficulty:
                    mock_game_choosing_difficulty.side_effect = self.fake_game_choosing_difficulty2

                    with patch("main.Game.run", new_callable=Mock) as mock_run:
                        mock_run.side_effect = self.fake_run
                        with patch("zombie_game.board.Board.draw_input", new_callable=Mock) as mock_draw_input:
                            mock_draw_input.side_effect = self.fake_draw_input
                            with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
                                mock_quit_game.side_effect = self.fake_quit_game2
                                zombie_game.functions.quit_game = Mock()
                                zombie_game.functions.quit_game.side_effect = self.fake_quit_game

                                self.alpha = []
                                for i in range(26):
                                    c = chr(ord('a') + i)
                                    self.alpha.append(c)
                                for i in range(26):
                                    c = chr(ord('A') + i)
                                    self.alpha.append(c)
                                    
                                self.counter = 0
                                #generate all events
                                self.tmp = []
                                word = ""

                                self.all_test = [Event(pg.QUIT, None, None)]
                                self.expected = ["quit_game"]
                                self.expected.append(word)

                                self.all_test.append(Event(pg.KEYDOWN, pg.K_BACKSPACE, ""))
                                self.expected.append(word)

                                for i in range(26):
                                    c = chr(ord('a') + i)
                                    self.all_test.append(Event(pg.KEYDOWN, None, c))
                                    word += c
                                    self.expected.append(word)

                                self.all_test.append(Event(pg.KEYDOWN, pg.K_BACKSPACE, ""))
                                word = word[:-1]
                                self.expected.append(word)

                                for i in range(26):
                                    c = chr(ord('A') + i)
                                    self.all_test.append(Event(pg.KEYDOWN, None, c))
                                    word += c
                                    self.expected.append(word)

                                self.all_test.append(Event(pg.KEYDOWN, pg.K_ESCAPE, ""))
                                self.expected.append("game_choosing_difficulty")
                                self.expected.append(word)

                                self.game.menu.game_input("dont care")
                                self.assertEqual(self.tmp, self.expected)

        print("\ttest game_input : OK")

    def fake_pg_event_get2(self):
        self.counter = len(self.all_test)
        return self.all_test

    def fake_draw_game_over(self, scoreboard, message):
        return self.fake_pg_display_flip()

    def fake_game_intro2(self):
        self.tmp.append("game_intro")
        pass

    def test6_game_over(self):
        with patch("zombie_game.board.Board.draw_game_over", new_callable=Mock) as mock_draw_game_over: #for break infinite_while_loop
            mock_draw_game_over.side_effect = self.fake_draw_game_over

            with patch("pygame.event.get", new_callable=Mock) as mock_pg_event_get:
                mock_pg_event_get.side_effect = self.fake_pg_event_get2

                with patch("zombie_game.menu.Menu.game_intro", new_callable=Mock) as mock_game_intro:
                    mock_game_intro.side_effect = self.fake_game_intro2

                    with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
                        mock_quit_game.side_effect = self.fake_quit_game2
                        zombie_game.functions.quit_game = Mock()
                        zombie_game.functions.quit_game.side_effect = self.fake_quit_game

                        self.counter = 0
                        #generate all events
                        self.tmp = []
                        word = ""

                        self.all_test = [Event(pg.QUIT, "", "")]
                        self.expected = ["quit_game"]

                        self.all_test.append(Event(pg.KEYDOWN, pg.K_BACKSPACE, ""))

                        self.all_test.append(Event(pg.KEYDOWN, pg.K_SPACE, ""))
                        self.expected.append("game_intro")

                        self.all_test.append(Event(pg.KEYDOWN, pg.K_RETURN, ""))
                        self.expected.append("game_intro")

                        self.all_test.append(Event(pg.KEYDOWN, pg.K_ESCAPE, ""))

                        self.game.menu.game_over("dont care", "dont care")
                        self.assertEqual(self.tmp, self.expected)

        print("\ttest game_over : OK")

    def fake_set_the_mob(self, size):
        pass

    def fake_draw(self, a):
        pass

    def fake_previous(self):
        self.tmp.append("previous")
        pass

    def test7_set_mob_limit(self):
        with patch('zombie_game.menu.Menu.set_the_mob', new_callable=Mock) as mock_set_the_mob:
            mock_set_the_mob.side_effect = self.fake_set_the_mob

            with patch("pygame.event.get", new_callable=Mock) as mock_pg_event_get:
                mock_pg_event_get.side_effect = self.fake_pg_event_get2

                with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
                    mock_quit_game.side_effect = self.fake_quit_game2
                    zombie_game.functions.quit_game = Mock()
                    zombie_game.functions.quit_game.side_effect = self.fake_quit_game
                    self.counter = 0
                    #generate all events except event.key == pg.K_DOWN or event.key == pg.K_s AND event.key = pg.K_RETURN
                    self.tmp = []
                    self.game.menu.i = 0.6
                    self.all_test = [Event(pg.QUIT, "", "")]
                    self.expected = ["quit_game"]

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_ESCAPE, ""))
                    self.expected.append("quit_game")
                    self.expected.append("previous")

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_BACKSPACE, ""))
                    self.expected.append("previous")

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_UP, ""))

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_SPACE, ""))

                    
                    self.game.menu.set_mob_limit(0.3, 300, 500, OPTIONS_SPRITE_POS_X, self.fake_draw, self.fake_previous, "dont care")
                    self.assertEqual(self.tmp, self.expected)
                    self.assertTrue(abs(self.game.menu.i - 0.3) < 0.0001)
                    #
                    self.counter = 0

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_w, ""))

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_RETURN, ""))
                    self.game.menu.set_mob_limit(0.3, 300, 500, OPTIONS_SPRITE_POS_X, self.fake_draw, self.fake_previous, "dont care")
                    self.assertTrue(abs(self.game.menu.i - 0.3) < 0.0001)

                    #otherwise
                    self.counter = 0
                    self.game.menu.i = 0.6
                    self.all_test = [Event(pg.KEYDOWN, pg.K_DOWN, "")]

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_SPACE, ""))

                    self.game.menu.set_mob_limit(0.3, 300, 500, OPTIONS_SPRITE_POS_X, self.fake_draw, self.fake_previous, "dont care")
                    self.assertTrue(abs(self.game.menu.i - 0.9) < 0.0001)

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_s, ""))

                    self.all_test.append(Event(pg.KEYDOWN, pg.K_RETURN, ""))

                    self.assertTrue(abs(self.game.menu.i - 0.9) < 0.0001)

        print("\ttest set_mob_limit : OK")

    def test8_set_position(self):
        param_list = [(4, 2, 2, 3, (8, 6)),
                      (3, 1, 3, 3, (9, 3)),
                      (100, 5, 20, 2, (2000, 10)),
                      (17, 2, 8.5, 2.4, (17 * 8.5, 2 * 2.4)),
                      (6, 5, 1.2, 7, (6 * 1.2, 5 * 7)),
                      (1, 6, 2, [], AssertionError)]
        for height, width, i, x, expected in param_list:
            with self.subTest():
                self.game.height = height
                self.game.width = width
                self.game.menu.i = i
                if expected == AssertionError:
                    self.assertRaises(expected, self.assertEqual, self.game.menu.set_position(x), expected)
                else:
                    self.assertEqual(self.game.menu.set_position(x), expected)

        print("\ttest set_position : OK")

    def test9_set_the_mob(self):
        self.game.menu.set_the_mob()
        print("\ttest set_the_mob")

if __name__ == '__main__':
    unittest.main()