import pygame

pygame.init()

clock = pygame.time.Clock()

win_res = [1000, 800]

window = pygame.display.set_mode(win_res)
pygame.display.set_caption("Voxel Engine")

bg_color = (120, 200, 255)

voxel_size = [20, 20]

stone_img = pygame.image.load("data/images/stone.png")
dirt_img = pygame.image.load("data/images/dirt.png")
grass_img = pygame.image.load("data/images/grass.png")
deep_slate_img = pygame.image.load("data/images/deep_slate.png")
plank_img = pygame.image.load("data/images/plank.png")
log_img = pygame.image.load("data/images/log.png")
wood_stair_l_img = pygame.image.load("data/images/wood_stair_l.png")
wood_stair_r_img = pygame.image.load("data/images/wood_stair_r.png")
stone_stair_l_img = pygame.image.load("data/images/stone_stair_l.png")
stone_stair_r_img = pygame.image.load("data/images/stone_stair_r.png")
stone_brick_img = pygame.image.load("data/images/stone_brick.png")
stone_brick_stair_l_img = pygame.image.load("data/images/stone_brick_stair_l.png")
stone_brick_stair_r_img = pygame.image.load("data/images/stone_brick_stair_r.png")
deep_slate_brick_img = pygame.image.load("data/images/deep_slate_brick.png")
deep_slate_brick_stair_l_img = pygame.image.load("data/images/deep_slate_brick_stair_l.png")
deep_slate_brick_stair_r_img = pygame.image.load("data/images/deep_slate_brick_stair_r.png")
deep_slate_stair_l_img = pygame.image.load("data/images/deep_slate_stair_l.png")
deep_slate_stair_r_img = pygame.image.load("data/images/deep_slate_stair_r.png")
tuff_img = pygame.image.load("data/images/tuff.png")
flower_img = pygame.image.load("data/images/flower.png")
amethyst_img = pygame.image.load("data/images/amethyst.png")
cobble_stone_img = pygame.image.load("data/images/cobble_stone.png")
copper_img = pygame.image.load("data/images/copper.png")
netherrack_img = pygame.image.load("data/images/netherrack.png")
end_stone_img = pygame.image.load("data/images/end_stone.png")
end_stone_brick_img = pygame.image.load("data/images/end_stone_brick.png")

button_images = [grass_img, dirt_img, stone_img, deep_slate_img, plank_img, log_img, stone_brick_img, deep_slate_brick_img,
                 tuff_img, flower_img, amethyst_img, cobble_stone_img, copper_img, netherrack_img, end_stone_img, end_stone_brick_img,
                 wood_stair_l_img, wood_stair_r_img, stone_stair_l_img, stone_stair_r_img, stone_brick_stair_l_img, stone_brick_stair_r_img,
                 deep_slate_stair_l_img, deep_slate_stair_r_img, deep_slate_brick_stair_l_img, deep_slate_brick_stair_r_img]

voxel_images = {
    1: grass_img,
    2: dirt_img,
    3: stone_img,
    4: deep_slate_img,
    5: plank_img,
    6: log_img,
    7: stone_brick_img,
    8: deep_slate_brick_img,
    9: tuff_img,
    10: flower_img,
    11: amethyst_img,
    12: cobble_stone_img,
    13: copper_img,
    14: netherrack_img,
    15: end_stone_img,
    16: end_stone_brick_img
}


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
    for y in range(20):
        for x in range(25):
            if y == 16:
                v_s.append(1)
            elif y > 16:
                v_s.append(2)
            else:
                v_s.append(0)

    return v_s


rotated_images = {
    17: {
        0: wood_stair_l_img,
        180: pygame.transform.flip(wood_stair_l_img, False, True)
    },
    18: {
        0: wood_stair_r_img,
        180: pygame.transform.flip(wood_stair_r_img, False, True)
    },
    19: {
        0: stone_stair_l_img,
        180: pygame.transform.flip(stone_stair_l_img, False, True)
    },
    20: {
        0: stone_stair_r_img,
        180: pygame.transform.flip(stone_stair_r_img, False, True)
    },
    21: {
        0: stone_brick_stair_l_img,
        180: pygame.transform.flip(stone_brick_stair_l_img, False, True)
    },
    22: {
        0: stone_brick_stair_r_img,
        180: pygame.transform.flip(stone_brick_stair_r_img, False, True)
    },
    23: {
        0: deep_slate_stair_l_img,
        180: pygame.transform.flip(deep_slate_stair_l_img, False, True)
    },
    24: {
        0: deep_slate_stair_r_img,
        180: pygame.transform.flip(deep_slate_stair_r_img, False, True)
    },
    25: {
        0: deep_slate_brick_stair_l_img,
        180: pygame.transform.flip(deep_slate_brick_stair_l_img, False, True)
    },
    26: {
        0: deep_slate_brick_stair_r_img,
        180: pygame.transform.flip(deep_slate_brick_stair_r_img, False, True)
    }
}

rotatable = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


def menu_buttons():
    r = []
    rows = 10
    cols = 10
    for i in range(rows):
        for j in range(cols):
            if len(r) >= len(button_images):
                return r
            r.append(pygame.Rect([j * 50, i * 50, 40, 40]))

    return r


def game_loop():
    facings = ["right" for _ in range(500)]

    voxels = generate_voxels()
    voxel_states = generate_voxel_state()

    placing_state = 3
    buttons = menu_buttons()

    menu = False
    running = True
    while running:
        if menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or pygame.K_m:
                        menu = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    m_x, m_y = pygame.mouse.get_pos()
                    m_r = pygame.Rect([m_x, m_y, 1, 1])

                    for i, button in enumerate(buttons):
                        if m_r.colliderect(button):
                            placing_state = i + 1
                            menu = False

            window.fill(bg_color)

            for i, button in enumerate(buttons):
                window.blit(button_images[i], (button.x, button.y))

        else:
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
                            elif event.button == 3 and (voxel_states[i] == 0 or voxel_states[i] in rotatable):
                                voxel_states[i] = placing_state
                                if voxel_states[i] in rotatable:
                                    if facings[i] == "left":
                                        facings[i] = "right"
                                    elif facings[i] == "right":
                                        facings[i] = "left"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m or event.key == pygame.K_ESCAPE:
                        menu = True

            window.fill(bg_color)

            for i, voxel in enumerate(voxels):
                state = voxel_states[i]
                if state in voxel_images:
                    window.blit(voxel_images[state], (voxel.x, voxel.y))

                elif state in rotated_images:
                    if facings[i] == "left":
                        window.blit(rotated_images[state][0], (voxel.x, voxel.y))
                    elif facings[i] == "down":
                        window.blit(rotated_images[state][90], (voxel.x, voxel.y))
                    elif facings[i] == "right":
                        window.blit(rotated_images[state][180], (voxel.x, voxel.y))
                    elif facings[i] == "up":
                        window.blit(rotated_images[state][270], (voxel.x, voxel.y))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


game_loop()
