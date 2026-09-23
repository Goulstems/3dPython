"""Handles Rendering / ursina loading."""


# [[Dependencies]]
from ursina import *
from ursina.shaders import *
from codeModules.setupScene import setupScene
from Mindustry.GAME import GAME
from codeModules.matrixPrint import print

# ================================================
# [[Declarations]]

scene = setupScene() #Scene setup 
Game = GAME()

# ================================================
# [[Run the game !]]

scene.run()