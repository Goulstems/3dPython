from Mindustry.NodeClasses.NodeType import NodeType
from typing import Optional

class Node: 
   left: Optional["Node"] = None
   right: Optional["Node"]  = None
   top: Optional["Node"] = None
   bottom: Optional["Node"] = None
   front: Optional["Node"] = None
   back: Optional["Node"]  = None
   position: tuple[float, float, float] = (0, 0, 0)
   type: NodeType = NodeType.Empty
