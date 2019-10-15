

# Path to sprites
# Basically here are lot of variations of roots here: from left corner of side to right, each got unique sprite for it
# i'm bit lazy, so just used middle to middle sprites, if you generate ones, you can browse path to it here

# Sprites counts from left to right, then first avaliable at clockwise direction.
# Corner sprites must be in "L" pattern

def get_sprite(fill, type, fat):

    if fill == 0:       # 0 - Dirt
        return get_grid_sprites("dirt")

    elif fill == 1:     # 1 - Root
        if type == 0:   # 0 - Straight
            if fat == 0:        # 0 - Thick
                return get_roots_sprites("thick", "straight", "m-m")
            if fat == 1:        # 1 - Neck
                return get_roots_sprites("neck", "straight", "m-m")
            if fat == 2:        # 2 - Thin
                return get_roots_sprites("thin", "straight", "m-m")
        elif type == 1:   # 1 - Corner
            if fat == 0:        # 0 - Thick
                return get_roots_sprites("thick", "corner", "m-m")
            if fat == 1:        # 1 - Neck
                return get_roots_sprites("neck", "corner", "m-m")
            if fat == 2:        # 2 - Thin
                return get_roots_sprites("thin", "corner", "m-m")
        elif type == 2:   # 2 - Tail
            return get_roots_sprites("thin", "tail", "m-m")

    elif fill == 2:    # 2 - Stone
        return get_grid_sprites("stone")

    elif fill == 3:    # 3 - Lakiaro
        return get_grid_sprites("grass")


# Assignment function looks like a mess, but currently i got no idea how to make look it better


def get_roots_sprites(fat, type, align, data=1):
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
                "m-l": [11, "sprites/m-m.png"],  # Middle to left
                "m-m": [12, "sprites/m-m.png"],
                "m-r": [13, "sprites/m-m.png"],
                "l-l": [14, "sprites/m-m.png"],  # Left to left
                "l-m": [15, "sprites/m-m.png"],
                "l-r": [16, "sprites/m-m.png"],
                "r-l": [17, "sprites/m-m.png"],  # Right to left
                "r-m": [18, "sprites/m-m.png"],
                "r-r": [19, "sprites/m-m.png"]
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
                "m-l": [31, "sprites/m-m.png"],  # Middle to left
                "m-m": [32, "sprites/m-m.png"],
                "m-r": [33, "sprites/m-m.png"],
                "l-l": [34, "sprites/m-m.png"],  # Left to left
                "l-m": [35, "sprites/m-m.png"],
                "l-r": [36, "sprites/m-m.png"],
                "r-l": [37, "sprites/m-m.png"],  # Right to left
                "r-m": [38, "sprites/m-m.png"],
                "r-r": [39, "sprites/m-m.png"]
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
                "m-l": [51, "sprites/m-m.png"],  # Middle to left
                "m-m": [52, "sprites/m-m.png"],
                "m-r": [53, "sprites/m-m.png"],
                "l-l": [54, "sprites/m-m.png"],  # Left to left
                "l-m": [55, "sprites/m-m.png"],
                "l-r": [56, "sprites/m-m.png"],
                "r-l": [57, "sprites/m-m.png"],  # Right to left
                "r-m": [58, "sprites/m-m.png"],
                "r-r": [59, "sprites/m-m.png"]
            },
            "tail": {
                "straight": {
                    "l": [61, "sprites/m-m.png"],
                    "m": [62, "sprites/m-m.png"],
                    "r": [63, "sprites/m-m.png"]
                }

            },

        },
    }
    return sprites[fat][type][align][data]


def get_grid_sprites(name,data=0):
    sprites = {
        "grass": ["sprites/grass.png"],
        "dirt": ["sprites/dirt.png"],
        "stone": ["sprites/grass.png"]
    }
    return sprites[name][data]

