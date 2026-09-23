from ursina import Entity, color
from ursina.shaders import lit_with_shadows_shader
from Mindustry.NodeClasses.NodeMap import NodeMap
from Mindustry.NodeClasses.NodeType import NodeType


emptyEntity = Entity(
    enabled=False,
)

groundEntity = Entity(
    model="cube",
    color=color.green,
    shader=lit_with_shadows_shader,
    enabled=False
)

nodeStyleEntities: dict[str, Entity] = {
    NodeType.Empty: emptyEntity,
    NodeType.Ground: groundEntity,
}


class NodeMapRenderer:
    @staticmethod
    def render(node_map: NodeMap) -> None:
        for pos, node in node_map.nodes.items():
            if node.type == NodeType.Empty:
                continue
            NodeMapRenderer._make_entity(pos, node.type)

    @staticmethod
    def _make_entity(pos: tuple[int, int, int], node_type: NodeType) -> Entity:
        x, y, z = pos
        style = nodeStyleEntities[node_type]
        tile_size = 1
        return Entity(
            model=style.model,
            scale=tile_size,
            position=(
                x * tile_size,
                y * tile_size,
                z * tile_size,
            ),
            color=style.color,
            shader=style.shader,
            name=f"node_{x}_{y}_{z}",
        )