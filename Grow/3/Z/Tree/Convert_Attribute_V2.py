#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Attribute_V2 - Convert Python Abstract Syntax Tree Targets to Tree classes, Version 2.
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


from    Z.Tree.Attribute_V1                 import  create_Tree_Attribute
from    Z.Tree.Convert_Context              import  convert_delete_load_OR_store_context
from    Z.Tree.Convert_Zone                 import  convert_zone
from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Attribute_Expression


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT


#
#   convert_attribute_expression(v)
#
#       Convert a `Native_AbstractSyntaxTree_Attribute_Expression` (i.e.: `_ast.Expr`) to a `Tree_Attribute`.
#
assert Native_AbstractSyntaxTree_Attribute_Expression._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Attribute_Expression._fields     == (('value', 'attr', 'ctx'))


def convert_attribute_expression(v):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                  (v.value)
    assert fact_is_full_native_string                                              (v.attr)
    assert fact_is__ANY__native__abstract_syntax_tree__DELETE_LOAD_OR_STORE_CONTEXT(v.ctx)

    z = convert_zone

    return create_Tree_Attribute(
               v.lineno,
               v.col_offset,

               z.convert_expression                (z, v.value),
               v.attr,
               convert_delete_load_OR_store_context(v.ctx),
          )
