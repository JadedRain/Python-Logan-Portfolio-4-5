#Asteroids 1.0
#Created by Logan Douglas


#Imports
from superwires import games, color
import random
import math


#Globals
games.init(screen_width=1280, screen_height=720, fps=60)


#Functions


#Classes
class Game(object):
    def __init__(self):
        #Set level
        self.level = 0
        #Load sound for level advance
        self.sound = games.load_sound("Sound/Advance.wav")
        #Create score
        self.score = games.Text(value=0,
                                size=30,
                                color=color.white,
                                top=5,
                                right = games.screen.width-10,
                                is_collideable = False)
        games.screen.add(self.score)
        self.ship = Ship(game = self,
                           x = games.screen.width/2,
                           y = games.screen.height/2)
        games.screen.add(self.ship)



    def play(self):
        #games.music.load("Sound/theme.mid")
        #games.music.play(-1)

        bg_img = games.load_image("Art/BackGround1280x720.jpg")
        games.screen.background = bg_img

        self.advance()

        games.screen.mainloop()

    def advance(self):
        self.level+=1

        #Space to help player
        BUFFER = 250
        for i in range(self.level + 5):
            #Calculate buffer distance from ship
            x_min = random.randrange(BUFFER)
            y_min = BUFFER -x_min
            #Choose distnace along x axis and y axis
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            #Calculate location
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance
            #Wrap if need
            x %= games.screen.width
            y %= games.screen.height

            newAsteroid = Asteroids(game = self, x = x, y = y, size =  Asteroids.LAR)
            games.screen.add(newAsteroid)
    #Display level number
        levelMessage = games.Message(value = "Level: "+str(self.level),
                                    size = 40,
                                    color = color.yellow,
                                    x = games.screen.width/2,
                                    y = games.screen.width/10,
                                    lifetime = 3 * games.screen.fps,
                                    is_collideable = False)
        games.screen.add(levelMessage)

        self.lives = 3
        self.livesMessage = games.Text(value="Lives: "+str(self.lives),
                                size=35,
                                color=color.white,
                                top=5,
                                right = 100,
                                is_collideable = False)
        games.screen.add(self.livesMessage)



        if self.level > 1:
            self.sound.play()

    def end(self):
        if self.lives > 0:
            self.lives-=1
            self.ship = Ship(game=self,
                             x=games.screen.width / 2,
                             y=games.screen.height / 2)
            games.screen.add(self.ship)

            self.livesMessage.destroy()

            self.livesMessage = games.Text(value="Lives: " + str(self.lives),
                                      size=35,
                                      color=color.white,
                                      top=5,
                                      right=100,
                                      is_collideable=False)
            games.screen.add(self.livesMessage)

        if self.lives <= 0:
            endMessage = games.Message(value = "Game Over",
                                   size = 90,
                                   color = color.red,
                                   x = games.screen.width/2,
                                   y = games.screen.height/2,
                                   lifetime = 5 * games.screen.fps,
                                   after_death = games.screen.quit,
                                   is_collideable = False)
            games.screen.add(endMessage)


class Wrapper(games.Sprite):
    def update(self):
        # Wraps the ship on the screen
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
    def die(self):
        self.destroy()

class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
    def die(self):
        newExplosion = Explosion(x = self.x,
                                 y = self.y)
        games.screen.add(newExplosion)
        self.destroy()

class Asteroids(Wrapper):
    SMA = 1
    MED = 2
    LAR = 3

    images = {SMA : games.load_image("Art/asteroid_small.png"),
              MED : games.load_image("Art/asteroid_medium.png"),
              LAR : games.load_image("Art/asteroid_large.png")}
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self, game,  x, y, size):
        Asteroids.total+=1
        super(Asteroids, self).__init__(image= Asteroids.images[size],
                                        x = x,
                                        y = y,
                                        dx = random.choice([1,-1]) * Asteroids.SPEED * random.random()/size,
                                        dy=random.choice([1, -1]) * Asteroids.SPEED * random.random() / size                                        )
        self.size = size
        self.game = game


    def die(self):
        Asteroids.total -=1
        #If asteroid isnt small replace with smaller asteroids
        #Add to score
        self.game.score.value += int(Asteroids.POINTS / self.size)
        self.game.score.right = games.screen.width -10
        if self.size != Asteroids.SMA:
            for i in range(Asteroids.SPAWN):
                newAsteroid = Asteroids(game = self.game,
                                        x = self.x,
                                        y = self.y,
                                        size = self.size-1)
                games.screen.add(newAsteroid)
        self.destroy()
        if Asteroids.total == 0:
            self.game.advance()
        super(Asteroids, self).die()


class Ship(Collider):
    image = games.load_image("Art/Playership.png")
    sound = games.load_sound("Sound/RocketThrust.wav")
    sound.set_volume(0.2)
    ROTATION_STEP = 5
    VELOCITY_STEP = 0.05
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        super(Ship,self).__init__(image=Ship.image,
                                  x = x, y = y)
        self.game = game
        self.missileWait = 0

    def update(self):
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)


        #If waiting until the ship can fire nex, decreae wait
        if self.missileWait > 0:
            self.missileWait -= 1


        #Fire missile if spacebar is pressed
        if games.keyboard.is_pressed(games.K_SPACE) and self.missileWait == 0:
            newMissile = Missile(self.x, self.y, self.angle)
            games.screen.add(newMissile)
            self.missileWait = Ship.MISSILE_DELAY

    def die(self):
        self.game.end()
        super(Ship, self).die()


class Missile(Collider):
    image = games.load_image("Art/Laser.png")
    sound = games.load_sound("Sound/laser.wav")
    BUFFER =120
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, shipX, shipY, shipAngle):
        Missile.sound.play()

        #Convert angle to radians
        angle = shipAngle * math.pi / 180

        #Calculate missile starting posision
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = shipX + buffer_x
        y = shipY + buffer_y

        #Calculate missles velocity
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        #Create missile
        super(Missile, self).__init__(image= Missile.image,
                                      x = x, y = y,
                                      dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME
        self.angle=shipAngle

    def update(self):
        super(Missile, self).update()
        #If lifetime is gone destroy
        self.lifetime -=1
        if self.lifetime == 0:
            self.destroy()

class Explosion(games.Animation):
    sound = games.load_sound("Sound/Explosion.wav")
    images = ["Art/exp1.png","Art/exp2.png","Art/exp3.png",
              "Art/exp4.png","Art/exp5.png","Art/exp6.png",
              "Art/exp7.png","Art/exp8.png","Art/exp9.png",
              "Art/exp10.png","Art/exp11.png","Art/exp12.png",
              "Art/exp13.png","Art/exp14.png","Art/exp15.png",
              "Art/exp16.png","Art/exp17.png","Art/exp18.png",
              "Art/exp19.png","Art/exp20.png","Art/exp21.png",
              "Art/exp22.png","Art/exp23.png","Art/exp24.png",
              "Art/exp25.png","Art/exp26.png","Art/exp27.png",
              "Art/exp28.png","Art/exp29.png","Art/exp30.png",
              "Art/exp31.png","Art/exp32.png","Art/exp33.png",
              "Art/exp34.png","Art/exp35.png","Art/exp36.png",
              "Art/exp37.png",]
    def __init__(self, x, y):
        super(Explosion, self).__init__(images= Explosion.images,
                                        x = x, y = y,
                                        repeat_interval=4, n_repeats=1,
                                        is_collideable=False)
        Explosion.sound.play()




#Main
def main():
    astriods = Game()
    astriods.play()
#Run
main()
