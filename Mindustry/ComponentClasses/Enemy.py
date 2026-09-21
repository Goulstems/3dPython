from GameComponent import GameComponent

class Enemy(GameComponent):
    enemyID: str
    maxHealth: int
    health: int

    def __init__(self,ID:str) -> None:
        super().__init__(ID)
        print("New enemy was created !")
        self.spawn()

    def spawn(self) -> None:
        print("Enemy was spawned!")
        """TODO: - random area selection on current map?"""

    def move(self) -> None:
        print("Enemy moved!")
        """TODO: pathfinding / AI?"""

    def attack(self,entity:GameComponent) -> None:
        print("Enemy attacked!")
        """"""