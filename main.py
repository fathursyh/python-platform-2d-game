from ursina import *
import player

app = Ursina()
player.player

bg = Entity(
            model = 'quad', 
            scale = (16, 9),
            texture = 'assets/bg1.png',
            z = 1
)
ground = Entity(
                model = 'cube', 
                y = -2,
                scale_x = 10,
                collider = 'box',
                color = color.blue
)
app.run()