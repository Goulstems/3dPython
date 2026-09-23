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

        node_map:NodeMap = NodeMap()
        seed:int =randint(1,100)

        for xPos in range(x):
            for yPos in range(y):
                for zPos in range(z):
                    node:Node = Node()
                    node.type = NodeType.Ground

                    # vertical displacement.
                    noiseOffset = noise3d(
                        xPos,yPos,zPos,seed,1
                    )

                    newNodePos = (
                        xPos,yPos+noiseOffset,zPos
                    )

                    node_map.set(node,newNodePos)

        return node_map