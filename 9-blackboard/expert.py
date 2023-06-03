class Expert:
    def __init__(self, name):
        self.name = name

    def update(self, blackboard, key, value):
        return False


class ExpertA(Expert):
    def update(self, blackboard, key, value):
        if key == "dataA":
            print(f"{self.name} received {value} from bb.")


class ExpertB(Expert):
    def update(self, blackboard, key, value):
        if key == "dataB":
            print(f"{self.name} received {value} from bb.")


class ExpertC(Expert):
    def update(self, blackboard, key, value):
        if key == "dataC":
            print(f"{self.name} received {value} from bb.")
