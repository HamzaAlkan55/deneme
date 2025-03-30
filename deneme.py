import pygame

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Başlık
pygame.display.set_caption("Basit Oyun Penceresi")

# Renkler
WHITE = (255, 255, 255)

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # Arka planı beyaz yap
    pygame.display.flip()  # Ekranı güncelle

pygame.quit()
