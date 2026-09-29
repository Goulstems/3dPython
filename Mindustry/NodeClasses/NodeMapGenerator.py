from Mindustry.NodeClasses.Node import Node
from Mindustry.NodeClasses.NodeMap import NodeMap
from Mindustry.NodeClasses.NodeType import NodeType
from codeModules.noise import noise
from random import randint

class NodeMapGenerator:
    @staticmethod
    def generate(x: int,z:int) -> NodeMap:

        #Create our <NodeMap> datastructure
        node_map: NodeMap = NodeMap()

        #Tuning vars for the generation - - -
        seed:int = randint(1, 100)
        amp: float = 2 #amplitude
        freq: float = 0.08 #frequency
        # - - - - - - - - - - - - - - - - - - 

        #MAIN GENERATOR LOOP ! X by Z area
        for xPos in range(x):
            for zPos in range(z):
                node: Node = Node()                     #Create new node
                node.type = NodeType.Ground             #All types are ground to start with for first pass
                noisePos = (                           #Get noisePos for current coord
                    xPos,
                    noise(xPos*freq,zPos*freq,seed)*amp,
                    zPos
                )
                node_map.set(node, noisePos)            #Append new node into new nodemap
                node.position = noisePos                #Set new node's pos field

        return node_map