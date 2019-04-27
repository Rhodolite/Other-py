#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Statement - Interface to tree classes that represent statement.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   interface Tree_Statement - Interface to tree classes that represent statements.
#           dump_statement_tokens(f : Build_DumpToken)
#           is_tree_statement := true
#


#
#   USAGE:
#
#       v.is_tree_statement                 #   Test if `v` is a tree statement.
#
#       v.dump_statement_tokens(f)          #   Dump the tokens representing the tree statement to `f`.
#
#       assert fact_is_tree_statement(v)    #   Assert that `v` is a tree statement.
#



#
#   fact_is_tree_statement(v) - Assert that `v` is a `Tree_Statement`.
#
if __debug__:
    def fact_is_tree_statement(v):
        assert v.is_tree_statement

        return True
#</facts>


#
#   Import the version of tree statements we want to use.
#
from    Z.Tree.Global                   import  tree_globals


version = tree_globals.statement_version


if version == '1':
    from    Z.Tree.Statement_V1         import  (
                create_Tree_Assert_Statement_V1         as  create_Tree_Assert_Statement,
                create_Tree_Assign_Statement_V1         as  create_Tree_Assign_Statement,
                create_Tree_Break_Statement_V1          as  create_Tree_Break_Statement,
                create_Tree_Class_Definition_V1         as  create_Tree_Class_Definition,
                create_Tree_Continue_Statement_V1       as  create_Tree_Continue_Statement,
                create_Tree_Delete_Statement_V1         as  create_Tree_Delete_Statement,
                create_Tree_Execute_Statement_V1        as  create_Tree_Execute_Statement,
                create_Tree_Expression_Statement_V1     as  create_Tree_Expression_Statement,
                create_Tree_For_Statement_V1            as  create_Tree_For_Statement,
                create_Tree_From_Import_Statement_V1    as  create_Tree_From_Import_Statement,
                create_Tree_Function_Definition_V1      as  create_Tree_Function_Definition,
                create_Tree_Global_Statement_V1         as  create_Tree_Global_Statement,
                create_Tree_If_Statement_V1             as  create_Tree_If_Statement,
                create_Tree_Import_Statement_V1         as  create_Tree_Import_Statement,
                create_Tree_Modify_Statement_V1         as  create_Tree_Modify_Statement,
                create_Tree_Pass_Statement_V1           as  create_Tree_Pass_Statement,
                create_Tree_Print_Statement_V1          as  create_Tree_Print_Statement,
                create_Tree_Raise_Statement_V1          as  create_Tree_Raise_Statement,
                create_Tree_Return_Statement_V1         as  create_Tree_Return_Statement,
                create_Tree_Try_Except_Statement_V1     as  create_Tree_Try_Except_Statement,
                create_Tree_Try_Finally_Statement_V1    as  create_Tree_Try_Finally_Statement,
                create_Tree_While_Statement_V1          as  create_Tree_While_Statement,
                create_Tree_With_Statement_V1           as  create_Tree_With_Statement,
        )
else:
    from    Capital.Core                import  FATAL

    FATAL('Z/Tree/Statement.py: unknown tree statment version: {!r}', version)