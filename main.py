# # Project: Numbers in words
# # Author: Yuri Lima
# # Email: y.m.lima19@gmail.com
# # GitHub: https://github.com/Yuri-Lima
# # Goals: The main ideia this project is in the future i will create a API.
# # This API will help developments find every numbers in words.

from convertnumbers import Convert_numbers_english
#====================================================================================================

number_typed = list()

# number_typed = input('Please give me a number (Max = 13 Decimal Places):')
number_typed = '1021010105010101'#'101101'

word = Convert_numbers_english(number_typed)
word.start_convertion()
txt = word.str_number_in_word()
print('<' + '-'*len(txt) + '>')

print(f'String: {txt}\n')
# print(f'List: {word.list_number_in_word()}\n')
# print(f'Even or Odd: {word.even_or_odd()}\n')
print(f'Decimal Places: {word.how_many_decimal_places()}\n')
print(f'Places Filled: \n{word.place_decimal()}\n')
print(f'After First position check if are only zeros: {word.bool_check_zeros()}\n')

print('<' + '-'*len(txt) + '>')