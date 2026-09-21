from Mindustry.ComponentClasses.Map import Map
from Mindustry.ComponentClasses.Base import Base
from Mindustry.ComponentClasses.GameComponent import GameComponent
from Mindustry.ComponentClasses.Enemy import Enemy
from Mindustry.ComponentClasses.EnemyClasses import Enemy1

class GAME:
    map: Map
    base: Base
    currentResources: dict[str, int] #resourceName, amount
    currentComponents: dict[str, int] = {
        "Base": 1,
        "Player": 1,
        "Enemy": 0,
            "Enemy1": 0
    }

    def __init__(self) -> None:
        print("New Game")

    def spawnEnemy(self,enemyType:str) -> Enemy:
        enemyConstructorMap:dict[str,Enemy] = {
            "Basic" : Enemy1
        }
        enemyConstructor:Enemy = enemyConstructorMap[enemyType]
        self.currentComponents["Enemy"]+=1
        self.currentComponents[enemyType]+=1
        enemyConstructor(f"{enemyType}{self.currentComponents[enemyType]}")
        


    def unitPlacement(self, unitType:str,coords:list[int]):
        print(f"Player wants to place a [{unitType}] at : ({coords})")

    def unitDestroy(self,unitID: str) -> None:
        print(f"unit : [{unitID}] was destroyed!")
    