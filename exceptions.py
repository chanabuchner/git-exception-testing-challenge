# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(1.234.upper())
    pass


# KeyError
def produce_key_error():
    my_dict = { "name": "Patricia" }
    print(my_dict["age"])
    pass


# IndexError
def produce_index_error():
    my_list = [1,2,3]
    my_list[100]
    pass


# NameError
def produce_name_error():
    return my_var
    pass


# UnboundLocalError
def produce_unbound_local_error():
    print(f"{my_var}")
    my_var = 10
    pass


# TypeError
def produce_type_error():
    print("dfgdfs" + 3)
    pass


# ValueError
def produce_value_error():
    int("abc")
    pass


# ZeroDivisionError
def produce_zero_division_error():
    100/0
    pass


# OverflowError
def produce_overflow_error():
    10.0 ** 9999999
    pass


# FileNotFoundError
def produce_file_not_found_error():
    open("sdfdsf.txt", "r")
    pass


# UnicodeEncodeError
def produce_unicode_encode_error():
    "ä".encode("ascii") # UTF-8
    pass


# ModuleNotFoundError
def produce_module_not_found_error():
    import dfsalkdf
    pass


# ImportError
def produce_import_error():
    from random import kdjflsdjf
    pass
