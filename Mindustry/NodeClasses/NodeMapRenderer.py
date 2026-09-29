from ursina import Entity, color
from ursina.shaders import lit_with_shadows_shader
from Mindustry.NodeClasses.NodeMap import NodeMap
from Mindustry.NodeClasses.NodeType import NodeType

NODE_STYLES = {
    NodeType.Ground: {
        "model": "cube",
        "color": color.hex("#4c8a3d"),
        "shader": lit_with_shadows_shader,
    },
}


class NodeMapRenderer:
    @staticmethod
    def render(node_map: NodeMap, tile_size: float = 2.0) -> None:
        if not node_map.nodes:
            return

        xs = [pos[0] for pos in node_map.nodes]
        zs = [pos[2] for pos in node_map.nodes]
        center_x = (min(xs) + max(xs)) / 2
        center_z = (min(zs) + max(zs)) / 2
        root = Entity(name="NodeMap")

        for pos, node in node_map.nodes.items():
            if node.type == NodeType.Empty:
                continue
            x, y, z = node.position
            style = NODE_STYLES.get(node.type)
            if style is None:
                continue
            Entity(
                parent=root,
                model=style["model"],
                scale=tile_size,
                position=(
                    (x - center_x) * tile_size,
                    y * tile_size,
                    (z - center_z) * tile_size,
                ),
                color=style["color"],
                shader=style["shader"],
                name=f"node_{x}_{y}_{z}",
            )