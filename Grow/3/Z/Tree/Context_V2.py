#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  enumeration


if __debug__:
    from    Capital.Fact                import  fact_is_native_boolean
    from    Capital.Fact                import  fact_is_full_native_string


#
#   AN ENUMERATION.
#
#       In this file we are creating an enumeration with four enumerators.
#
#       We really want to say something like the following:
#
#           enumeration Tree_Context_2
#               delete
#               load
#               parameter
#               store
#
#   HOWEVER:
#
#       python does not support enumerations directly.
#
#   INSTEAD:
#
#       So instead we create a `Tree_Context_2` "class" (which is our enumeration).
#
#       Then we create four instances of this class (which is our four enumerators).
#
#           `.delete`       - The enumerator "delete"
#           `.load`         - The enumerator "load"
#           `.parameter`    - The enumerator "parameter"
#           `.store`        - The enumerator "store".
#
#   FUTURE:
#
#       In the future we our code generator will support enumreators directly.
#
#       When translating to python, it will translate to code similiar to what is below.
#
#       When translating to other languages, that have direct support for enumerations, it will translate to code that
#       uses the language support for enumerations.
#
#   SEE ALSO:
#
#       See the note in "Capital/Core.py" which explains the usage of `@enumeration" to mark "Tree_Context_2" as *NOT*
#       really a class, but really an enumeration.
#


#
#   Tree Context - Tells the context in which to interpret an expression.
#
#       tree_delete_context     - Delete context (i.e.: "delete" a value).
#       tree_load_context       - Load   context (i.e.: "get" a value).
#       tree_store_context      - Store  context (i.e.: "SET" a value).
#
#   Consider the following statements being turned into a parse tree:
#
#       a.b = c.d
#       del e.f
#
#   In the parse tree, we will have the following tree contexts:
#
#       `a`     - tree "load"   context (because we need to "get" `a` to "SET" `a.b`)
#       `a.b`   - tree "store"  context (because we need to "SET" `a.b`)
#       `c`     - tree "load"   context (because we need to "get" `c` to "get" `c.d`)
#       `c.d`   - tree "load"   context (because we need to "get" `c.d`)
#       `e`     - tree "load"   context (because we need to "get" `e` to "delete" `e.f`)
#       `e.f`   - tree "delete" context (because we need to "delete" `e.f`)
#
#   These are named `tree_load_context` and `tree_store_context` since that matches what they are called in `_ast`
#   (the python abstract syntax tree module).
#
#   Also they are not called `*_get` and `*_set` since these have a hamming distance of one (i.e.: differ by one
#   character) -- and are thus too easy to confuse with each other.
#
#   (NOTE: For the same reason we use "SET" in the comment above to make it differ by three characters from "get").
#
#   The following is how we convert `_ast` instances:
#
#       _ast instance of        converted to
#       ----------------        ------------
#       _ast.Delete             tree_delete_context
#       _ast.Load               tree_load_context
#       _ast.Store              tree_store_context
#
#   NOTE:
#       Here we fake a `.name` member, by *NOT* using a real member, but instead inheriting from `str`.
#
#       Whenever we want to access our [fake] `.name` member, we instead use `self`.
#
#       For example, below in `Tree_Context_2.__repr__`, we refer to our [fake] `.name` member as `self` (since `self`
#       is both our own instance and also our own [fake] `.name` member).
#
#   NOTE:
#       Later we'll turn this back into a normal class (with one member named `.name`) -- and our code generator will
#       either:
#
#           1.  Leave it as a class with one member; OR
#
#           2.  "Optimize" it to a class inherited from `str`
#
#       Depending on the code generation option we use.
#
#       For now we demonstrate this as a "optimized" class inherited from `str` for educational purposes -- as a simple
#       example of how a class can inherit from `str`.
#
@enumeration
class Tree_Context_2(object):
    __slots__ = ((
        'name',                         #   NativeString
        'is_tree_delete_context',       #   NativeBoolean
        'is_tree_expression_context',   #   NativeBoolean
        'is_tree_load_context',         #   NativeBoolean
        'is_tree_parameter_context',    #   NativeBoolean
        'is_tree_store_context',        #   NativeBoolean
    ))


    is_tree_context = True


    def __init__(
            self, name, is_tree_delete_context, is_tree_expression_context, is_tree_load_context,
            is_tree_parameter_context, is_tree_store_context,
    ):
        self.name = name

        self.is_tree_delete_context     = is_tree_delete_context
        self.is_tree_expression_context = is_tree_expression_context
        self.is_tree_load_context       = is_tree_load_context
        self.is_tree_parameter_context  = is_tree_parameter_context
        self.is_tree_store_context      = is_tree_store_context


    def __repr__(self):
        return arrange('<Tree_Context_2 {}>', self.name)


    def dump_context_token(self, f):
        f.arrange('<context {}>', self.name)


def create_Tree_Context_2(
        name,

        is_tree_delete_context    = False,
        is_tree_load_context      = False,
        is_tree_parameter_context = False,
        is_tree_store_context     = False,
):
    assert fact_is_full_native_string(name)

    assert fact_is_native_boolean(is_tree_delete_context)
    assert fact_is_native_boolean(is_tree_load_context)
    assert fact_is_native_boolean(is_tree_parameter_context)
    assert fact_is_native_boolean(is_tree_store_context)

    assert (is_tree_delete_context + is_tree_load_context + is_tree_parameter_context + is_tree_store_context) == 1

    return Tree_Context_2(
               name,

               is_tree_delete_context     = is_tree_delete_context,
               is_tree_expression_context = (is_tree_load_context) or (is_tree_store_context),
               is_tree_load_context       = is_tree_load_context,
               is_tree_parameter_context  = is_tree_parameter_context,
               is_tree_store_context      = is_tree_store_context,
           )


#
#   Now we declare our four enumerators.
#
Tree_Context_2.delete    = create_Tree_Context_2('delete',    is_tree_delete_context    = True)
Tree_Context_2.load      = create_Tree_Context_2('load',      is_tree_load_context      = True)
Tree_Context_2.parameter = create_Tree_Context_2('parameter', is_tree_parameter_context = True)
Tree_Context_2.store     = create_Tree_Context_2('store',     is_tree_store_context     = True)