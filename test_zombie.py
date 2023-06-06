import unittest
import pygame as pg
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
from zombie_game.item import *
from zombie_game.player import *
from zombie_game.bullet import *  # Replace with the actual module and class name
from zombie_game.zombie import *
from zombie_game.smoke import *
from zombie_game.walls import *
from zombie_game.functions import *
import math


class TestBullet(unittest.TestCase):

    def setUp(self):
        self.game = Game()  # Create a sprite group for testing
        self.game.player.position = (0,0)
        self.game.player.rect = pg.Rect(0, 0, 2, 2)
        self.game.items = pg.sprite.Group()
        
    #mock the uniform function so that it will always return 1.0
    def test_zombie_draw_shield(self):
        
        print("Test for draw_shield in zombie.py:")
        #stubing pos , dir
        cx = 1
        cy = 1
        
        
    
        zombie = Zombie(self.game, cx, cy)
        #stub zombie shield
        s = 0
        
        while(s < 100):
            zombie.shield = s
            zombie.draw_shield()
            if (s > 60):
                self.assertEqual(zombie.color,GREEN)
            elif (s > 30):
                self.assertEqual(zombie.color,YELLOW)
            else:
                self.assertEqual(zombie.color,RED)
            s+=10
            
        zombie.rect.width = 100
        stub_wid = int(100*zombie.shield/ZOMBIE_SHIELD)
        zombie.draw_shield()
        self.assertEqual(zombie.shield_bar,pg.Rect(0,0,stub_wid,7))
        
        pg.draw.rect = Mock()
        zombie.shield = 0
        zombie.draw_shield()
        self.assertEqual(pg.draw.rect.call_count,1)

        

    
        print("\ttest draw_shield() : OK")
    
    def test_zombie_update(self):

        print('Test for update in zombie.py:')
        cx = 0.1
        cy = 0.1

        zombie = Zombie(self.game, cx, cy)
        zombie._update_collisisions = Mock()
        zombie._update_position = Mock()
        zombie._update_damage = Mock()
        zombie._update_image = Mock()
        zombie._update_zombie_moan_sounds = Mock()
        zombie.update()

        self.assertEqual(zombie._update_collisisions.call_count,1)
        self.assertEqual(zombie._update_position.call_count,1)
        self.assertEqual(zombie._update_damage.call_count,1)
        self.assertEqual(zombie._update_image.call_count,1)
        self.assertEqual(zombie._update_zombie_moan_sounds.call_count,1)
        
        

        zombie.die = Mock()
        zombie.shield = -1
        zombie.update()
        self.assertEqual(zombie.die.call_count,1)

        print("\ttest update(): OK")
    
    @patch('zombie_game.zombie.randint', return_value=80)
    def test_zombie_die(self,mock_randint):

        print('Test for die in zombie.py:')
        
        cx = 1
        cy = 1
        

        zombie = Zombie(self.game, cx, cy)
        zombie.kill = Mock()

        zombie.die()

        self.assertEqual(zombie.test_size,80)
        self.assertEqual(zombie.test_smoke.rect.center,vector(cx,cy))
        self.assertEqual(zombie.kill.call_count,1)

        print("\ttest die(): OK")

    
    @patch('zombie_game.zombie.randint', return_value=80)
    def test_zombie_update_collision(self,mock_randint):

        print('Test for update collisions in zombie.py:')
        
        cx = 10
        cy = 10
        

        zombie = Zombie(self.game, cx, cy)
        zombie.hit_rect = pg.Rect(0, 0, 9, 9)
        zombie._avoid_other_zombies = Mock()

        '''
        wall centerx > zombie centerx
        '''
        #create walls
        self.game.walls= pg.sprite.Group()
        #direction = x, hits[0].rect.centerx > sprite.hit_rect.centerx
        wall_1 = Obstacle(self.game, 0,0,10,10)
        self.game.walls.add(wall_1)
        zombie._update_collisisions()
        self.assertEqual(zombie.position.x,wall_1.rect.left-zombie.hit_rect.width/2)
        #self.assertEqual(zombie.position.y,wall_1.rect.top-zombie.hit_rect.height/2)


        '''
        wall centerx < zombie centerx
        '''
        #create walls
        self.game.walls= pg.sprite.Group()
        #direction = x, hits[0].rect.centerx < sprite.hit_rect.centerx
        zombie.hit_rect = pg.Rect(0, 0, 10, 10)
        wall_1 = Obstacle(self.game, 0,0,9,9)
        self.game.walls.add(wall_1)
        zombie._update_collisisions()
        self.assertEqual(zombie.position.x,wall_1.rect.right+zombie.hit_rect.width/2)
        self.assertEqual(zombie.vel.x,0)
        self.assertEqual(zombie.hit_rect.centerx,zombie.position.x)

        '''
        wall centery > zombie centery
        '''
        #create walls
        self.game.walls= pg.sprite.Group()
        zombie.hit_rect = pg.Rect(0, 0, 10, 8)
        wall_1 = Obstacle(self.game, 0,0,10,10)
        self.game.walls.add(wall_1)
        zombie._update_collisisions()
        self.assertEqual(zombie.position.y,wall_1.rect.top-zombie.hit_rect.height/2)


        '''
        wall centery < zombie centery
        '''
        #create walls
        self.game.walls= pg.sprite.Group()
        zombie.hit_rect = pg.Rect(0, 0, 10, 10)
        wall_1 = Obstacle(self.game, 0,0,10,6)
        self.game.walls.add(wall_1)
        zombie._update_collisisions()
        self.assertEqual(zombie.position.y,wall_1.rect.bottom+zombie.hit_rect.height/2)
        self.assertEqual(zombie.vel.y,0)
        self.assertEqual(zombie.hit_rect.centery,zombie.position.y)
        
        self.assertEqual(zombie._avoid_other_zombies.call_count,4)


        print("\ttest _update_collision(): OK")

    
    def test_avoid_other_zombie(self):

        print('Test for avoid_other_zombie in zombie.py:')
        
        self.game.zombies = pg.sprite.Group()
        cx = 10
        cy = 10
        #create 1 zombies
        zmb = Zombie(self.game,cx,cy)
        self.game.zombies.add(zmb)
        zombie_self = Zombie(self.game, 11, 11)
        expected_dist = zombie_self.position - zmb.position
        zombie_self._avoid_other_zombies()
        self.assertAlmostEqual(zombie_self.acc,expected_dist.normalize())

        print("\ttest avoid_other_zombie(): OK")

    @patch('zombie_game.zombie.random', return_value=0.001)
    def test_update_zombie_moan_sounds(self,mock_random):

        print('Test for avoid_other_zombie in zombie.py:')
        
        cx = 10
        cy = 10
        #create 1 zombies
        zombie = Zombie(self.game,cx,cy)
        zombie._update_zombie_moan_sounds()
        self.assertIn(zombie.test_moan,self.game.zombie_moan_sounds)

        print("\ttest update_zombie_moan_sounds(): OK")
    

    def test_update_damage(self):

        print('Test for update_damage in zombie.py:')
        
        cx = 10
        cy = 10
        #create 1 zombies
        zombie = Zombie(self.game,cx,cy)
        get_hit(zombie)
        zombie._update_damage()
        self.assertEqual(zombie.test_alpha,0)

        #make the iteration stop
        get_hit(zombie)
        for i in range(100):
            zombie._update_damage()
        self.assertEqual(zombie.damaged,False)

        print("\ttest update_damage(): OK")
    
    def test_update_image(self):

        print('Test for update_image in zombie.py:')
        
        cx = 10
        cy = 10
        #create 1 zombies
        zombie = Zombie(self.game,cx,cy)
        get_hit(zombie)
        expected_roat = (vector(0,0) - zombie.position).angle_to(vector(1, 0))
        pg.transform.rotate = Mock()
        zombie._update_image()
        self.assertEqual(zombie.rotation,expected_roat)
        pg.transform.rotate.assert_called_once_with(self.game.zombie_img,expected_roat)
        

        print("\ttest update_image(): OK")

    
    def test_update_postion(self):

        print('Test for update_position in zombie.py:')
        
        cx = 10
        cy = 10
        #create 1 zombies
        zombie = Zombie(self.game,cx,cy)
        zombie.rect = pg.Rect(0, 0, 10, 10)
        self.game.dt = 1/100
        zombie.rotation = 90 #acc = [0,-1]
        zombie.speed = 100 #acc = [0,-100]
        expected_acc = [0,-100]+vector(1,1)*(-1)
        zombie.vel = vector(1,1)
        expected_vel = zombie.vel + expected_acc * 1/100
        expected_pos = zombie.position+expected_vel*1/100+(expected_acc*1/100**2)/2
        zombie._update_position()
        self.assertEqual(zombie.acc,expected_acc)
        self.assertEqual(zombie.vel,expected_vel)
        self.assertEqual(zombie.position,expected_pos)
        self.assertEqual(zombie.hit_rect.centerx,round(expected_pos.x))
        self.assertEqual(zombie.hit_rect.centery,round(expected_pos.y))
        self.assertEqual(zombie.rect.center,zombie.hit_rect.center)
        

        print("\ttest update_position(): OK")
        

    






       




    # Add more test methods for other scenarios...

if __name__ == '__main__':#pragma: no cover
    unittest.main()
