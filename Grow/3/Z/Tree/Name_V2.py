#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Name_V2 - Implementation of Tree Name, Version 2
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2
#
#   Version 1:
#
#       `Tree_Name` had a `.id : NativeString` member.
#
#   Version 2:
#
#       `Tree_Name` removes the `.id` member, and replaces it with a `.symbol : Symbol` member.
#


from    Capital.Core                    import  arrange
from    Z.Parser.Symbol                 import  conjure_symbol


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Parser.Symbol             import  fact_is_symbol
    from    Z.Tree.Context              import  fact_is_tree_context
    from    Z.Tree.Context              import  fact_is_tree_delete_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_parameter_context
    from    Z.Tree.Context              import  fact_is_tree_store_context
    


#
#   Tree: Name - A name (in a specific context)
#
#       See "Z.Tree.Context" for explanation of contexts.
#
#       Because a `Tree_Name` can appear both as an expression, as a parameter, and as a target, it implements the
#       `Tree_Expression`, `Tree_Parameter`, and `Tree_Target` interfaces.
#
class Tree_Name(object):
    #
    #   Implements Tree_Delete_Target,
    #              Tree_Expression,
    #              Tree_Parameter,
    #              Tree_Store_Target
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'symbol',                       #   Symbol
        'context',                      #   Tree_Context
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, symbol, context):
        self.line_number = line_number
        self.column      = column

        self.symbol  = symbol
        self.context = context


    def _dump_tree_name_token(self, f):
        f.arrange('<name @{}:{} {} ', self.line_number, self.column, self.symbol)
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Delete_Target
    #
    if __debug__:
        @property
        def is_tree_delete_target(self):
            return self.context.is_tree_delete_context


    if __debug__:
        def dump_delete_target_tokens(self, f):
            assert fact_is_tree_delete_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_delete_target_tokens = _dump_tree_name_token


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        @property
        def is_tree_expression(self):
            return self.context.is_tree_expression_context


    if __debug__:
        def dump_evaluate_tokens(self, f):
            assert fact_is_tree_load_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_evaluate_tokens = _dump_tree_name_token


    #
    #   Interface Tree_Parameter
    #
    if __debug__:
        is_tree_keyword_parameter = False
        is_tree_parameters_all    = False
        

        @property
        def is_tree_parameter(self):
            return self.context.is_tree_parameter_context


        is_tree_normal_parameter = is_tree_parameter



    if __debug__:
        def dump_parameter_tokens(self, f):
            assert fact_is_tree_parameter_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_parameter_tokens = _dump_tree_name_token


    #
    #   Interface Tree_Store_Target
    #
    if __debug__:
        @property
        def is_tree_store_target(self):
            return self.context.is_tree_store_context


    if __debug__:
        def dump_store_target_tokens(self, f):
            assert fact_is_tree_store_context(self.context)

            self._dump_tree_name_token(f)
    else:
        dump_store_target_tokens = _dump_tree_name_token


    #
    #   Public
    #
    is_tree_token_name = True


    def __repr__(self):
        return arrange('<Tree_Name @{}:{} {!r} {}>', self.line_number, self.column, self.symbol, self.context)


def create_Tree_Name(line_number, column, symbol, context):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_symbol      (symbol)
    assert fact_is_tree_context(context)

    return Tree_Name(line_number, column, symbol, context)