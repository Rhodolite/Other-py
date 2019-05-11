#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Temporary_String_V7 - Temporary String Implementation, Version 7.
#


#
#   Differences between Version 6 & Version 7.
#
#       Version 6:
#
#           String classes use `object` as their base class.
#
#       Version 7:
#
#           String classes use `Native_String` (i.e.: `str`) as their base class.
#


from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Native_String           import  Native_String
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0


if __debug__:
    from    Capital.Native_String       import  fact_is_full_native_string


#
#   method__Native_String__representation
#
#       The python implemention of `repr` for `Native_String` (i.e.: `str.__repr__`).
#
method__Native_String__representation = Native_String.__repr__


#
#   Temporary_String - Temporary String Implementation
#
class Temporary_String(
        Native_String,
        TRAIT_Maybe_Temporary_0,
        #
        #   NOTE:
        #       Does *NOT* implement the `String` interface.
        #
        #       This is *NOT* a `String`, but a temporary element (that *MIGHT* be transformed to a `String`).
        #
):
    #
    #   `__slots__` are equivalent to the slots of `Capital.Private.String_V7.Full_String_Leaf` (which an instance of
    #   this class is transformed to).
    #
    __slots__ = (())


    #
    #   Interface Maybe_Temporary
    #
   #@replace
    definitively_not_temporary = False


    #
    #   Public
    #
    def __repr__(self):
        return arrange('<Temporary_String {!r}>', method__Native_String__representation(self))


@export
@creator
def create_temporary_string(s):
    assert fact_is_full_native_string(s)

    return Temporary_String(s)
