from Mindustry.ComponentClasses.GameComponent import GameComponent
from codeModules.matrixPrint import print

class Enemy(GameComponent):
    enemyID: str
    maxHealth: int
    health: int
    dmg: int = 15

    def __init__(self,ID:str) -> None:
        super().__init__(ID)
        self.spawn()

    def spawn(self) -> None:
        """TODO: - random area selection on current map?"""

    def move(self) -> None:
        """TODO: pathfinding / AI?"""

    def attack(self,entity:GameComponent) -> None:
        """TODO: implement attacking given entity"""