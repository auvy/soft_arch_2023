class Blackboard:
    def __init__(self):
        self.data = {}
        self.experts = []

    def register_expert(self, expert):
        self.experts.append(expert)

    def add_data(self, key, value):
        self.data[key] = value
        self.propagate_data(key, value)

    def get_data(self, key):
        return self.data.get(key)

    def propagate_data(self, key, value):
        for expert in self.experts:
            expert.update(self, key, value)

