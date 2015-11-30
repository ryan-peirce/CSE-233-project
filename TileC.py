import pygame, func

#a class to create and modify tiles for a tile map
class Tile(pygame.Rect):

	List = []
	SolidList = []
	width, height = 40, 40
	total_tiles = 1
	H,V = 1, 26

	def __init__(self, x, y, Type,):

		self.type = Type
		self.number = Tile.total_tiles
		Tile.total_tiles += 1
		self.walkable = True
		self.top = y
		self.bottom = y + 40
		self.left = x
		self.right = x + 40

                #checks type to decide if it can be walked through
		if Type == 'empty':
			self.walkable = True
		else:
			self.walkable = False
			Tile.SolidList.append(self)
			self.image = pygame.image.load("img/tile.jpg")
			
		pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

		self.rect = (x, y , Tile.width, Tile.height)
		Tile.List.append(self)
                        
        #returns tile at a number
	@staticmethod
	def get_tile(number):
		for tile in Tile.List:
			if tile.number == number:
				return tile

        #emptys all tile lists
	@staticmethod
	def empty_tiles():
                for tile in Tile.List:
                        Tile.List.remove(tile)
                for tile in Tile.SolidList:
                        Tile.SolidList.remove(tile)
                total_tiles = 1

        #draws current tiles
	@staticmethod
	def draw_tiles(screen):
		for tile in Tile.List:

			if not(tile.type == 'empty'):
				screen.blit(tile.image, (tile.x,tile.y))
			#func.text_to_screen(screen, tile.number, tile.x, tile.y)

        #returns tile at an x,y position
	@staticmethod
	def get_tile_at(x,y):
                for tile in Tile.List:
                        if tile.left <= x and tile.right >= x and tile.top <= y and tile.bottom >= y:
                                return tile

