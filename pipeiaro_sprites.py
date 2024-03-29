import pygame

# Path to sprites
# Basically here are lot of variations of roots here: from left corner of side to right, each got unique sprite for it
# i'm bit lazy, so just used middle to middle sprites, if you generate ones, you can browse path to it here

# Sprites counts from left to right, then first available at clockwise direction.
# Corner sprites must be in "L" pattern


def get_sprite(fill, root_type, fat):

    if fill == 0:       # 0 - Dirt
        return get_grid_sprites("dirt")

    elif fill == 1:     # 1 - Root
        if root_type == 0:   # 0 - Straight
            if fat == 0:        # 0 - Thick
                return get_roots_sprites("thick", "straight", "m-m")
            if fat == 1:        # 1 - Neck
                return get_roots_sprites("neck", "straight", "m-m")
            if fat == 2:        # 2 - Thin
                return get_roots_sprites("thin", "straight", "m-m")
        elif root_type == 1:   # 1 - Corner
            if fat == 0:        # 0 - Thick
                return get_roots_sprites("thick", "corner", "m-m")
            if fat == 1:        # 1 - Neck
                return get_roots_sprites("neck", "corner", "m-m")
            if fat == 2:        # 2 - Thin
                return get_roots_sprites("thin", "corner", "m-m")
        elif root_type == 2:   # 2 - Tail
            return get_roots_sprites("thin", "tail", "m")

    elif fill == 2:    # 2 - Stone
        return get_grid_sprites("stone")

    elif fill == 3:    # 3 - Lakiaro
        return get_grid_sprites("grass")


# Assignment function looks like a mess, but currently i have no idea how to make look it better


def get_roots_sprites(fat, root_type, align, data=1):
    sprites = {

        "thick": {
            "straight": {
                "m-l": [1, "sprites/root/straight_thick.png"],  # Middle to left
                "m-m": [2, "sprites/root/straight_thick.png"],
                "m-r": [3, "sprites/root/straight_thick.png"],
                "l-l": [4, "sprites/root/straight_thick.png"],  # Left to left
                "l-m": [5, "sprites/root/straight_thick.png"],
                "l-r": [6, "sprites/root/straight_thick.png"],
                "r-l": [7, "sprites/root/straight_thick.png"],  # Right to left
                "r-m": [8, "sprites/root/straight_thick.png"],
                "r-r": [9, "sprites/root/straight_thick.png"]
            },
            "corner": {
                "m-l": [11, "sprites/root/corner_thick.png"],  # Middle to left
                "m-m": [12, "sprites/root/corner_thick.png"],
                "m-r": [13, "sprites/root/corner_thick.png"],
                "l-l": [14, "sprites/root/corner_thick.png"],  # Left to left
                "l-m": [15, "sprites/root/corner_thick.png"],
                "l-r": [16, "sprites/root/corner_thick.png"],
                "r-l": [17, "sprites/root/corner_thick.png"],  # Right to left
                "r-m": [18, "sprites/root/corner_thick.png"],
                "r-r": [19, "sprites/root/corner_thick.png"]
            }
        },
        "neck": {
            "straight": {
                "m-l": [21, "sprites/root/straight_neck.png"],  # Middle to left
                "m-m": [22, "sprites/root/straight_neck.png"],
                "m-r": [23, "sprites/root/straight_neck.png"],
                "l-l": [24, "sprites/root/straight_neck.png"],  # Left to left
                "l-m": [25, "sprites/root/straight_neck.png"],
                "l-r": [26, "sprites/root/straight_neck.png"],
                "r-l": [27, "sprites/root/straight_neck.png"],  # Right to left
                "r-m": [28, "sprites/root/straight_neck.png"],
                "r-r": [29, "sprites/root/straight_neck.png"]
            },
            "corner": {
                "m-l": [31, "sprites/root/corner_neck.png"],  # Middle to left
                "m-m": [32, "sprites/root/corner_neck.png"],
                "m-r": [33, "sprites/root/corner_neck.png"],
                "l-l": [34, "sprites/root/corner_neck.png"],  # Left to left
                "l-m": [35, "sprites/root/corner_neck.png"],
                "l-r": [36, "sprites/root/corner_neck.png"],
                "r-l": [37, "sprites/root/corner_neck.png"],  # Right to left
                "r-m": [38, "sprites/root/corner_neck.png"],
                "r-r": [39, "sprites/root/corner_neck.png"]
            }
        },
        "thin": {
            "straight": {
                "m-l": [41, "sprites/root/straight_thin.png"],  # Middle to left
                "m-m": [42, "sprites/root/straight_thin.png"],
                "m-r": [43, "sprites/root/straight_thin.png"],
                "l-l": [44, "sprites/root/straight_thin.png"],  # Left to left
                "l-m": [45, "sprites/root/straight_thin.png"],
                "l-r": [46, "sprites/root/straight_thin.png"],
                "r-l": [47, "sprites/root/straight_thin.png"],  # Right to left
                "r-m": [48, "sprites/root/straight_thin.png"],
                "r-r": [49, "sprites/root/straight_thin.png"]
            },
            "corner": {
                "m-l": [51, "sprites/root/corner_thin.png"],  # Middle to left
                "m-m": [52, "sprites/root/corner_thin.png"],
                "m-r": [53, "sprites/root/corner_thin.png"],
                "l-l": [54, "sprites/root/corner_thin.png"],  # Left to left
                "l-m": [55, "sprites/root/corner_thin.png"],
                "l-r": [56, "sprites/root/corner_thin.png"],
                "r-l": [57, "sprites/root/corner_thin.png"],  # Right to left
                "r-m": [58, "sprites/root/corner_thin.png"],
                "r-r": [59, "sprites/root/corner_thin.png"]
            },
            "tail": {
                    "l": [61, "sprites/root/tail.png"],
                    "m": [62, "sprites/root/tail.png"],
                    "r": [63, "sprites/root/tail.png"]
            },

        },
    }
    return sprites[fat][root_type][align][data]


def get_grid_sprites(name, data=0):
    sprites = {
        "grass": ["sprites/grass.png"],
        "dirt": ["sprites/dirt.png"],
        "stone": ["sprites/stone.png"]
    }
    return sprites[name][data]


def get_selection_sprites():
    sprites = {
        "blue": pygame.image.load("sprites/selection_blue.png"),
        "green": pygame.image.load("sprites/selection_green.png"),
        "red": pygame.image.load("sprites/selection_red.png")
    }
    return sprites
