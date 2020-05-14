import string

ALPHABET = "abcdefghijklmnopqrstuvwxyz "


LETTER_TO_INDEX = dict(zip(ALPHABET, range(len(ALPHABET))))
INDEX_TO_LETTER = dict(zip(range(len(ALPHABET)), ALPHABET))


def encrypt(message, key):
    message = message.lower()
    if len(key) != len(message):
        key = format_key(message, key)

    message_indices = [LETTER_TO_INDEX[c] for c in message]
    key_indices = [LETTER_TO_INDEX[c] for c in key]

    encrypted_message = ""
    for i in range(len(message)):
        shift_factor = (message_indices[i] + key_indices[i]) % len(ALPHABET)
        encrypted_message += INDEX_TO_LETTER[shift_factor]

    return encrypted_message


def decrypt(message, key):
    message = message.lower()
    if len(key) != len(message):
        key = format_key(message, key)

    message_indices = [LETTER_TO_INDEX[c] for c in message]
    key_indices = [LETTER_TO_INDEX[c] for c in key]

    decrypted_message = ""
    for i in range(len(message)):
        shift_factor = ((len(ALPHABET) + message_indices[i]) - key_indices[i]) % len(
            ALPHABET
        )
        decrypted_message += INDEX_TO_LETTER[shift_factor]

    return decrypted_message


def format_key(message, key):
    new_key = ""

    while len(new_key) < len(message):
        for c in key:
            if len(new_key) < len(message):
                new_key += c

    return new_key
