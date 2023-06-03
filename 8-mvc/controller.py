class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_model(self, data):
        self.model.set_data(data)

    def display_data(self):
        data = self.model.get_data()
        self.view.display_data(data)