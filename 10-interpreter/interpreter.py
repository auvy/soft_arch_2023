class Context:
    def __init__(self):
        self.vars = {}

    def set_var(self, var, value):
        self.vars[var] = value

    def get_var(self, var):
        return self.vars.get(var)


class Expression:
    def interpret(self, context):
        pass


class Var(Expression):
    def __init__(self, var):
        self.var = var

    def interpret(self, context):
        return context.get_var(self.var)


class Const(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class Add(Expression):
    def __init__(self, left_expr, right_expr):
        self.left_expr = left_expr
        self.right_expr = right_expr

    def interpret(self, context):
        left_value = self.left_expr.interpret(context)
        right_value = self.right_expr.interpret(context)
        return left_value + right_value


class Sub(Expression):
    def __init__(self, left_expr, right_expr):
        self.left_expr = left_expr
        self.right_expr = right_expr

    def interpret(self, context):
        left_value = self.left_expr.interpret(context)
        right_value = self.right_expr.interpret(context)
        return left_value - right_value