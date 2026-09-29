from Mindustry.NodeClasses.Node import Node
from Mindustry.NodeClasses.NodeMap import NodeMap
from Mindustry.NodeClasses.NodeType import NodeType
from codeModules.noise import noise2d
from random import randint

class NodeMapGenerator:
    @staticmethod
    def generate(
        x: int,
        y: int,
        z: int,
        height_amplitude: float = 2,
        noise_frequency: float = 0.08,
    ) -> NodeMap:
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError("Dimensions <= 0")
        if height_amplitude < 0:
            raise ValueError("Height amplitude cannot be negative")
        if noise_frequency < 0:
            raise ValueError("Noise frequency cannot be negative")

        node_map: NodeMap = NodeMap()
        node_map.seed = randint(1, 100)

        for xPos in range(x):
            for yPos in range(y):
                for zPos in range(z):
                    node: Node = Node()
                    node.type = NodeType.Ground
                    node_map.set(node, (xPos, yPos, zPos))
                    node.position = (
                        xPos,
                        yPos
                        + noise2d(
                            xPos * noise_frequency,
                            zPos * noise_frequency,
                            node_map.seed,
                        )
                        * height_amplitude,
                        zPos,
                    )

        return node_map