#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Context - Convert Python Abstract Syntax Tree Contexts to Tree classes.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#
#       See "Z/Tree/Context.py" for an explanation of "contexts".
#


from    Z.Tree.Context                          import  tree_delete_context
from    Z.Tree.Context                          import  tree_load_context
from    Z.Tree.Context                          import  tree_parameter_context
from    Z.Tree.Context                          import  tree_store_context
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Delete_Context
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Load_Context
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Store_Context
from    Z.Tree.Native_AbstractSyntaxTree        import  Native_AbstractSyntaxTree_Parameter_Context


if __debug__:
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__delete_context
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__native__abstract_syntax_tree__parameter_context


#
#   convert_delete_context
#
#       Convert a `Native_AbstractSyntaxTree_Delete_Context` to the singleton `tree_delete_context`.
#
assert Native_AbstractSyntaxTree_Delete_Context._attributes == (())
assert Native_AbstractSyntaxTree_Delete_Context._fields     == (())

def convert_delete_context(self):
    assert fact_is__native__abstract_syntax_tree__delete_context(self)

    return tree_delete_context


#
#   convert_delete_load_OR_store_context
#
#       Convert a "delete", "load", or "store" context to a `Tree_Context` enumerator.
#
map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
        Native_AbstractSyntaxTree_Delete_Context : tree_delete_context,
        Native_AbstractSyntaxTree_Load_Context   : tree_load_context,
        Native_AbstractSyntaxTree_Store_Context  : tree_store_context,
    }


if __debug__:
    def assert_no_context_fields():
        for k in map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context:
            assert k._attributes == (())
            assert k._fields     == (())


    assert_no_context_fields()


def convert_delete_load_OR_store_context(self):
    return map__Native_AbstractSyntaxTree_DELETE_LOAD_OR_STORE_CONTEXT__to__Tree_Context[type(self)]


#
#   convert_load_OR_store_context
#
#       Convert a "load" or "store" context to a `Tree_Context` enumerator.
#
map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context = {
        Native_AbstractSyntaxTree_Load_Context  : tree_load_context,
        Native_AbstractSyntaxTree_Store_Context : tree_store_context,
    }


if __debug__:
    def assert_no_context_fields():
        for k in map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context:
            assert k._attributes == (())
            assert k._fields     == (())


    assert_no_context_fields()


def convert_load_OR_store_context(self):
    return map__Native_AbstractSyntaxTree_LOAD_OR_STORE_CONTEXT__to__Tree_Context[type(self)]


#
#   convert_parameter_context
#
#       Convert a `Native_AbstractSyntaxTree_Parameter_Context` to the singleton `tree_parameter_context`.
#
assert Native_AbstractSyntaxTree_Parameter_Context._attributes == (())
assert Native_AbstractSyntaxTree_Parameter_Context._fields     == (())

def convert_parameter_context(self):
    assert fact_is__native__abstract_syntax_tree__parameter_context(self)

    return tree_parameter_context
