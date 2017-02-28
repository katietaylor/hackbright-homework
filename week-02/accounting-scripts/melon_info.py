"""
Prints out all the melons in our inventory
"""

from melons import melon_data


def print_melon(melon_data):
    for melon, attributes in melon_data.items():
        print melon
        for attribute, value in attributes.items():
            print "{}: {}".format(attribute, value)
        print \

print_melon(melon_data)
