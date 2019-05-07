#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Convert_Simple_Statement_V2 - Convert Python Abstract Syntax Tree Statements to Tree classes, Version 2.
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
#           All convert functions take a `z` parameter of type `Convert_Zone.
#


if __debug__:
    from    Capital.Fact                        import  fact_is_full_native_list
    from    Capital.Fact                        import  fact_is_full_native_string
    from    Capital.Fact                        import  fact_is_native_boolean
    from    Capital.Fact                        import  fact_is_positive_integer
    from    Capital.Fact                        import  fact_is_some_native_list
    from    Capital.Fact                        import  fact_is_substantial_integer
    from    Z.Tree.Convert_Zone                 import  fact_is_convert_zone
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is__ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION
    from    Z.Tree.Native_AbstractSyntaxTree    import  fact_is___native_none___OR___ANY__native__abstract_syntax_tree__TARGET
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assert_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Assign_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Break_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Continue_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Delete_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Execute_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Expression_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_From_Import_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Function_Definition
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Global_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Import_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Modify_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Pass_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Print_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Raise_Statement
    from    Z.Tree.Native_AbstractSyntaxTree    import  Native_AbstractSyntaxTree_Return_Statement


#
#   create_keyword_statement(v, create) - Common code for `convert_{break,continue,pass}_statement`.
#
def convert_keyword_statement(v, create):
    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    return create(v.lineno, v.col_offset)



#
#   convert_assert_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Assert_Statement` (i.e.: `_ast.Assert`) to a `Tree_Assert_Statement`.
#
assert Native_AbstractSyntaxTree_Assert_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Assert_Statement._fields     == (('test', 'msg'))


def convert_assert_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                    (v.test)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.msg)

    return z.create_Tree_Assert_Statement(
               v.lineno,
               v.col_offset,

               z.convert_expression        (z, v.test),
               z.convert_none_OR_expression(z, v.msg),
           )


#
#   convert_assign_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Assign_Statement` (i.e.: `_ast.Assign`) to a `Tree_Assign`.
#
assert Native_AbstractSyntaxTree_Assign_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Assign_Statement._fields     == (('targets', 'value'))


def convert_assign_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list                              (v.targets)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.value)

    return z.create_Tree_Assign_Statement(
               v.lineno,
               v.col_offset,

               z.convert_full_list_of_targets(z, v.targets),
               z.convert_expression          (z, v.value),
           )


#
#   convert_break_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Break_Statement` (i.e.: `_ast.Break`) to a `Tree_Break_Statement`.
#
assert Native_AbstractSyntaxTree_Break_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Break_Statement._fields     == (())


def convert_break_statement(z, v):
    assert fact_is_convert_zone(z)

    return convert_keyword_statement(v, z.create_Tree_Break_Statement)


#
#   convert_continue_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Continue_Statement` (i.e.: `_ast.Continue`) to a
#       `Tree_Continue_Statement`.
#
assert Native_AbstractSyntaxTree_Continue_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Continue_Statement._fields     == (())


def convert_continue_statement(z, v):
    assert fact_is_convert_zone(z)

    return convert_keyword_statement(v, z.create_Tree_Continue_Statement)


#
#   convert_delete_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Delete_Statement` (i.e.: `_ast.Delete`) to a `Tree_Extended_Delete_Statement`.
#
assert Native_AbstractSyntaxTree_Delete_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Delete_Statement._fields     == (('targets',))


def convert_delete_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list(v.targets)

    return z.create_Tree_Delete_Statement(
               v.lineno,
               v.col_offset,

               z.convert_full_list_of_targets(z, v.targets),
           )


#
#   convert_execute_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Execute_Statement` (i.e.: `_ast.Exec`) to a
#       `Tree_Execute_Statement`.
#
assert Native_AbstractSyntaxTree_Execute_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Execute_Statement._fields     == (('body', 'globals', 'locals'))


def convert_execute_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION                    (v.body)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.globals)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.locals)

    return z.create_Tree_Execute_Statement(
               v.lineno,
               v.col_offset,

               z.convert_expression        (z, v.body),
               z.convert_none_OR_expression(z, v.globals),
               z.convert_none_OR_expression(z, v.locals),
           )


#
#   convert_expression_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Expression_Statement` (i.e.: `_ast.Expr`) to a
#       `Tree_Expression_Statement`.
#
assert Native_AbstractSyntaxTree_Expression_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Expression_Statement._fields     == (('value',))


def convert_expression_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION(v.value)

    return z.create_Tree_Expression_Statement(
               v.lineno,
               v.col_offset,

               z.convert_expression(z, v.value),
           )


#
#   convert_global_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Global_Statement` (i.e.: `_ast.Global`) to a
#       `Tree_Global_Statement`.
#
assert Native_AbstractSyntaxTree_Global_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Global_Statement._fields     == (('names',))


def convert_global_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list(v.names)

    return z.create_Tree_Global_Statement(
               v.lineno,
               v.col_offset,

               v.names,
           )


#
#   convert_from_import_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_From_Import_Statement` (i.e.: `_ast.ImportFrom`) to a
#       `Tree_From_Import_Statement`.
#
assert Native_AbstractSyntaxTree_From_Import_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_From_Import_Statement._fields     == (('module', 'names', 'level'))


def convert_from_import_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_string (v.module)
    assert fact_is_full_native_list   (v.names)
    assert fact_is_substantial_integer(v.level)

    return z.create_Tree_From_Import_Statement(
               v.lineno,
               v.col_offset,

               v.module,
               z.convert_full_list_of_symbol_aliases(z, v.names),
               v.level,
           )



#
#   convert_import_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Import_Statement` (i.e.: `_ast.Import`) to a `Tree_Import_Statement`.
#
assert Native_AbstractSyntaxTree_Import_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Import_Statement._fields     == (('names',))


def convert_import_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is_full_native_list(v.names)

    return z.create_Tree_Import_Statement(
               v.lineno,
               v.col_offset,

               z.convert_full_list_of_module_aliases(z, v.names),
           )


#
#   convert_modify_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Modify_Statement` (i.e.: `_ast.AugAssign`) to a `Tree_Modify_Statement`.
#
assert Native_AbstractSyntaxTree_Modify_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Modify_Statement._fields     == (('target', 'op', 'value'))


def convert_modify_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is__ANY__native__abstract_syntax_tree__TARGET         (v.target)
    assert fact_is__ANY__native__abstract_syntax_tree__MODIFY_OPERATOR(v.op)
    assert fact_is__ANY__native__abstract_syntax_tree__EXPRESSION     (v.value)

    return z.create_Tree_Modify_Statement(
               v.lineno,
               v.col_offset,

               z.convert_target         (z, v.target),
               z.convert_modify_operator(z, v.op),
               z.convert_expression     (z, v.value),
           )


#
#   convert_pass_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Pass_Statement` (i.e.: `_ast.Pass`) to a `Tree_Pass_Statement`.
#
assert Native_AbstractSyntaxTree_Pass_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Pass_Statement._fields     == (())


def convert_pass_statement(z, v):
    assert fact_is_convert_zone(z)

    return convert_keyword_statement(v, z.create_Tree_Pass_Statement)


#
#   convert_print_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Print_Statement` (i.e.: `_ast.Print`) to a `Tree_Print_Statement`.
#
assert Native_AbstractSyntaxTree_Print_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Print_Statement._fields     == (('dest', 'values', 'nl'))


def convert_print_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.dest)
    assert fact_is_some_native_list                                                  (v.values)
    assert fact_is_native_boolean                                                    (v.nl)

    return z.create_Tree_Print_Statement(
               v.lineno,
               v.col_offset,

               z.convert_none_OR_expression      (z, v.dest),
               z.convert_some_list_of_expressions(z, v.values),
               v.nl,
           )


#
#   convert_raise_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Raise_Statement` (i.e.: `_ast.Raise`) to a `Tree_Raise_Statement`.
#
assert Native_AbstractSyntaxTree_Raise_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Raise_Statement._fields     == (('type', 'inst', 'tback'))


def convert_raise_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.type)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.inst)
    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.tback)

    return z.create_Tree_Raise_Statement(
               v.lineno,
               v.col_offset,

               z.convert_none_OR_expression(z, v.type),
               z.convert_none_OR_expression(z, v.inst),
               z.convert_none_OR_expression(z, v.tback),
           )


#
#   convert_return_statement(z, v)
#
#       Convert a `Native_AbstractSyntaxTree_Return_Statement` (i.e.: `_ast.Return`) to a `Tree_Return_Statement`.
#
assert Native_AbstractSyntaxTree_Return_Statement._attributes == (('lineno', 'col_offset'))
assert Native_AbstractSyntaxTree_Return_Statement._fields     == (('value',))


def convert_return_statement(z, v):
    assert fact_is_convert_zone(z)

    assert fact_is_positive_integer   (v.lineno)
    assert fact_is_substantial_integer(v.col_offset)

    assert fact_is___native_none___OR___ANY__native__abstract_syntax_tree__EXPRESSION(v.value)

    return z.create_Tree_Return_Statement(
               v.lineno,
               v.col_offset,

               z.convert_none_OR_expression(z, v.value),
           )
