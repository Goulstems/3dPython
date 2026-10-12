from Mindustry.NodeClasses.NodeType import NodeType
from ursina import color
from ursina.shaders import *

NODE_STYLES = {
    NodeType.Ground: {
        "model": "cube",
        "color": color.hex("#4c8a3d"),
        "shader": lit_with_shadows_shader,
    },
    NodeType.Stone: {
        "model": "cube",
        "color": color.hex("#808080"),
        "shader": lit_with_shadows_shader,
    },
}