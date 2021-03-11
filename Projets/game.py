import pygame

pygame.init()

window_resolution = (640,480)
blue_color = (89,152,255)
black_color = (0,0,0)

pygame.display.set_caption("mon jeu")

window_surface = pygame.display.set_mode(window_resolution)
window_surface.fill(blue_color)

pygame.draw.line(window_surface, black_color, [10,10], [100,100])

pygame.display.flip()

launcher = True
while launcher :
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			launcher = False

