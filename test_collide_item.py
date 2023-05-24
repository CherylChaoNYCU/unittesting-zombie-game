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


class TestCollideItem(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.items = []
        self.game = Game()

        #self.assertRaises(Exception,self.game.menu.game_intro())
        print('setting up')
        
        
        #testing for items, stubing: shotgun/pistol/ammo_small/key/id card/money
        self.player = self.game.player
        self.item_img = self.game.items_images
        

    #Should this be written in another class?
    def test_collide_health(self):
        
        #stubing hits, suppose the player collide with health
        
        health_item = pg.sprite.Sprite()
        health_item.type = 'health'
        self.items.append(health_item)
        stub_shield = PLAYER_SHIELD - 10
        self.game.player.shield = stub_shield
        self.game.hit_test = self.items
        self.game._collide_player_with_items()
        self.assertEqual(self.game.player.shield, PLAYER_SHIELD)
        #self.assertEqual(self.game.sound_effects.call_count,1)


        #testing get_health
        with patch.object(self.game,'get_health') as mock_get_health:
            stub_shield = PLAYER_SHIELD - 10
            self.game.player.shield = stub_shield
            self.game.hit_test = self.items
            self.game._collide_player_with_items()
            
            self.assertEqual(mock_get_health.call_count,1)

    
    def test_collide_weapon(self):
        
        #shotgun
        gun_item = pg.sprite.Sprite()
        gun_item.type = 'shotgun'
        self.items.append(gun_item)
        self.game.hit_test = self.items

        #pistol
        pistol_item = pg.sprite.Sprite()
        pistol_item.type = 'pistol'
        self.items.append(pistol_item)
        self.game.hit_test = self.items

        #uzi
        uzi_item = pg.sprite.Sprite()
        uzi_item.type = 'uzi'
        self.items.append(uzi_item)
        self.game.hit_test = self.items

        #rifle
        rifle_item = pg.sprite.Sprite()
        rifle_item.type = 'rifle'
        self.items.append(rifle_item)
        self.game.hit_test = self.items




        self.game._collide_player_with_items()
        #self.assertEqual(self.player.weapon,'shotgun')
        self.assertIn('shotgun',self.player.all_weapons)
        #self.assertEqual(self.player.weapon,'pistol')
        self.assertIn('pistol',self.player.all_weapons)
        #self.assertEqual(self.player.weapon,'uzi')
        self.assertIn('uzi',self.player.all_weapons)
        self.assertEqual(self.player.weapon,'rifle')
        self.assertIn('rifle',self.player.all_weapons)

        
        with patch.object(self.game,'get_weapon') as mock_get_weapon:
            self.game.hit_test = self.items
            self.game._collide_player_with_items()
            
            self.assertEqual(mock_get_weapon.call_count,4)



    def test_collide_ammo(self):
        
        

        #stub ammo value
        origin_ammo = []
        for w in ['shotgun','pistol','uzi','rifle']:
            item = pg.sprite.Sprite()
            item.type = w
            self.items.append(item)
            self.player.ammo[w] = WEAPONS[w]['ammo_limit']-1
            #origin_ammo.append(self.player.ammo[w])
        
        ammo_item = pg.sprite.Sprite()
        ammo_item.type = 'ammo_small'
        self.items.append(ammo_item)
        type_of_pack = {'small': 0.8, 'big': 1.2}

        ammobig_item = pg.sprite.Sprite()
        ammobig_item.type = 'ammo_big'
        self.items.append(ammobig_item)

        
        self.game.hit_test = self.items

        self.game._collide_player_with_items()
  
        for w in ['pistol','shotgun','uzi','rifle']:
            self.assertEqual(self.player.ammo[w],WEAPONS[w]['ammo_limit'])


    def test_kim(self):
        for i in ['key','id_card','money']:
            item = pg.sprite.Sprite()
            item.type = i
            self.items.append(item)
        
        self.game.hit_test = self.items
        self.game._collide_player_with_items()

            
        self.assertEqual(self.player.has_key,True)
        self.assertEqual(self.player.has_id,True)
        self.assertEqual(self.player.money,True)






 



    
    def tearDown(self):
        print('tearing down')
        #pg.quit()
        #del self.game




if __name__ == '__main__':
    unittest.main()