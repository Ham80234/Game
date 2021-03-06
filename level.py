import pygame 
from tiles import Tile
from Settings import *
from Player import Player

class Level:
    def __init__(self, level_data, surface): 
        #Tiles Surface 
        self.display_surface= surface
        self.setup_level(level_data)
        #Value the world shifts by
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout): 
            for col_index, cell in enumerate(row): 
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if cell == 'X': 
                    tile = Tile((x,y),TILE_SIZE) 
                    self.tiles.add(tile)
                if cell == 'P': 
                    player = Player((x,y)) 
                    self.player.add(player)

    def run(self): 
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)