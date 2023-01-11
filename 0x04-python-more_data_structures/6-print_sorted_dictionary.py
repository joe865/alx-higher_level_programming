orted_dictionary(a_dictionary):
    for value in sorted(a_dictionary.keys()):
        print("{}: {}".format(value, a_dictionary[value]))
