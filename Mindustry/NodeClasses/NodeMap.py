from Mindustry.NodeClasses.Node import Node
from typing import Optional

class NodeMap:
    """pos : Node reference"""
    nodes: dict[tuple[int,int, int], Node]

    def __init__(self)->None:
        self.nodes = {}

    def get(self, pos: tuple[int,int,int]) -> Optional["Node"]:
        return self.nodes.get(pos)

    def set(self, node: Node, pos: tuple[int,int,int]) -> None:
        x, y, z = pos
        node.position = pos
        node.left   = self.get((x - 1, y, z))
        node.right  = self.get((x + 1, y, z))
        node.bottom = self.get((x, y - 1, z))
        node.top    = self.get((x, y + 1, z))
        node.back   = self.get((x, y, z - 1))
        node.front  = self.get((x, y, z + 1))
        self.nodes[pos] = node

