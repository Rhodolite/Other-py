#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Capital.Private.Integer_V8 - Private implementation of the public "Integer" Interfaces, Version 8.
#
#       Integers are Unique.
#


from    Capital.Core                    import  arrange
from    Capital.Core                    import  creator
from    Capital.Core                    import  export
from    Capital.Integer                 import  TRAIT_Contrary_Integer
from    Capital.Integer                 import  TRAIT_Integer
from    Capital.Integer                 import  TRAIT_Keen_Integer
from    Capital.Integer                 import  TRAIT_Negative_Integer
from    Capital.Integer                 import  TRAIT_Positive_Integer
from    Capital.Integer                 import  TRAIT_Zero
from    Capital.Maybe_Temporary         import  TRAIT_Maybe_Temporary_0


if __debug__:
    from    Capital.Cannot              import  raise__CANNOT__construct__ERROR
    from    Capital.Cannot              import  raise__CANNOT__create__ERROR
    from    Capital.Native_Integer      import  fact_is_native_zero
    from    Capital.Native_Integer      import  fact_is_native_integer


#
#<methods>
#
#   Common Methods
#


#
#   method__Native_Integer__representation
#
#       The python implemention of `repr` for `Native_Integer` (i.e.: `int.__repr__`).
#
method__Native_Integer__representation = Native_Integer.__repr__


def method__Integer__operator_representation(self):
    return arrange('<{}>', method__Native_Integer__representation(self))


@property
def property__Integer__native_integer_subclass(self):
    return self


#</methods>


#
#   Zero [Leaf] Integer - A singleton wrapper around the `Native_Integer` (i.e.: `int`) with a value of `0`.
#
class Zero_Leaf(
        Native_Integer,
        #
        #   Implements Contrary_Integer
        #
        TRAIT_Integer,
        #
        #   Implements Keen_Integer
        #
        TRAIT_Maybe_Temporary_0,
        #
        #   Implements Zero
        #
):
    __slots__ = (())


    #
    #   Interface Integer
    #
    is_contrary_integer = True
    is_keen_integer     = True
    is_negative_integer = False
    is_positive_integer = False
    is_zero_integer     = True


    native_integer_subclass = property__Integer__native_integer_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Integer`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Integer`
    #
    __repr__ = method__Integer__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Integer`
    #       with the same value as the `Native_Integer` that `self` wraps.
    #
    python_code = method__Native_Integer__representation


#
#   Negative Integer [Leaf] - A wrapper around a negative native integer (i.e.: `int` with a value less than 0).
#
class Negative_Integer_Leaf(
        Native_Integer,
        #
        #   Implements Contrary_Integer
        #
        TRAIT_Integer,
        TRAIT_Maybe_Temporary_0,
        #
        #   Implements Negative_Integer
        #
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Integer
    #
    is_contrary_integer = True
    is_keen_integer     = False
    is_negative_integer = True
    is_positive_integer = False
    is_zero_integer     = False


    native_integer_subclass = property__Integer__native_integer_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Integer`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Integer`
    #
    __repr__ = method__Integer__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Integer`
    #       with the same value as the `Native_Integer` that `self` wraps.
    #
    python_code = method__Native_Integer__representation



#
#   Postive Integer [Leaf] - A wrapper around a positive native integer (i.e.: `int` with a value greater than 0).
#
class Positive_Integer_Leaf(
        Native_Integer,
        TRAIT_Integer,
        #
        #   Implements Keen_Integer
        #
        TRAIT_Maybe_Temporary_0,
        #
        #   Implements Positive_Integer
        #
):
    __slots__ = (())


    #
    #   Private
    #
    if __debug__:
        __init__ = raise__CANNOT__construct__ERROR
        __new__  = raise__CANNOT__create__ERROR


    #
    #   Interface Integer
    #
    is_contrary_integer = False
    is_keen_integer     = True
    is_negative_integer = False
    is_positive_integer = True
    is_zero_integer     = False


    native_integer_subclass = property__Integer__native_integer_subclass


    #
    #   Public
    #


    #
    #   .format(format_specification) - Inherited from `Native_Integer`.
    #


    #
    #   .__repr__() - Return the representation of a `Zero_Integer`
    #
    __repr__ = method__Integer__operator_representation


    #
    #   .python_code()
    #
    #       Return a `Full_Native_String` that is the python code that python will compile to a `Native_Integer`
    #       with the same value as the `Native_Integer` that `self` wraps.
    #
    python_code = method__Native_Integer__representation




@creator
def create_zero_integer(v):
    assert fact_is_native_zero(v)

    return Zero_Leaf(v)


zero_integer = create_zero_integer(0)


#
#   zero_integer - The singleton `Integer` wrapper around the `Native_Integer` (i.e.: `int`) with a value of `0`.
#
export(zero_integer)


[conjure_avid_number, conjure_contrary_number, conjure_negative_number, conjure_number, conjure_positive_number] = (
    produce_conjure_number_functions(
        number_name             = 'integer',
        fact_is_number          = fact_is_native_integer,
        create_temporary_number = create_temporary_integer,
        Negative_Number_Type    = Negative_Integer_Leaf,
        Positive_Number_Type    = Positive_Integer_Leaf,
        zero_number             = zero_integer,
    )
