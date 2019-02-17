#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Comprehension_V1 - Implementation of `Tree_Comprehension`, Version 1.
#
#       Copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#   See "Z/Tree/Comprehension.py" for an explanation of comprehensions.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  trace


if __debug__:
    from    Capital.Fact                import  fact_is_some_native_list
    from    Z.Tree.Expression           import  fact_is_tree_expression
    from    Z.Tree.Target               import  fact_is_tree_store_target


#
#   Tree: Comprehension Clause, Version 1
#
class Tree_Comprehension_Clause_V1(object):
    #
    #   implements Tree_Expression
    #
    __slots__ = ((
        'target',                       #   Tree_Expression
        'sequence',                     #   Tree_Expression
        'if_tests',                     #   SomeNativeList of Tree_Expression
    ))


    #
    #   Private
    #
    def __init__(self, target, sequence, if_tests):
        self.target   = target
        self.sequence = sequence
        self.if_tests = if_tests


    #
    #   Interface Tree_Expression
    #
    if __debug__:
        is_tree_expression = True


    def dump_comprehension_clause_tokens(self, f):
        f.write('<comprehension-clause for ')
        self.target.dump_store_target_tokens(f)
        f.write(' in ')
        self.sequence.dump_evaluate_tokens(f)

        for v in self.if_tests:
            f.write(' if ')
            v.dump_evaluate_tokens(f)

        f.greater_than_sign()


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Comprehension_Clause_V1 {!r}.{} {}>',
                       self.target, self.sequence, self.if_tests)


def create_Tree_Comprehension_Clause_V1(target, sequence, if_tests):
    assert fact_is_tree_store_target(target)
    assert fact_is_tree_expression  (sequence)
    assert fact_is_some_native_list(if_tests)

    return Tree_Comprehension_Clause_V1(target, sequence, if_tests)
