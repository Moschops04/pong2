import pygame

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 1940, 1160  # Resolução 4K
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Criação da tela
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong 4K")

# Configurações das raquetes e bola
raquete_largura, raquete_altura = 40, 200
bola_tamanho = 40

# Posições iniciais
raquete_esquerda = pygame.Rect(50, HEIGHT//2 - raquete_altura//2, raquete_largura, raquete_altura)
raquete_direita = pygame.Rect(WIDTH - 90, HEIGHT//2 - raquete_altura//2, raquete_largura, raquete_altura)
bola = pygame.Rect(WIDTH//2 - bola_tamanho//2, HEIGHT//2 - bola_tamanho//2, bola_tamanho, bola_tamanho)

# Velocidades
raquete_velocidade = 10
bola_velocidade_x, bola_velocidade_y = 10, 10

aio_velocidade = 10  # Velocidade da IA

# Loop principal
ejecutando = True
clock = pygame.time.Clock()

while ejecutando:
    tela.fill(BLACK)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    
    # Movimentação das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete_esquerda.top > 0:
        raquete_esquerda.y -= raquete_velocidade
    if keys[pygame.K_s] and raquete_esquerda.bottom < HEIGHT:
        raquete_esquerda.y += raquete_velocidade
    
    # IA da raquete direita
    if raquete_direita.centery < bola.centery:
        raquete_direita.y += aio_velocidade
    elif raquete_direita.centery > bola.centery:
        raquete_direita.y -= aio_velocidade
    
    # Movimento da bola
    bola.x += bola_velocidade_x
    bola.y += bola_velocidade_y
    
    # Colisões com o topo e base
    if bola.top <= 0 or bola.bottom >= HEIGHT:
        bola_velocidade_y *= -1
    
    # Colisões com as raquetes
    if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
        bola_velocidade_x *= -1
    
    # Reiniciar bola se sair da tela
    if bola.left <= 0 or bola.right >= WIDTH:
        bola.x, bola.y = WIDTH//2 - bola_tamanho//2, HEIGHT//2 - bola_tamanho//2
        bola_velocidade_x *= -1
    
    # Desenha os elementos
    pygame.draw.rect(tela, WHITE, raquete_esquerda)
    pygame.draw.rect(tela, WHITE, raquete_direita)
    pygame.draw.ellipse(tela, WHITE, bola)
    pygame.draw.aaline(tela, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    
    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
