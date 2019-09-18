import pygame
from pygame.locals import *
import random



#Pong class that handles everything about the ball

class Pong(object):
    def __init__(self, screensize):

        #initiate screensize and random trajectory for the ball to spawn randomly

        self.screensize = screensize

        self.serve_trajectory = [0.2,0.3,0.4,0.5,0.6,0.7,0.8]

        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*random.choice(self.serve_trajectory))

        self.radius = 8

        self.ballsize = 5

        #create ball
        self.rect = pygame.Rect(self.centerx-self.radius, self.centery-self.radius, self.radius*2, self.radius*2)

        self.color = (100,100,255)

        self.random_direction = [-1,1]

        self.direction = [random.choice(self.random_direction),random.choice(self.random_direction)]

        self.speedx = 3
        self.speedy = 5

        self.hit_edge_left = False
        self.hit_edge_right = False
        self.hit_edge_top = False
        self.hit_edge_bottom = False

    #reset function used to reset the whole game when a point is over
    def reset(self, screensize):
        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*random.choice(self.serve_trajectory))
        self.direction = [random.choice(self.random_direction),random.choice(self.random_direction)]
        self.hit_edge_left = False
        self.hit_edge_right = False
        self.hit_edge_top = False
        self.hit_edge_bottom = False

    def update(self, player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree):

        self.centerx += self.direction[0]*self.speedx
        self.centery += self.direction[1]*self.speedy

        self.rect.center = (self.centerx, self.centery)


        #sets values to true if the ball collides with edges
        if self.rect.right >= self.screensize[0] -1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True
        elif self.rect.top < 2:
            self.hit_edge_top = True
        elif self.rect.bottom > self.screensize[1] -2:
            self.hit_edge_bottom = True

        #sends the ball the other direction & play music if the ball collides with paddles
        if self.rect.colliderect(player_paddle.rect):
            pygame.mixer_music.load('pong_hit.wav')
            pygame.mixer_music.play(0)
            self.direction[0] = -1
        if self.rect.colliderect(player_paddletwo.rect):
            pygame.mixer_music.load('pong_hit.wav')
            pygame.mixer_music.play(0)
            self.direction[1] = -1
        if self.rect.colliderect(player_paddlethree.rect):
            pygame.mixer_music.load('pong_hit.wav')
            pygame.mixer_music.play(0)
            self.direction[1] = 1


        if self.rect.colliderect(pc_paddle.rect):
            pygame.mixer_music.load('pong_hit.wav')
            pygame.mixer_music.play(0)
            self.direction[0] = 1
        if self.rect.colliderect(pc_paddletwo.rect):
            pygame.mixer_music.load('pong_hit.wav')
            pygame.mixer_music.play(0)
            self.direction[1] = 1
        if self.rect.colliderect(pc_paddlethree.rect):
            pygame.mixer_music.load('pong_hit.wav')
            pygame.mixer_music.play(0)
            self.direction[1] = -1

    def render(self,screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), self.rect.center, self.radius, 1)


class PCPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        #placement of paddle
        self.centerx = 5
        self.centery = int(screensize[1]*0.5)

        self.height = 100
        self.width = 10

        #create paddle
        self.rect = pygame.Rect(0, self.centery- int(self.height*0.5), self.width, self.height)

        self.color = (255,100,100)

        self.speed = 5

    def update(self, pong):
        #where the AI is handled
        if pong.rect.top < self.rect.top:
            self.centery -= self.speed
        elif pong.rect.bottom > self.rect.bottom:
            self.centery += self.speed

        self.rect.center = (self.centerx, self.centery)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

class PCPaddleTwo(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = int(screensize[0] * 0.1)
        self.centery = 5

        self.height = 10
        self.width = 100

        self.rect = pygame.Rect(self.centerx-int(self.width*0.5), 0, self.width, self.height)

        self.color = (255,100,100)

        self.speed = 4
    def update(self, pong):
        if pong.rect.left < self.rect.left:
            self.centerx -= self.speed
        elif pong.rect.right > self.rect.right:
            self.centerx += self.speed

        if self.centerx > 280:
            self.centerx = 280

        self.rect.center = (self.centerx, self.centery)

    def render(self,screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

class PCPaddleThree(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = int(screensize[0] * 0.1)
        self.centery = 475

        self.height = 10
        self.width = 100

        self.rect = pygame.Rect(self.centerx-int(self.width*0.5), 0, self.width, self.height)

        self.color = (255,100,100)

        self.speed = 4
    def update(self, pong):
        if pong.rect.left < self.rect.left:
            self.centerx -= self.speed
        elif pong.rect.right > self.rect.right:
            self.centerx += self.speed

        if self.centerx > 280:
            self.centerx = 280

        self.rect.center = (self.centerx, self.centery)

    def render(self,screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

class PlayerPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = screensize[0] - 5
        self.centery = int(screensize[1]*0.5)

        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery- int(self.height*0.5) , self.width, self.height)

        self.color = (100,255,100)

        self.speed = 4
        self.direction = 0

    def update(self):
        #only manipulate y position since we are going up and down
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)

        #prohibits paddle to go beyond bounds
        if self.rect.top < self.rect.top:
            self.centerx -= self.speed
        elif self.rect.bottom > self.rect.bottom:
            self.centerx += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

class PlayerPaddleTwo(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = int(screensize[0]*0.5)
        self.centery = screensize[1] - 5

        self.height = 10
        self.width = 100

        self.rect = pygame.Rect(self.centery - int(self.height*0.5), 0, self.width, self.height)

        self.color = (100,255,100)

        self.speed = 4
        self.direction = 0


    def update(self):
        self.centerx += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)



        if self.rect.left < self.rect.left:
            self.centerx -= self.speed
        elif self.rect.right> self.rect.right:
            self.centerx += self.speed

        if self.centerx < 390:
            self.centerx = 390

        if self.centerx > 590:
            self.centerx = 590

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

class PlayerPaddleThree(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = int(screensize[0]*0.5)
        self.centery = screensize[1] - 475

        self.height = 10
        self.width = 100

        self.rect = pygame.Rect(self.centery - int(self.height*0.5), 0, self.width, self.height)

        self.color = (100,255,100)

        self.speed = 4
        self.direction = 0


    def update(self):
        self.centerx += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)



        if self.rect.left < self.rect.left:
            self.centerx -= self.speed
        elif self.rect.right> self.rect.right:
            self.centerx += self.speed

        if self.centerx < 390:
            self.centerx = 390

        if self.centerx > 590:
            self.centerx = 590

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)


def main():
    player_score = 0
    pc_score = 0

    player_games = 0
    pc_games = 0
    pygame.init()


    screensize = (640,480)


    screen = pygame.display.set_mode(screensize)
    clock = pygame.time.Clock()



    pong = Pong(screensize)
    pc_paddle = PCPaddle(screensize)
    pc_paddletwo = PCPaddleTwo(screensize)
    pc_paddlethree = PCPaddleThree(screensize)
    player_paddle = PlayerPaddle(screensize)
    player_paddletwo = PlayerPaddleTwo(screensize)
    player_paddlethree = PlayerPaddleThree(screensize)


    running = True

    #loop that handles running the game. If running = false then game ends

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            #handles up, down, left, and right for player paddles

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player_paddle.direction = -1
                elif event.key == K_DOWN:
                    player_paddle.direction = 1
            if event.type == KEYUP:
                if event.key == K_UP and player_paddle.direction == -1:
                    player_paddle.direction = 0
                elif event.key == K_DOWN and player_paddle.direction == 1:
                    player_paddle.direction = 0


            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player_paddletwo.direction = -1
                    player_paddlethree.direction = -1
                elif event.key == K_RIGHT:
                    player_paddletwo.direction = 1
                    player_paddlethree.direction = 1
            if event.type == KEYUP:
                if event.key == K_LEFT and player_paddletwo.direction == -1 and player_paddlethree.direction == -1:
                    player_paddletwo.direction = 0
                    player_paddlethree.direction = 0
                elif event.key == K_RIGHT and player_paddletwo.direction == 1 and player_paddlethree.direction == 1:
                    player_paddletwo.direction = 0
                    player_paddlethree.direction = 0


        pc_paddle.update(pong)
        pc_paddletwo.update(pong)
        pc_paddlethree.update(pong)
        player_paddle.update()
        player_paddletwo.update()
        player_paddlethree.update()
        pong.update(player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree)

        #if statements to add score when the ball hits an edge & plays music

        if pong.hit_edge_left:
            pygame.mixer_music.load('small_win.mp3')
            pygame.mixer_music.play(0)
            player_score += 1
            if player_score == 11:
                player_games += 1
                player_score = 0
            pong.update(player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree)
            pong.reset(screensize)
        elif pong.hit_edge_right:
            pygame.mixer_music.load('small_lose.wav')
            pygame.mixer_music.play(0)
            pc_score += 1
            if pc_score == 11:
                pc_games += 1
                pc_score = 0
            pong.update(player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree)
            pong.reset(screensize)
        elif pong.hit_edge_top and pong.centerx < 332:
            pygame.mixer_music.load('small_win.mp3')
            player_score += 1
            if player_score == 11:
                player_games += 1
                player_score = 0
            pong.update(player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree)
            pong.reset(screensize)
        elif pong.hit_edge_top and pong.centerx > 332:
            pygame.mixer_music.load('small_lose.wav')
            pygame.mixer_music.play(0)
            pc_score += 1
            if pc_score == 11:
                pc_games += 1
                pc_score = 0
            pong.update(player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree)
            pong.reset(screensize)
        elif pong.hit_edge_bottom and pong.centerx < 332:
            pygame.mixer_music.load('small_win.mp3')
            player_score += 1
            if player_score == 11:
                player_games += 1
                player_score = 0
            pong.update(player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree)
            pong.reset(screensize)
        elif pong.hit_edge_bottom and pong.centerx > 332:
            pygame.mixer_music.load('small_lose.wav')
            pygame.mixer_music.play(0)
            pc_score += 1
            if pc_score == 11:
                pc_games += 1
                pc_score = 0
            pong.update(player_paddle, pc_paddle, pc_paddletwo, pc_paddlethree, player_paddletwo, player_paddlethree)
            pong.reset(screensize)

        #Once someone wins 3/5 the game will ask in console to play again or not
        #this needs to be worked on more since I couldn't figure out how to display the msg in game

        if player_games == 3 and pc_games < 3:
            print("You win!")
            pc_games = 0
            player_games = 0
            pc_score = 0
            player_score = 0

            pygame.mixer_music.load('big_win.mp3')
            pygame.mixer_music.play(0)

            answer = input("Play Again? Y or N")
            print(answer)
            if answer == 'Y':
                pong.reset(screensize)
            if answer == 'N':
                running = False

        if pc_games == 3 and player_games < 3:
            print("You lose!")
            pc_games = 0
            player_games = 0
            pc_score = 0
            player_score = 0

            pygame.mixer_music.load('big_lose.wav')
            pygame.mixer_music.play(0)

            answer2 = input("Play Again? Y or N")
            print(answer2)
            if answer2 == 'Y':
                pong.reset(screensize)
            if answer2 == 'N':
                running = False

        #fills the screen gray and draw a line down the middle
        screen.fill((100, 100, 100))
        pygame.draw.line(screen, (255, 255, 255), (332, 0), (332, 480), 3)


        pc_paddle.render(screen)
        pc_paddletwo.render(screen)
        pc_paddlethree.render(screen)
        player_paddle.render(screen)
        player_paddletwo.render(screen)
        player_paddlethree.render(screen)
        pong.render(screen)

        #display score boards

        font = pygame.font.SysFont(None, 50)
        screen_text = font.render("AI", True, (255, 255, 255))
        screen.blit(screen_text, (166, 240))

        fontPlayer = pygame.font.SysFont(None, 50)
        screen_Playertext = fontPlayer.render("Player", True, (255, 255, 255))
        screen.blit(screen_Playertext, (400, 240))

        fontAIScore = pygame.font.SysFont(None, 25)
        screen_text_AIscore = fontAIScore.render("AI Score: " + str(pc_score), True, (255, 255, 255))
        screen.blit(screen_text_AIscore, (166, 100))

        fontPlayerScore = pygame.font.SysFont(None, 25)
        screen_text_playerscore = fontPlayerScore.render("Player Score:" + str(player_score), True, (255, 255, 255))
        screen.blit(screen_text_playerscore, (400, 100))

        fontAIGames = pygame.font.SysFont(None, 25)
        screen_text_AIgames = fontAIGames.render("AI Games: " + str(pc_games), True, (255, 255, 255))
        screen.blit(screen_text_AIgames, (166, 50))

        fontPlayerGames = pygame.font.SysFont(None, 25)
        screen_text_playergames = fontPlayerGames.render("Player Games: " + str(player_games), True, (255, 255, 255))
        screen.blit(screen_text_playergames, (400, 50))

        pygame.display.flip()

    pygame.quit()

main()