import pytest
from interpreter import Context, Var, Const, Add, Sub

@pytest.fixture
def context():
    ctx = Context()
    ctx.set_var("x", 10)
    ctx.set_var("y", 5)
    ctx.set_var("z", 2)
    return ctx

def test_interpreter_var(context):
    expression = Var("x")
    result = expression.interpret(context)
    assert result == 10

def test_interpreter_const(context):
    expression = Const(15)
    result = expression.interpret(context)
    assert result == 15

def test_interpreter_add(context):
    expression = Add(Var("x"), Const(5))
    result = expression.interpret(context)
    assert result == 15

def test_interpreter_sub(context):
    expression = Sub(Var("x"), Const(5))
    result = expression.interpret(context)
    assert result == 5

def test_interpreter_nested(context):
    expression = Sub(
        Add(Var("x"), Const(5)),
        Var("y")
    )
    result = expression.interpret(context)
    assert result == 10

def test_interpreter_complex(context):
    expression = Sub(
        Add(Var("x"), Const(5)),
        Add(Var("y"), Const(2))
    )
    result = expression.interpret(context)
    assert result == 8