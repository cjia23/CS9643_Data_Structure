from Maze import *
import pygame
import time

class App:
    
    def __init__(self, maze,name="aMaze"):
        self._running = True
        self._display_surf = None
        self._surfs = {}
        self._name = name
        
        self.maze = Maze(maze)
        self.windowHeight = len(maze) * 40
        self.windowWidth = len(maze[0]) * 40
        
        self.on_execute()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,
                                        self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption(self._name)
        
        self._running = True
        self._surfs['p'] = pygame.image.load('./images/curpath.png').convert()
        self._surfs['c'] = pygame.image.load('./images/current.png').convert()
        self._surfs['m'] = pygame.image.load('./images/empty.png').convert()
        self._surfs['E'] = pygame.image.load('./images/end.png').convert()
        self._surfs['f'] = pygame.image.load('./images/endFound.png').convert()
        self._surfs['x'] = pygame.image.load('./images/expath.png').convert()
        self._surfs[' '] = pygame.image.load('./images/open.png').convert()
        self._surfs['S'] = pygame.image.load('./images/start.png').convert()
        self._surfs['#'] = pygame.image.load('./images/wall.png').convert()	

    def on_loop(self):
        pass

    def on_render(self):
        pygame.event.get()
        self._display_surf.fill((0,0,0))
        self.maze.draw(self._display_surf, self._surfs)
        pygame.display.flip()

    def on_cleanup(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    pygame.display.quit()
                    pygame.quit()
                    self._running = False

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        self.on_render()
        self._running = True
    
    def pause_for_key(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pause = False




