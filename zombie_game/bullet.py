from random import uniform

from zombie_game.settings import *


class Bullet(pg.sprite.Sprite):

    def __init__(self, game, position, direction):
        self._layer = BULLET_LAYER
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        try:
            self.image = game.bullet_images[WEAPONS[game.player.weapon]['bullet_size']]
        except:
            self.image = None #key error, no weapons
        try:
            self.rect = self.image.get_rect()
        except:
            self.rect = None

        self.position = vector(position)
        self.game = game

        try:
            self.rect.center = position
        except:
            pass
        
        try:
            self.vel = direction * WEAPONS[game.player.weapon]['bullet_speed'] * uniform(0.9, 1.1)
        except:
            self.vel = None #no weapon, no bullet, vel = 0
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        print(self.game.dt)
        try:
            self.position += self.vel * self.game.dt
            self.rect.center = self.position
            
            self.image = pg.transform.rotate(self.game.bullet_images['large'], self.game.player.rotation - 90)

            if pg.sprite.spritecollideany(self, self.game.walls):
                self.kill()
        
            if pg.time.get_ticks() - self.spawn_time > WEAPONS[self.game.player.weapon]['bullet_lifetime']:
                self.kill()
        except:
            if pg.time.get_ticks() - self.spawn_time > 1000:
                self.kill()
