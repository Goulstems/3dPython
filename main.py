"""Handles Rendering / ursina loading."""


# [[Dependencies]]
from ursina import *
from ursina.shaders import *
from codeModules.setupScene import setupScene

# ================================================
# [[Declarations]]

scene = setupScene() #Scene setup 
shaderChoice = 'lit_with_shadows_shader'

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