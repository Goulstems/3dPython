from Mindustry.NodeClasses.Node import Node
from Mindustry.NodeClasses.NodeMap import NodeMap
from Mindustry.NodeClasses.NodeType import NodeType
from codeModules.noise import noise3d
from random import randint

class NodeMapGenerator:
    @staticmethod
    def generate(x:int,y:int,z:int) -> NodeMap:
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError("Dimensions <= 0")

        node_map = NodeMap()

        for x in range(x):
            for y in range(y):
                for z in range(z):
                    node = Node()
                    node.type = NodeType.Ground

                    # vertical displacement.
                    noiseOffset = noise3d(
                        x,y,z,randint(1,100),1
                    )

                    newNodePos = (
                        x,y+noiseOffset,z
                    )

                    node_map.set(node,newNodePos)

        return node_map