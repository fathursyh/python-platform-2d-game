from ursina import *
import player

app = Ursina()
player.player
bg_x = 24
x = 13
bg = Entity(
            model = 'quad', 
            scale = (bg_x, 15),
            position = (0, 0, 0),
            texture = 'assets/bg1.png',
            z = 1
)
duplicate(bg, x = bg_x)
ground = Entity(
                model = 'cube', 
                y = -3.5,
                scale_x = 10,
                collider = 'box',
                color = color.blue
)
duplicate(ground, x = x)

camera.add_script(SmoothFollow(target=player.player, speed=4, offset=[2, 2, -40]))
EditorCamera()
app.run()