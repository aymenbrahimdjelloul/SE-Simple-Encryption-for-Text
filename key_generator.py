"""
@author : Aymen Brahim Djelloul.
date : 2022.07.18
version : 0.1

// this module is for generate a random key to use it in cryptography purposes


"""

# Imports
import secrets
import sys

# define variables
__chars = 'abcdefghijklmnopqrstuvwxyz'
__nums = '0123456789'
__symbols = '=-+)(*&^%$#@!~}{][|":;/.,<>?_'


def generate_random_key(key_len=16):
	""" return a random generated key with default length '16' can be used in cryptography"""

	if key_len < 4:
		raise ValueError("Key Length must be greater than 4 characters")

	key = ''
	char_types = (__chars, __nums, __symbols)
	is_upper = False

	for i in range(key_len):
		# select random type to place it
		# chars or nums or symbols

		char_type = secrets.choice(char_types)
		char_to_set = secrets.choice(char_type)

		# switch characters between uppercase and lowercase
		if is_upper:
			is_upper = False
			char_to_set = char_to_set.lower()

		elif not is_upper:
			is_upper = True
			char_to_set = char_to_set.upper()

		key = f'{key}{char_to_set}'

	# clear variables
	del i, char_types, is_upper, char_type, char_to_set, key_len

	return key

# def generate_random_bytes(key_len=16):
# 	""" return a random bytes generated key in default length of '16' """
# 	return secrets.token_bytes(key_len)


def generate_custom_key(custom_char, key_len=16):
	""" return a random generated key with a custom string given as an attribute """

	if key_len < 8:
		raise ValueError("Key Length must be greater than 8 characters")

	if len(custom_char) >= key_len:
		raise ValueError(f"the length of custom value given must be less than {key_len} the generated key length ")

	key = custom_char
	chars_types = (__nums, __symbols)
	is_upper = False

	for i in range(key_len - len(custom_char)):

		choosen_type = secrets.choice(chars_types)
		char_to_set = secrets.choice(choosen_type)

		# switch characters between uppercase and lowercase
		if is_upper:
			is_upper = False
			char_to_set = char_to_set.lower()

		elif not is_upper:
			is_upper = True
			char_to_set = char_to_set.upper()

		key = f'{key}{char_to_set}'

	# clear variables
	del custom_char, key_len, chars_types, is_upper, i, choosen_type, char_to_set

	return key


def generate_insane_key(key_len=16):
	""" return a complex random generated key used for cryptography contain more of special characters and symbols """

	if key_len < 8:
		raise ValueError("Key Length must be greater than 8 characters")

	# create a list of all character will be used
	special_chars = [chr(x) for x in range(32, 1500)]

	key = ''
	is_upper = False

	for i in range(key_len):

		char_to_set = secrets.choice(special_chars)

		if is_upper:
			is_upper = False
			char_to_set = char_to_set.lower()

		elif not is_upper:
			is_upper = True
			char_to_set = char_to_set.upper()

		key = f'{key}{char_to_set}'

	# clear variables
	del key_len, special_chars, is_upper, i, char_to_set

	return key


if __name__ == "__main__":
	sys.exit()