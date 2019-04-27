#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Many_V1 - Implementation of tree target classes (tuple & list), Version 1.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       See "Tree.Target" for an explanation of "target".
#


from    Capital.Core                    import  arrange


if __debug__:
    from    Capital.Fact                import  fact_is_positive_integer
    from    Capital.Fact                import  fact_is_some_native_list
    from    Capital.Fact                import  fact_is_substantial_integer
    from    Z.Tree.Context              import  fact_is_tree_context
    from    Z.Tree.Context              import  fact_is_tree_load_context
    from    Z.Tree.Context              import  fact_is_tree_store_context


#
#   Tree: Many Expression - Base class of `Tree_List_Expression` and `Tree_Tuple_Expression`
#
class Tree_Many_Expression(object):
    #
    #   implements Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = ((
        'line_number',                  #   PositiveInteger
        'column',                       #   SubstantialInteger

        'elements',                     #   SomeNativeList of Tree_Expression
        'context',                      #   Tree_Context
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, elements, context):
        self.line_number = line_number
        self.column      = column

        self.elements = elements
        self.context  = context


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_evaluate_tokens(self, f):
        assert fact_is_tree_load_context(self.context)

        first = True

        f.arrange('<{} @{}:{}', self.keyword, self.line_number, self.column)

        for v in self.elements:
            if first:
                first = False

                f.write(';')
            else:
                f.write(',')

            f.space()
            v.dump_evaluate_tokens(f)

        f.write('; ')
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Interface Tree_Store_Target
    #
    #   NOTE:
    #       The method `.dump_store_target_tokens` below has TWO lines different from method `.dump_evaluate_tokens`
    #       above:
    #
    #           1)  assert fact_is_tree_store_context(self.context)
    #           2)  v.dump_store_target_tokens(f)
    #
    if __debug__:
        @property
        def is_tree_store_target(self):
            return self.context.is_tree_store_context


    def dump_store_target_tokens(self, f):
        assert fact_is_tree_store_context(self.context)

        first = True

        f.arrange('<{} @{}:{}', self.keyword, self.line_number, self.column)

        for v in self.elements:
            if first:
                first = False

                f.write(';')
            else:
                f.write(',')

            f.space()
            v.dump_store_target_tokens(f)

        f.write('; ')
        self.context.dump_context_token(f)
        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<{} @{}:{} {!r} {!r}>',
                       self.__class__.__name__, self.line_number, self.column, self.elements, self.context)


def create_Tree_Many_Expression(Meta, line_number, column, elements, context):
    assert fact_is_positive_integer   (line_number)
    assert fact_is_substantial_integer(column)

    assert fact_is_some_native_list(elements)
    assert fact_is_tree_context    (context)

    return Meta(line_number, column, elements, context)


#
#   Tree: List Expression
#
class Tree_List_Expression(Tree_Many_Expression):
    #
    #   implements Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = (())


    keyword = 'list-expression'


def create_Tree_List_Expression(line_number, column, elements, context):
    return create_Tree_Many_Expression(Tree_List_Expression, line_number, column, elements, context)


#
#   Tree: Tuple Expression
#
class Tree_Tuple_Expression(Tree_Many_Expression):
    #
    #   implements Tree_Expression,
    #              Tree_Store_Target
    #
    __slots__ = (())


    keyword = 'tuple-expression'


def create_Tree_Tuple_Expression(line_number, column, elements, context):
    return create_Tree_Many_Expression(Tree_Tuple_Expression, line_number, column, elements, context)