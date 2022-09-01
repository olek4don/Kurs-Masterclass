raw_string = r"Something is\twrong here\nhere to"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + "with" + chr(9) + "ascii"
print(b_string)

g = "Venom and\r Maria"
print(g)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

# error_string = r"this string ends with \"     # can't end with backslash cuz it points to escape char
# print(error_string)

error_string = r"this string ends with \\"
print(error_string)
