import pygame
import sys
import math
import random

pygame.init()

# Dimensiones de la ventana
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aproximación de π - Método Monte Carlo")

# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Parámetros del círculo inscrito en el cuadrado
center = (width // 2, height // 2)
radius = width // 2

# Variables para el cálculo
inside_points = 0
total_points = 0

# Fuentes para textos y botones
font = pygame.font.SysFont("Arial", 24)
button_font = pygame.font.SysFont("Arial", 20)

# Definición de botones
start_pause_button_rect = pygame.Rect(10, height - 50, 120, 40)
reset_button_rect = pygame.Rect(140, height - 50, 120, 40)

simulation_running = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if start_pause_button_rect.collidepoint(mouse_pos):
                simulation_running = not simulation_running
            elif reset_button_rect.collidepoint(mouse_pos):
                simulation_running = False
                inside_points = 0
                total_points = 0

    # Fondo blanco y dibujo del círculo
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, center, radius, 2)
    
    # Actualizar simulación solo si está en ejecución
    if simulation_running:
        # Generar 10 puntos por iteración para una animación más lenta
        for _ in range(10):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            total_points += 1
            # Comprobar si el punto cae dentro del círculo
            if math.hypot(x - center[0], y - center[1]) <= radius:
                inside_points += 1
                color = BLUE
            else:
                color = RED
            pygame.draw.circle(screen, color, (int(x), int(y)), 2)
    
    # Calcular la aproximación de π
    pi_estimate = 4 * inside_points / total_points if total_points > 0 else 0
    pi_text = font.render(f"π ≈ {pi_estimate:.6f}", True, BLACK)
    screen.blit(pi_text, (10, 10))

    # Dibujar botón de Iniciar/Pausar
    pygame.draw.rect(screen, GRAY, start_pause_button_rect)
    start_text = "Pausar" if simulation_running else "Iniciar"
    text_surface = button_font.render(start_text, True, BLACK)
    text_rect = text_surface.get_rect(center=start_pause_button_rect.center)
    screen.blit(text_surface, text_rect)
    
    # Dibujar botón de Reiniciar
    pygame.draw.rect(screen, GRAY, reset_button_rect)
    reset_text = button_font.render("Reiniciar", True, BLACK)
    reset_rect = reset_text.get_rect(center=reset_button_rect.center)
    screen.blit(reset_text, reset_rect)
    
    pygame.display.flip()
    clock.tick(15)  # 15 FPS para una animación más lenta
