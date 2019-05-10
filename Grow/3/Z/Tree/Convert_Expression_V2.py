#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Expression_V2 - Convert Python Abstract Syntax Tree Expressions to Tree classes, Version 2.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Difference between Version 1 & Version 2.
#
#       Version 1:
#
#           Does not use `Convert_Zone`.
#
#       Version 2:
#
#           All "convert" routines take a `z` parameter of type `Convert_Zone`.
#


from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Z.Tree.Convert_Zone             import  fact_is_convert_zone


#
#   convert_expression(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a `Tree_Value_Expression`.
#
#       Calls all the other `convert_*` pseudo methods.
#
def convert_expression(z, v):
    convert_expression__function = (
            z.map__Native_AbstractSyntaxTree_EXPRESSION__to__convert_expression__function[type(v)]
        )

    return convert_expression__function(z, v)


#
#   convert_none_OR_expression(z, v)
#
#       Convert `None` to `None; OR convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.AST`) to a
#       `Tree_Value_Expression`.
#
def convert_none_OR_expression(z, v):
    assert fact_is_convert_zone(z)

    if v is None:
        return None

    return convert_expression(z, v)


#
#   convert_full_list_of_expressions(z, sequence)
#
#       Convert a `Full_Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Full_Native_List of Tree_Value_Expression`.
#
convert_full_list_of_expressions = produce__convert__full_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)


#
#   convert_some_list_of_expressions(z, sequence)
#
#       Convert a `Native_List of Native_AbstractSyntaxTree_*` (i.e.: `list of _ast.AST`) to a
#       `Native_List of Tree_Value_Expression`.
#
convert_some_list_of_expressions = produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_expression)
