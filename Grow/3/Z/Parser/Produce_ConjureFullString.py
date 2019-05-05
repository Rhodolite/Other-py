#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Z.Parser.Produce_ConjureFullName - An identifier used in the Z parser.
#


from    Capital.TemporaryString_V6      import  create_temporary_string


if __debug__:
    from    Capital.Fact                import  fact_is_full_native_string


#
#   produce_conjure_full_name(Meta)
#
#       Produce a `conjure_full_name(s)` method.
#
#       This produce method is pretty much a copy of `produduce_conjure_string` in "Capital.Private.ConjureString_V6".
#
#       Differences betweeen `produce_conjure_full_name` and `produce_conjure_string`:
#
#           `produce_conjure_full_name(Meta)`:
#
#               1)  The produced function `conjure_full_name` does not allow empty strings.
#
#               2)  `produce_conjure_full_name` does *NOT* take a parameter named `empty_string`; and
#                   instead initializes it's `string_cache` as follows:
#
#                       string_cache = {}
#   
#               3)  `produce_conjure_full_name` does *NOT* take a parameter named `create_temporary_string`; instead
#                   it always uses `Capital.Private.TemporaryString_V6.create_temporary_string` (defined above).
#
#               4)  The produced function `conjure_full_name` uses `fact_is_full_native_string(s)` (i.e.: it's `s`
#                   parameter must be a *FULL* native string).
#
#               5)  `produce_conjure_full_name` does not have extensive comments.
#
#                   Instead, read the comments in `produce_conjure_string`, to understand the multi-threading and class
#                   transformation issues.
#
#           `produce_conjure_string(empty_string, create_temporary_string, Meta)`:
#
#               1)  The produced function `conjure_string` allows empty strings.
#
#               2)  `produce_conjure_string` takes a parameter named `empty_string`; and initilizes it's `string_cache`
#                   as follows:
#
#                       string_cache = { empty_string : empty_string }
#
#               3)  `produce_conjure_string` takes a parameter named `create_temporary_string`.
#
#               4)  The produced function `conjure_string` uses `fact_is_some_native_string(s)` (i.e.: it's `s`
#                   parameter may be an empty or full native string).
#
#               5)  `produce_conjure_string` has extensive comments to explain the multi-threading and class
#                   transformation issues.
#
def produce_conjure_full_name(Meta):
    cacche  = {}                        #   Map { StringKey | Meta } of { StringKey | Meta }
    lookup  = cacche.get
    provide = cacche.setdefault


    #
    #   conjure_full_name(s) - Conjure a `Meta`, based on `s`.  Guarentees Uniqueness.
    #
    #       `s` must be of type `NativeString` (or a type that is a subclass of `NativeString`).
    #
    #       `s` must be a "full" string (i.e.: length greater than 0).
    #
    def conjure_full_name(s):
        #
        #   See comments in "Capital.Private.ConjureString_V6.py" to understand this code.
        #
        assert fact_is_full_native_string(s)

        r = lookup_symbol(s)

        if r is not None:
            if r.temporary_element_has_definitively_been_transformed:
                return r

            r.__class__ = Meta

            assert r.temporary_element_has_definitively_been_transformed

            return r

        k = create_temporary_string(s)

        r = provide_string_key(k, k)

        if r.temporary_element_has_definitively_been_transformed:
            return r

        r.__class__ = Meta

        assert r.temporary_element_has_definitively_been_transformed

        return r


    return conjure_full_name
