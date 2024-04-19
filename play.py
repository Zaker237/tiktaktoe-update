import pygame
from tiktaktoe import TiktaktowGame
pygame.init()
pygame.mixer.init()
pygame.font.init()


# create tik tak toe board

# create the screen

screen = pygame.display.set_mode((600, 600))

# title and icon

pygame.display.set_caption("Tik Tak Toe")

# load the image

#icon = pygame.image.load("tik-tak-toe.png")

# set the icon

#pygame.display.set_icon(icon)

# create the board
game = TiktaktowGame(
    player1_simbol="X",
    player2_simbol="O"
)
# create the winning combinations
font = pygame.font.Font(None, 32)
# create the game over text
game_over_text = font.render("Game Over", True, (255, 255, 255))
# create the game over text rect
game_over_text_rect = game_over_text.get_rect(center=(300, 300))
# create the game over flag
game_over = False
# create the game loop
running = True
while running:
    # fill the screen
    screen.fill((0, 0, 0))
    # draw the board
    for i in range(1, 3):
        pygame.draw.line(screen, (255, 255, 255), (200 * i, 0), (200 * i, 600), 5)
        pygame.draw.line(screen, (255, 255, 255), (0, 200 * i), (600, 200 * i), 5)
    # draw the x and o
    for i in range(9):
        x = i % 3 * 200
        y = i // 3 * 200
        if game.board[i] == game.player1_simbol:
            pygame.draw.line(screen, (255, 255, 255), (x + 50, y + 50), (x + 150, y + 150), 5)
            pygame.draw.line(screen, (255, 255, 255), (x + 150, y + 50), (x + 50, y + 150), 5)
        elif game.board[i] == game.player2_simbol:
            pygame.draw.circle(screen, (255, 255, 255), (x + 100, y + 100), 50, 5)
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            i = x // 200 + (y // 200) * 3
            game.play(i)
    # draw the game over text
    if game.is_game_over:
        screen.blit(game_over_text, game_over_text_rect)
    # update the display
    pygame.display.flip()

# quit the game
pygame.quit()