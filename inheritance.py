
class Console:
    def __init__(self, name) -> None:
        self.name = name

class Xbox(Console):
    def info(self):
        print(self.name, "Produced by Micro$$oft")

class PlayStation(Console):
    def info(self):
        print(self.name, "Produced by Play$tation")

xbox = Xbox("x360")
ps = PlayStation("ps2") 

xbox.info()
ps.info()