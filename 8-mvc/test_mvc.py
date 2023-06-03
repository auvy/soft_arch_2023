from model import *
from view import *
from controller import *

def test_display_data(capsys):
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.update_model("LOOK HERE")

    controller.display_data()

    captured = capsys.readouterr()
    assert captured.out.strip() == 'Displaying: "LOOK HERE"'
