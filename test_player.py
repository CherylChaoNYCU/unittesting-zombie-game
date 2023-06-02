import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from random import randint, choice, uniform
from main import Game
from zombie_game.bullet import Bullet
from zombie_game.settings import *
from zombie_game.functions import collide_with_object
from zombie_game.smoke import Smoke
import pygame as pg
from os import path

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test0_add_shield(self):
        print("Test for Player class:")
        self.all_test = [] #all player HP: 0 ~ 200 amount
        self.expected = []
        for i in range(PLAYER_SHIELD + 1): 
            self.all_test.append(i)
        for i in self.all_test:
            if i + 60 < PLAYER_SHIELD:
                self.expected.append(i + 60)
            else:
                self.expected.append(PLAYER_SHIELD)
            if i + 100 < PLAYER_SHIELD:
                self.expected.append(i + 100)
            else:
                self.expected.append(PLAYER_SHIELD)
        self.tmp = []
        for i in self.all_test:
            self.game.player.shield = i
            self.game.player.add_shield(60) # MINI_HEALTH_PACK
            self.tmp.append(self.game.player.shield)
            self.game.player.shield = i
            self.game.player.add_shield(100) #BIG_HEALTH_PACK
            self.tmp.append(self.game.player.shield)

        self.assertEqual(self.tmp, self.expected)

        print("\ttest add_shield : OK")

    def fake_get_pressed(self):
        return self.test_keys

    def fake_shoot(self):
        return "shoot"

    def test1_get_keys(self):
        import copy
        self.all_test = []
        self.expected = []
        self.tmp = []

        keys = {pg.K_LEFT:False, pg.K_a:False, pg.K_RIGHT:False, pg.K_d:False, pg.K_UP:False, pg.K_w:False, pg.K_DOWN:False, pg.K_s:False, pg.K_SPACE:False, pg.K_1:False, pg.K_2:False, pg.K_3:False, pg.K_4:False, pg.K_5:False}

        #pg.K_LEFT = True
        keys[pg.K_LEFT] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_LEFT] = False
        self.expected.append(None)

        #pg.K_a = True
        keys[pg.K_a] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_a] = False
        self.expected.append(None)
        
        #pg.K_RIGHT = True
        keys[pg.K_RIGHT] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_RIGHT] = False
        self.expected.append(None)

        #pg.K_d = True
        keys[pg.K_d] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_d] = False
        self.expected.append(None)

        #pg.K_UP = True
        keys[pg.K_UP] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_UP] = False
        self.expected.append(True)

        #pg.K_w = True
        keys[pg.K_w] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_w] = False
        self.expected.append(True)

        #pg.K_DOWN = True
        keys[pg.K_DOWN] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_DOWN] = False
        self.expected.append(False)

        #pg.K_s = True
        keys[pg.K_s] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_s] = False
        self.expected.append(False)

        #1 pg.K_SPACE = True, if self.ammo[self.weapon] > 0:
        self.game.player.weapon = "pistol"
        self.game.player.ammo[self.game.player.weapon] = 1
        keys[pg.K_SPACE] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_SPACE] = False
        self.expected.append("shoot")
        
        #no weapon
        self.game.player.all_weapons = []

        #pg.K_1 = True
        keys[pg.K_1] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_1] = False
        self.expected.append(None)

        #pg.K_2 = True
        keys[pg.K_2] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_2] = False
        self.expected.append(None)

        #pg.K_3 = True
        keys[pg.K_3] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_3] = False
        self.expected.append(None)

        #pg.K_4 = True
        keys[pg.K_4] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_4] = False
        self.expected.append(None)

        #pg.K_5 = True
        keys[pg.K_5] = True
        self.all_test.append(copy.deepcopy(keys))
        keys[pg.K_5] = False
        self.expected.append(None)

        with patch("pygame.key.get_pressed", new_callable=Mock) as mock_get_pressed:
            mock_get_pressed.side_effect = self.fake_get_pressed

            with patch("zombie_game.player.Player.shoot", new_callable=Mock) as mock_shoot:
                mock_shoot.side_effect = self.fake_shoot

                for test in self.all_test:
                    self.test_keys = test
                    self.tmp.append(self.game.player.get_keys())

            #2 pg.K_SPACE = True, otherwise
            self.game.player.weapon = "pistol"
            self.game.player.ammo[self.game.player.weapon] = 0
            keys[pg.K_SPACE] = True
            self.test_keys = copy.deepcopy(keys)
            keys[pg.K_SPACE] = False
            self.expected.append("play")
            self.tmp.append(self.game.player.get_keys())

            #all_weapon 
            weapons = ["pistol", "shotgun", "uzi", "rifle"]
            for weapon in weapons:
                self.game.player.all_weapons.append(weapon)

            #pg.K_1 = True
            keys[pg.K_1] = True
            self.test_keys = copy.deepcopy(keys)
            keys[pg.K_1] = False
            self.expected.append(None)
            self.tmp.append(self.game.player.get_keys())

            #pg.K_2 = True
            keys[pg.K_2] = True
            self.test_keys = copy.deepcopy(keys)
            keys[pg.K_2] = False
            self.expected.append("pistol")
            self.tmp.append(self.game.player.get_keys())

            #pg.K_3 = True
            keys[pg.K_3] = True
            self.test_keys = copy.deepcopy(keys)
            keys[pg.K_3] = False
            self.expected.append("shotgun")
            self.tmp.append(self.game.player.get_keys())

            #pg.K_4 = True
            keys[pg.K_4] = True
            self.test_keys = copy.deepcopy(keys)
            keys[pg.K_4] = False
            self.expected.append("uzi")
            self.tmp.append(self.game.player.get_keys())

            #pg.K_5 = True
            keys[pg.K_5] = True
            self.test_keys = copy.deepcopy(keys)
            keys[pg.K_5] = False
            self.expected.append("rifle")
            self.tmp.append(self.game.player.get_keys())

            self.assertEqual(self.tmp, self.expected)
        print("\ttest get_keys : OK")

    def test2_select_weapon(self):
        self.all_test = ["pistol", "shotgun", "uzi", "rifle"]
        for test in self.all_test:
            self.game.player.select_weapon(test)
            self.assertEqual(test, self.game.player.weapon)

        print("\ttest select_weapon : OK")

    def fake_get_ticks(self):
        return self.test_ticks

    def test3_shoot(self):
        self.all_test = ["pistol", "shotgun", "uzi", "rifle"]
        self.expected = []
        self.tmp = []

        with patch("pygame.time.get_ticks", new_callable=Mock) as mock_get_ticks:
            mock_get_ticks.side_effect = self.fake_get_ticks

            for test in self.all_test:
                self.game.player.last_shot = 0
                self.game.player.weapon = test

                # Trigger (A > B)
                self.test_ticks = WEAPONS[test]['rate'] + 1
                self.tmp.append(self.game.player.shoot())
                self.expected.append("shoot")

                # Not Trigger (A < B)
                self.test_ticks = WEAPONS[test]['rate'] - 1
                self.tmp.append(self.game.player.shoot())
                self.expected.append("no_shoot")

            self.assertEqual(self.tmp, self.expected)

        print("\ttest shoot : OK")

    def test4_update(self):
        # self.game.player.update()
        #nothing to do
        print("\ttest update : OK")

    def test5__run_kickback(self):
        # self.game.player._run_kickback
        #nothing to do
        print("\ttest run_kickback : OK")

    def test6__subtract_ammo(self):
        self.all_test = [("pistol", WEAPONS["pistol"]["bullet_count"]), ("shotgun", WEAPONS["shotgun"]["bullet_count"]), ("uzi", WEAPONS["uzi"]["bullet_count"]), ("rifle", WEAPONS["rifle"]["bullet_count"])]
        for test in self.all_test:
            self.game.player.weapon = test[0]
            self.game.player.ammo[test[0]] = 88
            self.game.player._subtract_ammo()
            self.assertEqual(self.game.player.ammo[test[0]], 88 - test[1])

        print("\ttest _subtract_ammo : OK")

    def test7__check_ammo_less_than_zero(self):
        self.all_test = ["pistol", "shotgun", "uzi", "rifle"]
        for test in self.all_test:
            self.game.player.weapon = test
            # less than zero
            self.game.player.ammo[test] = -1
            self.game.player._check_ammo_less_than_zero()
            self.assertEqual(self.game.player.ammo[test], 0)

            # otherwise
            self.game.player.ammo[test] = 0
            self.game.player._check_ammo_less_than_zero()
            self.assertEqual(self.game.player.ammo[test], 0)

            self.game.player.ammo[test] = 1
            self.game.player._check_ammo_less_than_zero()
            self.assertEqual(self.game.player.ammo[test], 1)

        print("\ttest _check_ammo_less_than_zero : OK")

    def test8__create_bullets(self):
        # self.game.player._create_bullets
        #nothing to do
        print("\ttest _create_bullets : OK")

    # def fake_play(self):
    #     print("haha")

    # def test9__run_weapon_sound(self):
    #     with patch('pygame.mixer.music.play', new_callable=Mock) as mock_play:
    #         mock_play.side_effect = self.fake_play
    #         self.game.player.weapon = "pistol"
    #         self.game.player._run_weapon_sound()
            
    #     sound = choice(self.game.weapon_sounds[self.game.player.weapon])
    #     if sound.get_num_channels() > 2:
    #         sound.stop()
    #     sound.play()

    def test10__create_smoke(self):
        # self.game.player._create_smoke()
        #nothing to do
        print("\ttest __create_smoke : OK")

    def test11__update_rotation(self):
        # self.game.player._update_rotation
        #nothing to do
        print("\ttest _update_rotation : OK")

    def fake_load(self, path):
        self.tmp.append(path[59:])

    def test12__update_weapon(self):
        with patch("pygame.image.load", new_callable=Mock) as mock_load:
            mock_load.side_effect = self.fake_load

            self.all_test = [None, "pistol", "shotgun", "uzi", "rifle"]
            self.expected = [PLAYER_IMAGE_NAKED, PLAYER_IMAGE_PISTOL, PLAYER_IMAGE_SHOTGUN, PLAYER_IMAGE_UZI, PLAYER_IMAGE_SHOTGUN]
            self.tmp = []

            for test in self.all_test:
                self.game.player.weapon = test
                self.game.player._update_weapon()

            self.assertEqual(self.tmp, self.expected)

        print("\ttest _update_weapon : OK")

    def test13__update_damage(self):
        # self.game.player._update_damage()
        #nothing to do
        print("\ttest _update_damage : OK")

    def test14__update_player(self):
        # self.game.player._update_player()
        #nothing to do
        print("\ttest _update_player : OK")

if __name__ == '__main__':
    unittest.main()