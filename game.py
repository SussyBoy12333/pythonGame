import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 60
SIZE = WIDTH, HEIGHT = 700, 600
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
class PlayerOne():
	def __init__(self):
		self.hearth = 3
		self.img = pygame.Surface((50, 80))
		self.img.fill((255, 0, 0))
		self.bullet_list = []
		self.vel = 3
		self.x = 0
		self.y = 0 
		self.bullvel = 7
		self.font = pygame.font.SysFont('operator mono', 18)
	def draw(self):
		screen.blit(self.img, (self.x, self.y))
		self.blitHearth()
	def blitHearth(self):
		self.hearthSurf = self.font.render(f'{self.hearth}', True, (0, 0, 0))
		self.img.blit(self.hearthSurf, (1, 1))
	def move(self):
		if self.x < 0: self.x = 0
		if self.x + 50 > WIDTH: self.x = WIDTH - 50
		if self.y < 0: self.y = 0
		if self.y + 80 > HEIGHT: self.y = HEIGHT - 80
	def shoot(self):
		bullet_object = []
		bullet = pygame.Surface((10, 10))
		bullet.fill((0, 0, 0))
		bullet_object.append(bullet)
		bullet_object.append(self.x)
		bullet_object.append(self.y)
		self.bullet_list.append(bullet_object)
	def showBullet(self, player):
		for bul in self.bullet_list:
			if bul != None:
				bul[1] += self.bullvel
				rect = [player.x, player.y, player.img.get_width(), player.img.get_height()]
				bul_rect = [bul[1], bul[2], 10, 10]
				if self.bulletCollision(rect, bul_rect) == True and not(bul == None):
					self.bullet_list[self.bullet_list.index(bul)] = None
					player.hearth -= 1
			if bul != None:
				screen.blit(bul[0], (bul[1], bul[2]))
	def bulletCollision(self, rect, bul_rect):
		if rect[0] <= bul_rect[0]+bul_rect[2] and bul_rect[0] <= rect[0]+rect[2] and rect[1] <= bul_rect[1]+bul_rect[3] and bul_rect[1] <= rect[1]+rect[3]:
			return True
		return False

class PlayerTwo():
	def __init__(self):
		self.hearth = 3
		self.img = pygame.Surface((50, 80))
		self.img.fill((0, 0, 255))
		self.bullet_list = []
		self.vel = 3
		self.x = WIDTH - 50
		self.y = 0
		self.font = pygame.font.SysFont('operator mono', 18)
		self.bullvel = 7
	def draw(self):
		screen.blit(self.img, (self.x, self.y))
		self.img.blit(self.blitHearth(), (1,1))
	def blitHearth(self):
		self.hearthSurf = self.font.render(f'{self.hearth}', True, (255, 255, 255))
		return self.hearthSurf
	def move(self):
		if self.x < 0: self.x = 0
		if self.x + 50 > WIDTH: self.x = WIDTH - 50
		if self.y < 0: self.y = 0
		if self.y + 80 > HEIGHT: self.y = HEIGHT - 80
	def shoot(self):
		bullet_object = []
		bullet = pygame.Surface((10, 10))
		bullet.fill((255, 255, 0))
		bullet_object.append(bullet)
		bullet_object.append(self.x)
		bullet_object.append(self.y)
		self.bullet_list.append(bullet_object)
	def showBullet(self, player):
		for bul in self.bullet_list:
			if bul != None:
				bul[1] -= self.bullvel
				rect = [player.x, player.y, player.img.get_width(), player.img.get_height()]
				bul_rect = [bul[1], bul[2], 10, 10]
				if self.bulletCollision(rect, bul_rect) == True and not(bul == None):
					self.bullet_list[self.bullet_list.index(bul)] = None
					player.hearth -= 1
			if bul != None:
				screen.blit(bul[0], (bul[1], bul[2]))
	def bulletCollision(self, rect, bul_rect):
		if rect[0] <= bul_rect[0]+bul_rect[2] and bul_rect[0] <= rect[0]+rect[2] and rect[1] <= bul_rect[1]+bul_rect[3] and bul_rect[1] <= rect[1]+rect[3]:
			return True
		return False

player1 = PlayerOne()
p1 = {
	"left": False,
	"right": False,
	"up": False,
	"down": False
}
player2 = PlayerTwo()
p2 = {
    "left": False,
    "right": False,
    "up": False,
    "down": False
}
run = True
while True:
	player1_rect = [player1.x, player1.y, player1.img.get_width(), player1.img.get_height()]
	player2_rect = [player2.x, player2.y, player2.img.get_width(), player2.img.get_height()]
	screen.fill((255, 255, 255)); 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				p1['up'] = True
			if event.key == pygame.K_DOWN:
				p1['down'] = True
			if event.key == pygame.K_LEFT:
				p1['left'] = True
			if event.key == pygame.K_RIGHT: 
				p1['right'] = True
			if event.key == pygame.K_c:
				player1.shoot()
			if event.key == pygame.K_w:
				p2['up'] = True
			if event.key == pygame.K_s:
				p2['down'] = True
			if event.key == pygame.K_a:
				p2['left'] = True
			if event.key == pygame.K_d:
				p2['right'] = True
			if event.key == pygame.K_m:
				player2.shoot()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				p1['up'] = False
			if event.key == pygame.K_DOWN:
				p1['down'] = False
			if event.key == pygame.K_LEFT:
				p1['left'] = False
			if event.key == pygame.K_RIGHT:
				p1['right'] = False
			if event.key == pygame.K_w:
				p2['up'] = False
			if event.key == pygame.K_s:
				p2['down'] = False
			if event.key == pygame.K_a:
				p2['left'] = False
			if event.key == pygame.K_d:
				p2['right'] = False

	if p1['up'] == True: player1.y -= player1.vel
	if p1['down'] == True: player1.y += player1.vel
	if p1['left'] == True: player1.x -= player1.vel
	if p1['right'] == True: player1.x += player1.vel
 
	if p2['up'] == True: player2.y -= player2.vel
	if p2['down'] == True: player2.y += player2.vel
	if p2['left'] == True: player2.x -= player2.vel
	if p2['right'] == True: player2.x += player2.vel
	player1.showBullet(player2)
	player2.showBullet(player1)
	player1.draw()
	player2.draw(); 
	player1.move(); 
	player2.move()
	if player1.hearth == 0 or player2.hearth == 0:
		run = False
	pygame.display.update()
	fpsClock.tick(FPS)