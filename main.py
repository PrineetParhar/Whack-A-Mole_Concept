import pygame
import os
import time
import random
import sys
pygame.font.init()

# for next time:

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole Concept")

# Load images

sadFace = pygame.image.load(os.path.join("assets", "EnemyFace.png"))  # enemy class
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "LightBlueBackground.png")), (WIDTH, HEIGHT)) # background
Practice = pygame.transform.scale(pygame.image.load(os.path.join("assets", "practice.png")), (WIDTH, HEIGHT))

class Person():

	dis = 100

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.person_img = None
		self.coolDownCounter = 0

	def draw(self, window):
		window.blit(self.person_img, (self.x, self.y))

	def Dissapear(self):
		if self.coolDownCounter >= self.dis:
			self.coolDownCounter = 0
		elif self.coolDownCounter > 0:
			self.coolDownCounter += 1

	def getWidth(self):
		return int(self.person_img.get_width())

	def getHeight(self):
		return int(self.person_img.get_height())

	def getX(self):
		return int(self.x)

	def getY(self):
		return int(self.y)

class Enemy(Person):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.person_img = sadFace
		self.mask = pygame.mask.from_surface(self.person_img)

	def draw(self, window):
		super().draw(window)

	def getWidth(self):
		return super().getWidth()

	def getHeight(self):
		return super().getHeight()

	def getX(self):
		return super().getX()

	def getY(self):
		return super().getY()			

def main():
	run = True
	fps = 60
	lives = 5
	mainFont = pygame.font.SysFont("timesnewroman", 50)
	clock = pygame.time.Clock()
	oldtime = time.time()
	enemiesKilled = 0
	level = 0

	enemies = []

	numEnemiesOnScreen = 0
	
	def redrawWindow():
		WIN.blit(bg, (0, 0))
		#draw text
		livesLabel = mainFont.render(f"Lives: {lives}", 1, (255, 255, 255))
		levelLabel = mainFont.render(f"Level: {level}", 1, (255, 255, 255))

		WIN.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))

		for enemy in enemies:
			enemy.draw(WIN)

		pygame.display.update()

	# end of redraw window function

	while run:
		clock.tick(fps)
		redrawWindow()

		if time.time() - oldtime > 30:
			print(f"Final Score: {level}")
			print(f"Final Number of Enemies Killed: {enemiesKilled}")
			time.sleep(2)
			run = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				a, b = event.pos
				for i in enemies:
					if a >= int(i.getX()) and a <= int(i.getX()) + int(i.getWidth()) and b >= int(i.getY()) and b <= int(i.getY()) + int(i.getHeight()):
						enemies.remove(i)
						enemiesKilled += 1
						break


		if len(enemies) == 0:
			level += 1
			numEnemiesOnScreen += 3
			for i in range(numEnemiesOnScreen):
				bg1 =  Enemy(random.randrange(50, WIDTH - 50), random.randrange(50, HEIGHT - 50))
				enemies.append(bg1)


main()