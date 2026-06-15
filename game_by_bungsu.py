import pygame
import random

# 1. Inisialisasi Pygame
pygame.init()

# Konfigurasi Layar
LEBAR, TINGGI = 600, 600 
screen = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("game hindar objek")


# Load gambar
mobil_img = pygame.image.load("mobil.png")
tong_img = pygame.image.load("tong.png")
jalan_img = pygame.image.load("jalan.png")

# Ubah ukuran
mobil_img = pygame.transform.scale(mobil_img, (60, 60))
tong_img = pygame.transform.scale(tong_img, (60, 60))
jalan_img = pygame.transform.scale(jalan_img, (400, 700))


jalan_list = [
    pygame.image.load("jalan.png"),
    pygame.image.load("jalan2.png")
]

for i in range(len(jalan_list)):
    jalan_list[i] = pygame.transform.scale(jalan_list[i], (LEBAR, TINGGI))

# Warna
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)  
BLACK = (20, 20, 20)

clock = pygame.time.Clock()
FPS = 60

# 3. Variabel Player (Hanya P1)
p_size = 50
p1_x = LEBAR // 2 - p_size // 2
p1_y = TINGGI - 70
speed = 7

# 4. Variabel Musuh
enemy_speed = 5
enemy_list = []
spawn_timer = 0

score = 0
font = pygame.font.SysFont("Arial", 35)
font_big = pygame.font.SysFont("Arial", 70, bold=True)

def draw_text(text, font_type, color, x, y):
    img = font_type.render(text, True, color)
    text_rect = img.get_rect(center=(x, y))
    screen.blit(img, text_rect)


bg1 = 0
bg2 = -TINGGI

gambar_atas = 0
gambar_bawah = 1

bg_speed = 5


# 5. Game Loop Utama
running = True
while running:
    screen.blit(jalan_list[gambar_atas], (0, bg1))
    screen.blit(jalan_list[gambar_bawah], (0, bg2))

    bg1 += bg_speed
    bg2 += bg_speed

    if bg1 >= TINGGI:
       bg1 = -TINGGI
       gambar_atas = (gambar_bawah + 1) % len(jalan_list)

    if bg2 >= TINGGI:
       bg2 = -TINGGI
       gambar_bawah = (gambar_atas + 1) % len(jalan_list)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    # Kontrol Player (Hanya Panah Kiri & Kanan)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and p1_x > 0: 
        p1_x -= speed
    if keys[pygame.K_RIGHT] and p1_x < LEBAR - p_size: 
        p1_x += speed

    p1_rect = pygame.Rect(p1_x, p1_y, p_size, p_size)

    # Logika Musuh
    spawn_timer += 1
    if spawn_timer > 30:
        ex = random.randint(0, LEBAR - 50)
        enemy_list.append(pygame.Rect(ex, -50, 50, 50))
        spawn_timer = 0

    for enemy in enemy_list[:]:
        enemy.y += enemy_speed
        if enemy.y > TINGGI:
            enemy_list.remove(enemy)
            score += 1
            if score % 10 == 0: 
                enemy_speed += 0.3

        # Cek Tabrakan
        if p1_rect.colliderect(enemy):
            screen.fill(BLACK)
            draw_text("KELARR", font_big, RED, LEBAR // 2, TINGGI // 2 - 50)
            draw_text(f"Final Score: {score}", font, WHITE, LEBAR // 2, TINGGI // 2 + 30)
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False

    # 6. Gambar Objek
    screen.blit(mobil_img, (p1_x, p1_y))# Gambar Player
    
    for enemy in enemy_list:
        for enemy in enemy_list:
            screen.blit(tong_img, (enemy.x, enemy.y))# Gambar Musuh

    # Gambar Skor
    score_img = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_img, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
