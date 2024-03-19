import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
WIDTH, HEIGHT = 800, 600
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Dimensions du terrain de football
FIELD_WIDTH, FIELD_HEIGHT = 600, 400
FIELD_OFFSET_X, FIELD_OFFSET_Y = (WIDTH - FIELD_WIDTH) // 2, (HEIGHT - FIELD_HEIGHT) // 2
# Dimensions du but
GOAL_WIDTH = 100
GOAL_HEIGHT = 240

# Création de la fenêtre
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de football")

# Position initiale des joueurs et du ballon
player1_x, player1_y = 50, HEIGHT // 2
player2_x, player2_y = WIDTH - 100, HEIGHT // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
# Taille des joueurs et du ballon
player_size = 20
ball_size = 20
# Vitesse de déplacement
player_vel = 5
ball_vel = [4, 4]  # Vitesse initiale du ballon

# Fonction pour dessiner les joueurs
def draw_players():
    pygame.draw.rect(win, WHITE, (player1_x, player1_y, player_size, player_size))
    pygame.draw.rect(win, WHITE, (player2_x, player2_y, player_size, player_size))

# Fonction pour dessiner le ballon
def draw_ball():
    pygame.draw.circle(win, WHITE, (int(ball_x), int(ball_y)), ball_size)

# Fonction pour dessiner le terrain de football
def draw_field():
    pygame.draw.rect(win, GREEN, (FIELD_OFFSET_X, FIELD_OFFSET_Y, FIELD_WIDTH, FIELD_HEIGHT), 2)
    pygame.draw.rect(win, WHITE, (FIELD_OFFSET_X - 10, FIELD_OFFSET_Y + (FIELD_HEIGHT - GOAL_HEIGHT) // 2, 10, GOAL_HEIGHT), 2)
    pygame.draw.rect(win, WHITE, (FIELD_OFFSET_X + FIELD_WIDTH, FIELD_OFFSET_Y + (FIELD_HEIGHT - GOAL_HEIGHT) // 2, 10, GOAL_HEIGHT), 2)

# Vérifier la collision entre les joueurs et le ballon
def check_collision():
    global ball_vel
    player1_rect = pygame.Rect(player1_x, player1_y, player_size, player_size)
    player2_rect = pygame.Rect(player2_x, player2_y, player_size, player_size)
    ball_rect = pygame.Rect(ball_x - ball_size, ball_y - ball_size, ball_size * 2, ball_size * 2)
    if player1_rect.colliderect(ball_rect) or player2_rect.colliderect(ball_rect):
        # Inverser la vélocité du ballon en cas de collision avec un joueur
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement des joueurs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        if player1_y > FIELD_OFFSET_Y:
            player1_y -= player_vel
    if keys[pygame.K_s]:
        if player1_y < FIELD_OFFSET_Y + FIELD_HEIGHT - player_size:
            player1_y += player_vel
    if keys[pygame.K_q]:
        if player1_x > FIELD_OFFSET_X:
            player1_x -= player_vel
    if keys[pygame.K_d]:
        if player1_x < FIELD_OFFSET_X + FIELD_WIDTH - player_size:
            player1_x += player_vel
    if keys[pygame.K_UP]:
        if player2_y > FIELD_OFFSET_Y:
            player2_y -= player_vel
    if keys[pygame.K_DOWN]:
        if player2_y < FIELD_OFFSET_Y + FIELD_HEIGHT - player_size:
            player2_y += player_vel
    if keys[pygame.K_LEFT]:
        if player2_x > FIELD_OFFSET_X:
            player2_x -= player_vel
    if keys[pygame.K_RIGHT]:
        if player2_x < FIELD_OFFSET_X + FIELD_WIDTH - player_size:
            player2_x += player_vel

    # Mouvement du ballon
    ball_x += ball_vel[0]
    ball_y += ball_vel[1]

    # Vérifier la collision entre les joueurs et le ballon
    check_collision()

    # Rebondir sur les bords horizontaux
    if ball_x < FIELD_OFFSET_X or ball_x > FIELD_OFFSET_X + FIELD_WIDTH:
        ball_vel[0] = -ball_vel[0]
    # Rebondir sur les bords verticaux
    if ball_y < FIELD_OFFSET_Y or ball_y > FIELD_OFFSET_Y + FIELD_HEIGHT:
        ball_vel[1] = -ball_vel[1]

    # Effacer l'écran
    win.fill(BLACK)
    
    # Dessiner le terrain de football
    draw_field()
    # Dessiner les joueurs
    draw_players()
    # Dessiner le ballon
    draw_ball()

    # Mettre à jour l'affichage
    pygame.display.update()

    # Limiter le nombre d'images par seconde
    pygame.time.Clock().tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()
