#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Tree.Definition_V7 - Implementation of tree compound statements, Version 7.
#
#       `Tree_*` classes are copies of classes from `Native_AbstractSyntaxTree_*` (i.e.: `_ast.*`) with extra methods.
#


#
#   Differences between Versions 3..7.
#
#       Version 3:
#
#           1)  Tree Statements implement `Tree_Statement`.
#
#           2)  A           list of statements is stored as `Full_Native_List of Tree_Statement`.
#
#           3)  An optional list of statements is stored as `Native_List of Tree_Statement`.
#
#       Version 4..6:
#
#           Do not exist.
#
#       Version 7:
#
#           1)  Tree Statements implement `Tree_Statement`; and ...
#
#               ... in addition also implement `Tree_Suite`, and `Tree_Suite_0`.
#
#           2)  A           list of statements is stored as `Tree_Suite`.
#
#           3)  An optional list of statements is stored as `Tree_Suite_0`.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Z.Tree.Statement                import  TRAIT_Tree_Statement
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite
from    Z.Tree.Suite                    import  TRAIT_Tree_Suite_0


if __debug__:
    from    Capital.Fact                import  fact_is_native_list
    from    Capital.Native_Integer      import  fact_is_positive_native_integer
    from    Capital.Native_Integer      import  fact_is_avid_native_integer
    from    Z.Parser.Symbol             import  fact_is_parser_symbol
    from    Z.Tree.Parameter_Tuple      import  fact_is_tree_parameter_tuple_0
    from    Z.Tree.Suite                import  fact_is_tree_suite


#
#   Tree: Class Definition
#
class Tree_Class_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'name',                         #   Parser_Symbol
        'bases',                        #   Native_List of Tree_Value_Expression
        'body',                         #   Tree_Suite
        'decorator_list',               #   Native_List of Tree_Decorator
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, name, bases, body, decorator_list):
        self.line_number = line_number
        self.column      = column

        self.name           = name
        self.bases          = bases
        self.body           = body
        self.decorator_list = decorator_list


    def _dump_bases_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.bases:
                v.dump_value_expression_tokens(f)
                f.line()


    def _dump_body_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            self.body.dump_suite_tokens(f)


    def _dump_decorator_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.decorator_list:
                f.write('@')
                v.dump_value_expression_tokens(f)
                f.line()


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        decorator_list = self.decorator_list

        f.arrange('<class-definition @{}:{} ', self.line_number, self.column)
        self.name.dump_symbol_token(f)
        f.line()

        with f.indent_2(None, '>'):
            self._dump_bases_tokens(f, 'bases: {', None)

            if len(self.decorator_list) == 0:
                self._dump_body_tokens     (f, '}; body: {',           '}')
            else:
                self._dump_body_tokens     (f, '}; body: {',           None)
                self._dump_decorator_tokens(f, '}; decorator_list: {', '}')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Class_Definition @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.name, self.bases, self.body, self.decorator_list)


@creator
def create_Tree_Class_Definition(line_number, column, name, bases, body, decorator_list):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol(name)
    assert fact_is_native_list  (bases)
    assert fact_is_tree_suite   (body)
    assert fact_is_native_list  (decorator_list)

    return Tree_Class_Definition(line_number, column, name, bases, body, decorator_list)


#
#   Tree: Function Definition
#
class Tree_Function_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'name',                         #   Parser_Symbol
        'parameters',                   #   Tree_Parameter
        'body',                         #   Tree_Suite
        'decorator_list',               #   Native_List of Tree_Decorator
    ))


    #
    #   Private
    #
    def __init__(self, line_number, column, name, parameters, body, decorator_list):
        self.line_number = line_number
        self.column      = column

        self.name           = name
        self.parameters     = parameters
        self.body           = body
        self.decorator_list = decorator_list


    def _dump_body_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            self.body.dump_suite_tokens(f)


    def _dump_decorator_tokens(self, f, header, trailer):
        with f.indent_2(header, trailer):
            for v in self.decorator_list:
                f.write('@')
                v.dump_value_expression_tokens(f)
                f.line()


    #
    #   Interface Tree_Statement
    #
    def dump_statement_tokens(self, f):
        decorator_list = self.decorator_list

        f.arrange('<function-definition @{}:{} ', self.line_number, self.column)
        self.name.dump_symbol_token(f)
        f.line()

        with f.indent_2(None, '>'):
            self.parameters.dump_parameter_tuple_tokens(f)

            if len(self.decorator_list) == 0:
                self._dump_body_tokens     (f, '{',                    '}')
            else:
                self._dump_body_tokens     (f, '{',                    None)
                self._dump_decorator_tokens(f, '}; decorator_list: {', '}')


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Tree_Function_Definition @{}:{} {!r} {!r} {!r} {!r}>',
                       self.line_number, self.column, self.name, self.parameters, self.body, self.decorator_list)


@creator
def create_Tree_Function_Definition(line_number, column, name, parameters, body, decorator_list):
    assert fact_is_positive_native_integer(line_number)
    assert fact_is_avid_native_integer    (column)

    assert fact_is_parser_symbol         (name)
    assert fact_is_tree_parameter_tuple_0(parameters)
    assert fact_is_tree_suite            (body)
    assert fact_is_native_list           (decorator_list)

    return Tree_Function_Definition(line_number, column, name, parameters, body, decorator_list)
