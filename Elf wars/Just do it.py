#Logan Douglas
#4/10/19

#Import
from superwires import games,color #This will import the screen, mouse, and keyboard
import random

SCORE = 0

games.init(screen_width = 768, screen_height = 480, fps = 50)

#Class
class Archer(games.Sprite):
  def update(self):
    global SCORE
    """Reverse a velocity componet if edge of screen is reached."""

     #Bounce mechanic
##    if self.right > games.screen.width or self.left<0:
##      self.dx = -self.dx
##      SCORE+=1
##
##    if self.bottom > games.screen.height or self.top <0:
##      self.dy = -self.dy
##      SCORE+=1
##        
     if self.left>games.screen.width:
       self.right=0
     if self.right<0:
       self.right=games.screen.width
##    if self.left>games.screen.width:
##      self.x=self.screen.width/2
##      self.top=0
##      self.dx=0
##      self.dy=-5
##      
##    if self.top>games.screen.height:
##      self.y=self.screen.height/2
##      self.right=self.screen.width
##      self.dx=-5
##      self.dy=0
##
##
##    
    
      
 
class ScText(games.Text):
  def update(self):
    self.value = SCORE



def main():
  #Load images
  bg_img = games.load_image("Art/spiritual-pathways-1.JPG", transparent = False)
  arch_img = games.load_image("Art/Untitled.PNG", transparent = True)

  #Set backround image
  games.screen.background = bg_img

  #Create "Archer" sprite
  archer = Archer(image = arch_img,
                        x=games.screen.width/2,
                        y=games.screen.height/2,
                        dx=5,
                        dy=0)
  games.screen.add(archer)

  #Create text value for score
  score = ScText(value=SCORE,
                     size=45,
                     color=color.white,
                     x=50,
                     y=25)
  games.screen.add(score)


##  game_over = games.Message(value = "Game Over",
##                            size = 75,
##                            color = color.red,
##                            x=games.screen.width/2,
##                            y=games.screen.height/2,
##                            lifetime = 250,
##                            after_death = games.screen.quit)
##  games.screen.add(game_over)

  games.screen.mainloop()

main()
