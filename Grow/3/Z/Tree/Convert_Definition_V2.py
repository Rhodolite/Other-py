#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Definition_V2 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 2.
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


from    Z.Tree.Convert_Decorator            import  convert_some_list_of_decorators
from    Z.Tree.Convert_Expression           import  convert_some_list_of_expressions
from    Z.Tree.Convert_Parameter            import  convert_parameters_all
from    Z.Tree.Definition_V1                import  create_Tree_Class_Definition                #   "_V1" on purpose
from    Z.Tree.Definition_V1                import  create_Tree_Function_Definition             #   "_V1" on purpose
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Class_Definition
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameters_all


#
#   convert_class_definition(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Class_Definition` (i.e.: `_ast.ClassDef`) to a `Tree_Class_Definition`.
#
assert Native_AbstractSyntaxTree_Class_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Class_Definition._fields     == (('name', 'bases', 'body', 'decorator_list'))


def convert_class_definition(z, v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string(v.name)
    assert fact_is_some_native_list  (v.bases)
    assert fact_is_full_native_list  (v.body)
    assert fact_is_some_native_list  (v.decorator_list)

    return create_Tree_Class_Definition(
               v.lineno,
               v.col_offset,

               v.name,
               convert_some_list_of_expressions (v.bases),
               z.convert_full_list_of_statements(z, v.body),
               convert_some_list_of_decorators  (v.decorator_list),
           )


#
#   convert_function_definition(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Function_Definition` (i.e.: `_ast.FunctionDef`) to a
#       `Tree_Function_Definition`.
#
assert Native_AbstractSyntaxTree_Function_Definition._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Function_Definition._fields     == (('name', 'args', 'body', 'decorator_list'))


def convert_function_definition(z, v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string                           (v.name)
    assert fact_is__native__abstract_syntax_tree__parameters_all(v.args)
    assert fact_is_full_native_list                             (v.body)
    assert fact_is_some_native_list                             (v.decorator_list)

    return create_Tree_Function_Definition(
               v.lineno,
               v.col_offset,

               v.name,
               convert_parameters_all           (v.args),
               z.convert_full_list_of_statements(z, v.body),
               convert_some_list_of_decorators  (v.decorator_list),
           )