import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

x=0
y=0
a= 30
b=290
speedY = 3
speedX = 3
counter = 0
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        x = speedX+x
        y = speedY+y
        
        #pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_UP]: y -= speedY
        #if pressed[pygame.K_DOWN]: y += speedY
        #if pressed[pygame.K_LEFT]: x -= SpeedX
        #if pressed[pygame.K_RIGHT]: x += SpeedX

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: a -= 4
        if pressed[pygame.K_RIGHT]: a += 4

    

        if y < 0:
                speedY *=-1
                
        if x > 350 or x < 0:
                speedX *= -1
        
                
        if x>a-40 and x<a+40 and y == 240:
            speedY *= -1
            counter+=1
            print(counter)

        if y >300:
                pygame.quit()

        
            

        screen.fill((255, 255, 255))
        
        screen.blit(get_image('ball.png'), (x, y))

        color = (0, 128, 255)
        
        pygame.draw.rect(screen, color, pygame.Rect(a, b, 80, 10))
        
        pygame.display.flip()
        clock.tick(60)
