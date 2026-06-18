import pygame
from math import floor, ceil

pygame.init()


class Camera:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @property
    def pos(self):
        return (self.x, self.y)


class App:
    def __init__(self, window_size, fps=100):
        self.window_size = window_size
        self.scale = 1
        self.window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        self.screen = pygame.Surface((window_size[0]//self.scale, window_size[1]//self.scale))

        pygame.display.set_caption("WorldSim")
        pygame.display.set_icon(pygame.Surface((16, 16)))

        self.clock = pygame.time.Clock()
        self.fps = fps

        self.camera = Camera(0.0, 0.0)

        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


                elif event.type == pygame.VIDEORESIZE:
                    old_center_x = self.screen.get_width() / 2
                    old_center_y = self.screen.get_height() / 2
                    self.window_size = event.size


                    new_w = ceil(event.w / self.scale)
                    new_h = ceil(event.h / self.scale)
                    self.screen = pygame.Surface((new_w, new_h))

                    new_center_x = new_w / 2
                    new_center_y = new_h / 2

                    self.camera.x -= (new_center_x - old_center_x)
                    self.camera.y -= (new_center_y - old_center_y)


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in (4, 5):
                        mouse_window_x, mouse_window_y = event.pos

                        mouse_old_screen_x = mouse_window_x / self.scale
                        mouse_old_screen_y = mouse_window_y / self.scale
                        
                        if event.button == 4:
                            self.scale *= 2
                        elif event.button == 5:
                            self.scale /= 2
                        
                        self.scale = min(max(1, self.scale), 4)

                        new_w = ceil(self.window_size[0] / self.scale)
                        new_h = ceil(self.window_size[1] / self.scale)

                        self.screen = pygame.Surface((new_w, new_h))

                        mouse_new_screen_x = mouse_window_x / self.scale
                        mouse_new_screen_y = mouse_window_y / self.scale

                        self.camera.x -= (mouse_new_screen_x - mouse_old_screen_x)
                        self.camera.y -= (mouse_new_screen_y - mouse_old_screen_y)
                        
                        pygame.mouse.get_rel()


            mouse_buttons = pygame.mouse.get_pressed()
            mouse_rel = pygame.mouse.get_rel()

            if mouse_buttons[0]:  
                self.camera.x -= mouse_rel[0] / self.scale
                self.camera.y -= mouse_rel[1] / self.scale


            self.screen.fill((120, 120, 120))
            pygame.draw.rect(self.screen, (180, 180, 180), (10 - self.camera.x, 10 - self.camera.y, 16, 16))

            self.window.blit(pygame.transform.scale_by(self.screen, self.scale), (0, 0))
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    app = App(window_size=(1200, 800))
    app.run()