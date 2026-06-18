import pygame
from math import floor, ceil

pygame.init()


class App:
	def __init__(self, window_size, fps=75):
		self.window_size = window_size
		self.window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
		self.screen = pygame.Surface((window_size[0]//2, window_size[1]//2))

		pygame.display.set_caption("WorldSim")
		pygame.display.set_icon(pygame.Surface((16, 16)))

		self.clock = pygame.time.Clock()
		self.fps = fps

		self.running = False

	def run(self):
		self.running = True
		while self.running:
			self.clock.tick(self.fps)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				elif event.type == pygame.VIDEORESIZE:
					self.window_size = event.size
					self.screen = pygame.Surface((ceil(event.w/2), ceil(event.h/2)))


			self.screen.fill((120, 120, 120))
			pygame.draw.rect(self.screen, (180, 180, 180), (10, 10, 50, 50))

			self.window.blit(pygame.transform.scale_by(self.screen, 2), (0, 0))
			pygame.display.flip()

		pygame.quit()


if __name__ == "__main__":
	app = App(window_size=(1200, 800))
	app.run()