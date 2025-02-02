import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
import pygame as pg
from zombie_game.bullet import Bullet
from zombie_game.settings import *
from zombie_game.player import *
from zombie_game.item import *
from zombie_game.menu import *
from os import path
import os


class TestGame(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.game = Game()

        
        #testing for items, stubing: shotgun/pistol/ammo_small/key/id card/money
        self.player = self.game.player
        self.item_img = self.game.items_images
        

    
    def test_load_scoreboard(self):
                # Create a temporary file to use for testing
        print("Test for load_scoreboard in main.py:")
        temp_file = 'temp_scoreboard.txt'
        tmp_score_list = []
        init = self.game.score_list
        self.game.score_list = tmp_score_list #stub with empty list

        with open(temp_file, 'w') as f:
            f.write('John 10\n')
            f.write('Jane 15\n')
            f.write('Bob 5\n')

        # Test loading scoreboard
        self.game.load_scoreboard(temp_file)

        # Assert that score_list was loaded correctly
        expected_scores = [('John', '10'), ('Jane', '15'), ('Bob', '5')]
        self.assertEqual(self.game.score_list, expected_scores)
        
        self.game.score_list = init

        print("\ttest load_scoreboard : OK")

   

 
        os.remove(temp_file)



    def test_load_flash_smoke(self):
        #self.game.load_flash_smoke()
        #print('test flash')
        self.assertNotEqual(len(self.game.gun_smoke), 0) #make sure that successfully load some smoke image
    
    def test_load_green_smoke(self):
        #self.game.load_green_smoke()
        #print('test green')
        self.assertNotEqual(len(self.game.zombie_death_smoke), 0)
    
    
    def test_load_light_mask(self):
        #self.game.load_light_mask()
        #print('test mask')
        self.assertIsNotNone(self.game.light_mask)
    
    def test_load_sounds(self):
        #self.game.load_sounds()
        #print('test load sound')
        print("Test for load_sounds in main.py:")

        self.assertNotEqual(len(self.game.sound_effects),0)
        self.assertNotEqual(len(self.game.weapon_sounds),0)
        self.assertNotEqual(len(self.game.zombie_moan_sounds),0)
        self.assertNotEqual(len(self.game.zombie_pain_sounds),0)
        self.assertNotEqual(len(self.game.zombie_die_sounds),0)
        self.assertNotEqual(len(self.game.player_die_sounds),0)
        self.assertNotEqual(len(self.game.player_pain_sounds),0)

        #to make sure that _add_sounds is called after calling load_sounds
    
        with patch.object(self.game,'_add_sounds') as mock_add_sounds:
            self.game.load_sounds()
            calls = len(self.game.weapon_sounds)+5
            self.assertEqual(mock_add_sounds.call_count,calls)
        
        print("\ttest load_sounds : OK")

    #stubing
    def test_add_sounds(self):
        #print('test add sound')

        print("Test for add_sounds in main.py:")
        sounds = ['test1.ogg','test2.ogg']
        sound_list = []
        vol = 0.5

        #mock function: pg.mixer.Sound in pygame
        mock_sound1 = MagicMock()
        mock_sound2 = MagicMock()

        mock_sound1.get_volume.return_value = vol
        mock_sound2.get_volume.return_value = vol

        with patch('pygame.mixer.Sound', side_effect=[mock_sound1, mock_sound2]):
            self.game._add_sounds(sounds, sound_list, vol)
        
        self.assertEqual(len(sounds),len(sound_list))
        for s in sound_list: #make sure all volumn is set correctly
            self.assertEqual(s.get_volume(),vol)
        print("\ttest add_sounds : OK")
    
    def test_load_items(self):
        print("Test for load_items in main.py:")


        for item in ITEM_IMAGES:
            self.assertIn(item, self.game.items_images)
            self.assertIsInstance(self.game.items_images[item], pg.Surface)
            if item == 'shotgun' or item == 'rifle':
                self.assertEqual(self.game.items_images[item].get_size(), (2 * ITEM_SIZE, ITEM_SIZE))
                #self.assertEqual(self.game.items_images['rifle'].get_size(), (2 * ITEM_SIZE, ITEM_SIZE))
            else:
                 self.assertEqual(self.game.items_images[item].get_size(), (ITEM_SIZE, ITEM_SIZE))
        print("\ttest load_items : OK")
    
    def test_load_splats(self):
        #self.game.load_splats() as the load splats is called while the game is initialized, so be careful not to call again
        #print(self.game.splats)
        #print('test splats')
        print("Test for load_splats in main.py:")
        self.assertEqual(len(self.game.splats),4) #check at the end...
        for splat in self.game.splats:
            self.assertEqual(splat.get_width(),64)
            self.assertEqual(splat.get_height(),64)
        print("\ttest load_splats : OK")
                

    def test_bullets(self):

        #print('test bullet')
        print("Test for load_bullets in main.py:")

        for sets in self.game.bullet_images:
            self.assertIn(sets,self.game.bullet_images)
            self.assertIsInstance(self.game.bullet_images[sets],pg.Surface)

            if sets == 'long':
                self.assertEqual(self.game.bullet_images[sets].get_size(),(5,15))
            elif sets == 'large':
                self.assertEqual(self.game.bullet_images[sets].get_size(),(5,10))
            else:
                self.assertEqual(self.game.bullet_images[sets].get_size(),(3,7))
        print("\ttest load_bullets : OK")

    



    


if __name__ == '__main__':#pragma:no cover
    unittest.main()