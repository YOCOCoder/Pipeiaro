

# Path to sprites
# Basically here are lot of variations of roots here: from left corner of side to right, each got unique sprite for it
# i'm bit lazy, so just used middle to middle sprites, if you generate ones, you can browse path to it here

# Sprites counts from left to right, then first avaliable at clockwise direction.
# Corner sprites must be in "L" pattern

def get_roots():
    sprites = {

        "thick": {
            "straight": {
                "m-l": [1, "sprites/m-m.png"],  # Middle to left
                "m-m": [2, "sprites/m-m.png"],
                "m-r": [3, "sprites/m-m.png"],
                "l-l": [4, "sprites/m-m.png"],  # Left to left
                "l-m": [5, "sprites/m-m.png"],
                "l-r": [6, "sprites/m-m.png"],
                "r-l": [7, "sprites/m-m.png"],  # Right to left
                "r-m": [8, "sprites/m-m.png"],
                "r-r": [9, "sprites/m-m.png"]
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
                "m-l": [21, "sprites/m-m.png"],  # Middle to left
                "m-m": [22, "sprites/m-m.png"],
                "m-r": [23, "sprites/m-m.png"],
                "l-l": [24, "sprites/m-m.png"],  # Left to left
                "l-m": [25, "sprites/m-m.png"],
                "l-r": [26, "sprites/m-m.png"],
                "r-l": [27, "sprites/m-m.png"],  # Right to left
                "r-m": [28, "sprites/m-m.png"],
                "r-r": [29, "sprites/m-m.png"]
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
                "m-l": [41, "sprites/m-m.png"],  # Middle to left
                "m-m": [42, "sprites/m-m.png"],
                "m-r": [43, "sprites/m-m.png"],
                "l-l": [44, "sprites/m-m.png"],  # Left to left
                "l-m": [45, "sprites/m-m.png"],
                "l-r": [46, "sprites/m-m.png"],
                "r-l": [47, "sprites/m-m.png"],  # Right to left
                "r-m": [48, "sprites/m-m.png"],
                "r-r": [49, "sprites/m-m.png"]
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
            }
        },
        "end": {
            "straight": {
                "l": [61, "sprites/m-m.png"],
                "m": [62, "sprites/m-m.png"],
                "r": [63, "sprites/m-m.png"]
            }
        },

    }
    return sprites