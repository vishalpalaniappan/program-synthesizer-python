import ast

def getFunctionDef(name, args, body):
    '''
        This function returns a function definition statement.
    '''
    return ast.FunctionDef(
        name=name,
        args=ast.arguments(
            posonlyargs=[],
            args=[ast.arg(arg=arg, annotation=None) for arg in args],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=body,
        decorator_list=[]
    )

def getPreParticipantLog(name):
    '''
        This function returns a log statement for participant
        before the behavior.
    '''
    return ast.Expr(
        value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='semanticLogger', ctx=ast.Load()),
                attr='logPreParticipant',
                ctx=ast.Load()
            ),
            args=[
                ast.Name(id=name, ctx=ast.Load()),
            ],
            keywords=[]
        )
    )

def getPostParticipantLog(name):
    '''
        This function returns a log statement for participant
        after the behavior.
    '''
    return ast.Expr(
        value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='semanticLogger', ctx=ast.Load()),
                attr='logPostParticipant',
                ctx=ast.Load()
            ),
            args=[
                ast.Name(id=name, ctx=ast.Load()),
            ],
            keywords=[]
        )
    )