# [[Dependencies]]
from ursina import *
from ursina.shaders import *
from codeModules.setupScene import setupScene

# ================================================
# [[Declarations]]

scene = setupScene() #Scene setup 

"""
possible 'model' attribute vals : 
    > 'cube', 'sphere', 'plane', 'quad', 'circle', 'cylinder', 'diamond', 'wireframe_cube', 'wireframe_sphere', 'arrow' .

    
possible 'color' attribute vals : 
    > color.white, color.black, color.gray, color.light_gray, color.dark_gray, color.red, color.orange, color.yellow, color.lime, 
    color.green, color.turquoise, color.cyan, color.azure, color.blue, color.violet, color.magenta, color.pink, color.brown, 
    color.gold, color.silver

        OR rgb format :

    > color.rgb(R, G, B)

        OR hex format :

    > color.hex('#ff8800')

possible 'shader' attribute vals:

    > None, 'default', 'lit_with_shadows_shader', 'unlit_shader', 'normals_shader', 'vertex_lit_shader', 'pbr_shader'

"""

shaderChoice = 'normals_shader'

#GROUND setup
ground = Entity(
    model='cube',
    scale=(20, 1, 20),
    color=color.hex("#543b0e"),
    shader=shaderChoice
)

#PLAYER SETUP :

player = Entity(
    model='cube',
    color=color.hex("#19690d"),
    scale=(2, 2, 2),
    y=1.5,  # sit on top of the ground (ground top is y=0.5)
    shader=shaderChoice
)

# ================================================
# [[Run the game !]]

scene.run()