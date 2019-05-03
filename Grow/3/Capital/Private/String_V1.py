#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.String_V1 - Private implementation of the public `String` Interface, Version 1.
#
#       Strings are Unique (in normal cases).
#
#       In abnormal cases, Non-unique strings can "leak".  Abnormal cases are:
#
#           1.  Multithreading race conditions;
#           2.  Tracebacks due to MemoryError (out of memory);
#           3.  Using `gc` (garbage collection) module to examine instances in another thread.
#
#       Later versions fix this issue (of non-uniqueness in abnormal cases), and strings are always unique
#       in later versions.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.NativeString            import  intern_native_string
from    Capital.String                  import  TRAIT_String


if __debug__:
    from    Capital.NativeString        import  fact_is_some_INTERNED_native_string


#
#   String_V1 - A very simple string wrapper.
#
#       NOTE: Named `String_V1` instead of `String`, since the name "String" is reserved for `interface String`.
#
#             (even though in the current implementation python (which does not have interfaces in python) does not
#             actually have anything really named `interface String` -- conceptually it does, and thus the name
#             "String" is still reserved for `interface String`).
#
@export
class String_V1(
        TRAIT_String,
):
    __slots__ = ((
        'interned_s',                   #   NativeString
    ))


    #
    #   Private
    #
    def __init__(self, interned_s):
        self.interned_s = interned_s


    #
    #   Interface String
    #
    @property
    def is_empty_string(self):
        return len(self.interned_s) == 0


    @property
    def is_full_string(self):
        return len(self.interned_s) != 0


    @property
    def native_subclass(self):
        return self.interned_s


    #
    #   Public
    #

    #
    #   .__format__ (format_specification)  - Format `String`
    #
    #       Delegated to the `NativeString` implementation via `.interned_s`.
    #
    #
    def __format__(self, format_specification):
        return self.interned_s.__format__(format_specification)


    #
    #   .__len__()  - Return the length.
    #
    #       Delegated to the `NativeString` implementation via `.interned_s`.
    #
    def __len__(self):
        return self.interned_s.__len__()


    #
    #   .__repr__() - Return the representation of a `String`
    #
    #   CURRENT
    #
    #       Surround the the result of `.python_code` with angle brackets.
    #
    #       Example:
    #
    #           assert __repr__(conjure_string('hello')) == "<'hello'>"
    #
    #   FUTURE
    #
    #       See `.python_code` for an explanation of how `.python_code` will behave differently in the future.
    #
    def __repr__(self):
        return arrange('<{}>', self.python_code())


    #
    #   .python_code()
    #
    #       Return a `str` instance that is the python code that python will compile to a `str` instance with the
    #       same characters.
    #
    #   CURRENT
    #
    #       For now, we just use the `NativeString` representation (i.e: `str.__repr__` via `.interned_s`).
    #
    #   FUTURE:
    #
    #       We will use the function `portray_python_string` which does a really good job of a python
    #       represenation (much more readable than `str.__repr__` when presented with a "raw" string).
    #
    #       However, that code is quite large, so we are not including it for now.
    #
    #       Also, really, we want to code generate the `portray_python_string` ... so will wait until the
    #       code generator can generate that function, before using it.
    #
    def python_code(self):
        return repr(self.interned_s)


@export
@creator
def create_string_v1(interned_s):
    assert fact_is_some_INTERNED_native_string(interned_s)

    return String_V1(interned_s)


empty_string = create_string_v1(intern_native_string(""))


export(empty_string)
