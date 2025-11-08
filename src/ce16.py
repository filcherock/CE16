import string
from random import randint

_CHAR = string.ascii_letters + string.digits + string.punctuation + string.whitespace + "йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"

def encode(text):
    positions = []
    for char in text:
        if char in _CHAR:
            positions.append(_CHAR.index(char))
        else:
            positions.append(-1)
    KEY = randint(20, 99) ** 2
    encoded_positions = []
    for element in positions:
        encoded_positions.append(hex(element * KEY))
    encoded_positions.append(hex(KEY))
    return "o".join(encoded_positions)

def decode(encoded_string):
    encoded_positions = encoded_string.split("o")
    last_hex_value = encoded_positions[-1]
    KEY = int(last_hex_value, 16)
    decoded_chars = []
    for hex_value in encoded_positions[:-1]:
        element = int(hex_value, 16)
        index = element // KEY
        decoded_chars.append(_CHAR[index])
    return ''.join(decoded_chars)

def nonDecodeEncoding(text):
    positions = []
    for char in text:
        if char in _CHAR:
            positions.append(_CHAR.index(char)**2)
        else:
            positions.append(-1)
    KEY = randint(2, 64)
    encoded_positions = []
    for element in positions:
        encoded_positions.append(hex(element * KEY))
    return "".join(encoded_positions)
