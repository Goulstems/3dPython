from ursina import Entity
from Mindustry.NodeClasses.NodeMap import Node
from Mindustry.NodeClasses.NodeMap import NodeMap
from Mindustry.NodeClasses.NodeType import NodeType
from Mindustry.NodeClasses.NodeStyles import NODE_STYLES

def renderNode(node: Node,tile_size: float=2.0)-> None:
    x, y, z = node.position
    style = NODE_STYLES.get(node.type)
    Entity(
        model=style["model"],
        scale=tile_size,
        position=(
            x* tile_size,
            y* tile_size,
            z* tile_size,
        ),
        color=style["color"],
        shader=style["shader"],
        name=f"node_{x}_{y}_{z}",
    )

class NodeMapRenderer:
    @staticmethod
    def render(node_map: NodeMap, tile_size: float = 2.0) -> None:
        for _, node in node_map.nodes.items():
            if node.type == NodeType.Empty:
                continue
            renderNode(node,tile_size)