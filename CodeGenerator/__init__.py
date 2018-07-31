#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CodeGenerator.__init__')
def module():
    transport('Capital.Absent',                     'absent')
    transport('Capital.Ascii',                      'lookup_ascii')
    transport('Capital.ContextManager',             'empty_context_manager')
    transport('Capital.Core',                       'arrange')
    transport('Capital.Core',                       'character')
    transport('Capital.Core',                       'enumerate')
    transport('Capital.Core',                       'execute')
    transport('Capital.Core',                       'false')
    transport('Capital.Core',                       'intern_string')
    transport('Capital.Core',                       'iterate_range')
    transport('Capital.Core',                       'length')
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'Map')
    transport('Capital.Core',                       'Method')
    transport('Capital.Core',                       'none')
    transport('Capital.Core',                       'Object')
    transport('Capital.Core',                       'ordinal')
    transport('Capital.Core',                       'partial')
    transport('Capital.Core',                       'portray')
    transport('Capital.Core',                       'rename')
    transport('Capital.Core',                       'String')
    transport('Capital.Core',                       'true')
    transport('Capital.Core',                       'Tuple')
    transport('Capital.Core',                       'type')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.Exception',                  'except_any_clause')
    transport('Capital.Exception',                  'raise_runtime_error')
    transport('Capital.Path',                       'path_join')
    transport('Capital.SimpleStringIO',             'create_SimpleStringOutput')
    transport('Capital.System',                     'module_path')
    transport('Capital.System',                     'program_exit')
    transport('Capital.System',                     'slice_all')
    transport('Capital.Traceback',                  'print_exception_chain')


    require_module('CodeGenerator.NestedConjure')
    require_module('CodeGenerator.GenerateTestPortrayString')
