import pygame
import os

file = open(f"frames/frames.txt", "w")
file.write("")
file.close()
file = open(f"frames/frames.txt", "a", encoding='utf8')
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
screen = pygame.display.set_mode((482, 362))
running = True
num = 0


while running:
    print(num)
    num += 1
    if num == 2192:
        file.close()
        pygame.quit()
        exit()
        num = 0
    background_image = pygame.image.load(f"frames/frame{num}.png").convert()
    file.write(str(num))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, (0, 0))
    x = 0
    y = 0


    def area(xstart, ystart):
        x = xstart
        y = ystart
        result = []
        for i in range(10):
            for l in range(10):
                x += 1
                get = screen.get_at((int(x), int(y)))
                li = list(get)
                result.append(li[0])
            x = xstart
            y += 1
        return sum(result) / len(result)


    for l in range(36):
        x = 0
        file.write(f"\n")
        for i in range(48):
            pixel = area(x, y)
            if pixel >= 0 and pixel <= 38:
                file.write("⬛")
            elif pixel >= 38 and pixel <= 74:
                file.write("🖤")
            elif pixel >= 74 and pixel <= 110:
                file.write("⚫")
            elif pixel >= 110 and pixel <= 146:
                file.write("🔳")
            elif pixel >= 146 and pixel <= 182:
                file.write("⚪")
            elif pixel >= 182 and pixel <= 218:
                file.write("🤍")
            elif pixel >= 218 and pixel <= 255:
                file.write("⬜")

            x += 10
        y += 10
    file.write("\nMade by: timnoot#4372 | inspired by: Lamp | Code: https://bit.ly/2Q6VjIW")
    file.write("\n")


