import pygame
import random

pygame.init()

width, height = (500, 450)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the ball")

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (40, 40))

running = True
circle_x = random.randint(0, width - 40)
circle_y = 0
circle_r = 20  # half of ball width

rect_w = 120
rect_h = 35
rect_x = random.randint(0, width - rect_w)
rect_y = height - rect_h

score = 0
missed = 0

while running:
    keys = pygame.key.get_pressed()
    pygame.time.delay(26)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_LEFT]:
        rect_x = max(0, rect_x - 10)
    if keys[pygame.K_RIGHT]:
        rect_x = min(width - rect_w, rect_x + 10)

    # Ball falling
    circle_y += 5

    # Check collision
    if rect_y <= circle_y + circle_r <= rect_y + rect_h and rect_x <= circle_x <= rect_x + rect_w:
        score += 1
        circle_x = random.randint(0, width - 40)
        circle_y = 0

    # Missed ball
    if circle_y + circle_r >= height:
        missed += 1
        circle_x = random.randint(0, width - 40)
        circle_y = 0

    screen.fill((255, 255, 255))
    screen.blit(ball, (circle_x, circle_y))
    pygame.draw.rect(screen, (0, 0, 255), (rect_x, rect_y, rect_w, rect_h))
    pygame.display.update()

print("Your score:", score)
print("You missed:", missed)
pygame.quit()
