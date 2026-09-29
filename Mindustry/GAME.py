from Mindustry.ComponentClasses.Map import Map
from Mindustry.ComponentClasses.Base import Base
from Mindustry.ComponentClasses.Enemy import Enemy
from Mindustry.ComponentClasses.EnemyClasses.Enemy1 import Enemy1
from codeModules.matrixPrint import print

from Mindustry.NodeClasses.NodeMapGenerator import NodeMapGenerator
from Mindustry.NodeClasses.NodeMapRenderer import NodeMapRenderer
from Mindustry.NodeClasses.NodeMap import NodeMap

class GAME:
    # map: Map = None
    # base: Base = None
    # currentResources: dict[str, int] = {}
    # currentComponents: dict[str, int] = {
    #     "Base": 1,
    #     "Player": 1,
    #     "Enemy": 0,
    #         "BasicEnemy": 0
    # }
    # currentEnemies: dict[str,Enemy] = {}

    def __init__(self) -> None:
        nodeMap: NodeMap = NodeMapGenerator.generate(100, 100)
        NodeMapRenderer.render(nodeMap)





































    def displayEnemies(self)->str:
        enemyDisplayStr = "   > [Current Enemies in Game]:\n"
        for enemyID,enemyOBJ in self.currentEnemies.items():
            enemyDisplayStr+="\t- "+enemyID+"\n"
        return enemyDisplayStr

    def spawnEnemy(self,enemyType:str="Basic") -> Enemy:
        enemyConstructorMap:dict[str,Enemy] = {
            "Basic" : Enemy1
        }
        enemyConstructor:Enemy = enemyConstructorMap[enemyType]
        self.currentComponents["Enemy"]+=1
        self.currentComponents[enemyType+"Enemy"]+=1
        newEnemy:Enemy = enemyConstructor(enemyType+str(self.currentComponents[enemyType+"Enemy"]))
        self.currentEnemies[newEnemy.ID] = newEnemy
        return newEnemy
        
    def unitPlacement(self, unitType:str,coords:list[int]):
        print(f"Player wants to place a [{unitType}] at : ({coords})")

    def unitDestroy(self,unitID: str) -> None:
        print(f"unit : [{unitID}] was destroyed!")
    