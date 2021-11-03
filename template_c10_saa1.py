import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
bird=pygame.Rect(100,250,30,30)
groundx=0
speed=0
def movedown():
    global speed
    gravity=0.2
    speed=speed+gravity
    bird.y=bird.y+speed
def moveup():
    global speed
    speed=speed-10
while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-550:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  movedown()
  screen.blit(images["bird"],bird)
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
    # Handle the event of UP arrow key getting pressed
    # Check if any key is pressed
    
        # Check if the pressed key is the UP key
        
            # Call the 'moveup()' function
            
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
