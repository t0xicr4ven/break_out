import pygame
from ball import Ball
from paddle import Paddle
from brick import Brick


pygame.init()
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (800,600)

score = 0
lives = 3

# set up screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Breakout Game')

#list of all sprites we will use in game
all_sprites_list = pygame.sprite.Group()

#paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

#ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195


#bricks
all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

#add sprites to list
all_sprites_list.add(paddle)
all_sprites_list.add(ball)


inProgress = True

clock = pygame.time.Clock()

while inProgress:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inProgress = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                inProgress = False

    #move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5)

    #update sprites
    all_sprites_list.update()

    # check if ball needs to bouce
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #game over
            font = pygame.font.Font(None, 74)
            text = font.render('GAME OVER', 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            inProgress = False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
    
    
    # check collision with paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # check collision with bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks)==0:
            font = pygame.font.Font(None, 74)
            text = font.render('LEVEL COMPLETE',1,WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            inProgress = False
    # change screen to blue and add line
    screen.fill(DARKBLUE)
    pygame.draw.line(screen,WHITE, [0,38], [800,38],2)

    #display score and lives
    font = pygame.font.Font(None, 34)
    text = font.render('Score: ' + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render('Lives: '+ str(lives), 1, WHITE)
    screen.blit(text, (650,10))
    
    #draw sprites
    all_sprites_list.draw(screen)



    #update screen
    pygame.display.flip()
    #set to 60 frame updates per second
    clock.tick(60)

pygame.quit()
