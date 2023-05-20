import arcade

def load_animations(load, file):
    animations = {'right':{}, 'left':{}}
    for y in range(len(load)):
        anim = load[y][0]
        count = load[y][1]
        animations['right'][anim] = []
        animations['left'][anim] = []
        for x in range(0, count*32, 32):
            t_r = arcade.load_texture(file, x, y*32, 32, 32)
            t_l = arcade.load_texture(file, x, y*32, 32, 32, True)
            id_r = sum(list(file.encode('utf8')))+x*100+y*10
            id_l = sum(list(file.encode('utf8')))+x*100+y*10 + 1
            duration = 100
            if anim == 'run':
                duration = 75
            animations['right'][anim].append(arcade.AnimationKeyframe(id_r, duration, t_r))
            animations['left'][anim].append(arcade.AnimationKeyframe(id_l, duration, t_l))
    return animations

def load_animations2(load, file):
    animations = {'right':{}, 'left':{}}
    for y in range(len(load)):
        anim = load[y][0]
        count = load[y][1]
        animations['right'][anim] = []
        animations['left'][anim] = []
        for x in range(0, count*24, 24):
            t_r = arcade.load_texture(file, x, y*24, 24, 24)
            t_l = arcade.load_texture(file, x+(24*4), y*24, 24, 24)
            id_r = sum(list(file.encode('utf8')))+x*100+y*10
            id_l = sum(list(file.encode('utf8')))+(x+(24*4))*100+y*10 + 1
            duration = 100
            if anim == 'run':
                duration = 80
            animations['right'][anim].append(arcade.AnimationKeyframe(id_r, duration, t_r))
            animations['left'][anim].append(arcade.AnimationKeyframe(id_l, duration, t_l))
    return animations

def load_animation(file, size, max_size, duration):
    width = max_size[0]
    height = max_size[1]
    animation = []
    for y in range(0, height, size):
        for x in range(0, width, size):
            texture = arcade.load_texture(file, x, y, size, size)
            id_ = sum(list(file.encode('utf8')))+x*100+y*10
            animation.append(arcade.AnimationKeyframe(id_, duration, texture))
    return animation
        