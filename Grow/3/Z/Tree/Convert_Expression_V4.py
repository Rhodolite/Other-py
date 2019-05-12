#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Expression_V4 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 4.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Version 2, Version 3, and Version 4.
#
#       Version 2:
#
#           `convert_value_expression_0` returns `None` or `Tree_Value_Expression`.
#
#       Version 3:
#
#           Does not exist.
#
#       Version 4:
#
#           `convert_value_expression_0` returns           `Tree_Value_Expression_0`.
#


from    Z.Parser.None                       import  parser_none
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__list__OF__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   convert_none_OR_value_expression(z, v)
#
#       Convert `None` to `None; OR convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a
#       `Tree_Value_Expression`.
#
def convert_none_OR_value_expression(z, v):
    assert fact_is_convert_zone(z)

    if v is None:
        return None

    return convert_value_expression(z, v)


#
#   convert_value_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Value_Expression`.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert_value_expression(z, v):
    convert_value_expression__function = (
            z.map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_value_expression__function[type(v)]
        )

    return convert_value_expression__function(z, v)


#
#   convert_value_expression_0(z, v)
#
#       1.  Convert `None` to `Tree_Value_Expression_0` (specifically to `parser_none`); or
#
#       2.  Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Value_Expression_0`.
#
def convert_value_expression_0(z, v):
    if v is None:
        return parser_none

    return convert_value_expression(z, v)


#
#   convert_full_list_of_value_expressions(z, sequence)
#
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Value_Expression`.
#
convert_full_list_of_value_expressions = (
        produce__convert__full_list__OF__Native_AbstractSyntaxTree_STAR(convert_value_expression)
    )


#
#   convert_list_of_value_expressions(z, sequence)
#
#       Convert a `Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Native_List of Tree_Value_Expression`.
#
convert_list_of_value_expressions = produce__convert__list__OF__Native_AbstractSyntaxTree_STAR(convert_value_expression)