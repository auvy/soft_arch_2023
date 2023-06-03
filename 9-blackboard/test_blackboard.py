import pytest
from blackboard import *
from expert import *


@pytest.fixture
def blackboard():
    return Blackboard()


def test_register_expert(blackboard):
    expertA = ExpertA("exA")
    expertB = ExpertB("exB")
    expertC = ExpertC("exC")

    blackboard.register_expert(expertA)
    blackboard.register_expert(expertB)
    blackboard.register_expert(expertC)

    assert len(blackboard.experts) == 3


def test_add_data(blackboard):
    expertA = ExpertA("exA")
    expertB = ExpertB("exB")
    expertC = ExpertC("exC")

    blackboard.register_expert(expertA)
    blackboard.register_expert(expertB)
    blackboard.register_expert(expertC)

    blackboard.add_data("dataA", 123)
    blackboard.add_data("dataB", "Hello")
    blackboard.add_data("dataC", [1, 2, 3])

    assert blackboard.get_data("dataA") == 123
    assert blackboard.get_data("dataB") == "Hello"
    assert blackboard.get_data("dataC") == [1, 2, 3]


def test_expert_updates(blackboard, capsys):
    expertA = ExpertA("exA")
    expertB = ExpertB("exB")
    expertC = ExpertC("exC")

    blackboard.register_expert(expertA)
    blackboard.register_expert(expertB)
    blackboard.register_expert(expertC)

    blackboard.add_data("dataA", 123)
    blackboard.add_data("dataB", "Hello")
    blackboard.add_data("dataC", [1, 2, 3])

    captured = capsys.readouterr()

    assert "exA received 123 from bb." in captured.out
    assert "exB received Hello from bb." in captured.out
    assert "exC received [1, 2, 3] from bb." in captured.out
