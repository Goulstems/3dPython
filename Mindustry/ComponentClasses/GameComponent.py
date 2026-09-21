class GameComponent:
    ID: str
    maxHealth: int
    health: int

    def __init__(self,ID:str)->None:
        self.ID = ID

    def takeDamage(self, amount:int)-> None:
        self.health-=amount
        if self.health <= 0:
            self.destroy()

    def destroy(self) -> None:
        print(f"GameComponent [{self.ID}] destroyed!")