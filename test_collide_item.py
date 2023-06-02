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
        self.game.player.position = (0,0)
        self.game.player.rect = pg.Rect(0, 0, 2, 2)
        self.game.items = pg.sprite.Group()
        

    #Should this be written in another class?
    def test_collide_health(self):
        
        #stubing hits, suppose the player collide with health
        print("Test for collide_health in main.py:")
      
        object_center = vector(1, 1)
        health_item = Item(self.game,object_center,'health')
        health_item.rect= pg.Rect(0, 0, 2, 2)
        self.game.items.add(health_item)

        stub_shield = PLAYER_SHIELD - 10
        self.game.player.shield = stub_shield
        
        self.game._collide_player_with_items()
        self.assertEqual(self.game.player.shield, PLAYER_SHIELD)
        #self.assertEqual(self.game.sound_effects.call_count,1)


        #testing get_health
        with patch.object(self.game,'get_health') as mock_get_health:
            stub_shield = PLAYER_SHIELD - 10
            self.game.player.shield = stub_shield
            object_center = vector(1, 1)
            health_item = Item(self.game,object_center,'health')
            health_item.rect= pg.Rect(0, 0, 2, 2)
            self.game.items.add(health_item)
            self.game._collide_player_with_items()
            
            self.assertEqual(mock_get_health.call_count,1)
        
        print("\ttest collide_health : OK")
    
    def test_collide_mini_health(self):
        
        print("Test for collide_health(mini) in main.py:")
        object_center = vector(2,2)
        health_item = Item(self.game,object_center,'mini_health')
        health_item.rect= pg.Rect(1, 1, 2, 2)
        self.game.items.add(health_item)

        stub_shield = 1
        self.game.player.shield = stub_shield
        self.game._collide_player_with_items()
        self.assertEqual(self.game.player.shield, MINI_HEALTH_PACK+1)
        #self.assertEqual(self.game.sound_effects.call_count,1)


        #testing get_health
        with patch.object(self.game,'get_health') as mock_get_health:
            stub_shield = 1
            object_center = vector(2,2)
            health_item = Item(self.game,object_center,'mini_health')
            health_item.rect= pg.Rect(1, 1, 2, 2)
            self.game.items.add(health_item)
            self.game._collide_player_with_items()
            
            self.assertEqual(mock_get_health.call_count,1)
        
        print("\ttest collide_health(mini) : OK")
    


    
    def test_collide_weapon(self):
        print("Test for collide_weapon in main.py:")
        #shotgun
        object_center = vector(1, 1)
        gun_item = Item(self.game,object_center,'shotgun')
        gun_item.rect= pg.Rect(0, 0, 2, 2)
        self.game.items.add(gun_item)

        #pistol
        object_center2 = vector( 2, 2)
        pistol_item = Item(self.game,object_center2,'pistol')
        pistol_item.rect = pg.Rect(1,1,2,2)
        self.game.items.add(pistol_item)
        

        #uzi
        object_center3 = vector(1.5, 1.5)
        uzi_item = Item(self.game,object_center3,'uzi')
        uzi_item.rect = pg.Rect(0,0,2,2)
        self.game.items.add(uzi_item)

        #rifle
        object_center4 = vector(1.6, 1.6)
        rifle_item = Item(self.game,object_center4,'rifle')
        rifle_item.rect = pg.Rect(0,0,2,2)
        self.game.items.add(rifle_item)




        self.game._collide_player_with_items()
        #self.assertEqual(self.player.weapon,'shotgun')
        self.assertIn('shotgun',self.game.player.all_weapons)
        #self.assertEqual(self.player.weapon,'pistol')
        self.assertIn('pistol',self.game.player.all_weapons)
        #self.assertEqual(self.player.weapon,'uzi')
        self.assertIn('uzi',self.game.player.all_weapons)
        self.assertEqual(self.game.player.weapon,'rifle')
        self.assertIn('rifle',self.game.player.all_weapons)
        self.assertListEqual(self.game.player.all_weapons,['shotgun','pistol','uzi','rifle'])



        print("Test for collide_ammo in main.py:")
        #self.game.items = pg.sprite.Group()
        #self.game.player.rect =  pg.Rect(10,10,20,20)

        #stub ammo value
        for w in ['shotgun','pistol','uzi','rifle']:
            self.game.player.ammo[w] = WEAPONS[w]['ammo_limit']-1
        
        object_center = vector(1, 1)
        ammo_item = Item(self.game,object_center,'ammo_small')
        ammo_item.rect = pg.Rect(1,1,2,2)
        self.game.items.add(ammo_item)


        object_center2 = vector(1.1, 1.1)
        ammobig_item = Item(self.game,object_center2,'ammo_big')
        ammobig_item.rect = pg.Rect(1.1,1.1,2,2)
        self.game.items.add(ammobig_item)

        

        self.game._collide_player_with_items()
  
        for w in ['pistol','shotgun','uzi','rifle']:
            self.assertEqual(self.game.player.ammo[w],WEAPONS[w]['ammo_limit'])
        
        print("\ttest collide_weapon + collide_ammo : OK")



    def test_kim(self):

        print("Test for collide_item (others) in main.py:")

        idx = 0
        for i in ['key','id_card','money']:
            object_center = vector(idx , idx)
            other_item = Item(self.game,object_center,i)
            other_item.rect = pg.Rect(0.1*idx,0.1*idx,2,2)
            self.game.items.add(other_item)
            idx+=1
        self.game._collide_player_with_items()

            
        self.assertEqual(self.game.player.has_key,True)
        self.assertEqual(self.game.player.has_id,True)
        self.assertEqual(self.game.player.money,True)

        print("\ttest collide_item(others) : OK")






 








if __name__ == '__main__':#pragma: no cover
    unittest.main()