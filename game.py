import pygame
import random
from pygame.locals import *
from pygame.sprite import Sprite

class Personaje(Sprite):
	def __init__(self):
		self.image = personaje = pygame.image.load("Imagenes/goku.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(500, 1000)
		self.muerto = 0
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_SPACE]:
			self.image = personaje = pygame.image.load("Imagenes/gokukamehameha.png").convert_alpha()
		elif kamehameha.rect.x > 860:
			self.image = personaje = pygame.image.load("Imagenes/goku.png").convert_alpha()

		if teclas[K_LEFT]:
			self.image = personaje = pygame.image.load("Imagenes/gokuleft.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 10
		elif teclas[K_RIGHT]:
			self.image = personaje = pygame.image.load("Imagenes/gokuright.png").convert_alpha()
			if self.rect.x < 1400:
				self.rect.x += 10

		if teclas[K_UP]:
			self.image = personaje = pygame.image.load("Imagenes/gokuup.png").convert_alpha()
			if self.rect.y > 32:
				self.rect.y -= 10
		elif teclas[K_DOWN]:
			if self.rect.y < 530:
				self.image = personaje = pygame.image.load("Imagenes/gokudown.png").convert_alpha()
				self.rect.y += 10

class Kamehameha(Sprite):
        	def __init__(self):
		self.image = kamehameha = pygame.image.load("Imagenes/kamehameha.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(1400, 1400)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x > 1350: # distancia final de mi kamehameha
			if teclas[K_SPACE]:
				self.rect.x = (personaje.rect.x + 60) #distancia en x esfera
				self.rect.y = (personaje.rect.y + 14) #distancia en y esfera
		if self.rect.x < 1400: # distancia hasta donde llega 1400 pixeles
			self.rect.x += 20

class Barravidagoku(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("Imagenes/barravidagoku.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(6, 14)
	def update(self):
		if barravidagoku.rect.x <= -170:
			personaje.muerto = 1
		if disparo.rect.y >= (personaje.rect.y - 56):
			if disparo.rect.y <= (personaje.rect.y + 62):
				if disparo.rect.x >= personaje.rect.x:
					if disparo.rect.x <= (personaje.rect.x + 43):
						barravidagoku.rect.x -= 26
						disparo.rect.x = -400
		if mini.rect.y >= (personaje.rect.y - 56):
			if mini.rect.y <= (personaje.rect.y + 62):
				if mini.rect.x >= personaje.rect.x:
					if mini.rect.x <= (personaje.rect.x + 43):
						barravidagoku.rect.x -= 26
						disparo.rect.x = -400

class Mini(Sprite):
	def __init__(self):
		self.image = mini = pygame.image.load("Imagenes/mini.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(1100, 300) #(x,y) distacia objeto.
		self.bandera = 0
		self.muerto = 0
	def update(self):
		if self.rect.y == 40:
			self.bandera = 0
		elif self.rect.y == 540:
			self.bandera = 1

		if self.bandera == 0:
			self.rect.y += 10
		elif self.bandera == 1:
			self.rect.y -= 10
	def dificil(self):
		if self.rect.x < 0:
			self.rect.x = 800
		if self.rect.y > 600:
			self.rect.y = 0
		self.rect.x -= 10
		self.rect.y += 10

class Disparo(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("Imagenes/camecame.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip( -400, -400)
	def update(self):
		if self.rect.x == -400:
			if mini.rect.y == personaje.rect.y:
				self.rect.x = (mini.rect.x - 60)
				self.rect.y = (mini.rect.y - 14)
		if self.rect.x > -400:
			self.rect.x -= 10 # velocidad de disparo en minibills

class Barravidamini(Sprite):

	def __init__(self):
		self.image = barravidamini = pygame.image.load("Imagenes/barravidamini.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(1181,14)
	def update(self):
		if self.rect.x >= 1871:
			mini.muerto = 1
		if kamehameha.rect.y >= mini.rect.y:
			if kamehameha.rect.y <= (mini.rect.y + 62):
				if kamehameha.rect.x >= mini.rect.x:
					if kamehameha.rect.x <= (mini.rect.x + 43):
						self.rect.x += 6
						kamehameha.rect.x = 900

if __name__ == '__main__':
	# Variables.
	salir = False

	# Establezco la pantalla.
	screen = pygame.display.set_mode((1400,858))

	# Establezco el título.
	pygame.display.set_caption(" Super Sayayin  -  Ing. Informatica de Sistemas")

	# Creo dos objetos surface.
	fondo = pygame.image.load("Imagenes/fondo2.jpg").convert()
	cuadrovidagoku = pygame.image.load("Imagenes/cuadrovidagoku.png").convert_alpha()
	cuadrovidamini = pygame.image.load("Imagenes/cuadrovidamini.png").convert_alpha()
	hasperdido = pygame.image.load("Imagenes/Hasperdido.png").convert()
	hasganado = pygame.image.load("Imagenes/Hasganado.png").convert()
	# .convert() convierten la superficie a un formato de color que permite imprimirlas mucho mas rápido.

	# Objetos
	temporizador = pygame.time.Clock()
	personaje = Personaje()
	kamehameha = Kamehameha()
	mini = Mini()
	disparo = Disparo()
	barravidagoku = Barravidagoku()
	barravidamini = Barravidamini()

	# Movimiento del personaje.
	while not salir:
		personaje.update()
		kamehameha.update()
		if barravidamini.rect.x < 1871:
			mini.update()
		else:
			mini.dificil()
		disparo.update()
		barravidagoku.update()
		barravidamini.update()

		# actualizacion grafica
		screen.blit(fondo, (0, 0))
		screen.blit(personaje.image, personaje.rect)
		screen.blit(kamehameha.image, kamehameha.rect)
		screen.blit(mini.image, mini.rect)
		screen.blit(disparo.image, disparo.rect)
		screen.blit(barravidagoku.image, barravidagoku.rect)
		screen.blit(barravidamini.image, barravidamini.rect)
		screen.blit(cuadrovidagoku, (0,0))
		screen.blit(cuadrovidamini, (1176,0))
		if personaje.muerto == 1:
			screen.blit(hasperdido, (250,264))
		if mini.muerto == 1:
			screen.blit(hasganado, (250,264))
		pygame.display.flip()

		if personaje.muerto == 1:
			pygame.time.delay(3000)
			salir = True
		elif mini.muerto == 1:
			pygame.time.delay(3000)
			salir = True
		temporizador.tick(60)

		# gestion de eventos
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
