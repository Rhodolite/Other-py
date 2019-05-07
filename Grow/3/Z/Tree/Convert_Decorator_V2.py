#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Decorator_V2 - Convert Python Abstract Syntax Tree Decorators to Tree classes, Version 2.
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


from    Capital.Core                        import  trace
from    Z.Tree.Produce_Convert_List_V2      import  produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR


if __debug__:
    from    Capital.Fact                    import  fact_is_some_native_list


#
#   convert_decorator(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) to a `Tree_Expression`.
#
#   CURRENT:
#
#       For now (since this is a 1-1 translation of `_ast`) a decorator is simply a `Tree_Expresion`.
#
#       Hence, all we do is call `z.convert_expression`.
#
#   FUTURE:
#
#       We will have a special class for a decorator.
#
def convert_decorator(z, v):
    return z.convert_expression(z, v)


#
#   convert_some_list_of_decorators(z, v)
#
#       Convert some `NativeList of Native_AbstractSyntaxTree_Decorator` (i.e.: `list of _ast.decorator`) to a
#       `NativeList of Tree_Decorator`.
#
convert_some_list_of_decorators = produce__convert__some_list_of__Native_AbstractSyntaxTree_STAR(convert_decorator)
