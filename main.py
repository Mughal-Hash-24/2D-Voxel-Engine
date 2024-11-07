import pygame

pygame.init()

clock = pygame.time.Clock()

win_res = [1000, 800]

window = pygame.display.set_mode(win_res)
pygame.display.set_caption("Mini Golf")

bg_color = (120, 200, 255)

voxel_size = [20, 20]

stone_img = pygame.image.load("data/images/stone.png")
dirt_img = pygame.image.load("data/images/dirt.png")
grass_img = pygame.image.load("data/images/grass.png")
deep_slate_img = pygame.image.load("data/images/deep_slate.png")
plank_img = pygame.image.load("data/images/plank.png")
log_img = pygame.image.load("data/images/log.png")
wood_stair_img = pygame.image.load("data/images/wood_stair.png")


def generate_voxels():
    vox = []
    rows = 20
    cols = 25
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect([x * 40, y * 40, 40, 40])
            vox.append(rect)

    return vox


def generate_voxel_state():
    v_s = []
    for y in range(20):  # Adjust the range to cover the entire grid
        for x in range(25):  # Adjust the range to cover the entire grid
            if y == 16:
                v_s.append(1)
            elif y > 16:
                v_s.append(2)
            else:
                v_s.append(0)

    return v_s


rotated_images = {
    7: {
        0: wood_stair_img,
        90: pygame.transform.rotate(wood_stair_img, 90),
        180: pygame.transform.rotate(wood_stair_img, 180),
        270: pygame.transform.rotate(wood_stair_img, 270)
    }
}


def game_loop():
    # Initialize facing direction for each voxel
    facings = ["right" for _ in range(500)]  # Assuming 500 voxels, adjust this as needed

    voxels = generate_voxels()
    voxel_states = generate_voxel_state()

    placing_state = 3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                m_r = pygame.Rect([m_x, m_y, 1, 1])
                for i, voxel in enumerate(voxels):
                    if m_r.colliderect(voxel):
                        if event.button == 1:
                            voxel_states[i] = 0
                        elif event.button == 3 and (voxel_states[i] == 0 or voxel_states[i] == 7):
                            voxel_states[i] = placing_state
                            if voxel_states[i] == 7:
                                # Change facing direction for the current voxel
                                if facings[i] == "left":
                                    facings[i] = "down"
                                elif facings[i] == "down":
                                    facings[i] = "right"
                                elif facings[i] == "right":
                                    facings[i] = "up"
                                else:
                                    facings[i] = "left"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    placing_state = 1
                elif event.key == pygame.K_2:
                    placing_state = 2
                elif event.key == pygame.K_3:
                    placing_state = 3
                elif event.key == pygame.K_4:
                    placing_state = 4
                elif event.key == pygame.K_5:
                    placing_state = 5
                elif event.key == pygame.K_6:
                    placing_state = 6
                elif event.key == pygame.K_7:
                    placing_state = 7

        window.fill(bg_color)

        for i, voxel in enumerate(voxels):
            if voxel_states[i] != 0:
                if voxel_states[i] == 7:
                    if facings[i] == "left":
                        window.blit(wood_stair_img, (voxel.x, voxel.y))
                    elif facings[i] == "down":
                        window.blit(rotated_images[7][90], (voxel.x, voxel.y))
                    elif facings[i] == "right":
                        window.blit(rotated_images[7][180], (voxel.x, voxel.y))
                    else:
                        window.blit(rotated_images[7][270], (voxel.x, voxel.y))
                if voxel_states[i] == 6:
                    window.blit(log_img, (voxel.x, voxel.y))
                if voxel_states[i] == 5:
                    window.blit(plank_img, (voxel.x, voxel.y))
                if voxel_states[i] == 4:
                    window.blit(deep_slate_img, (voxel.x, voxel.y))
                if voxel_states[i] == 3:
                    window.blit(stone_img, (voxel.x, voxel.y))
                if voxel_states[i] == 2:
                    window.blit(dirt_img, (voxel.x, voxel.y))
                if voxel_states[i] == 1:
                    window.blit(grass_img, (voxel.x, voxel.y))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


game_loop()
