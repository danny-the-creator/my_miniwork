# print('something'.ljust(16, '~'))       # text to the left
# print('something'.rjust(16, '~'))       # text to the right
# print('something'.center(16, '~'))      # text in center
#
# 'string.txt'.rsplit('.', 1)             # splits from the right

# If we have to replace a lot of different strings, then translate should be used instead of replace

# translation_map = {ord('a'): '*', ord('b'): '?'}
# print('abracadabra'.translate(translation_map))
# ''.istitle()                            # predicator - there are a lot of them, could be quite useful

# print('bin: {0:b}, hex: {0:x}'.format(69))  # a easy way to translate a number into binary/ hex/ decimals

# !!! There are much more specification apart from {0:b}    See documentation !!!

# string has a lot of constants
# import string

# string.digits
# string.ascii_letters
# ...

# Bytes:

# b = b'\00\42\24\00'         # way of writing bytes in python
# chunk = 'I am a string!'.encode('utf-8')        # way of encoding a string
# print(chunk.decode('utf-8'))                    # way of decoding a byte array

# Almost all operators from string work with bytes
